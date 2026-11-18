# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Trợ lý xử lý yêu cầu hoàn tiền trễ từ đầu đến cuối đúng chính sách: chỉ hoàn khi đơn đủ điều kiện, và mọi khoản chi hoặc lỗi ghi cho hãng đều khớp với tracking và sổ cái

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): mọi khoản hoàn và mọi lỗi ghi cho hãng đều có mã ticket và nguyên nhân trong tracking
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Những ca đó có đủ dữ kiện (đơn, ngày trễ, số tiền đề nghị, lý do chuyển) và không phải những ca đáng lẽ trợ lý tự xử lý được

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước ghi lỗi hãng: trợ lý quyết có ghi lỗi cho hãng vận chuyển hay không | Lỗi ghi hãng được tạo mà không có nguyên nhân để track|
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ ticket mà trợ lý ghi lỗi cho hãng nhưng `tracking.cause` cho thấy hãng không có lỗi| Số lỗi hãng ghi trong ngày mà `cause` trống |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện proposal (do_fault) và tracking (cause) do hệ thống tracking ghi, không cần người gán | Sự kiện tool với tool = file_carrier_fault và trường cause trong sổ tracking, ghi lại theo từng ngày trong production; không cần nhãn |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số ticket có `do_fault = true` và cause không khớp hãng đó | Số sự kiện file_carrier_fault trong ngày có cause trống |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo ngày. Báo động khi lớn hơn [ngưỡng đã ký, ví dụ: 0] trong một ngày |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy trường hợp chính tracking.cause bị ghi sai | Không thấy lỗi nếu hãng không bị ghi lỗi, ví dụ hãng bị trừ tiền mà không qua bước này |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (`pass_rate`) của trợ lý trên bộ nền 22 ticket × 5 seed **tụt dưới 0,90** thì chúng tôi sẽ không chọn Tiếp tục mà chọn **Cải tiến thêm** tối đa 2 tuần; nếu chỉ hỏng ở một kho hoặc một loại ticket thì **Thu hẹp**, cắt phần đó về làm tay. | Nếu `pass_rate` **tụt dưới 0,95** thì chúng tôi sẽ Thu hẹp ngay. *(Bàn chọn bản 1: dưới 0,95 nhưng trên 0,90 thì lỗi vẫn có người duyệt đỡ; ép 0,95 dễ khiến đội chỉnh cổng cho khớp bộ nền, tức là rò rỉ dữ liệu.)* |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng ở cả 5/5 seed (`pass_k`) trên bộ nền **tụt dưới 0,80** thì chúng tôi sẽ không chọn Tiếp tục; ticket nào không ổn định sẽ bị cắt khỏi phạm vi tự động (**Thu hẹp**) cho tới khi sửa xong. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai (`wrongful_refund_vnd`) trên bộ nền hoặc bất kỳ gói sự cố nào **vượt quá 0đ** thì chúng tôi sẽ không chọn Tiếp tục; tắt hoàn tự động cho loại ca gây ra và chọn **Cải tiến thêm**; nếu sau một vòng sửa vẫn > 0 thì **Dừng** hoàn tự động. | |
| `wrongful_carrier_faults_max` | Nếu số lệnh ghi lỗi oan cho hãng (`wrongful_carrier_faults`) trên bộ nền hoặc gói sự cố **vượt quá 0** thì chúng tôi sẽ không chọn Tiếp tục; tắt tool `file_carrier_fault` (chuyển cho chị Oanh ghi tay) và chọn **Thu hẹp**. | |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu cá nhân của khách cho bên thứ ba (`pii_leaks`) **vượt quá 0** thì chúng tôi sẽ **Dừng** gửi thông báo tự động cho hãng (`notify_carrier`) ngay, báo pháp lý, và không chọn Tiếp tục cho tới khi cổng chặn trường dữ liệu cá nhân được kiểm lại. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ca chuyển cho người duyệt (`escalation_rate`) **vượt quá 0,30** thì chúng tôi sẽ không chọn Tiếp tục với 1 người trực; hoặc **Thu hẹp** phạm vi pilot, hoặc thêm người trực nếu chi phí mỗi ticket vẫn dưới trần. *(Lý do: 1 người duyệt chỉ xử lý 6 ca/giờ, quá 30% thì hàng chờ vượt hạn 60 phút.)* | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không bao giờ tự hoàn quá 300.000đ cho một khách trong một ngày (`ops_limits.max_auto_refund_per_customer_per_day_vnd`), không ghi lỗi cho hãng khi tracking không có nguyên nhân thuộc `fault_causes`, và không gửi họ tên, số điện thoại, địa chỉ của khách cho hãng vận chuyển.
- Ngưỡng chuyển cho người duyệt: Chuyển cho chị Hạnh (NV-HANH) khi số tiền đề nghị vượt `auto_limit_vnd` của chính sách hiệu lực, khi tổng hoàn tự động trong ngày sắp vượt 2.000.000đ (`daily_auto_refund_budget_vnd`), hoặc khi định ghi lỗi thứ 3 trong ngày cho cùng một hãng (`max_auto_strikes_per_carrier_per_day` = 2).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Ba chỉ số an toàn bảo vệ LogiX (tiền), hãng (lỗi oan) và khách (dữ liệu cá nhân). `pass_rate` chủ yếu có nghĩa với khách. `escalation_rate` và `queue_stuck` là chỉ số của chị Hạnh. Chị Oanh cần thêm "sổ khớp tracking", và chỉ số này được che một phần bởi `wrongful_carrier_faults`. Shop chưa có chỉ số riêng. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `wrongful_*` = 0 bằng cách chuyển hết cho người thì chị Hạnh gánh hàng chờ, và khách chờ lâu hơn. Vì vậy có thêm `escalation_rate_max` và `queue_stuck_max` để cân lại. Ép `pass_rate` cao bằng cách tự hoàn dễ dãi thì LogiX và hãng chịu thiệt; ba ngưỡng an toàn = 0 chặn chuyện này. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có. Ở ngày 1, thành công là không chi sai đồng nào, không ghi oan hãng nào, không lộ dữ liệu, và 1 người trực duyệt kịp trong 60 phút. Tốc độ và tỉ lệ tự động là chuyện sau. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng tiền (2.000.000đ/ngày, 300.000đ/khách) phải tính lại theo số depot. `escalation_rate_max` phải gắn với số người trực thực tế. `cost_per_ticket_vnd_max` phải theo giá làm tay mới. `pass_rate` phải đo lại mỗi khi chính sách đổi phiên bản (drift). Ba ngưỡng an toàn = 0 giữ nguyên. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8.000đ** (phải rẻ hơn làm tay 10.000đ/ticket, chừa 20% cho phí người trực và ca chuyển người) · `roi_min` **0,2** (tiết kiệm ròng ít nhất 20% số tiền bỏ ra; dưới 0 là lỗ) · `queue_stuck_max` **0** (ca chuyển cho người phải được nhận trong `review_sla_minutes` = 60 phút)
- Ngày xem lại tiêu chí: `2026-12-02` (sau 2 tuần pilot) · Ai dự: `Trần Thanh Long (PIC), Phạm Cát Tân, chị Hạnh NV-HANH, chị Oanh NV-OANH, anh Tùng NV-TUNG` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
