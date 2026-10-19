# SPEC — SẢN PHẨM MẪU A (matching + pricing)

> [Suy luận] Mô phỏng dựa trên mô tả công khai của Green SM (xem `GREEN_SM_CONTEXT.md`). **Mọi con số là GIẢ**, không phải giá hay tham số thật.

## 1. Dữ liệu tổng hợp — `product/data/gen_mock.py`

Seed cố định `42`.

**Vùng chính** (tài xế và phần lớn chuyến): hộp tọa độ giả `lat 21.00–21.08, lon 105.78–105.88`.

**Sửa 19/10 theo quyết định của Bách — nguyên tắc phủ nhánh.** Mọi nhánh quyết định của A phải được chạy **ít nhất một lần** trên mock data. Hộp tọa độ cũ (~9×10 km) làm ba nhánh không bao giờ chạy: không tìm được tài xế, và hai bậc giá trên 12 km. Vì vậy `rides.json` bổ sung hai nhóm chuyến:

| Nhóm | Tỷ lệ | Mục đích | Nhánh được phủ |
|---|---|---|---|
| **Chuyến ngoài vùng phủ** | 3–5% | điểm đón nằm ngoài vùng có tài xế, cách mọi tài xế hơn `radius_km` | `no_driver_in_radius`, `driver_id = None` |
| **Chuyến dài** | đủ để mỗi bậc giá có ≥ 1 chuyến | điểm đến xa, quãng đường vượt 12 km và vượt 25 km | bậc `(12;25]` và bậc `>25` thật sự được tính tiền |

Tham số của hai nhóm này nằm trong `product/config/mock_data.json` (`CLAUDE.md §2.4`), không hardcode. Tài xế vẫn chỉ nằm trong **vùng chính** — không dời tài xế để tạo ra kết quả mong muốn.

| Bảng | Số bản ghi | Trường |
|---|---|---|
| `drivers.json` | 200 | `driver_id` (D0001…), `lat`, `lon`, `status` (idle / busy / offline), `vehicle_type` (car / premium), `acceptance_rate` (0–1), `trips_today` |
| `customers.json` | 300 | `customer_id` (C0001…), `segment` (A / B) — nhóm giả để đo chênh lệch |
| `rides.json` | 1.000 | `ride_id`, `customer_id`, `vehicle_type`, `pickup_lat/lon`, `dropoff_lat/lon`, `requested_at` (ISO, rải 24h) |

## 2. Matching — `match(ride, drivers, config) -> dict`

Đầu ra: `{driver_id | None, auto_accept: bool, reason: str}`

1. Lọc `status == "idle"` và đúng `vehicle_type`.
2. Tính khoảng cách haversine. Giữ ứng viên có khoảng cách ≤ `radius_km` (config, mặc định 5).
3. Chọn ứng viên gần nhất. Hòa → `trips_today` thấp hơn → `driver_id` nhỏ hơn (để kết quả xác định).
4. Nếu tài xế được chọn có `acceptance_rate < auto_accept_threshold` (config, mặc định 0.70) → `auto_accept = true`.
   *(Mô phỏng quy tắc công khai của Green SM Bike.)*
5. Không có ứng viên → trả `driver_id = None`, `reason = "no_driver_in_radius"`.
6. **Log:** mỗi ứng viên (khoảng cách, đạt/loại, lý do), người thắng, lý do thắng.

## 3. Pricing — `fare(distance_km, requested_at, config) -> dict`

Đầu ra: `{fare_vnd, breakdown, time_coef, reason}`

`product/config/pricing.json` (version `"0.1"`):

| Thành phần | Giá trị giả |
|---|---|
| Mở cửa (2 km đầu) | 30.000đ |
| Km 3–12 | 15.000đ/km |
| Km 13–25 | 14.000đ/km |
| Km 26+ | 12.000đ/km |
| Hệ số 0h–6h | 0.9 |
| Hệ số 7–9h, 17–19h | 1.2 |
| Hệ số còn lại | 1.0 |
| Trần hệ số | 1.3 |
| Làm tròn | lên bội số 1.000đ |

**Log:** từng bậc km và tiền của bậc, hệ số áp dụng và lý do, giá trước/sau làm tròn.

## 4. Chạy toàn bộ — `product/run_product.py`

Đọc mock → ghép từng chuyến → tính giá → ghi `reports/product_run_<run_id>.json` + log.
Phải chạy được bằng một lệnh: `python product/run_product.py`

## 5. Hợp đồng giao tiếp — `docs/INTERFACE.md` (coder-product viết)

Chỉ gồm: chữ ký hàm, đường dẫn config, schema dữ liệu, schema log, **danh sách thuộc tính được phép dùng làm đầu vào matching và pricing**.
**Không** mô tả logic bên trong. `coder-auditor` chỉ đọc file này.

**Sửa 19/10 theo quyết định Q02 của Bách:** danh sách thuộc tính được phép **do lead chốt** ở `docs/DECISIONS.md` mục Q02; `coder-product` **chép nguyên** sang `INTERFACE.md` — không thêm, không bớt. Muốn thêm thuộc tính phải xin lead. Lý do: người viết code không tự viết tiêu chí dùng để chấm mình, nếu không thì M02 vô hiệu. Danh sách là **danh sách trắng đóng**: chỉ ghi thuộc tính được phép, không ghi thuộc tính bị cấm.

## 6. Ngoài phạm vi — ghi vào báo cáo là KHOẢNG TRỐNG ĐÃ BIẾT

Thu nhập tài xế. Theo §4.2 hồ sơ v4, đây mới là phần có khả năng thuộc Phụ lục III điểm 4(b) Đạo luật AI.
