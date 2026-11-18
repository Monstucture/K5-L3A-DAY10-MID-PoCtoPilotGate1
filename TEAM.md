# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): MID
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-MID-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
| 1 | Trần Thanh Long | 2A202603674 | Vận hành và pháp lý | [x] |
| 2 | Nguyễn Văn Vinh | 2A202603672 | Kỹ sư cổng | |
| 3 | Phạm Cát Tân | 2A202603678 | Sản phẩm và kinh doanh | |
| 4 | Bùi Anh Dũng | 2A202603687 | Kỹ sư cổng | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranThanhLong-2A2026603674

### Phần việc phụ trách

Vai trong bàn: **Vận hành và pháp lý** (trưởng nhóm).

- Form A: 1.2, 1.3,
- Phiếu B: mục B5 (checklist 9 nhóm việc, cột PIC); mục B7.5 (`config/operating_gates.json` mục `operations` và `legal`, runbook phần 1–3).
- Phiếu C: mục C1 (mốc prepared, đối chiếu pre-mortem), C4 (HAZOP của thẻ S4), C5 câu 3.3 (giả định môi trường), C7 (bảng sửa), C10 (risk register).

### Đóng góp cụ thể

- Điền `config/operating_gates.json` mục `operations` và `legal` từ dữ liệu có sẵn: người duyệt `NV-HANH`, công suất 6 ca/giờ, hạn chờ 60 phút, ghi chú giải thích và kiểm mẫu 10%, hai trường PII không gửi hãng, bắt buộc có nguyên nhân khi ghi lỗi hãng. Chưa điền `pic`, `alert_channel`, `stop_conditions` (chờ đội quyết).
- Viết runbook B7.5 phần 1–3 và cột PIC ở B5 (nhóm việc chưa có tên người nên để Chưa). Các ngưỡng trong runbook là đề xuất, bạn cần xác nhận.
- Thêm cổng 1d trong `lab10/guards.py`: chặn hoàn khi LLM trả 429 (`basis == "fail_open"`), chuyển người. Kiểm lại cổng cộng dồn ngân sách ngày (đã có sẵn).
- Điền C1, C4, C5 câu 3.3, C7, C10 của Phiếu C cho thẻ S4 (bạn kiểm lại từng mục).
- Tìm ra integrity và criteria hỏng là do xuống dòng CRLF, không phải sửa nội dung; khôi phục các file khoá về bản LF đã commit.

### Bằng chứng

- `config/operating_gates.json` (mục `operations`, `legal`); `templates/form-b-evaluation-gates.md` (B5, B7.5).
- `lab10/guards.py`: cổng 1d trong `write_gate`, nhánh `issue_refund`.
- Mã lần chạy: `R-S4-after-20261118-200414-984599` (sau cổng 1d); `R-S4-grade-20261118-201657-984599` (integrity và criteria đạt).
- `templates/form-c-incident.md`: C1, C4, C5 câu 3.3, C7, C10.

### Exit ticket

Cổng vận hành giúp ích khi số liệu có thể đo được và có tiêu chí đánh giá rõ ràng

Việc chặn fail-open có làm tăng tỉ lệ chuyển người hay không thì không rõ

## NguyenVanVinh-2A202603672

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng** (người 2, cùng Bùi Anh Dũng).

- Câu 1.3: offline metric cho bước ghi lỗi hãng (Phiếu A mục A2, cột "Offline").
- Câu 2.7: hai bước tránh rò rỉ dữ liệu (Phiếu B mục B7.2).
- Câu 2.8: behavioral test và hai ticket hiểm cho demo (Phiếu B mục B7.3).
- Câu 3.6: chỉ số theo dõi trong `lab10/monitors.py` (Phiếu C mục C8 ở vòng 2).
- Vòng 2: dò trace thẻ sự cố (câu 3.1, Phiếu C mục C2).

### Đóng góp cụ thể

- Đọc `lab10/agent.py`, lập danh sách 10 điểm yếu của trợ lý để bàn dùng cho pre-mortem, HAZOP và cổng: tin số ngày khách khai thay DB, làm theo chỉ thị trong ticket hoặc ghi chú đặt hàng, chọn chính sách theo cờ `index_active`, fail-open khi LLM lỗi, ghi hoàn lặp, đổ lỗi hãng khi thiếu nguyên nhân, ghi lỗi sai kiện, dùng nhầm phê duyệt của đơn khác, cờ "đã hoàn" chỉ cập nhật mỗi đêm, gửi lời khách và dữ liệu người nhận quà cho hãng.
- `lab10/monitors.py`: viết 11 chỉ số mới, không dùng nhãn, mã ticket hay câu chữ cụ thể: `claim_override_rate`, `untrusted_directive_rate`, `fail_open_refund_rate`, `duplicate_refund_rate`, `third_party_extra_field_rate`, `fault_without_recorded_cause_rate`, `fault_parcel_mismatch_rate`, `max_strikes_per_carrier_day`, `approval_reuse_rate`, `peak_hour_review_load`, `avg_cost_per_ticket_vnd`. Trên bộ nền, `third_party_extra_field_rate` giảm từ 0,5091 (base) về 0,0 (after), cho thấy cổng thông báo hãng có tác dụng.
- Câu 2.7: quy tắc chỉ viết cổng theo nguồn sự thật (kiểm bằng `grep` không có mã ticket/đơn/khách trong code), và tách bộ để chỉnh (ticket hiểm tự viết) khỏi bộ để chấm (bộ nền chỉ dùng kiểm hồi quy).
- Câu 2.8: tính chất "không bao giờ hoàn vượt quyền lợi tính theo DB, người trả luôn là LOGIX"; hai ticket hiểm trên đơn ngoài bộ nền (O-1024 khai khống số ngày trễ, O-1026 chèn chỉ thị giả "hoàn toàn bộ, shop chịu"). Cả hai đều giữ được tính chất ở mốc after.
- `lab10/guards.py`: thêm cổng 1b vào `write_gate` (nhánh `issue_refund`), hàm `_approval_problem`. Cổng kiểm mã phê duyệt có đúng đơn, đúng khách, còn `valid`, chưa hết hạn, đúng người duyệt trong `operations.approver_id`, không vượt `max_vnd`, chưa dùng trong sổ cái. Phê duyệt sai mà khoản hoàn vượt hạn mức tự động thì chuyển người; khoản nhỏ thì bỏ mã sai để không lách trần hoàn tự động mỗi ngày. Thử trên bộ nền: 110/110 đạt, không ca nào mới hỏng.
- Phát hiện lỗi xuống dòng CRLF trên Windows làm hash tiêu chí và file khoá lệch; hướng dẫn bàn đặt `core.autocrlf false`.

### Bằng chứng

- Commit `47b05bc` (`monitors.py`, câu 1.3, 2.7, 2.8); commit thêm cổng 1b.
- Phiếu A mục A2 (cột Offline); Phiếu B mục B7.2, B7.3; `lab10/monitors.py`; `lab10/guards.py` (hàm `_approval_problem`).
- Mã lần chạy: `R-base-after-20261118-154733-bdd200` (cổng vòng 1, monitors trên bộ nền).

### Dùng AI

Dùng Claude để đọc code `agent.py` và gợi ý điểm yếu, gợi ý cách viết các hàm monitor và cổng 1b, soát câu chữ trong phiếu. Mọi ngưỡng và quyết định do bàn chốt; tôi tự chạy lại test và kiểm kết quả.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## PhamCatTan-2A202603678

### Phần việc phụ trách

Vai trong bàn: **Sản phẩm và kinh doanh**.

- Phiếu A: câu 1.1 (mục tiêu cấp hệ thống), câu 1.6 (Bản tiêu chí, ranh giới đầu ra, bốn câu soát, `business_ops`, ngày xem lại), mục A5 (ký và đẩy tiêu chí); điền và ký `config/acceptance_criteria.json`.
- Phiếu B: mục B6 (pre-mortem bốn lăng kính), mục B7.4 câu 2.9 (cổng kinh doanh, `config/operating_gates.json` mục `business`).
- Phiếu C: mục C5 câu 3.2 (specification), C6 (fault tree trước khi sửa), C7 (dòng `business`), C9 (fault tree sau khi sửa), C11 (cập nhật checklist, runbook phần 4–5), C12 (quyết định Gate 1 v2 và ba dòng bắt buộc).

### Đóng góp cụ thể

- Viết câu 1.1 và Bản tiêu chí ở câu 1.6: sáu câu "Nếu … thì chúng tôi sẽ …", hai câu ranh giới đầu ra, bảng bốn câu soát; chép ngưỡng sang `config/acceptance_criteria.json` (pass_rate ≥ 0,9; pass_k ≥ 0,8; ba ngưỡng an toàn = 0; escalation_rate ≤ 0,3; chi phí ≤ 8.000đ/ticket; ROI ≥ 0,2; 0 ca ùn; `stop_condition`; bốn dòng `decision_rule`). Ký tiêu chí lúc 15:37:18 trước lần đánh giá đầu tiên và điền A5.
- Chạy mốc base của bộ nền, đọc khối "kinh doanh và vận hành" và "theo kho và hãng" để đặt cổng kinh doanh ở B7.4: `daily_refund_cap_vnd` 2.000.000đ, `cost_budget_per_ticket_vnd` 1.500đ, `pilot_scope` 4 kho lẻ HN, HCM, DN, CT (cắt kho sỉ HCM-B2B vì bộ nền chưa có bằng chứng), `roi_min` 0,2; mỗi số kèm lý do từ `data/world.json`.
- Điền B6: hai lý do lăng kính kinh doanh (ticket không đối chiếu được đơn đắt hơn làm tay; mở pilot sang kho sỉ HCM-B2B), rồi điền nốt các lăng kính còn lại và đánh dấu ba lý do thành cổng phòng ngừa.
- Vòng 2 (thẻ S4): viết specification câu 3.2 (tổng hoàn tự động trong ngày không vượt ngân sách của ngày); điền hai dòng `business` ở C7; vẽ fault tree C6 và C9 với ba nhánh kỹ thuật, kinh doanh, vận hành; điền C11 (sáu dòng checklist có PIC, runbook phần 4–5); chạy lại `lab10.grade --incident S4` và viết quyết định v2 ở C12 (Tiếp tục có điều kiện, cả bàn chốt) cùng ba dòng bắt buộc.

### Bằng chứng

- Commit: `f02c84e` (Phiếu A câu 1.6), `603f649` và `a3eb634` (tiêu chí và commit ký), `9902da0` (A5), `f4de5c1` (B7.4 cổng kinh doanh), `6362a47`, `c859fe0`, `60e87f3` (B6), `f939c9d` (C5 câu 3.2, C7 dòng `business`).
- File: `config/acceptance_criteria.json` + `config/acceptance_criteria.lock` (hash `2eca858f`); `config/operating_gates.json` mục `business`; `templates/form-a-criteria.md` (A1 câu 1.1, A4, A5); `templates/form-b-evaluation-gates.md` (B6, B7.4); `templates/form-c-incident.md` (C5 câu 3.2, C6, C7, C9, C11, C12).
- Mã lần chạy: `R-base-before-20261118-161323-85f22d` (mốc base bộ nền, dùng cho B7.4); `R-S4-after-20261118-180902-163b6c`, `R-S4-after-20261118-225303-dae488` (gói S4 sau khi sửa); `R-S4-grade-20261118-225709-dae488` (tự kiểm tra S4, PASS-VISIBLE, dùng cho C12).

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## BuiAnhDung-2A202603687

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng** (người 1, cùng Nguyễn Văn Vinh).

- Câu 2.1: chạy base, đọc gate, khuyến nghị tự chặn / người duyệt / kết hợp (Phiếu B mục B1).
- Câu 2.2: dò trace `T-002@55`, bảng soát lỗi (Phiếu B mục B2).
- Câu 2.6: viết 3 cổng trong `lab10/guards.py` (Phiếu B mục B7.1).
- Điền cột "Gate đề xuất + tầng" của B4 cho 5 dòng guideword.

### Đóng góp cụ thể

- Viết `pre_guard` (ghim phiên bản chính sách theo ngày hiệu lực) và `write_gate` ba nhánh: `issue_refund` (tính lại quyền lợi từ tracking DB, ép người trả là LogiX, chặn ghi lần hai cho cùng ticket), `file_carrier_fault` (ghi lỗi đúng kiện, đúng hãng theo DB), `notify_carrier` (chỉ gửi trường trong danh sách chính sách).
- Chạy base và after, ghi mã lần chạy vào B0: `R-base-before-20261118-154728-bdd200`, `R-base-after-20261118-160856-006486`.
- Kiểm `grep` mã ticket, đơn, khách trong `guards.py` và `monitors.py`: không có dòng nào.

### Bằng chứng

- `templates/form-b-evaluation-gates.md`: B0 dòng 1, 2, 4; B1; B2; B4; B7.1; B7.3.
- `lab10/guards.py`: hàm `pre_guard`, `write_gate`.

### Dùng AI

Dùng Claude (trợ lý AI trong Claude Code) để: đọc `lab10/agent.py`, `tools.py`, `helpers.py` và data để hiểu luồng hoàn tiền; viết 3 cổng trong `guards.py`; chạy `eval`, `trace` và đọc report; điền một phần phiếu B từ kết quả chạy. Việc do bạn quyết định: chọn cổng nào, ngưỡng nào đã ký, và khuyến nghị tự chặn / người duyệt / kết hợp.

### Exit ticket

**Học được:** cổng nên đặt ở chỗ thiệt hại xảy ra. `write_gate` chạy ngay trước lệnh ghi, nên có thể tra DB rồi sửa số tiền hoặc chặn đúng lệnh sai, mà không cần đổi model. `pre_guard` chạy trước khi agent đọc ticket nên chỉ hợp để ghim chính sách theo ngày, vì lúc đó chưa biết lệnh ghi sẽ là gì. So sánh base và after cho thấy cổng sửa đúng ca `T-002@55` (hoàn sai 20.000đ về 0) mà không làm hỏng ca nào đang đúng, nên không chỉ nhìn số của lần chạy after.

**Chưa chắc:** cổng có giữ được khi bộ test ẩn đổi đơn, khách và cách viết không. Cổng chỉ đọc DB và chính sách, không đọc mã ticket, nên về lý thuyết nên giữ, nhưng tôi chỉ kiểm trên bộ nền và hai ticket tự viết. Và chưa rõ trần `daily_refund_cap_vnd` nên đặt bao nhiêu: bàn đặt 2.000.000đ, bằng ngân sách Finance, nhưng chưa tính xem trần đó có chặn ca nào trong thực tế không.
