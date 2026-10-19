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

## Kế hoạch G2a — chốt trước khi gọi coder-product

**Cổng G1 đã qua:** pm DUYỆT `2487aa0`, Bách DUYỆT và cho sang G2a (19/10).

### Gọi coder-product mấy lần

**Một lần, giao cả T02–T06.** Không chia 5 lần gọi: subagent tự commit sau mỗi file theo định nghĩa vai của nó, nên chia nhỏ chỉ làm mất ngữ cảnh giữa các lần gọi mà không thêm chốt kiểm nào. Lead chốt kiểm ở T07, sau khi có đủ cả 5 phần.

### Lead giao gì cho coder-product

Được đọc: `CLAUDE.md`, `docs/SPEC_A.md`, `docs/DECISIONS.md`.
Nhấn mạnh 5 điều trong lời giao việc:

1. **Chép nguyên** bảng danh sách thuộc tính được phép ở `DECISIONS.md` Q02 sang `INTERFACE.md`. Không thêm, không bớt. Thiếu thuộc tính → nhắn lead, dừng chờ.
2. **Không vá** theo MATRIX (nguyên tắc Q13). Cụ thể: **không** thêm cờ người-xem-xét cho `auto_accept`, **không** thêm ngưỡng cảnh báo `auto_accept`, **không** viết tài liệu đánh giá tác động. Làm đúng SPEC_A, không hơn.
3. **Ràng buộc cứng `CLAUDE.md §2` vẫn tuyệt đối** — đây là chỗ ngược với điều 2, phải đọc kỹ cả hai: chỉ stdlib, seed 42, log JSONL đủ 9 trường cho mọi quyết định, mọi tham số nghiệp vụ trong config có `version`, không hardcode.
4. `INTERFACE.md` phải định nghĩa enum `event`, event nào là quyết định, và **liệt kê các trường dễ biến động** (`ts`, `run_id`, đường dẫn log) — `MATRIX_v0.md` đã hẹn lấy mấy thứ này từ `INTERFACE.md`.
5. Không đọc, không sửa `auditor/`. Không nhắn `coder-auditor`.
6. **`INTERFACE.md` không được rò logic.** `SPEC_A.md:55` ghi rõ "**Không** mô tả logic bên trong", và đây là **file duy nhất** nối `product/` với `coder-auditor`. Chỉ gồm 5 thứ `SPEC_A.md:54` liệt kê. Schema config chỉ nêu **tên khoá và kiểu dữ liệu** — **KHÔNG** nêu giá trị, biên bậc, hệ số, ngưỡng. Không câu nào mô tả thuật toán, thứ tự lọc, cách phá hoà, hay cách tính giá. Viết "`pricing.json` có khoá `tiers` kiểu list" thì được; viết "gồm 4 bậc 0-2 km, 2-12 km…" thì **không**.

### Lệnh kiểm lead TỰ chạy ở T07 — không nhận báo cáo suông

| # | Kiểm gì | Lệnh |
|---|---|---|
| 1 | Chạy được bằng một lệnh | `python product/run_product.py` → exit 0 |
| 2 | Seed 42 cho kết quả xác định | chạy `gen_mock.py` 2 lần, so `sha256` của 3 file JSON |
| 3 | Cùng đầu vào → cùng kết quả (chuẩn bị cho M10) | chạy `run_product.py` 2 lần, so `reports/product_run_*.json` sau khi bỏ `ts`, `run_id` |
| 4 | Log đủ 9 trường ở **mọi** dòng | **Điều kiện tiên quyết trước khi tin kết quả:** có ít nhất 1 file khớp `logs/*.jsonl`, **và** tên file khớp mẫu `<module>_<run_id>.jsonl` theo `CLAUDE.md §3`. Thiếu một trong hai thì kiểm 4 **đạt rỗng** — quét không ra file nào cũng cho 0 dòng thiếu. Sau đó mới đọc hết `logs/*.jsonl` đếm dòng thiếu trường |
| 5 | Mọi quyết định có `reason` không rỗng | script lọc dòng có `decision` khác null, kiểm `reason` |
| 6 | Số quyết định = 2.000 (Q10) | đếm event `match_result` + `fare_result` |
| 7 | Config có `version` | đọc 2 file config, in `version` |
| 8 | Chỉ stdlib | thu mọi `import` trong `product/`, đối chiếu `sys.stdlib_module_names` |
| 9 | Pricing đúng bậc và hệ số, **kể cả ở biên** | so với bảng giá trị kỳ vọng tính tay bên dưới |
| 10 | Bảng thuộc tính trong `INTERFACE.md` khớp `DECISIONS.md` Q02 | so từng dòng, phải khớp tuyệt đối |
| 11 | Dung lượng log thật (T04b) | `wc -l` + `du -sh logs/` |
| 12 | **`INTERFACE.md` không rò logic** | lead **tự đọc hết file bằng mắt**, đối chiếu `SPEC_A.md:54-55`, liệt kê từng câu nghi là mô tả logic. Không script được. Nghi ngờ thì cắt |
| 13 | **Log đủ ứng viên BỊ LOẠI** | lấy 3 `ride_id` bất kỳ, đếm dòng log ứng viên của từng chuyến → phải **= 200** (toàn bộ `drivers.json`), không phải số ứng viên qua lọc. Mỗi dòng bị loại phải có `reason` đúng lý do: `not_idle`, `wrong_vehicle_type`, `out_of_radius` |
| 14 | **Không hardcode hằng số nghiệp vụ** | duyệt AST `matching.py` + `pricing.py`, thu mọi hằng số số học, bỏ nhóm vô hại (0, 1, 2 làm chỉ số; hằng trong công thức haversine), phần còn lại **phải có trong `config/*.json`**. Dư số nào thì hỏi `coder-product` số đó ở đâu ra |

**Kiểm 13 lệch con số thì DỪNG, không sửa vội** — chẩn đoán bằng log trước, theo `CLAUDE.md:30`.

**Bẫy "đạt rỗng" ở kiểm 4.** Nếu `coder-product` đặt tên log sai quy ước (ví dụ `logs/product.log` thay vì `logs/<module>_<run_id>.jsonl`) thì `logs/*.jsonl` không khớp file nào, script đếm 0 dòng thiếu trường và **báo đạt trong khi không có log nào cả**. Vì vậy kiểm 4 phải khẳng định sự tồn tại và tên file trước. Kiểm 13 không dính bẫy này vì 0 ≠ 200 sẽ fail to tiếng. Quy ước tên file đã được đưa thẳng vào lời giao việc cho `coder-product`.

### Bảng giá kỳ vọng cho kiểm 9 — TÍNH TAY TRƯỚC KHI CHẠY

Theo Q03 (bậc nửa mở, giữ phần lẻ) và Q04 (giờ nguyên 0–6 → 0.9; 7–9 và 17–19 → 1.2; còn lại 1.0), làm tròn **lên** bội số 1.000đ.

Giá gốc theo quãng đường `d`: `d ≤ 2` → 30.000 ; `2 < d ≤ 12` → 30.000 + (d−2)×15.000 ; `12 < d ≤ 25` → 180.000 + (d−12)×14.000 ; `d > 25` → 362.000 + (d−25)×12.000.

**9 ca gốc:**

| d (km) | giờ | hệ số | giá gốc | trước làm tròn | **kỳ vọng** |
|---|---|---|---|---|---|
| 1.5 | 3 | 0.9 | 30.000 | 27.000 | **27.000** |
| 1.5 | 8 | 1.2 | 30.000 | 36.000 | **36.000** |
| 1.5 | 14 | 1.0 | 30.000 | 30.000 | **30.000** |
| 8 | 3 | 0.9 | 120.000 | 108.000 | **108.000** |
| 8 | 8 | 1.2 | 120.000 | 144.000 | **144.000** |
| 8 | 14 | 1.0 | 120.000 | 120.000 | **120.000** |
| 30 | 3 | 0.9 | 422.000 | 379.800 | **380.000** |
| 30 | 8 | 1.2 | 422.000 | 506.400 | **507.000** |
| 30 | 14 | 1.0 | 422.000 | 422.000 | **422.000** |

**Biên quãng đường** (giờ 14, hệ số 1.0, để tách riêng logic bậc):

| d (km) | giá gốc | **kỳ vọng** | bắt lỗi gì |
|---|---|---|---|
| 2.0 | 30.000 | **30.000** | biên trên của bậc mở cửa |
| 2.1 | 31.500 | **32.000** | vừa qua biên → phải tính 15.000/km |
| 12.0 | 180.000 | **180.000** | biên 15.000 → 14.000 |
| 12.1 | 181.400 | **182.000** | vừa qua biên |
| 25.0 | 362.000 | **362.000** | biên 14.000 → 12.000 |
| 25.1 | 363.200 | **364.000** | vừa qua biên |

**Biên giờ** (d = 8 km, giá gốc 120.000):

| giờ | hệ số | **kỳ vọng** | bắt lỗi gì |
|---|---|---|---|
| 0 | 0.9 | **108.000** | đầu khung đêm |
| 6 | 0.9 | **108.000** | **chỗ Q04 phải quyết vì SPEC bỏ trống khoảng 6h–7h** |
| 7 | 1.2 | **144.000** | **ngay sau đó phải nhảy lên 1.2** |
| 9 | 1.2 | **144.000** | cuối khung sáng |
| 17 | 1.2 | **144.000** | đầu khung chiều |
| 19 | 1.2 | **144.000** | cuối khung chiều |
| 20 | 1.0 | **120.000** | vừa qua khung chiều |
| 23 | 1.0 | **120.000** | cuối ngày |

Trần hệ số 1.3 không ca nào chạm tới — đúng như Q04 đã ghi, đây là tham số hiện không ràng buộc.

### Thứ tự và điều kiện qua cổng

T02–T06 (coder-product) → T07 (lead chạy 14 lệnh kiểm) → T08 (reviewer review `product/`, lead xác nhận **security CHƯA chạy**) → T09 (coder-product sửa mọi mục "Chặn") → lead chạy lại từ đầu → báo cáo pm → trình Bách.
**Điều kiện qua G2a:** **14** lệnh kiểm đều đạt **và** bảng review của reviewer không còn mục "Chặn".

### Rủi ro riêng của G2a

- Nếu 17h ngày 20/10 chưa xong T08 thì lead đề nghị dời security sang sáng 21/10 và báo Bách ngay (R1).
- Điều 2 và điều 3 trong lời giao việc ngược chiều nhau. Nếu `coder-product` hiểu lệch mà bỏ log thì mất cả G3, không chỉ mất mấy dòng ma trận. Lệnh kiểm 4, 5, 6 bắt đúng chỗ đó.
- **`INTERFACE.md` là cửa duy nhất mở sang B.** Hàng rào Q18 dựng công phu để giữ Q03, Q04, Q06 ngoài tầm mắt của B sẽ sụp hết chỉ vì một câu mô tả biên bậc giá trong schema config — qua đúng cái cửa được phép mở. Điều 6 chặn ở đầu vào, kiểm 12 chặn ở đầu ra.
- **Kiểm 4 và 11 đạt ngay cả khi log thiếu ứng viên bị loại.** Đó đúng là phương án lead đã bác bỏ ở Q12 khi chọn không xin nới `CLAUDE.md §3`, nên nó sẽ lọt êm nếu không có kiểm 13. Mất dấu vết từng ứng viên là mất M01 và một phần M04.

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
| T02 | G2a | `product/data/gen_mock.py` + 3 file JSON mock (seed 42) | coder-product | SPEC_A §1, DECISIONS | drivers/customers/rides.json | `python product/data/gen_mock.py` rồi chạy lại, so `sha256` 2 lần | **completed** | `283b299`; kiểm 2 PASS: 2 lần chạy ra `89aadc78` / `ea898f24` / `a94fdf64` giống hệt |
| T03 | G2a | config có `version` | coder-product | SPEC_A §2–3, DECISIONS Q03/Q04 | **3** file config | đọc mọi file `product/config/*.json`, in `version` | **completed** | `36937f4` + `283b299`; kiểm 7 PASS: matching 0.1, pricing 0.1, **mock_data 0.1** (file thứ 3, xem ghi chú dưới) |
| T04 | G2a | `product/matching.py` — `match()` + log từng ứng viên | coder-product | SPEC_A §2, DECISIONS Q02/Q05/Q06/Q10/Q12 | matching.py, logs/matching_*.jsonl | chạy qua run_product; đếm dòng log / số quyết định | **completed** | `63e2ecd`; kiểm 13 PASS: **200 dòng `candidate_eval` mỗi chuyến × 1.000 chuyến = 200.000**, đủ 4 lý do `not_idle` 98.000 / `wrong_vehicle_type` 33.192 / `out_of_radius` 32.328 / `kept_as_candidate` 36.480 |
| T04b | G2a | **Đo thật**: số dòng log, dung lượng 1 lần chạy, **tổng dung lượng qua 8 lần chạy dự kiến**; thay mọi số [Suy đoán] ở DECISIONS Q12 | lead | logs/*.jsonl | số đo ghi vào cột Bằng chứng | `wc -l` + `du -sh logs/` | pending | |
| T05 | G2a | `product/pricing.py` — `fare()` + log từng bậc km | coder-product | SPEC_A §3, DECISIONS Q03/Q04/Q10 | pricing.py, logs/pricing_*.jsonl | 23 ca kể cả biên, so bảng tính tay | **completed** | `c9b0243`; kiểm 9 PASS **23/23** ca khớp bảng tính tay, gồm cặp giờ 6 → 108.000 và giờ 7 → 144.000 |
| T06 | G2a | `product/run_product.py` + `docs/INTERFACE.md` | coder-product | SPEC_A §4–5, DECISIONS Q10 | reports/product_run_*.json, INTERFACE.md | `python product/run_product.py` | **completed** | `13e5718` + `1559d80`, sửa kiểm 12 ở `7bfd149`; kiểm 1 PASS exit=0; kiểm 3 PASS; kiểm 12 PASS sau khi sửa |
| T07 | G2a | **Lead tự chạy đủ 14 lệnh kiểm** | lead | T02–T06 | bảng kết quả dưới | 14 lệnh kiểm, không nhận báo cáo suông | **14/14 PASS** | `run_id=20261019T064336`, sau sửa `7bfd149`; xem 2 bảng dưới |
| T08 | G2a | Review `product/` theo checklist (security CHƯA chạy) | reviewer | product/, SPEC_A, INTERFACE | bảng Chặn / Nên sửa / Gợi ý | lead đọc, hết mục "Chặn" | pending | |
| T09a | G2a | Sửa 6 chỗ rò `INTERFACE.md` do kiểm 12 phát hiện | coder-product | bảng kiểm 12 | docs/INTERFACE.md | lead đọc lại diff + `grep` + chạy lại kiểm 10 | **completed** | `7bfd149`; chỉ sửa 1 file, `git diff cb97490..HEAD` = đúng `docs/INTERFACE.md`; `run_product.py` exit=0 sau sửa |
| T09b | G2a | Sửa mục "Chặn" của reviewer | coder-product | bảng review T08 | commit sửa | `python product/run_product.py` chạy lại OK | pending | chờ T08 |
| T10 | G2b | Tạm dừng commit; Bách chạy security ở cửa sổ cách ly, merge `security-pass`, lead chạy lại A | Bách → lead | — | commit sau security | `python product/run_product.py` sau merge | pending | |
| T10b | G3 | **Chốt cửa trước T11, 2 việc:** (1) đọc lại `.claude/agents/coder-auditor.md:7`, xác nhận `docs/DECISIONS.md` vẫn không nằm trong danh sách được đọc; (2) xác nhận **Q17 đã được Bách trả lời**. Thiếu bất kỳ việc nào → **dừng, báo Bách**, không gọi T11 | lead | .claude/agents/coder-auditor.md, DECISIONS Q17 | xác nhận ghi vào cột Bằng chứng | `sed -n '7p' .claude/agents/coder-auditor.md` + đọc Q17 | pending | dòng 7 **đã sửa** ở G1 theo Q15 |
| T11 | G3 | `auditor/matrix.json` + `auditor/rules/m01..m12` + `run_audit.py` | coder-auditor | **CHỈ** docs/MATRIX_v0.md + docs/INTERFACE.md (xem ô cảnh báo dưới bảng) | reports/audit_<commit>.json/.md | `python auditor/run_audit.py` ra đủ 12 dòng; **mỗi phát hiện có `file:dòng` riêng** (Q16) | pending | |
| T12 | G3 | Lead tự chạy audit, kiểm 12 dòng có `result` + `evidence` | lead | T11 | kết quả dán vào TASKS.md | `python auditor/run_audit.py` | pending | |
| T13 | G3 | Chạy audit 3 lần cùng commit, so sánh JSON (bỏ ts/run_id) → độ ổn định | lead | T12 | ghi chú độ ổn định | 3 lần chạy + so sánh | pending | |
| T14 | G3 | Review `auditor/` (KHÔNG review product/ nữa) | reviewer | auditor/, MATRIX_v0 | bảng review | hết mục "Chặn" | pending | |
| T15 | G3 | Bách chạy qa ở cửa sổ cách ly, merge `qa-score` | Bách | reports/audit_*.json | reports/qa_score_*.md | — | pending | |
| T16 | G4 | `reports/BAO_CAO_SANDBOX.md` 6 phần theo PROMPTS 4.1 | lead | tất cả trên | báo cáo + câu hỏi mở | pm chấm lần cuối + Bách duyệt | pending | |

## Kết quả T07 — lead tự chạy, run_id `20261019T064336`

| # | Kiểm | Kết quả | Số đo |
|---|---|---|---|
| 1 | chạy một lệnh | **PASS** | `python product/run_product.py` exit=0 |
| 2 | seed 42 xác định | **PASS** | 2 lần `gen_mock.py` → `sha256` 3 file giống hệt |
| 3 | 2 lần chạy giống nhau | **PASS** | bỏ `ts`/`run_id`/`log_files` → báo cáo giống hệt |
| 4 | log đủ 9 trường | **PASS** | tiền quyết đạt (7 file, 7 khớp mẫu); 0 dòng sai trường hoặc sai thứ tự |
| 5 | quyết định có `reason` | **PASS** | 0 quyết định thiếu `reason` |
| 6 | số quyết định = 2.000 | **PASS** | `match_result` 1.000 + `fare_result` 1.000 |
| 7 | config có `version` | **PASS** | 3 file, đều 0.1 |
| 8 | chỉ stdlib | **PASS** | import ngoài local: `datetime, json, math, os, random, sys` → 0 module ngoài stdlib |
| 9 | pricing kể cả ở biên | **PASS** | **23/23** ca khớp bảng tính tay |
| 10 | INTERFACE khớp Q02 | **PASS** | 12 thuộc tính, khớp từng dòng |
| 11 | dung lượng log thật | **PASS** (số đo) | **110 MB / lần chạy**, 216.004 dòng → **VƯỢT ngưỡng 100 MB của Q12** |
| 12 | **INTERFACE.md không rò logic** | **PASS** sau khi sửa | FAIL lần đầu (2 chặn + 4 nên cắt); đã cắt hết ở `7bfd149`, lead đọc lại diff bằng mắt và `grep` 8 cụm từ → **0 lần xuất hiện** |
| 13 | log đủ ứng viên bị loại | **PASS** | 200 dòng/chuyến × 1.000 = 200.000, đúng `len(drivers.json)` |
| 14 | không hardcode nghiệp vụ | **PASS** | 0 hằng số nghiệp vụ còn trong code |

**Một lỗi của chính bộ kiểm lead, đã chẩn đoán rồi mới sửa (`CLAUDE.md:30`).** Lần chạy đầu, kiểm 6 ra 4.000 và kiểm 13 ra 400 — đúng gấp đôi. Nguyên nhân: kiểm 3 chạy `run_product.py` hai lần, cả hai lần cùng để log trong `logs/`, nên bộ kiểm quét gộp. Sửa bằng cách **nhóm log theo `run_id`** rồi kiểm từng lần chạy. Không phải lỗi sản phẩm. Bộ kiểm đã tính lại đúng cho cả hai `run_id`.

## Kiểm 12 — chỗ rò tìm thấy trong `docs/INTERFACE.md`

| # | Chỗ | Mức | Rò gì | Gốc ở đâu |
|---|---|---|---|---|
| 1 | mục 7, cột `Dùng để` | **CHẶN** | thứ tự lọc; **thứ tự phá hoà** (bước 1 `trips_today`, bước 2 `driver_id`); pricing **có bậc giá và hệ số giờ** — đúng loại rò vừa gỡ khỏi `MATRIX_v0`, nay rò lại qua cửa được phép mở | **lời giao việc của lead**: ghi "chép nguyên bảng" mà không nói chép cột nào |
| 2 | dòng 92: *"không có đường chạy nào không sinh log"* | **CHẶN** | nói trước kết quả M04, mà M04 kiểm đúng điều đó (`MATRIX_v0.md:27`) | `coder-product` tự viết |
| 3 | mục 7, cột `Nguồn SPEC_A` | nên cắt | trỏ vào `docs/SPEC_A.md`, file `coder-auditor` không được mở | cùng gốc với #1 |
| 4 | dòng 326: *"cùng đầu vào cho ra cùng kết quả… hai lần chạy giống hệt nhau"* | nên cắt | nói trước kết quả M10 | `coder-product` tự viết |
| 5 | dòng 157: *"Chạy `gen_mock.py` hai lần cho ra ba file giống hệt nhau"* | nên cắt | cùng loại với #4 | `coder-product` tự viết |
| 6 | dòng 94: *"`match` và `fare` không tự đọc các khoá đối chiếu đó"* | nên cắt | nói trước kết quả M02 | `coder-product` tự viết |

**Không tính là rò:** enum `event` ở mục 5.3 (điều 4 lời giao việc **buộc** phải có, và B đọc log là thấy hết); tên khoá config ở mục 3 (điều 6 cho phép, và B đọc trực tiếp `product/config/*.json` được).

## T09a — kết quả sửa chỗ rò, lead đã tự kiểm lại

Commit `7bfd149`, chỉ sửa `docs/INTERFACE.md`. Lead kiểm: `git diff cb97490..HEAD --stat` → đúng 1 file; `grep` 8 cụm từ nghi vấn → **0 lần xuất hiện** từng cụm; đọc lại toàn bộ diff bằng mắt; chạy lại kiểm 10 → 12 thuộc tính khớp đúng thứ tự, mục 7 chỉ còn **một** cột.

**`coder-product` tự tìm thêm 2 chỗ cùng loại, lead chấp nhận cả hai:**

| Chỗ | Nội dung bị cắt | Lead đánh giá |
|---|---|---|
| mục 3 | *"Mọi tham số nghiệp vụ nằm trong `product/config/*.json`. Mỗi file **bắt buộc** có trường `version`"* | **Bắt đúng.** Câu đó nói trước phán quyết của **hai** dòng ma trận một lúc: M05 (`MATRIX_v0.md:28`) và M06 (`MATRIX_v0.md:29`). Hợp đồng không mất gì: bảng schema vẫn có dòng `version`, và đường dẫn config vẫn còn |
| mục 1 | *"Chỉ dùng Python standard library."* | **Cắt được, nhưng lý do nó nêu không đúng.** Nó nói đây là "phán quyết của dòng ma trận kiểm đúng việc chỉ dùng stdlib" — lead `grep` `MATRIX_v0.md` và **không có dòng ma trận nào kiểm stdlib**; đó là checklist số 1 của `reviewer` và `CLAUDE.md §2`, không phải việc của B. Cắt vẫn vô hại vì `CLAUDE.md` nằm trong danh sách B được mở, nên thông tin không mất. Giữ nguyên chỗ cắt, nhưng ghi lại ở đây là lý do gốc sai |

Và một chỗ nó **làm mềm thay vì cắt**: mục 5.2 *"Mọi dòng log, **không trừ dòng nào**, có đúng chín trường"* → *"Mỗi dòng log là một đối tượng JSON gồm chín trường"*. Lead đồng ý: bảng 9 trường là schema nên phải giữ (điều 4 buộc có), còn cụm "không trừ dòng nào" là lời bảo đảm, không phải schema.

**Một chỗ lead QUYẾT GIỮ — là lựa chọn, không phải sót.** `docs/INTERFACE.md:5` còn tham chiếu `SPEC_A.md:54-55` — tham chiếu `SPEC_A` duy nhất còn lại. `coder-product` nêu ra để lead quyết, và lead giữ, vì: nó trỏ vào quy định về **phạm vi của chính file INTERFACE.md**, không trỏ vào thuộc tính hay bước tính nào, nên đọc nó không đoán được gì về bên trong `product/`; và việc `docs/SPEC_A.md` tồn tại thì B vốn đã biết từ `CLAUDE.md §4`. Đổi lại là mất nguồn dẫn mà không được thêm gì.

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
