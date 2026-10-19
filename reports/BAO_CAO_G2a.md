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
| Manifest đã commit | `reports/logs_manifest_20261019T143340880.json` — `schema_version 0.4` (nâng từ 0.3 vì `worktree_clean` tách thành `_at_run`/`_at_manifest`), 6 trường tái lập (Q12 điều kiện (b)) |
| Bản sao lưu ngoài repo | 3 log + report, `sha256` khớp manifest (kiểm 18) |
| Log trong git | **không** — `logs/*.jsonl` ignore (Q12/Q20) |

Bằng chứng cổng đã đổi nhiều lần trong quá trình làm (`064336` → `075936693` → `081010446` → `142131055` → `143340880`). **Ba lần chạy gần nhất có manifest đã commit, mỗi lần một `product_tree_at_run` khác nhau** — `6f73768`, `eec8271`, `3b2892b` — nên việc code thật sự đổi giữa các lần là kiểm chứng được từ ngoài bằng `git rev-parse <commit>:product`, không cần tin lời lead. Hai lần chạy trước đó có từ khi cơ chế manifest chưa tồn tại, không đối chiếu được theo cách này.

## 3. Kết quả bộ kiểm — chạy lại toàn bộ trên bằng chứng cuối

| Nhóm | Kết quả |
|---|---|
| 15 kiểm máy (`tests/t07b_check.py`) | **PASS 15/15** |
| Kiểm 12 — `INTERFACE.md` không rò logic, bằng mắt | **PASS** (T09f, reviewer xác nhận lại) |
| Kiểm 17 — mọi đường thoát có log trước đó | **PASS** — 44 `return`/`raise`, 29 miễn có nguồn gốc |
| Kiểm 18 — manifest khớp bản sao lưu | **PASS** 3/3 `sha256` |
| **Kiểm 19 — nguyên tắc phủ nhánh (Q19)** | **FAIL 1 mục (j)**, PASS 9/10 — xem mục 4b |
| Kiểm 20 — nhánh trần hệ số giờ | **PASS 5/5** |

Bộ kiểm đã được commit vào `tests/` (trước khi security chạy, theo quyết định Bách 19/10). **Mã** tái lập được từ repo. Kiểm 17, 18, 19 cần thêm **thư mục sao lưu ngoài repo** và log của lần chạy bằng chứng — hai thứ cố ý không vào git (Q12/Q20) — nên chỉ chạy lại được trên máy giữ bản sao lưu đó; thiếu thư mục đó thì kiểm 18 báo **SKIPPED có lý do**, không phải lỗi.

## 4. Nguyên tắc phủ nhánh (Q19) — ba nhánh chết đã chạy thật

| Nhánh | Trước T09e | Sau T09e |
|---|---|---|
| Không ghép được tài xế | `n_unmatched = 0` | **40** (4,0%) |
| Bậc giá `(12;25]` tính tiền | 0 chuyến | **40** chuyến |
| Bậc giá `>25` tính tiền | 0 chuyến | **20** chuyến |
| Quãng đường max | 11,60 km | **39,18 km** |

Cách làm: **giữ** hộp toạ độ chính (tài xế không dời), thêm hai nhóm chuyến nhỏ (điểm đón ngoài vùng 4%; điểm đến xa 4%) — 920/1.000 chuyến giữ nguyên nguyên giá trị cũ, nên baseline so sánh trước/sau còn dùng được. Mọi tham số nằm trong `product/config/mock_data.json` (v0.2); tên khoá/biến/log **chỉ tả hình học dữ liệu**, không tả quan hệ với kết quả của A (T09e-b, sau khi `coder-product` tự nêu một tên khoá chưa trung tính).

## 4b. Nhánh chết thứ tư — pm phát hiện, chưa đóng được ở G2a

**`tie_break` ghi 960/960 dòng đều `no_tie`.** Quy tắc phá hoà `SPEC_A.md:32` (*"để kết quả xác định"*) chưa quyết định điều gì lần nào trên `rides.json` hiện tại — khoảng cách haversine là float nên hoà thật gần như không xảy ra. Lead đã xếp nhầm nhánh này là không thuộc diện thiếu (lý do *"ghi log mọi chuyến"* đúng cho `auto_accept_eval` nhưng sai cho `tie_break`: ghi log bước đánh giá không có nghĩa là nhánh **rẽ** đã chạy).

**Kiểm 21 (chẩn đoán, cùng khuôn kiểm 15/kiểm 20) xác nhận code đúng khi bị buộc phải hoà** — cả hai ca (hoà `trips_today` khác nhau; hoà cả hai) đều PASS. Nhưng **điều đó không làm nhánh thật chạy**: kiểm 19 mục j vẫn **FAIL**, vì số lần hoà thật trên dữ liệu mặc định là 0.

**Đây là điểm G2a chưa đóng, cần Bách quyết giữa hai lựa chọn** (pm đề xuất, khác nhau ở G4):

| | Cách A — đưa hoà thật vào dữ liệu | Cách B — ghi Q19 có một ngoại lệ |
|---|---|---|
| Làm gì | Hai tài xế **cùng toạ độ** → mọi chuyến đều hoà với cặp đó, tất định, hình học thuần | Giữ dữ liệu nguyên; ghi Q19 có đúng 1 ngoại lệ, lý do *khoảng cách float nên hoà thật không xuất hiện tự nhiên*, bằng chứng = kiểm 21 |
| Được | Q19 **không ngoại lệ nào** | Không đổi dữ liệu lần nữa ngay trước cổng |
| Mất | Đổi `mock_data.json` lần nữa ngay trước cổng | Q19 mất tính "không ngoại lệ" — sau khi kiểm 20 vừa gỡ ngoại lệ cuối cùng ở trần hệ số |

Hệ quả nếu **không chọn cách nào** (để nguyên): nếu thứ tự phá hoà bị sửa sau này thì **không dòng log nào, không lệnh kiểm nào, và cả M10 cũng không phát hiện**.

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
| Nhánh phá hoà (mục 4b) | Chưa chạy thật trên dữ liệu mặc định; cần Bách quyết có đưa vào `mock_data.json` không | G3 (M10 không kiểm được nhánh chưa chạy) |
| Chỉ thị 21:01 — chỉ nhận một phần | Lead đã nhận **nội dung mục B** (Bách trích trực tiếp vào câu trả lời ngày 19/10 dùng cho Q21: *"B xây và chạy trên A sạch → reviewer hết mục Chặn → tag b-freeze → báo tôi → tôi mới merge security-pass"*) và đã áp dụng đúng vào Q21. **Chưa xác nhận nhận được mục A, C, D** hay văn bản gốc đầy đủ — Bách cho biết đã gửi 19/10, có thể là chuyện giao nhận giữa các tab chứ không phải Bách quên |

## 7. Việc cần Bách quyết, không chặn G2a

1. **Quyết định chính của mục này: có đưa dữ liệu hoà thật vào `mock_data.json` để đóng mục j của kiểm 19 không** (mục 4b). Không chặn G2a nhưng để ngỏ thì M10 không kiểm được đúng nhánh này ở G3.
2. Bổ sung **bước 6 vào Q21** + ngoại lệ dạng *loại* cho quy tắc 1 (G2b) — để T14c chạy được.
3. Cập nhật thứ tự **G2b/G3** trong `CLAUDE.md §5` theo Q21.
4. Xác nhận/gửi lại **mục A, C, D** của chỉ thị 21:01 nếu còn nội dung lead chưa nhận.

## 8. Đề xuất

**Ba điều kiện hình thức của G2a đều ĐẠT** (mục 1): A chạy được, log đủ, `reviewer` hết mục Chặn. Bằng chứng cổng đầy đủ; mã kiểm tái lập được từ repo, ba lệnh kiểm cần thêm bản sao lưu ngoài repo (mục 3).

**Nhưng bộ kiểm không "mọi lệnh kiểm kỹ thuật ĐẠT" — có 1 mục FAIL đã biết và đã khai báo** (kiểm 19 mục j, nhánh phá hoà). Đề xuất: **Bách duyệt G2a với FAIL này được ghi nhận rõ**, không phải G2a "sạch tuyệt đối" — cùng cách R6 được giữ là "mở lại" ở mục 6 thay vì gọi là đã xử lý. Bốn việc ở mục 7 không chặn G2a nhưng cần trả lời trước khi làm G3 (B xây và chạy trên A sạch), và mục 7.1 nên trả lời sớm nhất vì nó còn ảnh hưởng tới chính `mock_data.json`.
