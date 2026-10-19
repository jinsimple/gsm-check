# Bộ lệnh kiểm của lead

> **[Suy luận]** Thư mục này là **bộ kiểm độc lập của `lead`**, không phải unit test của `product/`.
> Nó tồn tại để báo cáo G4 nói "18/18 PASS" là một **số đo tái lập được**, không phải một lời nói.

## ⚠️ Hai cảnh báo đọc trước khi chạy bất cứ gì

### 1. `coder-auditor` KHÔNG mở thư mục này

Bách chốt 19/10, đã ghi vào `.claude/agents/coder-auditor.md`. Lý do: `t07b_check.py` chứa **24 ca giá tính tay với số tiền kỳ vọng**, tên `tier_id`, tên `event`, và kỳ vọng độ phủ nhánh — tức là **đặc tả bên trong `product/`**. Agent kiểm thử B phải tự tìm những thứ đó bằng quy tắc tự động; đó chính là điều đang được đo.

### 2. Từ G2b trở đi, KHÔNG chạy bất cứ file nào ở đây

Sau khi Bách merge `security-pass`, bộ kiểm này là một **máy dò đáp án chính xác**: kiểm 9 chỉ ra ca giá nào lệch, kiểm 13 chỉ ra bước lọc bị sửa, kiểm 14 chỉ ra hằng số bị cắm vào, kiểm 17 chỉ ra chỗ log bị bỏ, kiểm 19 chỉ ra nhánh bị đổi, kiểm 20 so thẳng với **số tiền**. Chạy nó là `lead` tự đọc đáp án, phá `CLAUDE.md §3`.

Quy tắc đầy đủ ở `docs/TASKS.md`, ô **"Việc của lead ở G2b"** — 6 quy tắc, và rủi ro **R12**. Tóm lại: ở G2b `lead` được chạy **đúng một** lệnh, `python product/run_product.py`, và chỉ đọc exit code.

## Cách chạy

Mọi script nhận **đường dẫn tuyệt đối** làm đối số, không đoán thư mục. Trên Windows cần `PYTHONIOENCODING=utf-8` vì console cp1252 không in được tiếng Việt.

| File | Lệnh | Kiểm gì |
|---|---|---|
| `t07b_check.py` | `<repo> <run_id>` | 15 lệnh kiểm máy: chạy được, seed xác định, 9 trường log, `reason`, số quyết định, `version` config, chỉ stdlib, **24 ca giá tính tay**, `INTERFACE` khớp Q02, dung lượng log, log đủ ứng viên bị loại, không hardcode hằng số nghiệp vụ (quét **hết** `product/**/*.py`), `sha256` dữ liệu trong log |
| `kiem17_18.py` | `<repo> <thư mục sao lưu> <run_id>` | **kiểm 17** — mọi đường thoát `return`/`raise` trên đường quyết định có log trước đó (vế 2 của M04), bằng AST không bằng regex. **kiểm 18** — manifest khớp bản sao lưu ngoài repo |
| `kiem19_manifest.py` | `<repo> <thư mục sao lưu> <run_id> [commit_lúc_chạy]` | **kiểm 19** — mỗi nhánh quyết định chạy ≥ 1 lần (10 mục a–j; **j hiện FAIL**: nhánh phá hoà trong `match()` chưa hoà thật trên dữ liệu bằng chứng — xem `kiem21_tiebreak.py`). Và sinh **manifest `schema_version` 0.4** (0.3 → 0.4 khi `worktree_clean` tách thành hai trường; 0 file log khớp thì FAIL và **không viết file**, không còn ghi manifest cho một lần chạy chưa từng xảy ra) |
| `kiem20_cap.py` | `<repo>` | **kiểm 20** — nhánh trần hệ số giờ, bằng bản sao config **trong bộ nhớ**; không sửa `product/config/pricing.json` |
| `kiem21_tiebreak.py` | `<repo>` | **kiểm 21** — chẩn đoán nhánh phá hoà trong `match()`, gọi trực tiếp với dữ liệu dựng tay; không sửa `mock_data.json`. PASS chỉ chứng minh code đúng **khi bị buộc hoà**, không chứng minh nhánh đã chạy thật trên `rides.json` |
| `verify_refs.py` | `<repo>` | mọi dẫn chiếu `file:dòng` trong `docs/` còn trỏ đúng chỗ, **và** không có dẫn chiếu nào chưa được đăng ký |

## Ba nguyên tắc dựng bộ kiểm này

**1. Danh sách miễn phải có nguồn gốc, không whitelist mù.** Kiểm 14 và kiểm 17 đều in **toàn bộ** danh sách miễn mỗi lần chạy, mỗi chỗ khớp file + giá trị/tên hàm + chuỗi ngữ cảnh, kèm lý do. Lý do: một chỗ từng được miễn **do may** — `_RUN_ID_MS_DIGITS = 3` lọt qua chỉ vì số `3` trùng tình cờ với một giá trị config. Miễn do may thì lần sau một hằng số nghiệp vụ trùng giá trị config cũng sẽ lọt.

**2. Một lệnh kiểm quét quá ít file thì báo PASS, không báo lỗi.** Kiểm 14 ban đầu chỉ quét 2 file và **PASS**, trong khi hằng số nghiệp vụ nằm ở `run_product.py` — ngoài phạm vi quét. `reviewer` tìm ra. Nay mọi lệnh quét `product/**/*.py` và **in số file đã quét**.

**3. Kiểm 17 xét vị trí trong AST, không khớp chuỗi.** Heuristic kiểu *"có `if log is not None` trong cửa sổ trước `raise`"* báo **dương tính giả**, vì chuỗi đó còn trong dòng gán `log = log if log is not None else default_logger()`.

## Giới hạn đã biết

- `kiem17_18.py` còn sinh manifest `schema_version` **0.1** (chỉ `run_id` + hash). Bản dùng thật là **0.3** trong `kiem19_manifest.py`. Khối manifest trong `kiem17_18.py` là **di sản**, giữ để chạy lại được lịch sử; đừng dùng nó làm bằng chứng mới.
- `kiem19_manifest.py` lấy commit lúc chạy từ **đối số thứ 4**. Thiếu đối số đó thì nó dùng `HEAD`, và `commit_at_run` sẽ **nói sai** nếu đã có commit nào chạm `product/` sau lần chạy. Trường `product_unchanged_since_run` bắt được chuyện đó và làm manifest **FAIL**, nhưng vẫn nên truyền đối số.
- Bộ kiểm này **không** đo được chính nó. Nó đã sai **năm** lần và cả năm lần do người khác (pm, hoặc lead tự kiểm chéo sau khi pm chỉ hướng) tìm ra, không do nó tự báo: whitelist âm thầm theo giá trị config (kiểm 14), vacuous-pass khi quét 0 file (ba chỗ riêng — `t07b_check.py`, `kiem17_18.py`, `kiem19_manifest.py`), một lệnh kiểm ghi đè manifest của lệnh khác, và một trường đơn (`worktree_clean`) mô tả hai thời điểm khác nhau của cùng một quá trình.
- `kiem19_manifest.py` **từ chối ghi đè** một manifest đã commit cho cùng `run_id` — in một dòng, thoát mã 2. Muốn sinh lại thì dùng `run_id` mới. Một file bằng chứng bị viết lại mỗi lần chạy thì không còn là bằng chứng đóng băng.
- Thiếu đối số bắt buộc (`<repo>`, thư mục sao lưu, `run_id`) in dòng hướng dẫn và thoát mã 2, thay vì traceback. Thiếu **thư mục sao lưu** (cố ý không nằm trong repo, Q12/Q20) thì kiểm 18 in **SKIPPED có lý do**, thoát mã 0 — khác với FAIL: không có gì để đối chiếu, không phải sai lệch.
