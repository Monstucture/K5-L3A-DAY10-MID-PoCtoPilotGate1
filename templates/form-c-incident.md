# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-MID-PoCtoPilotGate1 · **Thẻ đã bốc:** S4 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S4-prepared-20261118-212702-35ac51` | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 1,0 | 1,0 | 0 · 0 · 0 | 0,3659 | Cổng vòng 1 đỡ được hoàn sai và lỗi hãng oan; không đỡ được hàng chờ (4 ca ùn, tổng hoàn 422.000đ > 300.000đ) |
| 2 | `R-S4-after-20261118-212702-35ac51` | Sx · after | Cổng 1d đã có trong `guards.py` (`basis == "fail_open"` thì chuyển người) và config 2 người trực, 12 ca/giờ | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,5756 | Mọi chỉ số bắt buộc đạt, 0 ca ùn, tổng hoàn 294.000đ ≤ 300.000đ; chưa đạt nice-to-have (chuyển người 0,5756 > 0,3), ROI 0,28 và chi phí 7.795đ sát ngưỡng đã ký |
| 3 | | Sx · after | | | | | | |
| 4 | `R-base-after-20261118-212741-35ac51` | base · after | (kiểm không regression, grade integrity ✅) | 1,0 [1,0; 1,0] | 1,0 | 0 · 0 · 0 | 0,2727 | 110/110 đạt, không ca nào đang đúng bị hỏng; chuyển người 0,2727 (gồm kiểm lại 10%), ROI 0,72 |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S4-grade-20261118-212702-35ac51` · base: `R-S4-before-20261118-212702-35ac51` · prepared: `R-S4-prepared-20261118-212702-35ac51` · after: `R-S4-after-20261118-212702-35ac51`. Mốc prepared dùng được: grader báo "đã chốt `f9436b2e`, còn nguyên", kiểm 1 integrity ✅, kiểm 2 criteria ✅ (PASS-VISIBLE). Lần grade trước (`R-S4-grade-20261118-172245-8c2343`) báo integrity ❌ vì xuống dòng CRLF trên Windows làm hash file khoá lệch, không phải do ai sửa nội dung; đã đưa 19 file khoá về LF (`core.autocrlf false`) rồi chạy lại.
- Cổng vòng 1 đỡ được (cột visible, base → prepared): hoàn sai 160.000đ → 0; lỗi hãng oan 27 → 0; pass_rate 0,8683 → 1,0; pass_k 0,6829 → 1,0. **Không đỡ được** hàng chờ: chờ lâu nhất 78 phút và 4 ca ùn giữ nguyên.
- Khối kinh doanh và vận hành còn dòng vượt trần: ở mốc prepared tổng hoàn tự động một ngày **422.000đ > ngân sách 300.000đ**; số ca ùn 4 và tỉ lệ chuyển người 0,3659 giữ nguyên so với base. Ở mốc after: 294.000đ (không vượt, nhưng sát trần), 0 ca ùn, tỉ lệ chuyển người 0,5756 (vượt ngưỡng nice-to-have 0,3).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chủ yếu **con người và vận hành** (một người trực, hàng chờ ngập giờ cao điểm), cộng **kinh doanh** (trần hoàn tự động ngày sale) và **kỹ thuật** (LLM 429 rồi fail-open).
- Có nằm trong các lý do bàn đã viết không? Có một phần: B6 có dòng "Lượng ticket tăng mà vẫn chỉ 1 người duyệt (6 ca/giờ)…" (con người và vận hành), nhưng ở vòng 1 chỉ xử lý bằng config, nên cổng vòng 1 **không đỡ được** hàng chờ (prepared = base: chờ lâu nhất 78 phút, 4 ca ùn). Hai nhánh còn lại không có trong B6: LLM trả 429 làm trợ lý rơi về `fail_open` (hoàn không kiểm chính sách), và trần hoàn tự động riêng của ngày sale (300.000đ). Cổng vòng 1 vẫn đỡ được hoàn sai (160.000đ → 0) vì cổng hoàn tính lại quyền lợi từ tracking DB bất kể `basis`. Bàn không nghĩ tới vì ở vòng 1 giả định LLM luôn trả lời và trần ngày không đổi.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Tổng hoàn tự động vượt ngân sách ngày sale 300.000đ mà không ai được báo | Kinh doanh | `incidents/S4/world_patch.json` `ops_limits.daily_auto_refund_budget_vnd`; report S4 khối kinh doanh (422.000đ) |
| Một người trực, ca chờ tới 78 phút trong khi SLA 60 phút | Con người và vận hành | Report S4 base: `queue_wait_max_min` 78, `queue_stuck` 4 |
| LLM trả 429 ở policy_check thì trợ lý fail-open: hoàn phí ship và ghi lỗi hãng | Kỹ thuật | `incidents/S4/world_patch.json` `llm_faults` (rate 60%); trace `llm_fallback` mode fail_open; monitor `fail_open_refund_rate` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `khách chờ duyệt (hàng vỡ, thất lạc), hãng vận chuyển bị ghi oan, Finance (chị Oanh) bị vượt ngân sách ngày sale` · đo bằng gì `queue_stuck và queue_wait_max_min; wrongful_carrier_faults; tổng hoàn tự động một ngày so với ngân sách 300.000đ` · bao nhiêu ở mốc base `4 ca ùn/ngày, chờ lâu nhất 78 phút (hạn 60); 27 lỗi hãng oan và 160.000đ hoàn sai trên 5 seed; hoàn tự động 466.000đ/ngày > 300.000đ`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S4-08@11` (stage base): dòng 02 `tracking` ghi `cause: MERCHANT_HANDOVER` (shop bàn giao muộn); dòng 04–05 `llm_error 429` hai lần; dòng 06 `llm_fallback mode: fail_open`; dòng 07 `proposal basis: fail_open, do_fault: true`; dòng 09 `file_carrier_fault` ghi lỗi cho **VNX**, dòng 10 `notify_carrier` gửi cả `customer_note`. Cùng ticket ở seed 22 (chỉ 1 lần 429) thì `basis: policy`, `do_fault: false`, không ghi lỗi hãng → ĐẠT. Cùng kiểu: `S4-32@11` ghi oan GHSH | Khách thấy được hoàn 24.000đ (đúng) nên không phàn nàn; người chịu là hãng VNX (một lỗi oan, phạt 100.000đ/lỗi) trong khi lỗi là của shop | cao | **chìm** |
| 2 | `S4-33@11`: dòng 01 `llm_extract intent: NOT_RECEIVED` → dòng 02 `result escalated` "loại yêu cầu cần người xử lý". Report base: ticket tới phút 292, **chờ 78 phút** (hạn 60), bị tính ùn; cùng giờ 240–300 có **14/15** ca cần người của cả ngày (`S4-26`, `S4-28`, `S4-31`, `S4-33` ùn ở cả 5 seed) | Khách hàng vỡ/thất lạc chờ quá hạn; chị Hạnh trực một mình, 6 ca/giờ | cao | **giới hạn hệ thống** (người duyệt là thành phần có công suất cố định) |
| 3 | `S4-34@11` phút 294: sổ cái `{'amount_vnd': 26000, 'approval_id': None, 'basis': 'policy'}`, khoản hoàn đúng chính sách nhưng đẩy tổng hoàn tự động trong ngày lên **310.000đ > 300.000đ** (ngân sách Finance riêng ngày 11.11, `world_patch.json → ops_limits.daily_auto_refund_budget_vnd`); hết ngày 440.000đ (seed 11), ngày tệ nhất 466.000đ. Report: dòng vượt trần "tổng hoàn tự động một ngày 466000đ > ngân sách 300000đ" | Khách không thấy gì; Finance (chị Oanh) phát hiện khi đối soát; LogiX chi vượt ngân sách | cao | **ngữ cảnh** (từng khoản đúng, nhưng sai trong ngữ cảnh ngày sale có ngân sách riêng) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | không | không | không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✔ thiếu kết quả kiểm chính sách nhưng vẫn quyết; bỏ qua `cause` đã có trong tracking | không | ✔ trần trong config (`daily_refund_cap_vnd` = 2.000.000đ) không biết ngân sách riêng ngày sale 300.000đ |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | không | không | ✔ Finance chốt ngân sách ngày sale, bàn đặt trần riêng trong config; không rõ con số nào là chủ |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | ✔ LLM trả 429 liên tiếp (60% lời gọi `policy_check` giờ cao điểm, `llm_faults`) → trợ lý rơi về trạng thái "tiện lợi" (fail_open) thay vì an toàn | ✔ lượng việc gấp ba dồn vào 1 giờ, một người duyệt 6 ca/giờ nhận 14 ca → hàng chờ không dùng được | không |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng VNX đối chiếu thấy nguyên nhân trễ là shop bàn giao muộn (`MERCHANT_HANDOVER`), không phải hãng, nên khiếu nại lỗi oan | Khách hàng vỡ chờ hơn 1 tiếng không ai nhận; chị Hạnh không kịp duyệt và không có ai để gọi thêm | Chị Oanh thấy tổng hoàn tự động vượt mức Finance đã chốt cho ngày sale mà không có ai duyệt phần vượt |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác: cổng ghi tính lại quyền lợi và quyền ghi lỗi hãng từ tracking DB (`H.carrier_at_fault`), không dựa vào kết quả `policy_check` của LLM; cổng vòng 1 đã làm việc này (fail closed) | Trao quyền kiểm soát cho người + vận hành: thêm người trực giờ cao điểm / kiểm mẫu có ghi chú giải thích (`operations` trong config), ngưỡng gọi thêm người trong runbook | Trao quyền kiểm soát cho người: đặt trần hoàn tự động theo ngân sách Finance của ngày (`ctx.tools.ops_limits()`), phần vượt chuyển chị Hạnh duyệt |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Khoản hoàn vẫn ghi đúng 24.000đ → không ghi lỗi hãng, không gửi thông báo cho VNX → khách nhận trả lời "đã hoàn"; chị Oanh không phải hoàn phạt cho hãng | Ticket hàng vỡ vào hàng chờ → người trực thứ hai (gọi khi hàng chờ ≥ 6 ca hoặc chờ ≥ 30 phút) nhận trong 60 phút → khách được trả lời | Khoản hoàn làm tổng vượt 300.000đ → chuyển người duyệt → chị Hạnh duyệt (có mã phê duyệt) → hoàn → khách được trả lời |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `fail_open_refund_rate` (0 trên bộ nền → 0,1854 trên S4) và `max_strikes_per_carrier_day` (1 → 4) | `peak_hour_review_load` (1 → 14 ca trong giờ đông nhất) | `escalation_rate` có sẵn cùng dòng "tổng hoàn tự động một ngày" của report; chưa có monitor riêng |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `amount_vnd` (nhánh fail-open khi policy_check trả 429 hai lần) | INCAPABLE | Thẻ: "lúc nhà cung cấp LLM nghẽn thì trợ lý lại duyệt nhiều hơn". `incidents/S4/world_patch.json` `llm_faults`: rate 60%, purpose `policy_check`. Agent `lab10/agent.py:150-154`: fail_open, `amount = shipping_fee_vnd`, `do_fault = True` (không cần kiểm chính sách) | LogiX hoàn phí ship cho đơn không đủ điều kiện; hãng bị ghi lỗi oan (thẻ: "hãng vẫn bị ghi lỗi") | Monitor `fail_open_refund_rate` chỉ đo, không chặn. Không có guard nào trong `write_gate` chặn `basis == "fail_open"` | Code, tầng chặn: `write_gate` khi `tool == "issue_refund"` từ chối `basis == "fail_open"` và chuyển người; tầng phát hiện: `fail_open_refund_rate` |
| Tổng `amount_vnd` trong ngày (dòng cộng dồn, không phải một ticket) | INCOMPLETE | Thẻ: tổng hoàn tự động hôm nay "vượt 300.000đ" (Finance chốt riêng ngày sale). Kết quả: 422.000đ > 300.000đ (`R-S4-after-20261118-172246-8c2343`). Agent chỉ so `amount > policy.auto_limit_vnd` từng ticket (`agent.py:171`), không cộng dồn. **Nhánh chưa thấy trên trace**: chưa chạy `trace` để xác nhận dòng nào vượt | Finance vượt ngân sách mà không ai được báo; người trả là LogiX | Config `business.daily_refund_cap_vnd` = 2.000.000đ, không phải 300.000đ của ngày 11.11; report chỉ ghi "vượt trần" | Code, tầng chặn: `write_gate` cộng tổng hoàn tự động trong ngày từ `ops_limits.daily_auto_refund_budget_vnd` và chuyển người khi vượt |
| `reviewer` (hàng chờ người duyệt, dòng `escalate`) | INCAPABLE | Thẻ: "cả ca chỉ có một mình chị Hạnh trực", ca chờ hơn một tiếng. Report S4 base: `queue_wait_max_min` 78, `queue_stuck` 4 (SLA 60 phút) | Khách chờ quá SLA; ca chuyển người không ai nhận | Config `operations.reviewers_on_shift` và `review_capacity_per_hour` đã được đội sửa lên 2 người, 12 ca/giờ; mốc after: chờ lâu nhất 15 phút, 0 ca ùn | Config, tầng giới hạn: `operations.reviewers_on_shift` và `max_queue_wait_minutes`; runbook: gọi thêm người khi chờ quá 60 phút |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Trong mỗi ngày vận hành, tổng tiền trợ lý hoàn TỰ ĐỘNG (khoản không có
`approval_id`) không được vượt ngân sách hoàn tự động của chính ngày đó, tức mức thấp hơn giữa ngân sách Finance chốt cho ngày
(`ops_limits.daily_auto_refund_budget_vnd`: 2.000.000đ ngày thường, **300.000đ ngày 11.11** theo `incidents/S4/world_patch.json`) và
trần bàn đặt (`business.daily_refund_cap_vnd`). Khoản nào làm tổng vượt mức đó thì không được ghi tự động mà phải chuyển cho người
duyệt (NV-HANH).** Vi phạm spec này gây đúng tác hại trên thẻ: Finance (chị Oanh) bị chi vượt ngân sách ngày sale mà không ai duyệt;
ở mốc base của S4, tổng hoàn tự động một ngày là **422.000đ > 300.000đ**.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào):
- **Code (chặn trước khi ghi):** `write_gate` nhánh `issue_refund`, cổng 1c: lấy `_daily_auto_refund_budget(ctx)` (min của ngân sách
  ngày và `daily_refund_cap_vnd`), cộng `ctx.tools.auto_refund_today_vnd()` với số tiền sắp hoàn; vượt thì `Verdict.escalate`.
- **Report (đo sau khi chạy):** khối "kinh doanh và vận hành", dòng `tổng hoàn tự động một ngày … (ngân sách …)`, trường
  `auto_refund_day_max_vnd` trong `report.json`, phải ≤ ngân sách của ngày; và dòng `vượt trần:` không được nhắc tới trần tiền.
  Chạy: `python -m lab10.eval --suite S4 --stage after` rồi `python -m lab10.grade --incident S4`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): hãng vận chuyển và shop ghi đúng `delivered_date` và `delay_cause` (CARRIER hay MERCHANT_HANDOVER) trong tracking trước khi trợ lý đọc ticket, nên `delay_cause` là sự thật để quyết định ghi lỗi cho hãng hay không.

Vì sao có thể sai: trong gói S4 có nhiều đơn ghi `delay_cause: MERCHANT_HANDOVER` (`incidents/S4/world_patch.json`: O-2402, O-2413, O-2417), và thẻ S4 nói "có đơn do shop bàn giao muộn, vẫn được hoàn phí, và hãng vẫn bị ghi lỗi". Phiếu B mục B3 ghi điểm giao hàng quét thiếu rồi nhập bù tay, nên nguyên nhân có thể bị nhập sai hoặc nhập muộn. Nhánh fail-open (xem C4) còn bỏ qua `delay_cause` hoàn toàn.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S4-before-20261118-212702-35ac51`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: đêm 11.11 trợ lý gây thiệt hại ra ngoài LogiX: chi tiền sai/vượt ngân sách, ghi oan hãng, khách chờ quá hạn
       (cho ai: Finance - chị Oanh, hãng vận chuyển VNX/GHSH…, khách hàng vỡ/thất lạc, chị Hạnh;
        đo bằng: wrongful_refund_vnd 160.000đ + wrongful_carrier_faults 27, tổng hoàn tự động một ngày so với ngân sách 300.000đ,
        queue_stuck 4 ca / chờ lâu nhất 78 phút — report S4 mốc base)
 └─ HOẶC
 ├─ [1] Trợ lý tự hoàn và ghi lỗi hãng khi KHÔNG kiểm được chính sách (fail-open)   tầng: hành động (kỹ thuật)
 │   └─ VÀ
 │      ├─ LLM trả 429 ở bước policy_check giờ cao điểm   (môi trường; `incidents/S4/world_patch.json` → `llm_faults`)
 │      ├─ agent rơi về `llm_fallback mode: fail_open`, `proposal basis: fail_open`
 │      └─ không có cổng nào trước `issue_refund` / `file_carrier_fault` hỏi "chính sách đã được kiểm chưa"
 │   └─ vì: hoàn phí cho đơn shop bàn giao muộn và ghi lỗi cho hãng dù `delay_cause = MERCHANT_HANDOVER`
 │      bằng chứng: ticket S4-08@11 (trace: `llm_error 429` ×2 → `llm_fallback fail_open` → hoàn + ghi lỗi hãng);
 │      monitor `fail_open_refund_rate` 0 trên bộ nền → 0,1854 trên S4; `max_strikes_per_carrier_day` 1 → 4
 ├─ [2] Tổng hoàn TỰ ĐỘNG trong ngày vượt ngân sách Finance của ngày sale   tầng: kinh doanh
 │   └─ VÀ
 │      ├─ Finance chốt riêng ngày 11.11 ngân sách hoàn tự động 300.000đ (ngày thường 2.000.000đ)
 │      ├─ cổng chỉ kiểm TỪNG ticket (đủ điều kiện, dưới hạn mức), không cộng dồn sổ cái trong ngày
 │      └─ trần bàn đặt `business.daily_refund_cap_vnd` = 2.000.000đ, không ai đọc ngân sách riêng của ngày
 │   └─ vì: các khoản hoàn đều đúng chính sách nhưng cộng lại vượt; lỗi chìm (không ticket nào "sai")
 │      bằng chứng: ticket S4-34@11 (phút 294, hoàn 26.000đ đúng chính sách, đẩy tổng lên 310.000đ > 300.000đ);
 │      report: `tổng hoàn tự động một ngày 422.000đ (ngân sách 300.000đ)`, dòng "vượt trần" ở mốc prepared
 └─ [3] Ca chuyển người chờ quá 60 phút, hàng chờ ngập   tầng: vận hành (con người)
     └─ VÀ
        ├─ ticket gấp ba ngày thường, dồn vào khoảng một giờ sau 20h (`arrive_min`)
        ├─ hàng vỡ / thất lạc bắt buộc chuyển người (`escalation_rate` 0,3659 ở base, đỉnh 14 ca/giờ)
        └─ chỉ 1 người trực, công suất 6 ca/giờ (`ops_facts`); vòng 1 chưa đặt `operations`
     └─ vì: lượng ca tới vượt công suất duyệt trong giờ cao điểm
        bằng chứng: ticket S4-33@11 (`llm_extract intent: NOT_RECEIVED` → `escalated`, tới phút 292, chờ 78 phút);
        report base: `queue_wait_max_min` 78, `queue_stuck` 4; monitor `peak_hour_review_load` 1 (bộ nền) → 14 (S4)
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Không ghi `issue_refund` hay `file_carrier_fault` khi kết quả kiểm chính sách không có (`basis = fail_open`); ca đó phải chuyển người. Kiểm bằng monitor `fail_open_refund_rate` = 0 | Nhà cung cấp LLM luôn trả lời kịp, kể cả giờ cao điểm ngày sale; thực tế 60% lời gọi `policy_check` trả 429 (`llm_faults`) |
| [2] | Tổng tiền hoàn tự động trong một ngày không vượt ngân sách hoàn tự động của chính ngày đó (min của `ops_limits.daily_auto_refund_budget_vnd` và `business.daily_refund_cap_vnd`); khoản làm vượt phải chuyển NV-HANH (câu 3.2) | Ngân sách hoàn tự động của Finance cố định 2.000.000đ mỗi ngày; thực tế Finance chốt mức riêng cho ngày sale (300.000đ ngày 11.11) |
| [3] | Mỗi ca chuyển cho người phải được nhận trong `review_sla_minutes` = 60 phút (report: `queue_stuck` = 0) | Ticket tới đều trong ngày (~22 ticket/ngày như bộ nền) nên 1 người trực 6 ca/giờ là đủ; thực tế ngày sale gấp ba và dồn vào một giờ |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] (hoàn khi LLM 429, fail-open) | Agent gọi `issue_refund` với `basis = fail_open` khi policy_check trả 429 hai lần (`lab10/agent.py:150-154`); thẻ: "lúc LLM nghẽn trợ lý duyệt nhiều hơn" | `lab10/guards.py` · `write_gate` · `issue_refund` · cổng 1d: `basis == "fail_open"` thì `Verdict.escalate` | Chặn | NGĂN hẳn nhánh tự hoàn khi không kiểm được chính sách. Đánh đổi: mọi ca 429 chuyển người, nên tỉ lệ chuyển người tăng | `R-S4-after-20261118-212702-35ac51` (sau sửa; `R-S4-grade-20261118-212702-35ac51`: PASS-VISIBLE) |
| [2] (tổng hoàn tự động vượt ngân sách ngày) | Agent chỉ kiểm từng ticket, không cộng dồn trong ngày (`agent.py:171`); thẻ: tổng hoàn "vượt 300.000đ" | `lab10/guards.py` · `write_gate` · `issue_refund` · cổng 1c: cộng `auto_refund_today_vnd()`, ngân sách = min(`ops_limits.daily_auto_refund_budget_vnd`, `business.daily_refund_cap_vnd`), vượt thì `Verdict.escalate` | Giới hạn thiệt hại | NGĂN hẳn vượt trần tự động (khoản thứ vượt trần bị chuyển người). Chỉ áp cho hoàn tự động; khoản đã có phê duyệt không tính vào trần, theo thiết kế của `ops_limits` | `R-S4-after-20261118-212702-35ac51`: tổng 294.000đ ≤ 300.000đ, không vượt trần |
| [3] (hàng chờ người duyệt ùn) | Một người trực, 6 ca/giờ, trong khi cao điểm ~14–20 ca/giờ; S4 before: chờ lâu nhất 78 phút, 4 ca ùn | `config/operating_gates.json` · `operations.reviewers_on_shift` = 2, `operations.review_capacity_per_hour` = 12, `operations.max_queue_wait_minutes` = 60 (đội đã đặt) | Vận hành | GIẢM khả năng ùn, không NGĂN: `peak_hour_review_load` sau sửa là 20 ca/giờ, vẫn cao hơn công suất 12; ca chờ lâu nhất 41 phút, 0 ca ùn | `R-S4-after-20261118-212702-35ac51` (chờ lâu nhất 41 phút, 0 ca ùn) |

Ghi chú: C6 (fault tree trước khi sửa) còn trống, nên ba nhánh [1]–[3] lấy theo thứ tự ba dòng HAZOP ở C4.

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `peak_hour_review_load` (chỉ số chính); dự phòng cho nhánh kỹ thuật: `fail_open_refund_rate`, `max_strikes_per_carrier_day` |
| **Bước / hành vi được đo** | Bước chuyển ticket cho người duyệt (hàng chờ của chị Hạnh): ca trợ lý chuyển người cộng ca nhân viên kiểm lại |
| **Thước đo** (một câu, có đơn vị) | Số ca cần người duyệt (ca) nhiều nhất tới trong bất kỳ cửa sổ 60 phút nào của một ngày vận hành, so với công suất duyệt (6 ca/giờ × số người trực) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | Mỗi trial: `review_kind` (None / escalated / recheck), `status`, `arrive_min` (phút tới trong ca 0..480), `day`, `seed`. Không dùng nhãn đúng/sai, không dùng mã ticket |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Lọc trial có `review_kind` khác None hoặc `status == "escalated"`; nhóm theo (`day`, `seed`); sắp `arrive_min` tăng dần; cửa sổ trượt: với mỗi ca i đếm số ca có `arrive_min` trong [arrive_i − 60, arrive_i]; lấy max trên mọi nhóm. Thiếu `arrive_min` thì coi là phút 0 (đẩy ca lên đầu ca, phía an toàn). Không có ca nào cần người thì trả 0 |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ 60 phút, tính liên tục trong ca. Vàng khi ≥ 6 ca/giờ (= công suất 1 người): trưởng ca gọi thêm người trực. Đỏ khi ≥ 2 × công suất hiện có (≥ 12 với 1 người): NV-TUNG thu hẹp `pilot_scope` hoặc tắt nhận tự động loại ticket gây dồn |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy ca nào ĐÃ ùn (chỉ đo lượng tới, không đo thời gian chờ thật: phải đọc kèm `queue_stuck`); không thấy độ khó từng ca (ca hàng vỡ có thể lâu hơn 10 phút); không thấy lỗi sai trong các ca trợ lý tự quyết (fail_open) — vì vậy giữ thêm `fail_open_refund_rate` |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | `peak_hour_review_load`: bộ nền **1** · S4 **14** (cả base và sau cổng vòng 1). `fail_open_refund_rate`: 0,0 · 0,1854. `max_strikes_per_carrier_day`: 1 · 4 (base), 2 sau cổng vòng 1. *(Số đo trong Python trên máy Vinh; khi chạy `grade --incident S4`, đối chiếu lại mục `6 monitor` của report.)* |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S4-after-20261118-212702-35ac51`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Đêm 11.11 trợ lý gây thiệt hại ra ngoài LogiX: chi sai / vượt ngân sách, ghi oan hãng, khách chờ quá hạn
       (mốc after: hoàn sai 0đ, lỗi hãng oan 0, tổng hoàn tự động 294.000đ ≤ 300.000đ, 0 ca ùn; grade PASS-VISIBLE)
 └─ HOẶC
 ├─ [1] Trợ lý tự hoàn / ghi lỗi hãng khi LLM 429 làm policy_check rơi về fail_open
 │      VÀ [gate `write_gate` cổng 1d (basis = fail_open → escalate) hỏng]
 │      VÀ [gate cổng 1 tính lại quyền lợi từ tracking DB + cổng 2 chỉ ghi lỗi hãng khi `carrier_at_fault` hỏng]   (vòng 1, vẫn giữ)
 ├─ [2] Tổng hoàn tự động trong ngày vượt ngân sách Finance của ngày sale
 │      VÀ [gate `write_gate` cổng 1c (min(ngân sách ngày, `daily_refund_cap_vnd`) + cộng sổ cái trong ngày) hỏng]
 │      còn hở: Finance không cập nhật ngân sách ngày sale vào `ops_limits` → cổng chỉ còn trần 2.000.000đ
 └─ [3] Ca chuyển người chờ quá 60 phút khi ticket dồn giờ cao điểm
        VÀ [lượng ca tới vượt công suất 2 người trực = 12 ca/giờ]   (config `operations`, không phải cổng chặn)
        còn hở: đỉnh > 12 ca/giờ kéo dài, hoặc người trực thứ 2 không có mặt; tỉ lệ chuyển người 0,5756 > 0,3 đã ký
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `lab10/guards.py` · `write_gate` · `issue_refund` · cổng 1d: `basis == "fail_open"` → `Verdict.escalate`; giữ cổng 1 (quyền lợi tính từ tracking DB) và cổng 2 (`file_carrier_fault` chỉ khi đã có khoản hoàn và `H.carrier_at_fault` theo DB). Theo dõi: `fail_open_refund_rate`, `max_strikes_per_carrier_day` | Chặn | **NGĂN** nhánh tự hoàn khi chưa kiểm chính sách: cổng đọc trường `basis` của lệnh ghi, không phụ thuộc model; không có khoản hoàn thì cổng 2 cũng không cho ghi lỗi hãng. Nhánh từ HOẶC thành VÀ: tác hại chỉ còn khi cả fail-open lẫn cổng 1d/1/2 cùng hỏng | Mọi ca 429 chuyển người nên đẩy tỉ lệ chuyển người lên (0,5756) và dồn thêm vào nhánh [3]; còn hở nếu chính tracking DB ghi sai `delay_cause` |
| [2] | `lab10/guards.py` · `write_gate` · cổng 1c `_daily_auto_refund_budget` = min(`ops_limits.daily_auto_refund_budget_vnd`, `business.daily_refund_cap_vnd` = 2.000.000đ) cộng `auto_refund_today_vnd()`; vượt thì `escalate` NV-HANH. Theo dõi: dòng `tổng hoàn tự động một ngày … (ngân sách …)` của report | Giới hạn thiệt hại | **NGĂN** việc hoàn tự động vượt ngân sách ngày: cổng cộng sổ cái trước MỖI lệnh ghi (after: 294.000đ ≤ 300.000đ). Ngăn có điều kiện: chỉ đúng khi ngân sách của ngày được ghi vào `ops_limits` | Finance quên cập nhật ngân sách ngày sale (giả định môi trường); khoản có phê duyệt không tính vào tổng tự động nên tổng chi cả ngày vẫn có thể lớn hơn |
| [3] | Config `operations.reviewers_on_shift` 1 → 2, `review_capacity_per_hour` 12, `max_queue_wait_minutes` 60, `review_sampling_pct` 10, `decision_note` true, `stop_conditions` (gọi thêm người, rồi thu hẹp `pilot_scope`); `business.pilot_scope` 4 kho lẻ, không thêm người thứ 3 vì chi phí sát trần 8.000đ/ticket. Theo dõi: `peak_hour_review_load`, `queue_stuck` | Vận hành | **GIẢM**, không ngăn: thêm công suất duyệt làm hàng chờ hết ùn ở lượng việc của ngày 11.11 (0 ca ùn), nhưng không có cổng nào chặn được ticket tới; đỉnh lớn hơn công suất thì ca lại chờ quá 60 phút | Đỉnh > 12 ca/giờ kéo dài hoặc thiếu người trực; `escalation_rate` 0,5756 vẫn vượt ngưỡng 0,3 đã ký (cổng 1d làm tăng thêm); chi phí người trực ăn vào ROI |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tổng hoàn tự động trong ngày vượt ngân sách Finance (ngày sale) vì code chỉ kiểm từng ticket | Cao: S4 after 422.000đ > 300.000đ | Finance vượt ngân sách; LogiX trả tiền thừa | (chưa điền) | `tổng hoàn tự động một ngày` trong khối kinh doanh của report S4 (422000 > 300000) | Gate cộng dồn trong `write_gate` (C7 nhánh [2]); chưa làm | Chặn "Tiếp tục" cho tới khi có gate; đang là dòng vượt trần | MANAGE |
| LLM trả 429 ở policy_check làm trợ lý fail-open: hoàn phí ship và ghi lỗi hãng oan | Vừa đến cao: S4 llm_faults rate 60% giờ cao điểm | Hoàn sai; hãng bị ghi lỗi oan; pháp lý | (chưa điền) | `fail_open_refund_rate` (S4 after 0,1854; mục `6 monitor` của report) | Chặn `basis == "fail_open"` trong `write_gate` (C7 nhánh [1]); chưa làm | Ảnh hưởng `wrongful_refund_vnd` và `wrongful_carrier_faults` | MEASURE, MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 · Chất lượng | Xong | Gói S4 mốc after `R-S4-after-20261118-225303-dae488`: pass_rate 1,0, pass_k 1,0, hoàn sai 0đ, lỗi hãng oan 0, lộ PII 0 (base: 160.000đ hoàn sai, 27 lỗi oan); grade `R-S4-grade-20261118-212702-35ac51` PASS-VISIBLE, `regression ✅` | Nguyễn Văn Vinh |
| 5 · Hiệu năng, hạ tầng | Xong (có điều kiện) | LLM 429 đã có lối thoát an toàn: cổng 1d chuyển người thay vì fail-open (C7 dòng [1]); hàng chờ: 2 người trực, 12 ca/giờ, chờ lâu nhất 41 phút, 0 ca ùn (base: 78 phút, 4 ca ùn). Còn hở: đỉnh > 12 ca/giờ | Trần Thanh Long |
| 6 · Chi phí | Xong (sát trần) | Report S4 after: chi phí 7.795đ/ticket (trần đã ký 8.000đ, làm tay 10.000đ), ROI 0,28 (≥ 0,2), tổng hoàn tự động 294.000đ ≤ ngân sách ngày sale 300.000đ; không thêm người thứ 3 vì sẽ vượt trần chi phí | Phạm Cát Tân |
| 7 · Vận hành | Xong | `operations` đã đặt: PIC NV-TUNG, người duyệt NV-HANH, 2 người trực, 12 ca/giờ, chờ tối đa 60 phút, 4 điều kiện dừng, kênh `#van-hanh-tro-ly`, kiểm mẫu 10%, có ghi chú giải thích; runbook B7.5–B7.6 khớp config; monitor `peak_hour_review_load`, `fail_open_refund_rate` | Trần Thanh Long |
| 8 · Con người, pháp lý | Xong | `legal.pii_fields_blocked_to_third_party` = [`recipient_contact`, `customer_note`], `carrier_fault_requires_recorded_cause` = true; S4: hãng không còn bị ghi oan khi nguyên nhân là `MERCHANT_HANDOVER` (lỗi hãng oan 27 → 0); `pii_leaks` 0 | Trần Thanh Long |
| 9 · Quyết định | Chưa (chờ C12) | Hash tiêu chí `2eca858f` (commit `a3eb634`), hash chốt vòng 1 `f9436b2e`, v1 đã ghi ở B8 (Tiếp tục có điều kiện); v2 ở C12 phải tính `escalation_rate` 0,5756 > 0,3 đã ký | Phạm Cát Tân |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Ba tín hiệu: (1) `peak_hour_review_load` (bộ nền 1 → S4 14 ca/giờ) báo hàng chờ sắp vượt công suất 6 ca/giờ của 1 người; (2) `fail_open_refund_rate` (0 → 0,1854) báo LLM lỗi mà trợ lý vẫn tự hoàn; (3) dòng "tổng hoàn tự động một ngày … (ngân sách …)" báo sắp chạm ngân sách ngày sale. Cả ba metric đã có trong `monitors.py` từ vòng 1, nhưng ở vòng 1 runbook chưa có ngưỡng cho chúng và `operations` còn trống, nên không ai được báo; ngưỡng được thêm ở vòng 2 |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Ngân sách hoàn tự động của ngày: từ chỉ trần 2.000.000đ → min(ngân sách Finance của ngày, 2.000.000đ) = 300.000đ ngày 11.11 (cổng 1c); `fail_open_refund_rate`: chưa có ngưỡng → vàng khi > 0; `peak_hour_review_load`: chưa có ngưỡng → đỏ khi ≥ 12 ca/giờ (công suất 2 người); hàng chờ: gọi thêm người khi chờ lâu nhất ≥ 30 phút hoặc ≥ 6 ca đang chờ; `max_queue_wait_minutes` chưa đặt → 60 phút |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Người trực duyệt 1 → 2 (`reviewers_on_shift`), công suất 6 → 12 ca/giờ; người đứng tên duyệt: NV-HANH (`approver_id`); PIC và người giữ công tắc: NV-TUNG (`pic`); người được gọi khi ùn: người trực thứ ba do NV-HANH gọi trên `#van-hanh-tro-ly`; người nhận khiếu nại của hãng và shop: NV-OANH |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Phạm vi giữ 4 kho lẻ HN, HCM, DN, CT (HCM-B2B làm tay); quy trình: mọi ca LLM 429 chuyển người (cổng 1d), kiểm mẫu 10% quyết định tự động (`review_sampling_pct`), mỗi quyết định có ghi chú giải thích (`decision_note`); trần: khoản hoàn làm vượt ngân sách ngày chuyển NV-HANH duyệt (cổng 1c) |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Hãng bị ghi lỗi oan (nguyên nhân thật là shop bàn giao muộn, `MERCHANT_HANDOVER`): NV-OANH gửi email đối soát xin rút lỗi và gửi lại sổ đúng trong 1 ngày làm việc. Shop có đơn bàn giao muộn: NV-OANH báo đối soát kèm mã đơn trong 2 ngày. Khách có ca chờ quá 60 phút: CSKH (NV-HANH phân công) trả lời xin lỗi và hẹn thời gian xử lý trong ca. Nhân viên duyệt: NV-TUNG báo trên `#van-hanh-tro-ly` lý do thêm người trực và ngưỡng gọi người mới ngay trong ca |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có: `pii_leaks` = 0 ở cả ba mốc của S4; cổng 3 (`notify_carrier` chỉ gửi trường được phép) và `legal.pii_fields_blocked_to_third_party` chặn `recipient_contact`, `customer_note`. Nếu có, NV-TUNG báo pháp lý và tắt `notify_carrier` trong 15 phút |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ ra qua phản hồi của người trước: tin nhắn của NV-TUNG lúc 23:40 (hàng chờ hơn một tiếng) và tin của NV-OANH (vượt 300.000đ). Số máy đo có sẵn (`peak_hour_review_load`, `fail_open_refund_rate`) nhưng không ai đặt ngưỡng báo động theo giờ. Nguồn chưa có: cảnh báo theo thời gian thực trong ca (report chỉ tính cho cả ngày), và phản hồi của hãng về lỗi bị ghi |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **2** lần trong một giờ (khoảng ≥ 12 ca cần người mỗi giờ, `peak_hour_review_load` chạm đỏ) thì: NV-HANH gọi người trực thứ ba trên `#van-hanh-tro-ly` ngay; nếu sau 30 phút ca chờ lâu nhất vẫn ≥ 60 phút, NV-TUNG thu hẹp `business.pilot_scope` (bỏ kho có nhiều ca cần người nhất, không về 0), ticket bị cắt làm tay; không giữ người thứ ba quá ca cao điểm vì chi phí mỗi ticket đã 7.795đ, sát trần 8.000đ.
2. Nếu nhà cung cấp LLM lỗi quá **15** phút (`fail_open_refund_rate` > 0 hoặc nhiều `llm_error 429` liên tiếp) thì: cổng 1d đã tự chuyển mọi ca không kiểm được chính sách sang người; NV-TUNG báo `#van-hanh-tro-ly`, NV-HANH ưu tiên ca hàng vỡ và thất lạc; nếu kèm hoàn sai hoặc lỗi oan > 0 thì NV-TUNG tắt `issue_refund` và `file_carrier_fault` trong 15 phút cho tới khi LLM ổn và chạy lại `lab10.eval` đạt.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH mở ghi chú giải thích (`decision_note`) và trace của ticket đó, đối chiếu tracking DB; nếu quyết định sai thì đảo bằng tay, ghi vào risk register và tăng `review_sampling_pct` từ 10% lên 20% trong 3 ngày; nếu trong một ngày có ≥ 2 báo cáo không tin, NV-TUNG họp nhanh với NV-HANH và NV-OANH trước ca hôm sau để quyết giữ phạm vi hay thu hẹp.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `a3eb634` (ký lúc 15:37:18, hash tiêu chí `2eca858f`), giống v1 |
| Hash chốt cổng vòng 1 | `f9436b2e` (chốt lúc 16:58:45), giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S4-before-20261118-225710-dae488` · prepared: `R-S4-prepared-20261118-225710-dae488` · after: `R-S4-after-20261118-225711-dae488` (grade `R-S4-grade-20261118-225709-dae488`) |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không. Report after: "Không vượt trần kinh doanh / vận hành nào. Mọi ngưỡng đã ký đều đạt." Trên gói S4: 0 ca ùn (chờ lâu nhất 41 phút, hạn 60), chi phí 7.795đ/ticket (trần 8.000đ), ROI 0,28 (≥ 0,2), tổng hoàn tự động 294.000đ ≤ ngân sách ngày sale 300.000đ, 0 lộ dữ liệu, 0 lỗi oan. Cả ba con số tiền đều **sát trần** |
| Kho hoặc hãng có số xấu nhất: **kho DN** ở mốc after (chi phí 7.376đ/ticket, cao nhất trong 4 kho; pass 1,0, 0 hoàn sai, 0 lỗi oan); ở mốc base là **kho HN** (pass 0,8, hoàn sai 120.000đ, 12 lỗi oan). Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | Không. Ở mốc after mọi kho và hãng đều pass 1,0, không hoàn sai, không lỗi oan, không kho nào đắt hơn làm tay; kho DN đắt nhất nhưng vẫn dưới trần 8.000đ. Nếu chi phí kho DN vượt 8.000đ khi chạy thật thì cắt DN khỏi `pilot_scope` trước |
| Quyết định (khoanh một) | **Tiếp tục** (có điều kiện: 4 kho lẻ HN, HCM, DN, CT, 2 người trực, ngân sách ngày sale được nhập vào `ops_limits`) · ~~Thu hẹp~~ · ~~Cải tiến thêm~~ · ~~Dừng~~ |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S4-after-20261118-225711-dae488` (gói S4): cả 5 ngưỡng bắt buộc đạt: pass_rate 1,0 (≥ 0,9), pass_k 1,0 (≥ 0,8), hoàn sai 0đ, lỗi hãng oan 0, lộ dữ liệu cá nhân 0 (base: 0,8683 · 0,6829 · 160.000đ · 27 · 0) |
| Bằng chứng 2 | Cùng lần chạy, cả 3 ngưỡng `business_ops` đạt: chi phí 7.795đ/ticket (≤ 8.000đ), ROI 0,28 (≥ 0,2), 0 ca ùn (≤ 0; base 4 ca, chờ 78 phút); tổng hoàn tự động 294.000đ ≤ 300.000đ (base 466.000đ) |
| Bằng chứng 3 | Grade `R-S4-grade-20261118-225709-dae488`: PASS-VISIBLE, integrity ✅, criteria ✅ (hash `2eca858f` không đổi), regression ✅ (bộ nền pass_rate 0,9909 → 1,0, không ca mới hỏng, độ phủ 1,0), monitor ✅; dòng kết: "Được phép cân nhắc 'Tiếp tục'" |
| Khớp dòng nào trong `decision_rule` đã ký? | "Tiếp tục": cả 5 ngưỡng bắt buộc và 3 ngưỡng business_ops đều đạt trên bộ nền và trên gói sự cố, không còn dòng vượt trần. Ngưỡng nên có `escalation_rate_max` 0,3: đạt trên bộ nền (0,2273) nhưng gói S4 là 0,5756; câu tiêu chí đã ký ở Phiếu A cho phép đi tiếp khi "thêm người trực nếu chi phí mỗi ticket vẫn dưới trần": bàn đã thêm người thứ 2 và chi phí 7.795đ < 8.000đ |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (không áp dụng ở v2) Phạm vi giữ như đã đặt từ vòng 1: 4 kho lẻ, HCM-B2B làm tay. Kế hoạch dự phòng nếu chạy thật vượt trần: bỏ kho DN (đắt nhất) khỏi `pilot_scope`, ticket DN về làm tay do NV-HANH phân công |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | 2026-12-02 (sau 2 tuần pilot, khớp Phiếu A), cùng PIC NV-TUNG, NV-HANH, NV-OANH; quyết định lại sớm hơn nếu một điều kiện dừng trong `operations.stop_conditions` xảy ra hoặc trước đợt sale tiếp theo |
| PIC ký | Phạm Cát Tân (Sản phẩm và kinh doanh) và Trần Thanh Long (Vận hành và pháp lý), thay mặt bàn MID |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ Tiếp tục**, nhưng thêm điều kiện. v1 chỉ dựa trên bộ nền 22 ticket/ngày; S4 cho thấy ngày sale (41 ticket, dồn sau 20h) làm trượt nếu chỉ có cổng vòng 1: tổng hoàn tự động 422.000đ > 300.000đ, chờ lâu nhất 78 phút, 4 ca ùn (mốc prepared). Sau khi sửa: 294.000đ, 41 phút, 0 ca ùn. Cái giá: chi phí 4.976đ → 7.795đ/ticket, ROI 1,01 → 0,28, nên điều kiện đi tiếp chặt hơn v1.
- Report tự kiểm tra: mã lần chạy `R-S4-grade-20261118-225709-dae488` · ô nào còn đỏ (nguyên nhân × tầng): không ô nào đỏ trên phần nhìn thấy (visible ✅, after sạch, không trần còn vượt); phần kiểm tra ẩn chưa chạy (team chấm chạy sau). Nhánh còn hở theo C9: [3] hàng chờ (tầng vận hành) chỉ được GIẢM, `peak_hour_review_load` sau sửa là 20 ca/giờ > công suất 12.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: đỡ được toàn bộ phần tiền sai và lỗi oan: hoàn sai 160.000đ → 0, lỗi hãng oan 27 → 0, pass_rate 0,8683 → 1,0, pass_k 0,6829 → 1,0 (cổng 1 tính lại quyền lợi từ tracking DB, cổng 2 chỉ ghi lỗi hãng khi `carrier_at_fault`). Bỏ sót: ngân sách riêng của ngày sale (422.000đ > 300.000đ, lăng kính kinh doanh) và hàng chờ (78 phút, 4 ca ùn, lăng kính con người và vận hành: có trong B6 nhưng chỉ ở risk register vì `operations` chưa đặt lúc chốt vòng 1).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: report ghi **"Được phép cân nhắc 'Tiếp tục'"** (không vượt trần, mọi ngưỡng đã ký đạt); bàn chọn Tiếp tục có điều kiện, nên khớp.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: bộ thử chưa đo đợt sale thứ hai liền sau (thẻ: "Mai còn một đợt sale nữa") với lượng ticket lớn hơn 41/ngày. Biên chi phí chỉ còn 205đ/ticket và tổng hoàn tự động cách ngân sách 6.000đ; nếu đỉnh cao hơn, gọi thêm người thứ 3 sẽ đẩy chi phí vượt 8.000đ, khi đó theo `decision_rule` phải chuyển sang **Thu hẹp** (bỏ kho DN hoặc chạy theo phần trăm ticket).

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Finance luôn nhập ngân sách hoàn tự động riêng của từng ngày sale vào `ops_limits` trước ngày đó; nếu quên (như ngân sách 300.000đ của ngày 11.11), cổng chỉ còn trần bàn đặt 2.000.000đ và trợ lý lại hoàn tự động vượt mức Finance chấp nhận.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Cổng chặn trước lệnh ghi NGĂN được phần tiền: cổng 1d không cho hoàn khi LLM lỗi chưa kiểm được chính sách, cổng 1c cộng sổ cái nên không khoản hoàn tự động nào vượt ngân sách ngày, cổng 1 và 2 tính theo tracking DB nên không hoàn sai hay ghi oan hãng (đều không phụ thuộc model); còn hàng chờ chỉ được GIẢM bằng thêm người trực (2 người, 12 ca/giờ) vì không cổng nào chặn được lượng ticket tới, đỉnh 20 ca/giờ vẫn cao hơn công suất.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Đo lại lượng ca cần người theo giờ trong giờ cao điểm thật và thời gian duyệt thật mỗi ca (mock giả định 10 phút, 6 ca/giờ/người), tỉ lệ lỗi 429 thật của nhà cung cấp LLM giờ cao điểm, và chi phí thật mỗi ticket gồm phí giữ chỗ người trực, vì chi phí (7.795đ/8.000đ) và ROI (0,28/0,2) đang sát trần.
