# INTERFACE — hợp đồng giao tiếp của sản phẩm mẫu A

> [Suy luận] Sản phẩm mẫu A là **mô phỏng sandbox** (mô phỏng gọi xe), không phải sản phẩm thật của Green SM, không phải tư vấn pháp lý. Mọi con số trong `product/config/*.json` và `product/data/*.json` là **giả**.

Theo `SPEC_A.md:54-55`, file này chỉ gồm **năm** thứ và **không mô tả logic bên trong**:

1. Chữ ký hàm
2. Đường dẫn config
3. Schema dữ liệu
4. Schema log
5. Danh sách thuộc tính được phép làm đầu vào matching và pricing

Các hàm phụ trợ nội bộ khác của `product/` không thuộc hợp đồng này.

---

## 1. Lệnh chạy

| Việc | Lệnh |
|---|---|
| Chạy toàn bộ sản phẩm mẫu A | `python product/run_product.py` |
| Sinh lại dữ liệu tổng hợp | `python product/data/gen_mock.py` |

Máy dự án chỉ có lệnh `python` (3.13.9), **không có `python3`**.

---

## 2. Chữ ký hàm

### `product/matching.py`

```python
match(ride: dict, drivers: list[dict], config: dict, logger=None) -> dict
load_config(path: str | None = None, logger=None) -> dict
```

`match` trả về dict đúng 3 khoá:

| Khoá | Kiểu |
|---|---|
| `driver_id` | `str` hoặc `None` |
| `auto_accept` | `bool` |
| `reason` | `str` |

### `product/pricing.py`

```python
fare(distance_km: float, requested_at: str, config: dict, logger=None) -> dict
load_config(path: str | None = None, logger=None) -> dict
```

`fare` trả về dict đúng 4 khoá:

| Khoá | Kiểu |
|---|---|
| `fare_vnd` | `int` |
| `breakdown` | `list[dict]` — mỗi phần tử là một bước tính thành phần; tập khoá bên trong do triển khai quyết định, không thuộc hợp đồng này |
| `time_coef` | `float` |
| `reason` | `str` |

### `product/run_product.py`

```python
run(run_id: str | None = None) -> dict
main() -> int
```

### `product/data/gen_mock.py`

```python
main(run_id: str | None = None) -> dict
```

### `product/logger.py`

```python
make_run_id() -> str
process_run_id() -> str
load_json_config(path: str, logger=None) -> dict
default_logger() -> JsonlLogger
make_fallback_logger(module: str) -> JsonlLogger
rel(path: str) -> str
enable_utf8_stdout() -> None

class JsonlLogger:
    __init__(self, module: str, run_id: str, log_dir: str | None = None,
             autoflush: bool = False)
    log(self, func: str, event: str, inputs: dict | None = None,
        outputs: dict | None = None, decision=None, reason: str = "") -> None
    set_context(self, context: dict) -> None
    clear_context(self) -> None
    flush(self) -> None
    close(self) -> None
```

Tham số `logger` của `match` và `fare` là tùy chọn. Nếu người gọi không truyền, module tự tạo một `JsonlLogger` riêng.

`set_context` gán các khoá đối chiếu (ví dụ `ride_id`) do **người gọi** cung cấp vào trường `inputs` của các dòng log kế tiếp.

---

## 3. Đường dẫn config và schema config

Các file config của sản phẩm mẫu A nằm ở `product/config/`:

| Đường dẫn | Hàm đọc mặc định |
|---|---|
| `product/config/matching.json` | `matching.load_config()` |
| `product/config/pricing.json` | `pricing.load_config()` |
| `product/config/mock_data.json` | `gen_mock` đọc khi sinh dữ liệu |

Dưới đây **chỉ** là tên khoá và kiểu dữ liệu. Giá trị nằm trong chính các file đó.

### `matching.json`

| Khoá | Kiểu |
|---|---|
| `version` | `str` |
| `note` | `str` |
| `radius_km` | number |
| `auto_accept_threshold` | number |
| `idle_status` | `str` |

### `pricing.json`

| Khoá | Kiểu |
|---|---|
| `version` | `str` |
| `note` | `str` |
| `currency` | `str` |
| `tiers` | `list` |
| `time_coefficients` | `list` |
| `default_time_coef` | number |
| `max_time_coef` | number |
| `rounding` | `object` |

### `mock_data.json`

| Khoá | Kiểu |
|---|---|
| `version` | `str` |
| `note` | `str` |
| `seed` | `int` |
| `base_date` | `str` |
| `utc_offset_hours` | `int` |
| `bbox` | `object` |
| `coord_decimals` | `int` |
| `counts` | `object` |
| `id_format` | `object` |
| `driver_status_weights` | `object` |
| `vehicle_type_weights` | `object` |
| `customer_segment_weights` | `object` |
| `acceptance_rate_range` | `list` |
| `acceptance_rate_decimals` | `int` |
| `trips_today_range` | `list` |
| `ride_overlay_note` | `str` |
| `rides_outside_service_area` | `object` |
| `long_distance_rides` | `object` |

---

## 4. Schema dữ liệu

Dữ liệu **100% tổng hợp**, sinh từ seed cố định trong `mock_data.json`. Không có tên, số điện thoại, biển số, địa chỉ thật.

### `product/data/drivers.json` — `list[dict]`, 200 bản ghi

| Trường | Kiểu |
|---|---|
| `driver_id` | `str` |
| `lat` | `float` |
| `lon` | `float` |
| `status` | `str` |
| `vehicle_type` | `str` |
| `acceptance_rate` | `float` |
| `trips_today` | `int` |

### `product/data/customers.json` — `list[dict]`, 300 bản ghi

| Trường | Kiểu |
|---|---|
| `customer_id` | `str` |
| `segment` | `str` |

### `product/data/rides.json` — `list[dict]`, 1.000 bản ghi

| Trường | Kiểu |
|---|---|
| `ride_id` | `str` |
| `customer_id` | `str` |
| `vehicle_type` | `str` |
| `pickup_lat` | `float` |
| `pickup_lon` | `float` |
| `dropoff_lat` | `float` |
| `dropoff_lon` | `float` |
| `requested_at` | `str` — ISO 8601 kèm offset múi giờ |

### `reports/product_run_<run_id>.json` — kết quả một lần chạy

| Khoá mức cao nhất | Kiểu |
|---|---|
| `ts` | `str` |
| `run_id` | `str` |
| `schema_version` | `str` |
| `note` | `str` |
| `config_versions` | `object` — khoá `matching`, `pricing`, giá trị `str` |
| `log_files` | `list[str]` |
| `summary` | `object` |
| `results` | `list[dict]`, một phần tử cho mỗi chuyến |

`summary`:

| Khoá | Kiểu |
|---|---|
| `n_rides` | `int` |
| `n_matched` | `int` |
| `n_unmatched` | `int` |
| `n_auto_accept` | `int` |
| `n_decisions` | `int` |
| `n_decisions_by_module` | `object` — khoá là giá trị `module`, giá trị `int` |
| `total_fare_vnd` | `int` |

Mỗi phần tử của `results`:

| Khoá | Kiểu |
|---|---|
| `ride_id` | `str` |
| `customer_id` | `str` |
| `customer_segment` | `str` hoặc `None` |
| `vehicle_type` | `str` |
| `requested_at` | `str` |
| `distance_km` | `float` |
| `driver_id` | `str` hoặc `None` |
| `auto_accept` | `bool` |
| `match_reason` | `str` |
| `fare_vnd` | `int` |
| `time_coef` | `float` |
| `fare_reason` | `str` |

---

## 5. Schema log

### 5.1 Đường dẫn và định dạng

- Định dạng **JSON Lines**: mỗi dòng là một đối tượng JSON độc lập, mã hóa UTF-8, kết thúc dòng `\n`.
- Đường dẫn: `logs/<module>_<run_id>.jsonl`
- `run_id` dạng `YYYYmmddTHHMMSSfff` theo **UTC** — ngày giờ tới giây, cộng **3 chữ số milli giây**, tổng cộng 18 ký tự. Ví dụ: `20261019T075320123`. **Giống nhau cho mọi module trong cùng một lần chạy.**
- Mỗi lần chạy sinh file mới. `logs/*.jsonl` nằm trong `.gitignore`, nên log **không vào git**.
- File log mở bằng mode `"x"`, và `reports/product_run_<run_id>.json` cũng vậy: nếu file của `run_id` đó đã tồn tại thì **báo `FileExistsError`** chứ không ghi đè bằng chứng của lần chạy trước. Hai lần chạy liên tiếp sinh `run_id` khác nhau, nên đường chạy bình thường không chạm tới lỗi này.

Giá trị `module` đang có:

| `module` | File |
|---|---|
| `run_product` | `logs/run_product_<run_id>.jsonl` |
| `matching` | `logs/matching_<run_id>.jsonl` |
| `pricing` | `logs/pricing_<run_id>.jsonl` |
| `gen_mock` | `logs/gen_mock_<run_id>.jsonl` |
| `logger` | `logs/logger_<run_id>.jsonl` |

### 5.2 Chín trường bắt buộc

Mỗi dòng log là một đối tượng JSON gồm chín trường, theo thứ tự này:

| # | Trường | Kiểu | Ghi chú |
|---|---|---|---|
| 1 | `ts` | `str` | ISO 8601 UTC, thời điểm ghi dòng log |
| 2 | `run_id` | `str` | `YYYYmmddTHHMMSSfff` theo UTC, xem 5.1 |
| 3 | `module` | `str` | xem bảng 5.1 |
| 4 | `func` | `str` | tên hàm đã ghi dòng log |
| 5 | `event` | `str` | xem enum 5.3 |
| 6 | `inputs` | `object` | có thể rỗng; chứa cả khoá đối chiếu do người gọi gán qua `set_context` |
| 7 | `outputs` | `object` | có thể rỗng |
| 8 | `decision` | `str` / `int` / `null` | **khác `null` chỉ ở event quyết định**, xem 5.4 |
| 9 | `reason` | `str` | không rỗng ở mọi event quyết định |

### 5.3 Enum `event` — đầy đủ

| `module` | `event` | `decision` |
|---|---|---|
| `matching` | `match_start` | `null` |
| `matching` | `candidate_eval` | `null` |
| `matching` | `candidate_pool` | `null` |
| `matching` | `tie_break` | `null` |
| `matching` | `auto_accept_eval` | `null` |
| `matching` | **`match_result`** | **khác `null` — QUYẾT ĐỊNH** |
| `pricing` | `fare_start` | `null` |
| `pricing` | `fare_tier` | `null` |
| `pricing` | `base_fare_computed` | `null` |
| `pricing` | `time_coef_applied` | `null` |
| `pricing` | `time_coef_cap` | `null` |
| `pricing` | `fare_rounding` | `null` |
| `pricing` | `tier_kind_unsupported` | `null` |
| `pricing` | `rounding_mode_unsupported` | `null` |
| `pricing` | **`fare_result`** | **khác `null` — QUYẾT ĐỊNH** |
| `run_product` | `run_start` | `null` |
| `run_product` | `config_loaded` | `null` |
| `run_product` | `config_version_missing` | `null` |
| `run_product` | `mock_data_check` | `null` |
| `run_product` | `mock_data_generated` | `null` |
| `run_product` | `data_loaded` | `null` |
| `run_product` | `ride_distance` | `null` |
| `run_product` | `run_end` | `null` |
| `gen_mock` | `gen_start` | `null` |
| `gen_mock` | `config_version_missing` | `null` |
| `gen_mock` | `record_generated` | `null` |
| `gen_mock` | `overlay_selection` | `null` |
| `gen_mock` | `ride_group_assigned` | `null` |
| `gen_mock` | `ride_adjusted` | `null` |
| `gen_mock` | `clearance_check` | `null` |
| `gen_mock` | `table_written` | `null` |
| `gen_mock` | `gen_end` | `null` |
| `logger` | `config_version_missing` | `null` |

### 5.4 Định nghĩa "một quyết định"

Trường `decision` **khác `null` chỉ ở hai event**: `match_result` (module `matching`) và `fare_result` (module `pricing`). Mọi event khác có `decision = null`.

- **1 chuyến = 2 quyết định** (`match_result` + `fare_result`).
- **1 lần chạy 1.000 chuyến = 2.000 quyết định.**
- Mỗi quyết định có **ít nhất 1 dòng log** với `reason` **không rỗng**.
- Số quyết định kỳ vọng = số bản ghi trong `rides.json` × 2. `summary.n_decisions` là **con số sản phẩm tự báo**, dùng để đối chiếu chứ không dùng làm chuẩn.

### 5.5 Trường `reason`

`reason` là mã lý do dạng chuỗi ASCII `snake_case`. Tập giá trị của `reason` **không** thuộc hợp đồng này và có thể thay đổi; chỉ có ràng buộc "không rỗng ở mọi event quyết định" là ràng buộc cố định.

---

## 6. Các trường DỄ BIẾN ĐỘNG giữa hai lần chạy

Phải **bỏ** các thứ sau trước khi so sánh kết quả hai lần chạy khác nhau. Để nguyên thì mọi phép so sẽ luôn ra "khác nhau".

| Chỗ | Thứ dễ biến động |
|---|---|
| Mọi dòng log | trường `ts` |
| Mọi dòng log | trường `run_id` |
| Báo cáo | trường `ts` |
| Báo cáo | trường `run_id` |
| Báo cáo | trường `log_files` (danh sách đường dẫn log) |
| Tên file log | `logs/<module>_<run_id>.jsonl` — đổi theo `run_id` |
| Tên file báo cáo | `reports/product_run_<run_id>.json` — đổi theo `run_id` |
| Thứ tự dòng trong log | các dòng của những `module` khác nhau nằm ở **các file khác nhau**; so sánh theo từng file |

---

## 7. DANH SÁCH THUỘC TÍNH ĐƯỢC PHÉP

> Hai bảng dưới đây chép cột `Thuộc tính` từ bản chốt ở cổng G1 — đúng tên, đúng thứ tự, không thêm, không bớt, không đổi tên.
>
> Đây là **danh sách trắng đóng**: thuộc tính nào không có tên trong bảng thì không được dùng làm đầu vào. Theo yêu cầu của Bách, chỉ ghi danh sách **được phép**, không ghi danh sách bị cấm.

`matching` được đọc đúng 10 thuộc tính:

| Thuộc tính |
|---|
| `ride.vehicle_type` |
| `ride.pickup_lat` |
| `ride.pickup_lon` |
| `driver.status` |
| `driver.vehicle_type` |
| `driver.lat` |
| `driver.lon` |
| `driver.trips_today` |
| `driver.acceptance_rate` |
| `driver.driver_id` |

`pricing` được đọc đúng 2 thuộc tính:

| Thuộc tính |
|---|
| `distance_km` |
| `requested_at` |
