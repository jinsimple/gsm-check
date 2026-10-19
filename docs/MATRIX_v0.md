# MA TRẬN KIỂM v0 — ISO/IEC 42001 Annex A × Luật EU

> [Suy luận] Ma trận do phiên Claude soạn, không phải tư vấn pháp lý.
> [Chưa xác minh] Số hiệu control Annex A cần đối chiếu bản chuẩn ISO/IEC 42001:2023. Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1.

## Quy ước

- Kết quả mỗi dòng: **ĐẠT** | **KHÔNG ĐẠT** | **CẦN NGƯỜI XEM**
- Bằng chứng (cột Source): `file:dòng@commit`
- **Nguyên tắc bất đối xứng:** nghi ngờ → CẦN NGƯỜI XEM. Không bao giờ tự cho ĐẠT khi thiếu bằng chứng. Bỏ lọt đắt hơn báo động giả.
- Cột **Mechanism / Effect**: ĐỂ TRỐNG. Taxonomy nội bộ chưa được định nghĩa (§3.4 hồ sơ v4) — chị Ánh điền.

## Ma trận

| ID | Control Annex A | Căn cứ luật EU | Quy tắc kiểm bằng máy | Nguồn bằng chứng |
|---|---|---|---|---|
| M01 | A.5.4 Tác động lên cá nhân/nhóm | AI Act PL III 4(b); PWD Đ.8 | Chênh lệch tỷ lệ được ghép hoặc khoảng cách trung bình giữa các nhóm vượt ngưỡng (mặc định 10%) | log matching, kết quả chạy |
| M02 | A.7.4 Chất lượng dữ liệu | PWD Đ.7 | Code matching đọc thuộc tính KHÔNG nằm trong danh sách cho phép ở INTERFACE | phân tích tĩnh (AST) |
| M03 | A.7.5 Nguồn gốc dữ liệu | GDPR Đ.5(1)(c) | Mock data có trường mang định dạng dữ liệu cá nhân thật (SĐT, email, CCCD…) | quét regex trên data/ |
| M04 | A.6.2.8 Log sự kiện | AI Act Đ.12 | Số quyết định ≠ số quyết định có log; hoặc có nhánh `return` không gọi log | AST + đối chiếu log |
| M05 | A.6.2.3 Tài liệu thiết kế | AI Act Đ.11 | Hằng số số học nghiệp vụ trong code không có trong config | AST |
| M06 | A.6.2.7 Tài liệu kỹ thuật | AI Act Đ.11 | File config thiếu trường `version` | đọc config |
| M07 | A.9.2 Sử dụng có trách nhiệm | GDPR Đ.22; PWD Đ.10 | Có hành động bất lợi lên tài xế (khóa, phạt, hạ ưu tiên) mà không có bước/cờ con người xem xét | AST + log |
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
