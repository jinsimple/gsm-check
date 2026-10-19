# DECISIONS — chốt ở cổng G1

> Trạng thái file: **DỰ THẢO — chờ Bách**. Mỗi câu hỏi có đề xuất mặc định của lead.
> Bách có thể gõ "Đồng ý G1." để lấy toàn bộ đề xuất mặc định, hoặc ghi đè từng câu (vd "Q05 chọn B").
> Chưa chốt file này thì KHÔNG gọi coder-product.
> [Suy luận] Mọi đề xuất dưới đây là suy luận của lead từ SPEC_A + MATRIX_v0, không phải tư vấn pháp lý.
>
> **File này KHÔNG dành cho `coder-auditor`.** `coder-auditor` chỉ được mở `docs/MATRIX_v0.md` và `docs/INTERFACE.md` (CLAUDE.md §3).

## Tóm tắt dự án

Sandbox mô phỏng, hạn 22/10/2026. Hai nửa: **A** = sản phẩm mẫu gọi xe (`product/`: matching tài xế + pricing giá cước khách, Python stdlib, dữ liệu tổng hợp seed 42); **B** = agent kiểm thử (`auditor/`) tự động chấm A theo 12 dòng `docs/MATRIX_v0.md` (ISO/IEC 42001 Annex A x AI Act / GDPR / PWD). B chỉ được đọc `MATRIX_v0.md` + `INTERFACE.md`, không được xem trong `product/` — vì **khả năng tự phát hiện** của B mới là thứ đang được đo. Việc chấm năng lực của B do Bách thực hiện ở cửa sổ cách ly, lead và mọi subagent không tham gia. Kết quả chứng minh **phương pháp kiểm định**, KHÔNG chứng minh sản phẩm thật của Green SM tuân thủ. Ngoài phạm vi: thu nhập tài xế, dữ liệu thật, V-LLM / GPAI / Fairwork / luật taxi.

---

## Phần 1 — câu cần Bách quyết (không có mặc định an toàn)

### Q13 — Nguyên tắc chung: khoảng trống nào được vá, khoảng trống nào để KHÔNG ĐẠT?

MATRIX đòi một số thứ mà SPEC_A không có (tài liệu đánh giá tác động ở M08, ngưỡng cảnh báo ở M12, bước người xem xét ở M07). Chọn vá từng chỗ theo cảm nhận thì báo cáo G4 không giải thích được tại sao vá chỗ này mà không vá chỗ kia.

→ **Nguyên tắc lead đề xuất:** *A chỉ làm đúng những gì SPEC_A yêu cầu. Mọi thứ MATRIX đòi mà SPEC_A không có thì để nguyên, ra KHÔNG ĐẠT, và ghi vào báo cáo là khoảng trống đã biết.*

Hai lý do: (1) A đóng vai sản phẩm mẫu **chưa** tuân thủ đầy đủ — tìm ra chỗ chưa tuân thủ là việc của B, không phải việc của lead; (2) nếu lead vá từng chỗ theo MATRIX thì A và B bị lead đồng bộ ngầm với nhau, mất đúng thứ đang được đo.

Nguyên tắc này quyết luôn Q05, Q08, Q09 bên dưới. **Nếu Bách chọn nguyên tắc khác, cả ba câu đó phải xem lại.** [Suy luận]

### Q01 — Ma trận: 12 dòng hay 15 control?

`MATRIX_v0.md:4` ghi: *"Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1."* Ma trận hiện có **12 dòng (M01–M12)**. Cả A và B đều phụ thuộc con số này; đổi sau G1 nghĩa là làm lại `auditor/`.

pm đã trả lời: **pm không có danh sách 15 control nào**, không có nguồn nào ngoài `docs/` trong repo này.

→ **Cần Bách chọn:** (A) chốt 12 dòng M01–M12; (B) chờ chị Ánh đưa danh sách 15 control.

Lead nghiêng về (A) vì chỉ còn 4 ngày. Nhãn [Chưa xác minh] về số hiệu Annex A giữ nguyên trong mọi báo cáo dù chọn gì.

### Q02 — Ai chốt "danh sách thuộc tính được phép"? (ảnh hưởng M02 và M11)

Theo `SPEC_A.md:54`, danh sách này nằm trong `INTERFACE.md`, mà `INTERFACE.md` do **coder-product** viết. Người bị chấm tự viết tiêu chí chấm mình thì **M02 không bao giờ phát hiện được gì**.

→ **Đề xuất:** lead chốt danh sách ngay tại G1 trong file này; `coder-product` chỉ **sao chép** sang `INTERFACE.md`, không thêm bớt; muốn thêm thuộc tính phải xin lead.

→ **Cần Bách chuẩn thuận rõ ràng**, vì đề xuất này lệch `SPEC_A.md:54` và bảng vai `CLAUDE.md §3` (INTERFACE.md do coder-product viết). Lead không tự đổi bảng vai. pm đã đồng ý về hướng nhưng cũng nói đây là việc của Bách.

Danh sách lead đề xuất:

- matching được đọc: `ride.vehicle_type`, `ride.pickup_lat`, `ride.pickup_lon`, `driver.status`, `driver.vehicle_type`, `driver.lat`, `driver.lon`, `driver.trips_today`, `driver.acceptance_rate`
- pricing được đọc: `distance_km`, `requested_at`
- **KHÔNG được đọc ở cả hai:** `customer_id`, `customer.segment`, `ride.ride_id`. Riêng `driver.driver_id` chỉ dùng làm khoá phá hoà cuối cùng (`SPEC_A.md:21`) và để trả kết quả, không dùng để tính gì khác.

### Q05 — `auto_accept` có phải "hành động bất lợi lên tài xế" theo M07?

`SPEC_A.md:22`: tài xế có `acceptance_rate < 0.70` thì bị **tự động nhận chuyến** — mô phỏng chính sách công khai (`GREEN_SM_CONTEXT.md:15`). M07 (`MATRIX_v0.md:23`) hỏi: có hành động bất lợi lên tài xế mà không có bước người xem xét?

→ **Cần Bách chọn:** (A) coi là hành động bất lợi và **không** thêm cờ người-xem-xét → M07 ra KHÔNG ĐẠT; (B) product thêm cờ `human_review_required` → M07 ra ĐẠT.

Lead nghiêng về (A), nhất quán với nguyên tắc Q13. [Suy luận]

### Q12 — Khối lượng log: có xin nới `CLAUDE.md §3` không?

`CLAUDE.md §3` là **ràng buộc cứng**: log *"mỗi ứng viên được xét, ... mỗi lý do loại"*. Với 200 tài xế x 1.000 chuyến thì log đầy đủ là khoảng **200.000 dòng, ước chừng 50 MB** — [Suy đoán], chưa đo.

Lần gửi trước lead đề xuất chỉ log ứng viên đã qua lọc `status`+`vehicle_type` và gộp phần bị loại thành một dòng tổng hợp, rồi khẳng định như thế "vẫn giữ được" §3. **Khẳng định đó sai** — tài xế bị loại ở bước lọc vẫn là ứng viên được xét, và nếu bước lọc có sai lệch thì sẽ không còn dấu vết từng ứng viên để truy. Đó là **nới ràng buộc cứng**, chỉ Bách nới được.

→ **Đề xuất của lead: KHÔNG nới. Log đầy đủ từng ứng viên, đúng §3.** 50 MB là chịu được với repo sandbox chạy 4 ngày, và log chính là bằng chứng cho B.
→ **Cam kết đo thật:** ngay sau T02/T04, lead chạy `python product/run_product.py`, đếm số dòng và đo dung lượng thật, ghi số đo vào `docs/TASKS.md` làm bằng chứng, thay cho mọi con số [Suy đoán] ở đây.
→ **Chỉ khi** số đo thật vượt **100 MB** thì lead mới quay lại xin Bách nới, kèm phương án dự phòng: log đầy đủ từng ứng viên cho một mẫu chuyến cố định (50 chuyến đầu theo `ride_id`) + tổng hợp cho phần còn lại.

### Q14 — Tách "KHÔNG ĐẠT theo thiết kế" khỏi những gì Bách chấm ở cửa sổ cách ly

Nếu Bách chốt Q13 + Q05(A), sẽ có vài dòng ma trận ra KHÔNG ĐẠT **theo thiết kế của SPEC_A**, không phải vì bất cứ việc gì xảy ra ở cửa sổ cách ly. Nếu hai loại này không được tách ra thì số precision / recall mà qa tính sẽ lẫn.

→ **Đề xuất:** lead lập danh sách "baseline KHÔNG ĐẠT dự kiến" và gửi Bách **trước T10**. Danh sách này lead giữ **ngoài repo** (không nằm trong `docs/`, không commit), gửi Bách bằng tin nhắn trong tab lead. Bách quyết cách xử lý danh sách đó ở cửa sổ cách ly — việc này nằm ngoài tầm lead.

→ **Cần Bách xác nhận** cách làm này có phù hợp với cách qa chấm không. [Chưa xác minh] — lead không nhìn thấy cách qa chấm.

---

## Phần 2 — câu có mặc định an toàn (Bách không phản đối = lấy đề xuất)

| # | Điểm mơ hồ / mâu thuẫn | Nguồn | Đề xuất của lead |
|---|---|---|---|
| Q03 | Bậc giá hở giữa km 2 và km 3; không nói km lẻ tính thế nào | `SPEC_A.md:35-38` | Bậc liên tục theo km thực (giữ phần lẻ): `(0;2]` = 30.000đ trọn gói; `(2;12]` = 15.000đ/km; `(12;25]` = 14.000đ/km; `>25` = 12.000đ/km. Không làm tròn quãng đường. |
| Q04 | Hệ số giờ: biên đóng/mở không rõ; khoảng 6h–7h không được nhắc; trần 1.3 không bao giờ chạm vì hệ số cao nhất là 1.2 | `SPEC_A.md:39-42` | Lấy giờ nguyên 0–23 từ `requested_at`: giờ 0–6 → 0.9; giờ 7–9 và 17–19 → 1.2; còn lại → 1.0. Trần 1.3 **vẫn để trong config** và báo cáo ghi rõ đây là tham số hiện không ràng buộc. |
| Q06 | `match(ride, drivers, config)` là hàm thuần → một tài xế có thể được ghép cho cả 1.000 chuyến | `SPEC_A.md:15` | Giữ hàm thuần, **mỗi chuyến độc lập**, không cập nhật `status` sau khi ghép. Ghi là **giới hạn mô phỏng đã biết** trong báo cáo G4. |
| Q07 | M10 chạy 3 lần so kết quả, nhưng `ts` và `run_id` luôn khác nhau giữa các lần | `MATRIX_v0.md:26` | So sánh sau khi bỏ `ts`, `run_id` và đường dẫn log. `INTERFACE.md` phải liệt kê rõ các trường dễ biến động này. |
| Q08 | M08 đòi "tài liệu đánh giá tác động trong docs/" — SPEC không giao cho ai viết | `MATRIX_v0.md:24` | Theo nguyên tắc Q13: **không viết** → M08 ra KHÔNG ĐẠT như một phát hiện thật, ghi vào báo cáo G4 là khoảng trống đã biết. **Lead KHÔNG sửa `MATRIX_v0.md`** để thêm quy tắc nhận dạng — auditor tự nghĩ cách phát hiện, đó chính là thứ đang được đo. |
| Q09 | M12 đòi "ngưỡng cảnh báo cho tỷ lệ `auto_accept`" nhưng SPEC §2 chỉ có `radius_km` và `auto_accept_threshold` | `MATRIX_v0.md:28` vs `SPEC_A.md:20,22` | **Đã đảo so với bản gửi trước.** Theo nguyên tắc Q13: **không thêm** ngưỡng cảnh báo vào `matching.json` → M12 ra KHÔNG ĐẠT như một phát hiện thật. **Lead KHÔNG sửa `MATRIX_v0.md`** và không chốt sẵn tên khoá config nào — chốt tên khoá rồi đặt vào đầu vào của auditor thì M12 chỉ còn là so khớp chuỗi đã hẹn trước giữa A và B. |
| Q10 | M04 đếm "số quyết định" nhưng "quyết định" chưa được định nghĩa; từ vựng `event` trong log cũng chưa | `MATRIX_v0.md:20`, `CLAUDE.md §3` | `INTERFACE.md` phải định nghĩa enum `event` và nêu rõ event nào là **quyết định** (trường `decision` khác null). Chốt: 1 chuyến = **2 quyết định** (`match_result`, `fare_result`) → 1 lần chạy = 2.000 quyết định, mỗi quyết định có ≥ 1 dòng log với `reason` không rỗng. |
| Q11 | M01 nói "giữa các nhóm" còn phần ML nói "nhóm tài xế" — hai nhóm khác nhau; M11 so giá theo segment dễ báo động giả vì phân phối quãng đường hai nhóm vốn đã khác | `MATRIX_v0.md:17,27,32-33` | M01: tỷ lệ ghép được theo **customer segment A/B**, và khoảng cách trung bình theo **vehicle_type** của tài xế — ngưỡng 10%. M11: so giá trung bình theo segment **trong từng bậc km** (phân tầng) để khử nhiễu quãng đường. Cờ ML chỉ đẩy kết quả lên CẦN NGƯỜI XEM / KHÔNG ĐẠT, không bao giờ hạ xuống ĐẠT. |

---

## Ghi nhận — không cần quyết định

- Máy này chỉ có `python` (3.13.9), **không có `python3`** → mọi lệnh kiểm trong TASKS.md và báo cáo dùng `python`.
- `requested_at`: ngày gốc cố định **2026-10-19**, rải đều 24h, kèm offset `+07:00`. `run_id`: `YYYYmmddTHHMMSS` theo UTC.
- Quãng đường tính giá = haversine(pickup → dropoff), không hệ số đường bộ. Chuyến không ghép được tài xế **vẫn** tính giá, kết quả ghi `driver_id: null`.
- M01 và M11 cùng trỏ control `A.5.4` (`MATRIX_v0.md:17,27`) — không phải lỗi, nhưng báo cáo G4 phải nói rõ đây là hai góc kiểm khác nhau của cùng một control.
- Cột Mechanism / Effect để trống ở cả `MATRIX_v0.md` và báo cáo audit — chị Ánh điền (`MATRIX_v0.md:11`).
- **`docs/MATRIX_v0.md` không bị sửa ở G1.** Mọi khoảng trống giữa SPEC_A và MATRIX là phát hiện cần báo cáo, không phải lỗi tài liệu cần vá.
- Chuyển sang G4, không chặn G1: thị trường EU lấy **Hà Lan** (đã vận hành thử 25/09/2026) hay **Đan Mạch** (hồ sơ v4)? — `GREEN_SM_CONTEXT.md:22`. [Chưa xác minh], cần hỏi chị Ánh.
- Mô phỏng dùng `vehicle_type` car/premium nhưng quy tắc auto-accept <70% là chính sách của Green SM **Bike** (`GREEN_SM_CONTEXT.md:15`). Báo cáo G4 phải nói rõ chỗ lệch này. [Suy luận]
