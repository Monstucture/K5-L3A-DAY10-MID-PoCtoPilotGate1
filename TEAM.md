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
|   1 | Trần Thanh Long | 2A202603674 | Vận hành và pháp lý | [x] |
|   2 | Nguyễn Văn Vinh | 2A202603672 | Kỹ sư cổng |             |
|   3 | Phạm Cát Tân | 2A202603678 | Sản phẩm và kinh doanh |            |
|   4 |Bùi Anh Dũng           |2A202603687      | Kỹ sư cổng     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranThanhLong-2A2026603674

### Phần việc phụ trách

Vai trong bàn: Vận hành và pháp lý ; Form a: 1.2, 1.3,... 

### Đóng góp cụ thể

...

### Bằng chứng



### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
