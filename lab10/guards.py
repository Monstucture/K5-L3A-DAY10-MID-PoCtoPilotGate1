"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# ---------------------------------------------------------------------------------------------------------------
# VÒNG 1 · ba cổng phòng ngừa. Chỉ tra NGUỒN SỰ THẬT (tracking DB, chính sách đang hiệu lực, sổ cái), không đọc
# chữ khách viết, không nhắc tới mã ticket / mã đơn / câu chữ cụ thể.
#   Cổng 1 (write_gate · issue_refund)       : số tiền và người trả phải khớp quyền lợi tính từ DB và chính sách hiệu lực
#   Cổng 2 (write_gate · file_carrier_fault) : chỉ ghi lỗi hãng khi DB có nguyên nhân thuộc lỗi hãng, đúng kiện, đúng số ngày
#   Cổng 3 (write_gate · notify_carrier)     : chỉ gửi hãng các trường nằm trong danh sách của chính sách
#   (pre_guard)                              : ghim phiên bản chính sách theo ngày hiệu lực, không theo cờ "index_active"
# ---------------------------------------------------------------------------------------------------------------

def _facts(ctx, order_id):
    """(order, policy hiệu lực theo ngày, kiện trễ nhất, số ngày trễ theo DB, nguyên nhân) hoặc None nếu thiếu dữ kiện."""
    order = ctx.tools.lookup_order(order_id)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not order.get("parcels") or policy is None:
        return None
    worst = max(order["parcels"], key=lambda p: H.db_delay_days(p, ctx.as_of))
    delay = H.db_delay_days(worst, ctx.as_of)
    cause = worst.get("delay_cause") or ("CARRIER" if delay > 0 else None)
    return order, policy, worst, delay, cause


def _approval_problem(ctx, approval_id, order, amount):
    """Lý do mã phê duyệt KHÔNG dùng được cho khoản hoàn này (None = hợp lệ). Chỉ đọc bảng approvals và sổ cái."""
    found = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not found:
        return "không có trong bảng phê duyệt"
    a = found[0]
    if a.get("order_id") != order.get("order_id"):
        return "phê duyệt của đơn khác"
    if a.get("customer_id") and a["customer_id"] != order.get("customer_id"):
        return "phê duyệt của khách khác"
    if a.get("status") != "valid":
        return "trạng thái " + str(a.get("status"))
    if a.get("expires_at") and H.d(a["expires_at"]) < H.d(ctx.as_of):
        return "đã hết hạn"
    approver = ((ctx.gates or {}).get("operations") or {}).get("approver_id")
    if approver and a.get("approver_id") != approver:
        return "người duyệt không phải người đứng tên đã thống nhất"
    if a.get("max_vnd") is not None and amount > a["max_vnd"]:
        return "số tiền vượt mức đã duyệt"
    if ctx.tools.ledger_rows(approval_id=approval_id):
        return "mã đã dùng cho một khoản hoàn khác"
    return None


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is not None:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    if tool == "issue_refund":                                              # cổng 1
        if ctx.tools.ledger_rows(ticket_id=action.get("ticket_id")):
            return Verdict.deny("ticket này đã có khoản hoàn trong sổ cái: không ghi lần hai")
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.escalate("không đối chiếu được đơn hoặc chính sách hiệu lực: chuyển người")
        order, policy, _worst, delay, cause = facts
        entitled = H.entitlement_vnd(policy, order, delay, cause)
        if entitled <= 0:
            return Verdict.deny("theo tracking DB và chính sách hiệu lực, đơn không đủ điều kiện hoàn")
        amount = min(int(action.get("amount_vnd", 0)), entitled)
        approval_id = action.get("approval_id")
        if approval_id:                                                     # cổng 1b: phê duyệt phải hợp lệ
            problem = _approval_problem(ctx, approval_id, order, amount)
            if problem:
                ctx.log("approval_rejected", approval_id=approval_id, problem=problem)
                if amount > policy["auto_limit_vnd"]:
                    return Verdict.escalate("phê duyệt không hợp lệ (" + problem + "): chuyển người duyệt")
                # khoản nhỏ không cần phê duyệt; bỏ mã sai để nó không lách trần hoàn tự động mỗi ngày
                return Verdict.modify("bỏ mã phê duyệt không hợp lệ (" + problem + ")",
                                      amount_vnd=amount, payer="LOGIX", approval_id=None)
        if amount > policy["auto_limit_vnd"] and not approval_id:
            return Verdict.escalate("vượt hạn mức tự động và chưa có phê duyệt")
        if amount != action.get("amount_vnd") or action.get("payer", "LOGIX") != "LOGIX":
            ctx.log("refund_corrected", asked=action.get("amount_vnd"), entitled=entitled, payer=action.get("payer"))
            return Verdict.modify("đưa khoản hoàn về quyền lợi tính từ DB, người trả là LogiX",
                                  amount_vnd=amount, payer="LOGIX")

    elif tool == "file_carrier_fault":                                      # cổng 2
        if not ctx.tools.ledger_rows(ticket_id=action.get("ticket_id")):
            return Verdict.deny("chưa có khoản hoàn nào cho ticket này: không ghi lỗi hãng")
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.deny("không đối chiếu được đơn hoặc chính sách: không ghi lỗi hãng")
        order, policy, _worst, _delay, _cause = facts
        target = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        days = H.db_delay_days(target, ctx.as_of)
        if not H.carrier_at_fault(policy, target, days):
            return Verdict.deny("tracking DB không ghi nguyên nhân thuộc lỗi hãng cho kiện này")
        want = {"parcel_id": target["parcel_id"], "carrier_id": target["carrier_id"],
                "driver_id": target.get("driver_id"), "delay_days": days}
        if any(action.get(k) != v for k, v in want.items()):
            ctx.log("fault_corrected", asked={k: action.get(k) for k in want}, db=want)
            return Verdict.modify("ghi lỗi đúng kiện, đúng hãng, đúng số ngày theo tracking DB", **want)

    elif tool == "notify_carrier":                                          # cổng 3
        facts = _facts(ctx, (action.get("payload") or {}).get("order_id"))
        if facts is not None:
            allowed = set(facts[1].get("carrier_notice_fields") or [])
            payload = action.get("payload") or {}
            clean = {k: v for k, v in payload.items() if k in allowed}
            if clean != payload:
                ctx.log("notice_trimmed", dropped=sorted(set(payload) - allowed))
                return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép", payload=clean)

    return Verdict.allow()
