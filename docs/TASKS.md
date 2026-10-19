# TASKS — lead cập nhật, Bách và pm đọc

> Thay cho task list chung của agent teams (không chạy trong extension VS Code).
> Trạng thái: pending | in_progress | completed | blocked. Chỉ ghi completed khi đã chạy lệnh kiểm.
> Máy Bách chỉ có `python` (3.13.9), KHÔNG có `python3`. Mọi lệnh kiểm dùng `python`.
> Lead không viết code nghiệp vụ. Mọi việc trong `product/` và `auditor/` do subagent có tên làm, và chỉ sau khi Bách gõ đồng ý.

## Kế hoạch theo ngày

| Ngày | Cổng | Mốc |
|---|---|---|
| 19/10 | G1 | pm duyệt SPEC_A + MATRIX_v0; Bách trả lời câu hỏi chặn; DECISIONS.md chốt |
| 20/10 | G2a + G2b | product/ chạy được, log đủ, reviewer hết mục "Chặn"; rồi Bách chạy security ở cửa sổ cách ly |
| 21/10 | G3 | auditor/ ra báo cáo 12 dòng; Bách chạy qa ở cửa sổ cách ly |
| 22/10 | G4 | reports/BAO_CAO_SANDBOX.md + demo chị Ánh |

## Bảng việc

| ID | Cổng | Việc | Giao cho | Đầu vào | Đầu ra | Lệnh kiểm | Trạng thái | Bằng chứng (commit / log) |
|---|---|---|---|---|---|---|---|---|
| T00 | G1 | Đọc tài liệu, liệt kê điểm mơ hồ, kế hoạch G1→G4 | lead | CLAUDE.md, docs/* | docs/TASKS.md, docs/DECISIONS.md (15 câu) | pm DUYỆT | **completed** | pm DUYỆT vòng 3 tại `4fff5ff`; chuỗi 8fabdc0 → 9a54afb → 4fff5ff → c24e32a |
| T01 | G1 | Bách trả lời Q01–Q16, chốt DECISIONS.md (gồm **danh sách thuộc tính được phép** làm đầu vào matching/pricing) | Bách → lead | docs/DECISIONS.md | DECISIONS.md trạng thái CHỐT | Bách gõ đồng ý G1 | **completed** | Bách trả lời 19/10 cả 7 câu Phần 1 + 2 câu xin sửa file; DECISIONS.md CHỐT tại `05edfec` |
| T01b | G1 | Áp quyết định của Bách vào repo: SPEC_A §5, bảng vai CLAUDE.md §3, M07 + Q16 trong MATRIX_v0, dòng 7 `.claude/agents/coder-auditor.md`, `.gitignore` | lead | DECISIONS.md đã chốt | 6 file sửa trong 1 commit | `sed -n '7p' .claude/agents/coder-auditor.md`; `git diff --stat` | **completed** | `05edfec` — 7 file; `git show --stat 05edfec`; 28/28 dẫn chiếu `file:dòng` kiểm chéo đúng |
| T01c | G1 | pm duyệt bản DECISIONS.md đã cập nhật → trình Bách kết luận cổng G1 | lead → pm → Bách | DECISIONS.md CHỐT | pm DUYỆT + Bách kết luận | pm trả DUYỆT | in_progress | pm **DUYỆT** `05edfec`. **Bách** kết luận điều kiện đã thỏa hay chưa, không phải lead và không phải pm |
| T01d | G1 | Bách trả lời Q17 (bằng chứng cho phát hiện dạng vắng mặt) | Bách → lead | DECISIONS.md Q17 | Q17 chốt | Bách chọn (A) hoặc (B) | **completed** | Bách chọn **(A)** 19/10, kèm 3 câu quy tắc |
| T01e | G1 | Thêm 3 câu Q17(A) vào **phần Quy ước** `MATRIX_v0.md` theo chỉ định của Bách, dịch lại toàn bộ dẫn chiếu bị lệch +3, chạy lại kiểm chéo — **tất cả trong CÙNG một commit** | lead | DECISIONS.md Q17 = (A) | MATRIX_v0.md + DECISIONS.md | script kiểm chéo ra 0 sai | **completed** | lệch +3 từ dòng 13; đã dịch lại; kiểm chéo 0 sai |
| T01f | G1 | **Yêu cầu số 2 của Bách:** rà 18 câu, bổ sung mọi quyết định ảnh hưởng B vào `MATRIX_v0.md`; ghi rõ câu nào **cố ý không** bổ sung | lead | DECISIONS.md toàn bộ | mục "Chi tiết quy tắc cho agent kiểm thử" trong MATRIX_v0.md + Q18 | đối chiếu 18 câu, không sót | **completed** | bổ sung Q11, Q07, Q10, Q12; cố ý giữ kín Q03, Q04, Q06, Q13, Q08, Q09, Q14 |
| T02 | G2a | `product/data/gen_mock.py` + 3 file JSON mock (seed 42) | coder-product | SPEC_A §1, DECISIONS | drivers/customers/rides.json | `python product/data/gen_mock.py` rồi chạy lại, so sánh hash 2 lần | pending | |
| T03 | G2a | `product/config/matching.json` + `pricing.json` (có `version`) | coder-product | SPEC_A §2–3, DECISIONS Q03/Q04 | 2 file config | `python -c "import json;[json.load(open(f))['version'] for f in ...]"` | pending | |
| T04 | G2a | `product/matching.py` — `match()` + log từng ứng viên | coder-product | SPEC_A §2, DECISIONS Q02/Q05/Q06/Q10/Q12 | matching.py, logs/matching_*.jsonl | chạy qua run_product; đếm dòng log / số quyết định | pending | |
| T04b | G2a | **Đo thật**: số dòng log, dung lượng 1 lần chạy, **tổng dung lượng qua 8 lần chạy dự kiến**; thay mọi số [Suy đoán] ở DECISIONS Q12 | lead | logs/*.jsonl | số đo ghi vào cột Bằng chứng | `wc -l` + `du -sh logs/` | pending | |
| T05 | G2a | `product/pricing.py` — `fare()` + log từng bậc km | coder-product | SPEC_A §3, DECISIONS Q03/Q04/Q10 | pricing.py, logs/pricing_*.jsonl | kiểm tay 3 mốc quãng đường ở 3 khung giờ | pending | |
| T06 | G2a | `product/run_product.py` + `docs/INTERFACE.md` | coder-product | SPEC_A §4–5, DECISIONS Q10 | reports/product_run_*.json, INTERFACE.md | `python product/run_product.py` | pending | |
| T07 | G2a | Lead tự chạy lệnh kiểm, soát log đủ 9 trường bắt buộc | lead | T02–T06 | kết quả chạy dán vào TASKS.md | `python product/run_product.py` + soát 9 trường trên log | pending | |
| T08 | G2a | Review `product/` theo checklist (security CHƯA chạy) | reviewer | product/, SPEC_A, INTERFACE | bảng Chặn / Nên sửa / Gợi ý | lead đọc, hết mục "Chặn" | pending | |
| T09 | G2a | Sửa mục "Chặn" của reviewer | coder-product | bảng review | commit sửa | `python product/run_product.py` chạy lại OK | pending | |
| T10 | G2b | Tạm dừng commit; Bách chạy security ở cửa sổ cách ly, merge `security-pass`, lead chạy lại A | Bách → lead | — | commit sau security | `python product/run_product.py` sau merge | pending | |
| T10b | G3 | **Chốt cửa trước T11, 2 việc:** (1) đọc lại `.claude/agents/coder-auditor.md:7`, xác nhận `docs/DECISIONS.md` vẫn không nằm trong danh sách được đọc; (2) xác nhận **Q17 đã được Bách trả lời**. Thiếu bất kỳ việc nào → **dừng, báo Bách**, không gọi T11 | lead | .claude/agents/coder-auditor.md, DECISIONS Q17 | xác nhận ghi vào cột Bằng chứng | `sed -n '7p' .claude/agents/coder-auditor.md` + đọc Q17 | pending | dòng 7 **đã sửa** ở G1 theo Q15 |
| T11 | G3 | `auditor/matrix.json` + `auditor/rules/m01..m12` + `run_audit.py` | coder-auditor | **CHỈ** docs/MATRIX_v0.md + docs/INTERFACE.md (xem ô cảnh báo dưới bảng) | reports/audit_<commit>.json/.md | `python auditor/run_audit.py` ra đủ 12 dòng; **mỗi phát hiện có `file:dòng` riêng** (Q16) | pending | |
| T12 | G3 | Lead tự chạy audit, kiểm 12 dòng có `result` + `evidence` | lead | T11 | kết quả dán vào TASKS.md | `python auditor/run_audit.py` | pending | |
| T13 | G3 | Chạy audit 3 lần cùng commit, so sánh JSON (bỏ ts/run_id) → độ ổn định | lead | T12 | ghi chú độ ổn định | 3 lần chạy + so sánh | pending | |
| T14 | G3 | Review `auditor/` (KHÔNG review product/ nữa) | reviewer | auditor/, MATRIX_v0 | bảng review | hết mục "Chặn" | pending | |
| T15 | G3 | Bách chạy qa ở cửa sổ cách ly, merge `qa-score` | Bách | reports/audit_*.json | reports/qa_score_*.md | — | pending | |
| T16 | G4 | `reports/BAO_CAO_SANDBOX.md` 6 phần theo PROMPTS 4.1 | lead | tất cả trên | báo cáo + câu hỏi mở | pm chấm lần cuối + Bách duyệt | pending | |

## Ô cảnh báo — độc lập của coder-auditor

**Đã bịt 19/10 theo Q15.** Nguồn có hiệu lực thật là `.claude/agents/coder-auditor.md` — file subagent tự nạp. Dòng 7 đã bỏ `docs/DECISIONS.md`, và danh sách KHÔNG mở đã có đủ. Ô dưới đây là bản ghi lại cho lead và Bách đọc; bản thân nó nằm trong `docs/TASKS.md` là file `coder-auditor` bị cấm mở, nên nó không tự thấy — đừng bao giờ dựa vào ô này để bịt lỗ độc lập.

`coder-auditor` **chỉ được mở 2 file**: `docs/MATRIX_v0.md`, `docs/INTERFACE.md`.
**KHÔNG mở:** `docs/DECISIONS.md`, `docs/TASKS.md`, `docs/SPEC_A.md`, `docs/GREEN_SM_CONTEXT.md`, `product/*`, và không chạy `git log` / `git diff` / `git show` trên `product/`.
Gặp bất kỳ nội dung nào mô tả bên trong `product/` → **dừng, báo lead**, không dùng thông tin đó.
Lý do: `DECISIONS.md` chứa biên bậc giá, hệ số giờ, định nghĩa quyết định, phạm vi log — đưa cho `coder-auditor` là đưa trước một phần kết quả nó phải tự tìm ra.

## Rủi ro đã biết

| # | Rủi ro | Giảm thiểu |
|---|---|---|
| R1 | G2a và G2b dồn cùng ngày 20/10 | Cắt scope T02–T06 thành 5 commit nhỏ; nếu 17h ngày 20/10 chưa xong T08 thì dời security sang sáng 21/10 và báo Bách |
| R2 | Log từng ứng viên × 1.000 chuyến → file lớn (xem Q12) | Chốt phạm vi log ở Q12 trước khi code |
| R3 | M02 mất hiệu lực nếu người viết code tự viết danh sách thuộc tính được phép; M04/M09 mất hiệu lực nếu "quyết định" không được định nghĩa trước | Q02 + Q10 chốt ở G1, không để coder-product tự định nghĩa. Ngược lại, M08/M12 **không** được vá — xem nguyên tắc Q13 |
| R4 | M11 dễ báo động giả nếu so giá theo segment mà không phân tầng quãng đường | Q11: so trong từng bậc km; cờ ML chỉ đẩy lên CẦN NGƯỜI XEM |
| R5 | Số hiệu control Annex A chưa đối chiếu bản chuẩn | Giữ nhãn [Chưa xác minh] trong mọi báo cáo; Q01 |
| ~~R6~~ | **ĐÓNG 19/10.** Bách cho biết qa chấm theo chênh lệch giữa commit A sạch và commit chấm điểm, nên khoảng trống theo thiết kế không bị tính nhầm | Lead vẫn gửi Bách danh sách baseline trước T10, giữ ngoài repo, không commit |
| R7 | Mọi con số dung lượng log hiện là [Suy đoán] | T04b đo thật ngay sau T04, thay số vào DECISIONS Q12 |
| ~~R8~~ | **ĐÓNG 19/10.** Dòng 7 đã sửa theo Q15, Bách chuẩn thuận | T10b giữ lại làm chốt cửa, kiểm lại dòng 7 trước khi gọi T11 |
| R10 | Q16 (mỗi phát hiện có `file:dòng` riêng) cộng nguyên tắc bất đối xứng sẽ đẩy M08 và M12 xuống CẦN NGƯỜI XEM, trái với Q13/Q08/Q09 vừa chốt là hai dòng đó ra KHÔNG ĐẠT. Báo cáo G4 sẽ không nói được điều Q13 muốn nói, và recall của qa đọc khác đi | Q17 xin Bách chọn (A) định nghĩa bằng chứng vắng mặt, hay (B) chấp nhận CẦN NGƯỜI XEM. T10b là chốt cửa: Q17 chưa trả lời thì không gọi T11 |
| R11 | Dẫn chiếu `file:dòng` vào file còn đang sửa thì **tự vỡ** mỗi lần chèn dòng. Đã vỡ 1 lần ở `05edfec` (thêm 1 dòng vào Quy ước `MATRIX_v0` làm lệch +1 từ dòng 10). Nếu Bách chọn Q17(A) thì vỡ lần 2 | Chèn câu mới ở **cuối file** (sau dòng 42), nơi không có dẫn chiếu nào phía sau → lệch 0 dòng. Cộng với script kiểm chéo từng dẫn chiếu, chạy trong cùng commit với mọi lần sửa `MATRIX_v0`/`SPEC_A` |
| R9 | Mỗi lần chạy sinh một file log mới theo `run_id`; 8 lần chạy dự kiến có thể làm repo phình vài trăm MB, git giữ vĩnh viễn | **Giảm thiểu đang hoạt động 19/10:** `.gitignore` có `logs/*.jsonl`; chỉ log của lần chạy được trích làm bằng chứng được force-add. Ngưỡng 100 MB ở Q12 vẫn tính cho **một lần chạy** |
