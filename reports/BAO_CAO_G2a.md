# Báo cáo G2a — GSM sandbox

> **[Suy luận]** Soạn bởi `lead`, 20/10/2026. Trình pm chấm trước, sau đó trình Bách duyệt cổng. Mọi số liệu trong bảng lấy từ `docs/TASKS.md` / `docs/DECISIONS.md` đã commit, không viết mới ở đây.

## 1. Điều kiện qua G2a (`CLAUDE.md §5`)

| Điều kiện | Trạng thái |
|---|---|
| A chạy được trên mock data | **ĐẠT** — `python product/run_product.py` exit 0 |
| Log đủ | **ĐẠT** — 9 trường bắt buộc, 0 dòng sai, 0 quyết định thiếu `reason` |
| `reviewer` không còn mục "Chặn" | **ĐẠT** — T09f, 0 mục Chặn, review lần cuối trên `product/` |

## 2. Bằng chứng cổng

| | |
|---|---|
| `run_id` bằng chứng | `20261019T143340880` |
| `commit_at_run` | `d9f1f27` |
| `product_tree_at_run` | `3b2892b` |
| Manifest đã commit | `reports/logs_manifest_20261019T143340880.json` — `schema_version 0.3`, 5 trường tái lập (Q12 điều kiện (b)) |
| Bản sao lưu ngoài repo | 3 log + report, `sha256` khớp manifest (kiểm 18) |
| Log trong git | **không** — `logs/*.jsonl` ignore (Q12/Q20) |

Bằng chứng cổng đã đổi **năm** lần trong quá trình làm (`064336` → `075936693` → `081010446` → `142131055` → `142545373`/`143340880`), mỗi lần vì code hoặc dữ liệu đổi thật — không lần nào chọn lại vì kết quả không như ý.

## 3. Kết quả bộ kiểm — chạy lại toàn bộ trên bằng chứng cuối

| Nhóm | Kết quả |
|---|---|
| 15 kiểm máy (`tests/t07b_check.py`) | **PASS 15/15** |
| Kiểm 12 — `INTERFACE.md` không rò logic, bằng mắt | **PASS** (T09f, reviewer xác nhận lại) |
| Kiểm 17 — mọi đường thoát có log trước đó | **PASS** — 44 `return`/`raise`, 29 miễn có nguồn gốc |
| Kiểm 18 — manifest khớp bản sao lưu | **PASS** 3/3 `sha256` |
| **Kiểm 19 — nguyên tắc phủ nhánh (Q19)** | **PASS cả 9 mục a–i** |
| Kiểm 20 — nhánh trần hệ số giờ | **PASS 5/5** |

Bộ kiểm đã được commit vào `tests/` (trước khi security chạy, theo quyết định Bách 19/10) — tái lập được, không còn nằm ngoài repo.

## 4. Nguyên tắc phủ nhánh (Q19) — ba nhánh chết đã chạy thật

| Nhánh | Trước T09e | Sau T09e |
|---|---|---|
| Không ghép được tài xế | `n_unmatched = 0` | **40** (4,0%) |
| Bậc giá `(12;25]` tính tiền | 0 chuyến | **40** chuyến |
| Bậc giá `>25` tính tiền | 0 chuyến | **20** chuyến |
| Quãng đường max | 11,60 km | **39,18 km** |

Cách làm: **giữ** hộp toạ độ chính (tài xế không dời), thêm hai nhóm chuyến nhỏ (điểm đón ngoài vùng 4%; điểm đến xa 4%) — 920/1.000 chuyến giữ nguyên nguyên giá trị cũ, nên baseline so sánh trước/sau còn dùng được. Mọi tham số nằm trong `product/config/mock_data.json` (v0.2); tên khoá/biến/log **chỉ tả hình học dữ liệu**, không tả quan hệ với kết quả của A (T09e-b, sau khi `coder-product` tự nêu một tên khoá chưa trung tính).

## 5. Ba lỗi tự tìm ra và tự sửa trong quá trình G2a

| # | Lỗi | Ở đâu | Tìm ra bằng | Đã sửa |
|---|---|---|---|---|
| 1 | Whitelist âm thầm 20 số nguyên nhỏ (gồm biên bậc giá 12/25, giờ cao điểm 17/18/19) | bộ kiểm của lead (kiểm 14) | chạy lại trên dữ liệu mới, số liệu không khớp kỳ vọng | có, 47 chỗ miễn tường minh |
| 2 | Kiểm 18 báo PASS khi quét 0 file | bộ kiểm của lead | tự kiểm chéo sau sự cố 1 | có, 0 file nay là FAIL |
| 3 | Một lệnh kiểm ghi đè manifest của lệnh kiểm khác | bộ kiểm của lead | tự kiểm chéo | có, bỏ khối sinh trùng |

Không lỗi nào nằm trong `product/`. Chi tiết đầy đủ ở `docs/TASKS.md` mục "Kết quả T09e".

## 6. Rủi ro còn mở — không chặn G2a, chặn các cổng sau

| # | Rủi ro | Chặn cổng nào |
|---|---|---|
| R6 | Mở lại — đóng có điều kiện, điều kiện là T14c (chưa chạy) | G3 |
| R12 | Bộ kiểm của lead là máy dò đáp án + lead ngồi trong repo đọc được diff | G2b trở đi — đã có 6 quy tắc + R12 |
| Q21 thiếu bước 6 | Không có lần chạy B trên A có lỗi → TB-01/02/03 không tính được | G3 |
| `tests/` + `reports/` + checklist xếp loại | **Bách đã duyệt**, đã thực hiện | đã đóng |
| `CLAUDE.md §5` bảng cổng | Còn ghi G2b trước G3, trái trình tự Q21 | cần Bách sửa, không tự sửa |
| Chỉ thị 21:01 phần gốc | lead chưa nhận văn bản có mục A/B/C/D | đang chờ Bách gửi |

## 7. Việc cần Bách quyết, không chặn G2a

1. Bổ sung **bước 6 vào Q21** + ngoại lệ dạng *loại* cho quy tắc 1 (G2b) — để T14c chạy được.
2. Cập nhật thứ tự **G2b/G3** trong `CLAUDE.md §5` theo Q21.
3. Gửi lại phần gốc của **chỉ thị 21:01**.

## 8. Đề xuất

**G2a đủ điều kiện để Bách duyệt.** Mọi lệnh kiểm kỹ thuật ĐẠT, `reviewer` hết mục Chặn, bằng chứng cổng đầy đủ và tái lập được. Ba việc ở mục 7 không chặn G2a nhưng cần trả lời trước khi làm G3 (B xây và chạy trên A sạch).
