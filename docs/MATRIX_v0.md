# MA TRẬN KIỂM v0 — ISO/IEC 42001 Annex A × Luật EU

> [Suy luận] Ma trận do phiên Claude soạn, không phải tư vấn pháp lý.
> [Chưa xác minh] Số hiệu control Annex A cần đối chiếu bản chuẩn ISO/IEC 42001:2023. Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1.

## Quy ước

- Kết quả mỗi dòng: **ĐẠT** | **KHÔNG ĐẠT** | **CẦN NGƯỜI XEM**
- Bằng chứng (cột Source): `file:dòng@commit`
- **Mỗi phát hiện phải có bằng chứng `file:dòng` RIÊNG**, không chỉ tên file. Một dòng ma trận có nhiều phát hiện thì **liệt kê đủ từng cái**, không gộp. (Bách chốt 19/10)
- **Nguyên tắc bất đối xứng:** nghi ngờ → CẦN NGƯỜI XEM. Không bao giờ tự cho ĐẠT khi thiếu bằng chứng. Bỏ lọt đắt hơn báo động giả.
- Cột **Mechanism / Effect**: ĐỂ TRỐNG. Taxonomy nội bộ chưa được định nghĩa (§3.4 hồ sơ v4) — chị Ánh điền.
- **Phát hiện dạng VẮNG MẶT** (thứ cần có mà không có): bằng chứng = **phạm vi đã quét** (liệt kê đủ file / khoá đã kiểm) + **phương pháp quét** + **dòng log của agent kiểm thử** ghi lại kết quả quét. (Bách chốt 19/10)
- Phát hiện dạng vắng mặt **chỉ được ra KHÔNG ĐẠT khi lần quét đầy đủ**. Quét lỗi, hoặc không đủ phạm vi → **CẦN NGƯỜI XEM**. (Bách chốt 19/10)
- Log của chính agent kiểm thử ghi vào `reports/audit_<commit>.log.jsonl` và **được commit**. Log sản phẩm `logs/*.jsonl` không vào git. (Bách chốt 19/10)
- Vì log sản phẩm không được commit: agent kiểm thử **tự chạy `python product/run_product.py` sinh log mới trước khi kiểm**, không dùng log có sẵn. Chạy lỗi → các dòng cần log ra **CẦN NGƯỜI XEM**. (Bách chốt 19/10)
- Khi trích một dòng log sản phẩm làm bằng chứng: **chép NGUYÊN VĂN dòng đó** vào `reports/audit_<commit>.log.jsonl`, kèm `run_id` đã sinh và **lệnh đã chạy**. (Bách chốt 19/10)
- **Chỉ chép các dòng được trích làm bằng chứng**, không chép cả file log. (Bách chốt 19/10)

## Ma trận

| ID | Control Annex A | Căn cứ luật EU | Quy tắc kiểm bằng máy | Nguồn bằng chứng |
|---|---|---|---|---|
| M01 | A.5.4 Tác động lên cá nhân/nhóm | AI Act PL III 4(b); PWD Đ.8 | Chênh lệch tỷ lệ được ghép hoặc khoảng cách trung bình giữa các nhóm vượt ngưỡng (mặc định 10%) | log matching, kết quả chạy |
| M02 | A.7.4 Chất lượng dữ liệu | PWD Đ.7 | Code matching đọc thuộc tính KHÔNG nằm trong danh sách cho phép ở INTERFACE | phân tích tĩnh (AST) |
| M03 | A.7.5 Nguồn gốc dữ liệu | GDPR Đ.5(1)(c) | Mock data có trường mang định dạng dữ liệu cá nhân thật (SĐT, email, CCCD…) | quét regex trên data/ |
| M04 | A.6.2.8 Log sự kiện | AI Act Đ.12 | Số quyết định ≠ số quyết định có log; hoặc có nhánh `return` không gọi log | AST + đối chiếu log |
| M05 | A.6.2.3 Tài liệu thiết kế | AI Act Đ.11 | Hằng số số học nghiệp vụ trong code không có trong config | AST |
| M06 | A.6.2.7 Tài liệu kỹ thuật | AI Act Đ.11 | File config thiếu trường `version` | đọc config |
| M07 | A.9.2 Sử dụng có trách nhiệm | GDPR Đ.22; PWD Đ.10 | Có hành động bất lợi hoặc ràng buộc lên tài xế (khóa, phạt, hạ ưu tiên, tự động nhận chuyến) mà không có bước/cờ con người xem xét | AST + log |
| M08 | A.5.2 Quy trình đánh giá tác động | GDPR Đ.35; PWD Đ.8 | Không có tài liệu đánh giá tác động trong docs/ | quét docs/ |
| M09 | A.8.2 Thông tin cho người dùng | PWD Đ.9 | Quyết định không kèm `reason` đọc được | log |
| M10 | A.6.2.4 Kiểm chứng & xác nhận | AI Act Đ.15 | Cùng đầu vào chạy 3 lần → kết quả khác nhau | chạy lặp |
| M11 | A.5.4 (pricing) | Luật tiêu dùng EU [Suy luận] | Giá phụ thuộc thuộc tính của khách ngoài quãng đường và thời điểm | AST + thống kê theo segment |
| M12 | A.6.2.6 Vận hành & giám sát | AI Act Đ.72 [Suy luận] | Không có ngưỡng cảnh báo cho tỷ lệ `auto_accept` | đọc config + code |

## Phần ML đơn giản (stdlib `statistics`)

- Phân phối giá theo `segment` của khách → kiểm định chênh lệch trung bình → cờ cho **M11**
- Tỷ lệ được ghép, khoảng cách trung bình theo nhóm tài xế → cờ cho **M01**
- Cờ ML chỉ được đẩy kết quả lên **CẦN NGƯỜI XEM** hoặc **KHÔNG ĐẠT**, không bao giờ hạ xuống ĐẠT.

## Đầu ra agent kiểm thử

`reports/audit_<commit>.json` và `.md`, mỗi dòng gồm:
`ID | Control | Luật | Kết quả | Bằng chứng (file:dòng@commit) | Ghi chú | Mechanism (trống) | Effect (trống)`

Cột Bằng chứng là **danh sách**, không phải một chuỗi: mỗi phát hiện một phần tử, mỗi phần tử có `file:dòng@commit` riêng. Dòng ra KHÔNG ĐẠT hoặc CẦN NGƯỜI XEM mà chỉ trỏ tên file, không trỏ dòng, thì coi là **chưa đủ bằng chứng**.

## Chi tiết quy tắc cho agent kiểm thử — chốt G1

`coder-auditor` chỉ đọc `MATRIX_v0.md` và `INTERFACE.md`, nên mọi quyết định ảnh hưởng tới agent kiểm thử phải nằm ở một trong hai file đó. Phần này là một phần của ma trận.

**M01 — nhóm so sánh và ngưỡng.** So hai chiều: (1) tỷ lệ được ghép theo `segment` của khách (A / B); (2) khoảng cách trung bình theo `vehicle_type` của tài xế. Ngưỡng chênh lệch: **10%**. Câu "giữa các nhóm" ở dòng M01 và câu "theo nhóm tài xế" ở phần ML trỏ cùng về định nghĩa này.

**M11 — khử nhiễu quãng đường.** So giá trung bình theo `segment` của khách **trong từng nhóm quãng đường tương đương**: chia tập chuyến thành 4–5 nhóm theo **phân vị của `distance_km` quan sát được** (`statistics.quantiles`), rồi so trong từng nhóm — không so trên toàn bộ tập. Lý do: phân phối quãng đường của hai segment vốn đã khác nhau, so thẳng trên toàn bộ sẽ ra báo động giả.

**M10 — so sánh giữa các lần chạy.** Bỏ các trường dễ biến động trước khi so: `ts`, `run_id`, và mọi đường dẫn log. `INTERFACE.md` liệt kê đủ các trường này.

**M04 và M09 — định nghĩa "một quyết định".** Lấy từ `INTERFACE.md`: enum `event`, và event nào là quyết định (trường `decision` khác null). Agent kiểm thử **không** tự đặt định nghĩa riêng.

**Bằng chứng trỏ vào log sản phẩm.** `logs/*.jsonl` không vào git, nên bằng chứng dạng log ghi `logs/<tên file>.jsonl:<dòng>` **không kèm `@commit`**. Chỉ bằng chứng trỏ vào file có trong git mới có `@commit`. Đây là ngoại lệ duy nhất của quy ước `file:dòng@commit`.
