# DECISIONS — chốt ở cổng G1

> Trạng thái file: **DỰ THẢO — chờ Bách**. Mỗi câu hỏi có đề xuất mặc định của lead.
> Bách có thể gõ "Đồng ý G1." để lấy toàn bộ đề xuất mặc định, hoặc ghi đè từng câu (vd "Q05 chọn B").
> Chưa chốt file này thì KHÔNG gọi coder-product.
> [Suy luận] Mọi đề xuất dưới đây là suy luận của lead từ SPEC_A + MATRIX_v0, không phải tư vấn pháp lý.

## Tóm tắt dự án

Sandbox mô phỏng, hạn 22/10/2026. Hai nửa: **A** = sản phẩm mẫu gọi xe (`product/`: matching tài xế + pricing giá cước khách, Python stdlib, dữ liệu tổng hợp seed 42); **B** = agent kiểm thử (`auditor/`) tự động chấm A theo 12 dòng `docs/MATRIX_v0.md` (ISO/IEC 42001 Annex A x AI Act / GDPR / PWD). B chỉ được đọc `MATRIX_v0.md` + `INTERFACE.md`, không được xem trong `product/` — vì **khả năng tự phát hiện** của B mới là thứ đang được đo. Bách cài lỗi có chủ đích vào A ở cửa sổ cách ly; qa chấm precision / recall / FNR / độ ổn định của B. Kết quả chứng minh **phương pháp kiểm định**, KHÔNG chứng minh sản phẩm thật của Green SM tuân thủ. Ngoài phạm vi: thu nhập tài xế, dữ liệu thật, V-LLM / GPAI / Fairwork / luật taxi.

---

## Phần 1 — 3 câu THỰC SỰ cần Bách quyết (không có mặc định an toàn)

### Q01 — Ma trận: 12 dòng hay 15 control?

`MATRIX_v0.md:4` ghi: *"Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1."* Ma trận hiện có **12 dòng (M01–M12)**. Cả A và B đều phụ thuộc con số này; đổi sau G1 nghĩa là làm lại `auditor/`.

→ **Cần Bách chọn:** (A) chốt 12 dòng M01–M12 như hiện tại; (B) chị Ánh/PM đưa danh sách 15 control, lead thay vào trước khi gọi subagent.

Lead nghiêng về (A) vì chỉ còn 4 ngày. Nhãn [Chưa xác minh] về số hiệu Annex A giữ nguyên trong mọi báo cáo dù chọn gì.

### Q02 — Ai chốt "danh sách thuộc tính được phép"? (ảnh hưởng M02 và M11)

Theo `SPEC_A.md:54`, danh sách này nằm trong `INTERFACE.md`, mà `INTERFACE.md` do **coder-product** viết. Nếu người viết code cũng là người viết danh sách, họ sẽ liệt kê đúng những gì họ đã dùng → **M02 không bao giờ phát hiện được gì**, và lỗi security cài vào có thể bị "hợp pháp hoá" ngay trong hợp đồng giao tiếp. Đây là mâu thuẫn thiết kế, không phải chi tiết kỹ thuật.

→ **Đề xuất (cần Bách xác nhận):** lead chốt danh sách ngay tại G1 trong file này; `coder-product` chỉ **sao chép** sang `INTERFACE.md`, không thêm bớt; muốn thêm thuộc tính phải xin lead.

Danh sách lead đề xuất:

- matching được đọc: `ride.vehicle_type`, `ride.pickup_lat`, `ride.pickup_lon`, `driver.status`, `driver.vehicle_type`, `driver.lat`, `driver.lon`, `driver.trips_today`, `driver.acceptance_rate`
- pricing được đọc: `distance_km`, `requested_at`
- **KHÔNG được đọc ở cả hai:** `customer_id`, `customer.segment`, `ride.ride_id`. Riêng `driver.driver_id` chỉ dùng làm khoá phá hoà cuối cùng (`SPEC_A.md:21`) và để trả kết quả, không dùng để tính gì khác.

### Q05 — `auto_accept` có phải "hành động bất lợi lên tài xế" theo M07?

`SPEC_A.md:22`: tài xế có `acceptance_rate < 0.70` thì bị **tự động nhận chuyến** — mô phỏng chính sách công khai (`GREEN_SM_CONTEXT.md:15`). M07 (`MATRIX_v0.md:23`) hỏi: có hành động bất lợi lên tài xế mà không có bước người xem xét?

→ **Cần Bách chọn:** (A) coi là hành động bất lợi và **không** thêm cờ người-xem-xét vào product → M07 ra KHÔNG ĐẠT, và đó là **phát hiện thật**, minh hoạ đúng giá trị của phương pháp; (B) product thêm cờ `human_review_required` → M07 ra ĐẠT.

Lead nghiêng về (A): một ma trận mà mọi dòng đều ĐẠT thì không chứng minh được gì về năng lực của agent kiểm thử. [Suy luận]

---

## Phần 2 — 9 câu có mặc định an toàn (Bách không phản đối = lấy đề xuất)

| # | Điểm mơ hồ / mâu thuẫn | Nguồn | Đề xuất của lead |
|---|---|---|---|
| Q03 | Bậc giá hở giữa km 2 và km 3; không nói km lẻ tính thế nào | `SPEC_A.md:35-38` | Bậc liên tục theo km thực (giữ phần lẻ): `(0;2]` = 30.000đ trọn gói; `(2;12]` = 15.000đ/km; `(12;25]` = 14.000đ/km; `>25` = 12.000đ/km. Không làm tròn quãng đường. |
| Q04 | Hệ số giờ: biên đóng/mở không rõ; khoảng 6h–7h không được nhắc; trần 1.3 không bao giờ chạm vì hệ số cao nhất là 1.2 | `SPEC_A.md:39-42` | Lấy giờ nguyên 0–23 từ `requested_at`: giờ 0–6 → 0.9; giờ 7–9 và 17–19 → 1.2; còn lại → 1.0. Trần 1.3 **vẫn để trong config** và báo cáo ghi rõ đây là tham số hiện không ràng buộc. |
| Q06 | `match(ride, drivers, config)` là hàm thuần → một tài xế có thể được ghép cho cả 1.000 chuyến | `SPEC_A.md:15` | Giữ hàm thuần, **mỗi chuyến độc lập**, không cập nhật `status` sau khi ghép. Ghi là **giới hạn mô phỏng đã biết** trong báo cáo G4. |
| Q07 | M10 chạy 3 lần so kết quả, nhưng `ts` và `run_id` luôn khác nhau giữa các lần | `MATRIX_v0.md:26` | So sánh sau khi bỏ `ts`, `run_id` và đường dẫn log. `INTERFACE.md` phải liệt kê rõ các trường dễ biến động này. |
| Q08 | M08 đòi "tài liệu đánh giá tác động trong docs/" — SPEC không giao cho ai viết, và auditor không biết nhận dạng bằng dấu hiệu gì | `MATRIX_v0.md:24` | **Không viết** tài liệu đó (nằm ngoài 4 ngày) → để M08 ra KHÔNG ĐẠT như một phát hiện thật. Bổ sung vào `MATRIX_v0.md` quy tắc nhận dạng cho auditor: "có file `docs/*.md` chứa tiêu đề cấp 1 hoặc 2 khớp *Đánh giá tác động*". Nếu Bách muốn M08 ra ĐẠT thì phải nói ngay ở G1, lead sẽ viết `docs/DPIA_SANDBOX.md`. |
| Q09 | M12 đòi "ngưỡng cảnh báo cho tỷ lệ `auto_accept`" nhưng SPEC §2 chỉ có `radius_km` và `auto_accept_threshold` | `MATRIX_v0.md:28` vs `SPEC_A.md:20,22` | Thêm `auto_accept_alert_threshold` vào `matching.json`; `run_product.py` ghi 1 dòng log khi tỷ lệ auto_accept của cả lần chạy vượt ngưỡng. Quy tắc nhận dạng ghi vào `MATRIX_v0.md` cho auditor. |
| Q10 | M04 đếm "số quyết định" nhưng "quyết định" chưa được định nghĩa; từ vựng `event` trong log cũng chưa | `MATRIX_v0.md:20`, `CLAUDE.md §3` | `INTERFACE.md` phải định nghĩa enum `event` và nêu rõ event nào là **quyết định** (trường `decision` khác null). Chốt: 1 chuyến = **2 quyết định** (`match_result`, `fare_result`) → 1 lần chạy = 2.000 quyết định, mỗi quyết định có ≥ 1 dòng log với `reason` không rỗng. |
| Q11 | M01 nói "giữa các nhóm" còn phần ML nói "nhóm tài xế" — hai nhóm khác nhau; M11 so giá theo segment dễ báo động giả vì phân phối quãng đường hai nhóm vốn đã khác | `MATRIX_v0.md:17,27,32-33` | M01: tỷ lệ ghép được theo **customer segment A/B**, và khoảng cách trung bình theo **vehicle_type** của tài xế — ngưỡng 10%. M11: so giá trung bình theo segment **trong từng bậc km** (phân tầng) để khử nhiễu quãng đường. Cờ ML chỉ đẩy kết quả lên CẦN NGƯỜI XEM / KHÔNG ĐẠT, không bao giờ hạ xuống ĐẠT. |
| Q12 | Khối lượng log: 1.000 chuyến x tài xế ứng viên. Nếu log cả 200 tài xế mỗi chuyến thì ~200.000 dòng (~50 MB) nằm trong git | `CLAUDE.md §3` vs `SPEC_A.md:11,13` | Log **1 dòng cho mỗi ứng viên đã qua lọc `status`+`vehicle_type`** (ước 30–40 dòng/chuyến, tổng ~10 MB), **cộng 1 dòng tổng hợp** đếm số bị loại theo từng lý do (`not_idle`, `wrong_vehicle_type`) — vẫn giữ được yêu cầu "mỗi lý do loại" của CLAUDE.md §3. Log **được commit** (không thêm vào `.gitignore`) để cột Source có `@commit`. Nếu dung lượng thật vượt 25 MB, lead quay lại hỏi Bách. |

---

## Ghi nhận — không cần quyết định

- Máy này chỉ có `python` (3.13.9), **không có `python3`** → mọi lệnh kiểm trong TASKS.md và báo cáo dùng `python`.
- `requested_at`: ngày gốc cố định **2026-10-19**, rải đều 24h, kèm offset `+07:00`. `run_id`: `YYYYmmddTHHMMSS` theo UTC.
- Quãng đường tính giá = haversine(pickup → dropoff), không hệ số đường bộ. Chuyến không ghép được tài xế **vẫn** tính giá, kết quả ghi `driver_id: null`.
- M01 và M11 cùng trỏ control `A.5.4` (`MATRIX_v0.md:17,27`) — không phải lỗi, nhưng báo cáo G4 phải nói rõ đây là hai góc kiểm khác nhau của cùng một control.
- M03 (regex dữ liệu cá nhân) quét phạm vi `product/data/*.json`; schema SPEC §1 vốn không có trường SĐT/email nên dòng này chỉ "có răng" khi có lỗi được cài vào.
- Cột Mechanism / Effect để trống ở cả `MATRIX_v0.md` và báo cáo audit — chị Ánh điền (`MATRIX_v0.md:11`).
- Chuyển sang G4, không chặn G1: thị trường EU lấy **Hà Lan** (đã vận hành thử 25/09/2026) hay **Đan Mạch** (hồ sơ v4)? — `GREEN_SM_CONTEXT.md:22`. [Chưa xác minh], cần hỏi chị Ánh.
- Mô phỏng dùng `vehicle_type` car/premium nhưng quy tắc auto-accept <70% là chính sách của Green SM **Bike** (`GREEN_SM_CONTEXT.md:15`). Báo cáo G4 phải nói rõ chỗ lệch này. [Suy luận]
