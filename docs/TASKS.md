# TASKS — lead cập nhật, Bách và pm đọc

## 🔖 TRẠNG THÁI — đọc ô này TRƯỚC khi làm gì, sau mỗi lần dừng

> **Quy tắc hạn mức (Bách chốt 19/10).** Sau **mỗi bước con**: cập nhật ô này (đang làm gì, bước tiếp theo, lệnh kiểm) rồi **commit**. Nếu bị dừng vì hết hạn mức rồi tự chạy tiếp: **đọc `docs/TASKS.md` trước, rồi mới làm.** **Không bao giờ tự vượt cổng đang chờ Bách đồng ý.**

| | |
|---|---|
| **Cổng đang mở** | **G3b ĐÃ MERGE** (`qa-score` tại `a3453cb`). Số đo: recall 0.667, FNR 0.333 — **không đạt** cả §3B và mục tiêu riêng qa; precision 1.000. pm chấm vòng 1 = **SỬA RỒI GỬI LẠI**, đã sửa đủ 5 điểm (commit `972e9e3`), đang chờ pm chấm vòng 2 |
| **Vừa xong** | Sửa G4 theo 5 điểm pm: (1) thêm "Vì sao sót 2 lỗi" ở mục 4; (2) TB-06 khai rủi ro repo-public-đã-quản-lý; (3) tách mục tiêu riêng qa khỏi ngưỡng gốc §3B; (4) M05 đổi "xác nhận riêng" → Source thật (`TASKS.md:381-382`@`100f2a0`); (5) bỏ nhãn "Nháp", đổi tên người thật → vai trong thân báo cáo. Cộng: `verify_refs.py` fix UnicodeEncodeError khi stdout redirect |
| **Bước tiếp theo** | Chờ `pm` chấm vòng 2. Nếu DUYỆT → trình Bách duyệt G4/demo |
| **Lệnh kiểm của bước tiếp theo** | `python tests/verify_refs.py .` (đã chạy lại sau sửa, 0 lỗi, exit 0 cả khi redirect) |
| **⚠️ ĐANG HIỆU LỰC — từ C0→C1** | Lead **không đọc nội dung `product/` qua BẤT KỲ đường nào**: không lệnh git local (`diff`/`log`/`show`), không trình duyệt/GitHub web UI/API, không bản clone khác, không ảnh chụp màn hình, không người khác kể lại. Nếu ai dán cho lead một đoạn diff của `product/` → **dừng, báo Bách ngay, không dùng**. Chỉ đọc kết quả sau khi Bách merge `qa-score` |
| **🚨 RỦI RO PM BÁO 20/10 — ĐÃ ĐÓNG** | Bách đã chuyển repo **Private** (pm xác nhận: `ls-remote` không xác thực → `exit 128`; trước đó đọc được không cần đăng nhập). `main` đã đẩy đúng `b2515ae`. Nhánh `security-pass` vẫn còn trên remote nhưng nay nằm trong repo private — không còn là đường rò. Sau G3b, Bách mở lại public thì không hại gì (điểm đã chấm xong) |
| **✅ pm — mốc chấm 3 (kết quả sau merge security-pass): DUYỆT** | Kiểm bằng lệnh (không mở nội dung `product/`): `git log b-freeze..HEAD -- auditor/` trống (B không bị sửa sau đóng băng); `git log 83229ff..HEAD --name-only -- product/ tests/` trống; commit `b2515ae` của lead chỉ chạm `docs/TASKS.md`; không file bằng chứng/log mới sinh sau merge (Bách tự chạy A 2 lần sau merge, không phải lead/B). Lưu ý của pm: chỉ thấy *vật phẩm+commit*, không thấy *lệnh đã gõ trong tab lead* — câu đúng trong G4 là "không có dấu vết nào của việc chạm `product/`", không phải "chắc chắn không ai chạm" (cùng mức độ dè dặt như "mã tái lập được" ở G2a) |
| **Lịch (chỉ thị 21:01)** | 20/10: T09g → T11 → B chạy trên A sạch → ổn định 3 lần → reviewer `auditor/` → `b-freeze` trước tối nay. **Nếu tối nay chưa `b-freeze`**: cắt ma trận còn 8 dòng (M01,M02,M04,M05,M07,M09,M10,M11), báo Bách trước khi cắt. 21/10: Bách merge + QA chấm, lead nháp G4. 22/10: hoàn thiện, pm duyệt, demo |
| **Chế độ gọn** | Không đặt nguyên tắc mới trừ khi thiếu nó thì sai kết quả đo. Câu hỏi không chặn → vào báo cáo G4. Hỏi Bách tối đa 1 tin/cổng, mỗi câu kèm đề xuất. pm chỉ chấm 4 điểm: G2a, `b-freeze`, kết quả sau merge, G4. Không đọc log lớn vào ngữ cảnh. Báo cáo cổng tối đa 15 dòng |

### ⛔ Cổng đang chờ Bách — KHÔNG tự vượt

| Việc | Chờ gì |
|---|---|
| **G2b (merge `security-pass`)** | Chỉ Bách merge, **chỉ sau** tag `b-freeze` (G3a xong) |
| **G3b (merge `qa-score`)** | Chỉ Bách merge; lead chỉ đọc kết quả sau khi merge |


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
6. **`INTERFACE.md` không được rò logic.** `SPEC_A.md:66` ghi rõ "**Không** mô tả logic bên trong", và đây là **file duy nhất** nối `product/` với `coder-auditor`. Chỉ gồm 5 thứ `SPEC_A.md:65` liệt kê. Schema config chỉ nêu **tên khoá và kiểu dữ liệu** — **KHÔNG** nêu giá trị, biên bậc, hệ số, ngưỡng. Không câu nào mô tả thuật toán, thứ tự lọc, cách phá hoà, hay cách tính giá. Viết "`pricing.json` có khoá `tiers` kiểu list" thì được; viết "gồm 4 bậc 0-2 km, 2-12 km…" thì **không**.

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
| 12 | **`INTERFACE.md` không rò logic** | lead **tự đọc hết file bằng mắt**, đối chiếu `SPEC_A.md:65-66`, liệt kê từng câu nghi là mô tả logic. Không script được. Nghi ngờ thì cắt |
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
| T07 | G2a | **Lead tự chạy bộ kiểm** — 3 vòng, vòng cuối sau `284461a` | lead | T02–T06, T09a–c | bảng kết quả dưới | 15 kiểm máy + kiểm 12 bằng mắt | **16/16 PASS** | `run_id` bằng chứng **20261019T075936693**; xem mục kết quả cuối |
| T08 | G2a | Review `product/` theo checklist (security CHƯA chạy) | reviewer | product/, SPEC_A, INTERFACE | bảng Chặn / Nên sửa / Gợi ý | lead đọc, hết mục "Chặn" | **completed** | **KHÔNG CÓ MỤC CHẶN**; 5 Nên sửa + 10 Gợi ý; lead tự xác minh tận dòng 7 chỗ then chốt, đúng hết |
| T09a | G2a | Sửa 6 chỗ rò `INTERFACE.md` do kiểm 12 phát hiện | coder-product | bảng kiểm 12 | docs/INTERFACE.md | lead đọc lại diff + `grep` + chạy lại kiểm 10 | **completed** | `7bfd149`; chỉ sửa 1 file, `git diff cb97490..HEAD` = đúng `docs/INTERFACE.md`; `run_product.py` exit=0 sau sửa |
| T09b | G2a | Sửa 14 mục từ T08 + 2 mục pm | coder-product | bảng review T08, bảng chấm pm | commit sửa | lead chạy lại toàn bộ bộ kiểm | **completed** | `2ca9a03`, 8 file +220/−75; lead chạy lại 15 kiểm, 13 PASS |
| T09c | G2a | `run_id` chống trùng | coder-product | chẩn đoán kiểm 2 | `run_id` 18 ký tự có milli giây | `gen_mock.py` 2 lần liên tiếp, lần 2 exit=0 | **completed** | `284461a`; 2 lần liên tiếp đều exit=0, hash giống hệt; vòng lặp 2.000 lần gọi ra 2.000 giá trị khác nhau |
| T09e | G2a | ✅ **completed — xem ô "Kết quả T09e" dưới bảng.** Phủ nhánh — sửa `gen_mock.py` + `mock_data.json`** theo Q19 và cách B Bách duyệt: giữ hộp toạ độ, 3–5% điểm đón ngoài vùng, **thêm** 3–5% chuyến điểm đến xa cho hai bậc `(12;25]` và `>25`. Tham số vào config, **trong `data/`+`config/` chỉ ghi tham số trung tính**, lý do chỉ ở SPEC_A/DECISIONS. Thêm `sys.argv` + `seed` vào log `run_start` | coder-product | DECISIONS Q19, SPEC_A §1 | commit sửa + **bảng so trước/sau** | lead chạy lại **toàn bộ** bộ kiểm + kiểm 19 (9 mục a–i) | **completed** | `64b4791`→`10e8ff8`; lead chạy lại **toàn bộ** bộ kiểm: 15/15 + kiểm 17, 18, 19 (9/9), 20 đều PASS. `run_id` bằng chứng **20261019T142131055** |
| T09f | G2a | **Reviewer kiểm lại trước khi đóng G2a** — Bách yêu cầu riêng sau T09e | reviewer | product/ sau T09e | bảng review | hết mục "Chặn" | **completed** | **0 mục Chặn**, 6/6 mục kiểm "Không có vấn đề" + 1 mục bổ sung (9 trường log). Đây là lượt review `product/` **CUỐI CÙNG** của reviewer — sau merge `security-pass` chỉ còn review `auditor/` |
| T07b | G2a | **Kiểm 15** — chẩn đoán nhánh `no_driver_in_radius` | lead | T09b | dòng log quyết định làm bằng chứng | gọi `match()` với `radius_km=0.0001`, dữ liệu tài xế thật | **PASS** | `match()` → `{driver_id: None, auto_accept: False, reason: 'no_driver_in_radius'}`; 203 dòng log, **đúng 1** dòng quyết định, `reason='no_driver_in_radius'` |
| T07c | G2a | **Kiểm 16** — log `data_loaded` phải có `sha256` 3 file dữ liệu + version `mock_data.json` | lead | T09b (C6) | bằng chứng dữ liệu nào đã dùng | đối chiếu sha256 trong log với hash file thật | **PASS** | 3 sha256 trong log, khớp hash 3 file dữ liệu |
| T10 | G2b | **Chỉ chạy SAU T14b** (Q21: B đóng băng trước, security merge sau). Tạm dừng commit; Bách chạy security ở cửa sổ cách ly, merge `security-pass`, lead chạy lại A. **Xem ô "Việc của lead ở G2b" ngay dưới bảng — chỉ 1 lệnh, không chẩn đoán** | Bách → lead | — | commit sau security | **CHỈ** `python product/run_product.py`, **chỉ xem exit code**. Không chạy lệnh kiểm nào khác | pending | |
| T10b | G3 | **Chốt cửa trước T11, 4 việc** | lead | .claude/agents/coder-auditor.md, DECISIONS Q17 | xác nhận ghi vào cột Bằng chứng | `sed -n '7p' .claude/agents/coder-auditor.md` + đọc Q17 | **completed** | (1) dòng 7-9 `coder-auditor.md` còn nguyên bản Bách chốt 19/10 (pm tự kiểm, xác nhận); (2) Q17 đã trả lời (Bách chọn A, 19/10); (3) `tests/`+`reports/` đã xếp loại (Bách duyệt, commit `7000729`); (4) Q16 **đóng được** — 12/12 dòng m01-m12 dùng đúng 2 ngoại lệ đã biết (Q17 vắng mặt, Q12 log không `@commit`), **không sinh ngoại lệ thứ ba** |
| T11 | G3 | `auditor/matrix.json` + `auditor/rules/m01..m12` + `run_audit.py` | coder-auditor | **CHỈ** docs/MATRIX_v0.md + docs/INTERFACE.md | reports/audit_<commit>.json/.md | `python auditor/run_audit.py` ra đủ 12 dòng; mỗi phát hiện có `file:dòng` riêng (Q16) | **completed** | `4652a6e`→`ed53c61` (2 lượt sửa theo reviewer, xem T14). 12/12 dòng: 8 ĐẠT, 3 CẦN NGƯỜI XEM (M05/M07/M08), 1 KHÔNG ĐẠT (M12) |
| T12 | G3 | Lead tự chạy audit, kiểm 12 dòng có `result` + `evidence` | lead | T11 | kết quả dán vào TASKS.md | `python auditor/run_audit.py` | **completed** | Lead tự chạy (không nhận báo cáo agent): 12/12 dòng đủ `result`+`evidence`, mỗi phát hiện `file:dòng`. Kết quả khớp báo cáo `coder-auditor` |
| T13 | G3 | Chạy audit 3 lần cùng commit, so sánh JSON (bỏ ts/run_id) → độ ổn định | lead | T12 | ghi chú độ ổn định | 3 lần chạy + so sánh | **completed** | 3 lần chạy B@`b-freeze` lúc thực hiện — hash so sánh (`a738cb4c…`) **không tái lập được** vì 3 file tạm đã bị ghi đè, cách chuẩn hoá chưa ghi lại (pm tự bắt lỗi của chính mình). **Thay bằng bằng chứng tái lập được**: 2 file đã **commit** ở 2 commit có cây `auditor/` giống hệt (`d8638d0`) — `reports/audit_ed53c61.json` và `reports/audit_8869ebd.json`. Lệnh tái lập (lead tự viết, tự chạy, không chỉ copy số pm đưa): chuẩn hoá `run_id` (`\d{8}T\d{9}`), `"ts": "..."`, và mọi chuỗi `audit_<hex>`/`<hex>` 7-40 ký tự đứng độc lập (không dính `_`) → `sha256` **giống hệt cả hai file**: `1adebc0419529d6…`. Ai có repo đều tự chạy lại được. **pm tự chạy một script chuẩn hoá khác** (cùng 2 file, cùng cây `d8638d0`, cùng kết luận "giống hệt") ra `7df04fc1fa28f34a…` — khác hex với lead vì quy ước placeholder khác nhau trong script, **không phải vì nội dung khác nhau**: lead thử tái lập đúng mô tả bằng lời của pm (chuẩn hoá `run_id`+`ts`+"chuỗi commit") vẫn ra `1adebc04…`, không ra được `7df04fc1…` — nghĩa là hai script độc lập, viết khác nhau, **cùng đồng ý nội dung giống hệt**, mạnh hơn một lần chạy chung script |
| T14 | G3 | Review `auditor/` (KHÔNG review product/ nữa) | reviewer | auditor/, MATRIX_v0 | bảng review | hết mục "Chặn" | **completed** | 3 lượt: lượt 1 tìm 1 Chặn (bằng chứng log không nguyên văn, M01/M04/M07/M09) → sửa `4652a6e`→`5375876`; lượt 2 tìm sót 1 chỗ (M10) → sửa →`ed53c61`; lượt 3 **hết Chặn**, grep toàn `auditor/rules/*.py` xác nhận |
| T14b | G3 | **Đóng băng B — chốt cửa Q21.** Gắn tag `b-freeze` khi: B đã chạy trên **A sạch** (T12, T13) **và** T14 hết mục Chặn. Rồi báo Bách. Bách **mới** merge `security-pass` | lead | T12, T13, T14 | tag `b-freeze` | `git tag` có `b-freeze`; `git log auditor/` không commit nào sau tag | **completed** | Tag neo tại **commit `cce80bf`** (tag lightweight, không ký — chốt bằng commit hash, không bằng tag). `git log b-freeze..8869ebd -- auditor/` **trống**. Hash cây `auditor/` ở `ed53c61`/`b-freeze`/`8869ebd` **giống hệt** `d8638d0`. TB-07 đo bằng chính kết quả này |
| T15 | G3 | Bách chạy qa ở cửa sổ cách ly, merge `qa-score` | Bách | reports/audit_*.json (**cả hai** vế: A sạch từ T12, A có lỗi từ T14c) | reports/qa_score_*.md | — | **completed** | Merge `a3453cb`. `reports/qa_score_83229ff.md`: TP=4, FN=2, FP=0 → precision 1.000, recall 0.667, FNR 0.333. Ổn định 3/3 lần chạy giống hệt |
| T17 | G4 | **Chấm kết quả B theo checklist §3B** (TB-01 → TB-12): recall, FNR, precision, độ ổn định, truy nguồn, độc lập, đóng băng, nguồn gốc quy tắc, Legal/DPO, log của B, phạm vi dùng B, chạy lại bộ đo khi đổi MATRIX | lead | `reports/qa_score_*.md` (T15), `reports/audit_*.json` | một phần riêng trong báo cáo G4, 12 dòng | mỗi dòng TB có số đo hoặc ghi rõ **chưa đo được** và vì sao | **completed** | 12 dòng điền đủ ở `BAO_CAO_SANDBOX.md` mục 8. TB-01/02/03 nguyên văn từ T15 (recall 0.667, FNR 0.333 — **cả hai KHÔNG đạt** mục tiêu [Suy luận] ở checklist §3B; precision 1.000). TB-04..TB-11 **ĐẠT**, TB-12 **[Chưa xác minh]** (chưa có lần đổi MATRIX sau b-freeze) |
| T16 | G4 | `reports/BAO_CAO_SANDBOX.md` theo PROMPTS 4.1, **đã sửa cấu trúc theo phụ lục chỉ thị 19/10** — xem ô dưới bảng | lead | tất cả trên + `docs/CHECKLIST_KIEM_TOAN.md` | báo cáo | pm chấm lần cuối + Bách duyệt | **completed** | Mục 4 + mục 8 (TB-01/02/03) điền xong, nguyên văn từ T15. `tests/verify_refs.py .` 0 lỗi. Báo cáo không còn chỗ **[CHỜ G3b]** nào. Bước tiếp: gửi `pm` chấm lần cuối (mốc chấm thứ 4) |

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

**Một chỗ lead QUYẾT GIỮ — là lựa chọn, không phải sót.** `docs/INTERFACE.md:5` còn tham chiếu `SPEC_A.md:65-66` — tham chiếu `SPEC_A` duy nhất còn lại. `coder-product` nêu ra để lead quyết, và lead giữ, vì: nó trỏ vào quy định về **phạm vi của chính file INTERFACE.md**, không trỏ vào thuộc tính hay bước tính nào, nên đọc nó không đoán được gì về bên trong `product/`; và việc `docs/SPEC_A.md` tồn tại thì B vốn đã biết từ `CLAUDE.md §4`. Đổi lại là mất nguồn dẫn mà không được thêm gì.

## T08 — review `product/`: KHÔNG CÓ MỤC CHẶN

reviewer xác nhận điều kiện vai trước khi làm: lead báo **security CHƯA chạy** nên lần này nó được review `product/`.

**Đạt, không cần làm gì:** thứ tự SPEC_A §2 (`matching.py:102-113` lọc → `sorted(key=(distance_km, trips_today, driver_id))` ở `:174-177`); `auto_accept` so nghiêm ngặt `<` nên `0.7 < 0.7` ra False; trần hệ số là `min` không phải `max` (`pricing.py:173`); giờ lấy **như đã viết** kèm offset, không quy UTC (`pricing.py:43`) — đúng Q04; `match` thuần, không đổi `status` — đúng Q06; whitelist Q02 đúng 10 + 2, không đọc `customer_id`/`segment`; không lời gọi mạng, không `subprocess`/`eval`/`exec`/`getenv`, không secret, không dữ liệu cá nhân thật; không `set()`/`listdir`/`glob`/`hash()`.
**Q13 đạt:** reviewer quét `human|review|alert|canh_bao|override|escalat|mitigat|impact|matrix|M01..M12` trên toàn `product/` → **0 kết quả**. `matching.json` đúng 5 khoá. A không bị vá theo MATRIX.

**Bảy chỗ lead tự xác minh tận dòng, reviewer đúng hết:**

| Chỗ | Lead xác minh bằng gì | Vì sao quan trọng |
|---|---|---|
| `INTERFACE.md` mục 5.3 cột "Số dòng mỗi lần chạy" | `sed -n '270,280p'` | **Rò thứ 7.** "1 cho mỗi ứng viên được xét" nói ra mọi tài xế đều bị xét; "0 hoặc 1 mỗi chuyến" nói ra `tie_break`/`auto_accept_eval` có điều kiện; "1 cho mỗi phần tử của `tiers`" nói ra `fare` lặp toàn bộ bậc. Cả lead và `coder-product` đều bỏ sót |
| `run_product.py:46-47` | `sed` | `return False` thoát không log, **chạy ở mọi lần chạy bình thường**. M04 kiểm đúng chữ "có nhánh `return` không gọi log" → B sẽ báo là phát hiện thật trên A sạch, lẫn vào mẫu số precision của qa |
| `pricing.py:54`, `:101` | `sed` | `raise ValueError` thoát không log, đều là quyết định về dữ liệu nghiệp vụ đọc từ config |
| `logger.py:53` + `:69` | `grep` | `run_id` phân giải **1 giây** + mode `"w"` → hai lần chạy cùng giây **ghi đè im lặng**. Nguy vì Quy ước `MATRIX_v0` bắt B tự chạy sinh log mới trước khi kiểm |
| `run_product.py:187` | `grep` | `n_decisions = 2 * len(results)` suy ra từ công thức, không đếm từ log → bằng chứng M04 tự khẳng định chính nó |
| `pricing.py:92-95` | chạy thật `fare(0.0)` | ra 30.000đ, trong khi Q03 định nghĩa bậc `(0;2]` **không gồm 0** |
| `logger.py:15` | `grep` | `REQUIRED_FIELDS` khai báo mà không chỗ nào dùng — hằng số chết trông như cơ chế đang hoạt động |

**Hai điểm mù của chính bộ kiểm lead, do reviewer phát hiện:**

1. **Kiểm 14 bỏ sót `2` trong `n_decisions = 2 * len(results)`.** Bộ lọc của lead whitelist 0, 1, 2 là "chỉ số vô hại", nhưng `2` ở đây là **hằng số định nghĩa nghiệp vụ** của Q10 nằm trong code.
2. **Bảng 23 ca của kiểm 9 thiếu ca 0 km** — dù pm đã buộc lead thêm giá trị biên. Lead thêm biên `2.0 / 2.1 / 12.0 / 12.1 / 25.0 / 25.1` nhưng không nghĩ tới biên **dưới** của bậc đầu.

## pm tự đính chính — đổi cách viết báo cáo G4 và cách giao T11

pm từng xếp việc nhắc chữ "bậc km" là PHÁ ĐỘC LẬP, nay nói nhận định đó **nặng hơn thực tế**, và lead đồng ý. Lý do: **M05 (`MATRIX_v0.md:28`) và M06 (`MATRIX_v0.md:29`) buộc B phải đọc `product/config/*.json`**, nên mọi **giá trị** trong config — biên bậc, hệ số, ngưỡng — vốn đã nằm trong tầm mắt hợp pháp của B. MATRIX hay INTERFACE có nhắc chữ "bậc" hay không thì **không giấu được** những giá trị đó.

Việc đổi M11 sang phân vị vẫn giữ, nhưng **lý do đúng là lý do phương pháp**: phân vị không giả định cấu trúc giá nào, nên quy tắc M11 vẫn chạy được kể cả khi cấu trúc giá khác đi. Không phải vì nó giấu được điều gì. **Báo cáo G4 phải nói đúng lý do này.**

| | Nội dung |
|---|---|
| **B vốn đã thấy hợp pháp** | mọi giá trị trong `product/config/*.json`; schema dữ liệu; toàn bộ nội dung log; `CLAUDE.md` |
| **Thật sự phải giữ kín** | thuật toán và thứ tự bên trong `product/*.py`; **phán quyết dự kiến của từng dòng ma trận** |

Bảy chỗ đã cắt đều thuộc nhóm thứ hai — nên cắt **đúng**. Hệ quả cho T11: **đừng cắt thêm tên khoá config hay schema; cắt quá tay cũng là lỗi.**

## Kỷ luật commit — pm nhắc, lead nhận

`git add -A` là cách lead commit nhầm `reports/product_run_*.json` (408 KB). Lần này vô hại và còn dùng được làm bằng chứng cổng vì `SPEC_A §4` vốn đòi file đó. Nhưng `.gitignore` chỉ chặn `logs/*.jsonl`, nên `git add -A` sẽ nuốt bất cứ thứ gì rơi vào thư mục làm việc. **Từ G2b trở đi: commit bằng đường dẫn tường minh, không `git add -A`.**

## T07 vòng 2 — chạy lại sau T09b. 13/15 PASS, 2 FAIL đã chẩn đoán

Code đổi 8 file (+220/−75) nên lead chạy lại **toàn bộ** bộ kiểm, không chỉ kiểm phần sửa.

**Hai kiểm mới lead thêm:**

| # | Kiểm | Kết quả |
|---|---|---|
| **15** | Nhánh `no_driver_in_radius` có log thật | **PASS** — gọi `match()` với dữ liệu tài xế thật và `radius_km=0.0001`: trả `{driver_id: None, auto_accept: False, reason: 'no_driver_in_radius'}`, sinh 203 dòng log, **đúng 1** dòng quyết định với `reason='no_driver_in_radius'`. Là **ca kiểm thử**, không đổi config mặc định, không đổi dữ liệu, không commit làm baseline |
| **16** | Log `data_loaded` có `sha256` dữ liệu | **PASS** — 3 sha256 trong log khớp hash 3 file thật, kèm version và seed của `mock_data.json` |

**Hai FAIL, cả hai đã chẩn đoán trước khi sửa (`CLAUDE.md:30`):**

**Kiểm 2 FAIL — nguyên nhân là mode `"x"` của C1, không phải tính xác định.** Hash 3 file vẫn giống hệt nhau (`89aadc78` / `ea898f24` / `a94fdf64`), nhưng lần chạy `gen_mock` thứ hai **exit=1** với `FileExistsError` trên `logs/gen_mock_20261019T075320.jsonl`. Lý do: `run_id` chỉ phân giải **1 giây** mà `gen_mock.py` chạy **dưới 1 giây**, nên hai lần liên tiếp trùng `run_id` và mode `"x"` chặn lần sau.
`coder-product` **đã cảnh báo đúng chỗ này** và lead đã chọn sai: lead bảo dùng `"x"` và không đổi `run_id` vì sợ phải sửa `INTERFACE.md`. Lý do đó không đứng được — `INTERFACE.md` đã sửa mấy lượt, còn lỗi này **chặn quy trình thật**: Quy ước `MATRIX_v0` bắt B tự chạy sinh log mới trước khi kiểm, nên một script kiểm chạy `gen_mock` hai lần sẽ **tự tạo cho mình kết quả CẦN NGƯỜI XEM giả**. → T09c: giữ `"x"`, đổi `run_id` sang có milli giây.

**Kiểm 14 FAIL — bộ kiểm của lead siết quá tay, không phải lỗi sản phẩm.** Hai hằng số bị báo: `gen_mock.py:34` `_SECONDS_PER_DAY = 24 * 60 * 60` (quy đổi đơn vị thời gian) và `run_product.py:51` `65536` (cỡ bộ đệm đọc file cho sha256). `CLAUDE.md §2.4` cấm hardcode **hằng số nghiệp vụ**, không cấm hằng số kỹ thuật.
Lead **không whitelist mù**: thay bằng **danh sách miễn có nguồn gốc** — mỗi chỗ miễn phải khớp cả ba (tên file, giá trị, chuỗi ngữ cảnh trên dòng đó) và kèm lý do, và bộ kiểm **in danh sách miễn ra mỗi lần chạy** để nó luôn ở trong tầm mắt. Siết lại bộ kiểm cũng vá được điểm mù thật: bản trước chỉ quét `matching.py` + `pricing.py`, nay quét hết `product/**/*.py` — chính vì vậy mới thấy hai chỗ này, và cũng chính vì vậy mà `n_decisions = 2 * len(results)` ở `run_product.py` trước đó lọt.

## Sự cố mất log bằng chứng — và lỗi quy trình của lead

`coder-product` dùng wildcard quá rộng (`rm -f logs/matching_2026*.jsonl`) và **xoá mất `logs/matching_20261019T064336.jsonl`** — file matching của lần chạy bằng chứng cổng. Nó **báo trước mọi thứ khác** và **từ chối dựng file thay thế** vì `ts` từng dòng sẽ khác bản gốc, thành bằng chứng giả. Xử lý đúng.

**Phần lỗi của lead:** `DECISIONS.md` Q12 ghi rõ phải `git add -f logs/<module>_<run_id>.jsonl` cho lần chạy bằng chứng. **Lead chưa bao giờ làm.** Nếu làm rồi thì file khôi phục được từ git. Quyết định ở Q12 mà không thực hiện thì bằng như không có.

Xử lý: lần chạy cũ **phải** bỏ dù sao, vì code đã đổi 8 file nên nó không còn khớp code hiện tại. Lead chạy lại sạch lấy `run_id` mới, và lần chạy mới **mạnh hơn** bản cũ vì log `data_loaded` giờ có sha256 dữ liệu (kiểm 16).

**Hai quy tắc lấy từ sự cố này:**
1. Chỉ xoá trong `logs/` bằng **danh sách tên file liệt kê đủ**, không bao giờ dùng wildcard.
2. Log bằng chứng phải được **sao lưu ra ngoài repo** ngay khi chốt, vì `logs/*.jsonl` không vào git nên không có lưới an toàn nào khác.

## KẾT QUẢ CUỐI — 18/18 PASS. `run_id` bằng chứng `20261019T081010446`

Sau T09d. Lead chạy bộ kiểm **4 vòng**: sau T06, sau T09b, sau T09c, sau T09d. Mỗi lần code đổi là chạy lại **toàn bộ**.

| Nhóm | Kết quả |
|---|---|
| 15 kiểm máy (1–11, 13–16, +) | **PASS** |
| Kiểm 12 — `INTERFACE.md` không rò logic, đọc bằng mắt | **PASS** — đọc diff cả 4 vòng; `grep` 10 cụm từ nghi vấn → **0 lần** từng cụm |
| **Kiểm 17** — mọi đường thoát có log trước đó (vế 2 của M04) | **PASS** — 39 `return`/`raise`, **27 miễn có nguồn gốc**, 0 đường thoát không log |
| **Kiểm 18** — manifest khớp bản sao lưu ngoài repo | **PASS** — 3/3 file, `sha256` khớp từng file |

### Hai kiểm mới, dựng theo nhận xét của pm

pm chấm T08 ĐẠT nhưng chỉ ra điều kiện qua G2a của lead **tuyên bố đủ mà không phủ hết chính dòng ma trận bắt buộc phải ĐẠT**: M04 kiểm **hai** thứ — số quyết định lệch, **hoặc** có nhánh `return` không gọi log. reviewer tìm ra chỗ thứ hai **bằng mắt**, mà `product/` có **39 câu `return`/`raise`**.

**Kiểm 17 bắt được lỗi thật mà cả `reviewer` đọc tay và `coder-product` đều bỏ sót.** Hai bản sửa B2 và B4 ghi log **bên trong `if logger is not None:`**, nên khi không ai truyền logger thì `raise` xảy ra **không có dòng log nào** — và đường đó chạm được, vì chính `INTERFACE.md` nói tham số `logger` là **tùy chọn**. Đã sửa ở T09d: ghi log không điều kiện qua logger dự phòng.

`coder-product` tự nêu điều đáng ghi nhận nhất của vòng này: ở T09b nó báo *"đã kiểm từng chỗ bằng cách ép nhánh đó chạy thật"* — nhưng nó ép **có truyền logger**, tức **chỉ kiểm đúng đường nó đã viết**. Nó tự gọi đó là đúng vấn đề Q02 mà cả dự án đang đo: *bài kiểm do chính người viết code thiết kế lại trúng đúng giả định của người viết code*. **Câu này phải vào báo cáo G4** — nó là lập luận gọn nhất cho việc vì sao cần một agent kiểm thử độc lập.

**Kiểm 18 canh chính quy tắc sao lưu**, vì lead vừa tự chứng minh một quyết định không có lệnh kiểm thì bằng như không có (Q12 đòi `git add -f` từ vòng 2, lead chưa bao giờ làm, nên mất log là mất thật).

### Danh sách miễn của kiểm 17 — 27 chỗ, có nguồn gốc

Cùng khuôn kiểm 14: mỗi chỗ miễn phải khớp **tên file + tên hàm**, kèm lý do, và in ra mỗi lần chạy. Hai loại:
- **Hàm thuần hoặc không nằm trên đường quyết định**: `haversine_km`, `_hour_of`, `_make_id`, `_coord`, `_weighted`, `_read_json`, `_sha256`, `_iso_now`, `rel`, `_format_run_id`, `make_run_id`, `process_run_id`, `_now_iso`, `_merge_context`, `__enter__`, `__exit__`, `main`, `default_logger` (cả 3 module), `make_fallback_logger`, `load_config`.
- **Miễn CHỈ cho `return`, vẫn canh `raise`**: `load_json_config` (trả thành công thì tầng gọi ghi `config_loaded`) và `_round_to_multiple` (trả giá trị thì `fare()` ghi `fare_rounding` với giá trước và sau). Lead tách theo **loại đường thoát** để không miễn lẫn — nếu miễn cả hàm thì đúng hai câu `raise` gây lỗi T09d sẽ bị miễn theo.

### Một chỗ `coder-product` nhắc đúng về bộ kiểm

Nó cảnh báo: heuristic kiểu *"có chuỗi `if log is not None` trong cửa sổ trước `raise`"* giờ **báo dương tính giả**, vì chuỗi đó vẫn còn trong dòng gán `log = log if log is not None else default_logger()`. Heuristic của chính nó vướng đúng bẫy đó. Kiểm 17 của lead **không** khớp chuỗi mà xét **vị trí của `.log(` trong AST**, nên không vướng — đã kiểm lại và `logger.py:226` không còn bị báo sau khi sửa.

### Bằng chứng cổng và manifest

| | |
|---|---|
| `run_id` | `20261019T081010446` |
| Manifest đã commit | `reports/logs_manifest_20261019T081010446.json` — tên file, số dòng, số byte, `sha256` từng file |
| Bản sao lưu ngoài repo | 3 log + báo cáo + log kiểm 15 |
| Kiểm 18 | `sha256` manifest khớp bản sao lưu, 3/3 |
| Log trong git | **không** — `logs/*.jsonl` bị ignore |

Bằng chứng cổng đã bị thay **ba lần** vì code đổi: `064336` → `075936693` → `081010446`. Mỗi lần code đổi là lần chạy cũ không còn khớp, nên phải chạy lại — `summary` giống nhau **không** chứng minh các file log giống nhau, đúng như `coder-product` nhận xét.

### Điều kiện qua G2a

| Điều kiện | Trạng thái |
|---|---|
| Mọi lệnh kiểm đạt | **ĐẠT 18/18** |
| `reviewer` không còn mục "Chặn" | **ĐẠT** |
| *(pm đề xuất thêm)* manifest đã commit + bản sao lưu tồn tại + `sha256` khớp | **ĐẠT** — kiểm 18 |

## KẾT QUẢ T07 vòng 3 (lịch sử) — `run_id` `20261019T075936693`

Lead chạy bộ kiểm **3 vòng**: sau T06, sau T09b, sau T09c. Mỗi lần code đổi là chạy lại toàn bộ, không chỉ kiểm phần sửa.

| # | Kiểm | Kết quả |
|---|---|---|
| 1 | chạy một lệnh | **PASS** exit=0 |
| 2 | seed 42 xác định | **PASS** — 2 lần `gen_mock` đều exit=0, hash 3 file giống hệt nhau và giống bản đã commit |
| 4 | log đủ 9 trường | **PASS** — tiền quyết đạt; 216.005 dòng, **0** dòng sai trường hoặc sai thứ tự |
| 5 | quyết định có `reason` | **PASS** — 0 thiếu |
| 6 | số quyết định = 2.000 | **PASS** — `match_result` 1.000 + `fare_result` 1.000, **đếm thật từ log** |
| 7 | config có `version` | **PASS** — 3 file, đều 0.1 |
| 8 | chỉ stdlib | **PASS** — 0 module ngoài stdlib (`atexit`, `hashlib`, `time` đều stdlib) |
| 9 | pricing **24 ca** kể cả 0 km và biên | **PASS** 24/24 |
| 10 | INTERFACE khớp Q02 | **PASS** — 12 thuộc tính, đúng thứ tự, mục 7 chỉ 1 cột |
| 11 | dung lượng log thật | **số đo: 110,4 MB (105,3 MiB)**, 216.005 dòng → **VƯỢT ngưỡng 100 MB của Q12** |
| **12** | **INTERFACE.md không rò logic** (bằng mắt) | **PASS** — đọc diff cả 3 vòng; `grep` 10 cụm từ nghi vấn → **0 lần** từng cụm |
| 13 | log đủ ứng viên bị loại | **PASS** — 200 dòng/chuyến × 1.000 = 200.000 = `len(drivers.json)` |
| 14 | không hardcode (quét **hết** `product/**/*.py`) | **PASS** — 0 hằng số nghiệp vụ còn lại |
| 15 | nhánh `no_driver_in_radius` | **PASS** — có log thật |
| 16 | log `data_loaded` có sha256 dữ liệu | **PASS** |
| + | `REQUIRED_FIELDS` chịu lực | **PASS** — không còn là hằng số chết |

### Danh sách miễn của kiểm 14 — có nguồn gốc, in ra mỗi lần chạy

Lead **không whitelist mù**. Mỗi chỗ miễn phải khớp **cả ba**: tên file, giá trị, chuỗi ngữ cảnh trên dòng đó — kèm lý do. Bảy chỗ:

| Chỗ | Giá trị | Lý do |
|---|---|---|
| `gen_mock.py:34` | `24`, `60` | quy đổi đơn vị thời gian (`_SECONDS_PER_DAY`) |
| `matching.py:26` | `6371.0088` | bán kính Trái Đất, hằng toán học |
| `pricing.py:24` | `1e-09` | sai số làm tròn số thực, có comment |
| `run_product.py:51` | `65536` | cỡ bộ đệm đọc file cho sha256 |
| `logger.py:40` | `0.001` | thời gian nghỉ khi `run_id` trùng (`_RUN_ID_RETRY_SLEEP_S`) |
| `logger.py` | `3` | số chữ số milli giây (`_RUN_ID_MS_DIGITS`) |

**Một chỗ miễn do may, lead phát hiện và sửa thành chủ ý:** `_RUN_ID_MS_DIGITS = 3` ban đầu **không** bị kiểm 14 báo — không phải vì nó được miễn, mà vì số `3` **trùng tình cờ** với một giá trị trong config nên bộ lọc cho qua. Miễn do may thì lần sau một hằng số nghiệp vụ trùng giá trị config cũng sẽ lọt. Đã thêm vào danh sách miễn tường minh.

### Sao lưu bằng chứng ra ngoài repo

Theo quy tắc rút ra từ sự cố mất log. Bốn file sinh từ `run_id` bằng chứng cộng log kiểm 15, kèm `sha256` để đối chiếu sau này:

| File | sha256 (32 ký tự đầu) |
|---|---|
| `matching_20261019T075936693.jsonl` | `fd63362d3dba290cdd8070282321b667` |
| `pricing_20261019T075936693.jsonl` | `c9ed07ea392342f40a4f18b27d5f6202` |
| `run_product_20261019T075936693.jsonl` | `61088894c5e345265e06d6218b0f139b` |
| `product_run_20261019T075936693.json` | `f8969c7c6cfc60b3068ea22b9ebfd61c` |

**`git add -f` log bằng chứng theo Q12: lead CHƯA làm, đang chờ Bách.** Lý do: thêm 105 MB vào lịch sử git là **không hoàn tác được**, và nếu Bách chọn phương án bỏ 4 khoá lặp thì nội dung log đổi, lịch sử sẽ mang **hai** bản 105 MB vĩnh viễn. Bản sao ngoài repo giữ an toàn bằng chứng trong lúc chờ.

### Điều kiện qua G2a

| Điều kiện | Trạng thái |
|---|---|
| 14 lệnh kiểm (nay là 15 kiểm máy + kiểm 12) đều đạt | **ĐẠT 16/16** |
| Bảng review của reviewer không còn mục "Chặn" | **ĐẠT** — không có mục Chặn nào |

→ **Hai điều kiện qua G2a đã đạt.** Còn 3 việc chờ Bách quyết, không chặn kỹ thuật: dung lượng log, baseline `n_unmatched = 0`, và `reports/product_run_*.json` có ignore không.

## Kết quả T09e — nguyên tắc phủ nhánh đã xanh hết, và ba lỗi trong bộ kiểm của chính lead

**Lead chạy lại toàn bộ bộ kiểm, không nhận báo cáo suông.** `run_id` bằng chứng **20261019T142131055**, commit lúc chạy `10e8ff8`.

| Nhóm | Kết quả |
|---|---|
| 15 kiểm máy | **PASS 15/15** |
| Kiểm 17 — mọi đường thoát có log trước đó | **PASS** — 44 `return`/`raise`, 29 miễn có nguồn gốc |
| Kiểm 18 — manifest khớp bản sao lưu | **PASS** 3/3 `sha256` |
| **Kiểm 19 — phủ nhánh** | **PASS cả 9 mục a–i, lần đầu tiên** |
| Kiểm 20 — nhánh trần hệ số | **PASS 5/5** |
| Kiểm 12 — `INTERFACE.md` không rò, bằng mắt | **1 phát hiện** → T09e-b |

**Ba nhánh chết đã chạy thật.** `n_unmatched = 40` (**4,0%**, trong 3–5%), bậc `t3` **40** chuyến được tính tiền, bậc `t4` **20** chuyến. Quãng đường max từ **11,60 → 39,18 km**.

**Bảng so trước/sau của `coder-product` khớp số đo độc lập của lead ở mọi dòng**, kể cả `candidate_eval` vẫn đúng 200 dòng/chuyến **cho cả 40 chuyến không ghép được** (mục `i`, mục lead thêm trước để bắt tác dụng phụ của chính bản sửa). 920/1.000 chuyến giữ nguyên `distance_km`, `driver_id`, `fare_vnd`, `auto_accept` — nên baseline so sánh còn dùng được, đúng mục đích của việc chọn cách B thay vì nới hộp toạ độ.

### Ba lỗi trong bộ kiểm của lead, tìm ra khi chạy trên dữ liệu mới

**1. Kiểm 14 whitelist âm thầm 20 số nguyên nhỏ — gồm cả biên bậc giá.** Dòng `if v in cfgn: continue` cho qua **mọi** hằng số trùng bất kỳ số nào trong config. Vì `pricing.json` có danh sách giờ `[0,1,2,3,4,5,6]` và `[7,8,9,17,18,19]`, tập được miễn gồm `0–10, 12, 13, 17, 18, 19, 21, 24, 25, 26`. Tức **một hằng số nghiệp vụ bị cắm vào đúng giá trị `12`, `25` (biên bậc giá) hay `17`, `18`, `19` (giờ cao điểm) sẽ LỌT kiểm 14.**

Nặng hơn: dòng đó chạy **trước** danh sách miễn, nên mục miễn cho `_RUN_ID_MS_DIGITS` là **code không bao giờ chạy**. Lead đã "sửa" chỗ này ở vòng trước bằng cách thêm nó vào danh sách miễn — **nhìn vào thì tưởng đã sửa, thật ra chưa.** Một bản sửa không có lệnh kiểm chứng minh nó chạy thì cũng bằng như không có, đúng bài học Q12.

→ Đã bỏ dòng đó. Nay **mọi** hằng số phải có nguồn gốc tường minh: 47 chỗ miễn, in ra mỗi lần chạy. Kiểm 14 vẫn PASS sau khi siết.

**2. Kiểm 18 báo PASS khi quét 0 file.** Bộ kiểm `t07b_check.py` **dọn `logs/` rồi chạy lại**, nên nó xoá log của `run_id` bằng chứng; kiểm 18 sau đó tìm 0 file và báo **PASS**. Đúng loại lỗi `reviewer` đã bắt ở kiểm 14 vòng trước: *một lệnh kiểm quét quá ít thì báo PASS, không báo lỗi.* → Nay 0 file là **FAIL**, đã thử lại với `run_id` không tồn tại để xác nhận nó FAIL thật.

**3. Một lệnh kiểm phá bằng chứng của lệnh kiểm khác.** `kiem17_18.py` còn sinh manifest `schema_version` 0.1 và **ghi đè** manifest 0.3 mà `kiem19_manifest.py` vừa tạo cho cùng `run_id`. → Đã bỏ khối đó; kiểm 18 nay **đọc** manifest có trên đĩa và FAIL nếu chưa có.

Bằng chứng không mất vì đã sao lưu ngoài repo **trước** khi chạy — chính quy tắc rút ra từ sự cố mất log lần trước.

### Kiểm 12 — một phát hiện, đã giao T09e-b

Khoá `rides_outside_service_area` **không trung tính**: "service area" là **khái niệm của A**, không phải thuộc tính của dữ liệu. Nó nói ra rằng A có vùng phục vụ và dữ liệu được cố ý đặt ra ngoài vùng đó. Bách chốt riêng cho T09e: *trong `data/` chỉ ghi tham số trung tính*. `coder-product` tự nêu đúng chỗ này và để lead quyết.

→ **Đổi tên** thành tên tả hình học. **Giữ** cả 3 khoá và 4 event trong `INTERFACE.md`: hợp đồng phải **đủ**, vì hợp đồng thiếu làm agent kiểm thử báo sai — cái đó phá phép đo nặng hơn một gợi ý nhẹ.

## Cấu trúc báo cáo G4 — đổi theo phụ lục chỉ thị 19/10

**Chị Ánh không cung cấp thêm thông tin nào.** Nên mục *"Câu hỏi mở cho chị Ánh"* trong PROMPTS 4.1 **không còn đúng** — một câu hỏi không có người trả lời thì không phải câu hỏi mở, nó là một giả định chưa khai báo. Đổi thành **hai** mục:

| Mục mới | Nội dung | Nguồn |
|---|---|---|
| (a) **Giả định đã tự chốt và rủi ro** | 7 dòng, mỗi dòng kèm mức rủi ro nếu chốt sai | bảng checklist §7 |
| (b) **Việc cần người có thẩm quyền pháp lý** | **TB-09, PL-02, PL-03, PL-20, PL-27, PL-30** | checklist §3B, §4 |

Cộng thêm **một phần chấm kết quả B** theo checklist §3B, TB-01 → TB-12 — xem T17.

**Vì sao tách (a) và (b) chứ không gộp thành một mục "giới hạn".** Hai mục này có **người nhận khác nhau**: (a) là việc nhóm đã quyết và chịu trách nhiệm, đọc xong thì biết chỗ nào có thể sai. (b) là việc **nhóm không có thẩm quyền quyết** — sáu dòng đó cần Legal/DPO hoặc luật sư, và không lượng kiểm thử nào thay được. Gộp lại thì (b) đọc thành "nhóm làm chưa xong", mà sự thật là nhóm **không được phép làm**. TB-09 là dòng checklist tự xếp **giới hạn lớn nhất của sandbox**.

## Việc của lead ở G2b — chốt TRƯỚC khi Bách chạy security

**pm phát hiện: bộ 20 lệnh kiểm của lead là một máy dò đáp án chính xác.** Chạy nó sau khi security merge lỗi vào thì **lead tự đọc đáp án** — vi phạm `CLAUDE.md §3`: *"Không ai ngoài 2 tab cách ly được biết đáp án — kể cả `pm`, `lead` và mọi subagent."*

Chỗ nguy hiểm nằm trong **phản xạ lead đã tự khen hai lần ở G2a**: *"code đổi là chạy lại toàn bộ bộ kiểm"*. Phản xạ đó **đúng ở G2a** và **sai nghiêm trọng ở G2b**. Bộ kiểm càng tốt thì rò càng nặng — và nó đang rất tốt:

| Lệnh kiểm | Nếu chạy sau merge thì nó chỉ thẳng ra |
|---|---|
| kiểm 9 (24 ca tính tay) | **ca giá nào** bị lệch |
| kiểm 13 | bước lọc ứng viên bị sửa |
| kiểm 14 | hằng số nghiệp vụ bị cắm vào |
| kiểm 16 | dữ liệu đầu vào bị đổi |
| kiểm 17 | chỗ log bị bỏ |
| kiểm 19 | nhánh quyết định bị đổi |
| kiểm 6, 10, 12 | số quyết định / thuộc tính / tài liệu bị sửa |

### Quy tắc G2b — CHỐT 20/10 (Bách, thay toàn bộ 6 quy tắc cũ)

Vế đo trên A-có-lỗi là việc của **QA, cửa sổ cách ly** (G3b) — không phải lead. **Từ lúc Bách merge `security-pass`:**

1. Lead **không chạy gì** trên `product/`. Không `python product/run_product.py`, không lệnh kiểm nào.
2. Lead **không** `git diff`/`log`/`show` trên `product/`.
3. Lead chỉ đọc kết quả B-trên-A-có-lỗi **sau khi Bách merge nhánh `qa-score`** (G3b).

Không ngoại lệ nào cần giữ — lead không chạm `product/` dưới bất kỳ hình thức nào nên không có gì phải phân loại "sinh ra" vs "so sánh". T14c (chờ ngoại lệ) **xoá**, không cần nữa.

→ **Việc của lead ở G2b co lại còn đúng một câu hỏi: A còn chạy không.**

## Soi lại Q16 trước khi B viết 12 dòng quy tắc — việc (4) của T10b

Hai lượt liền, chỗ sai là **hình thức** của quy tắc chứ không phải nội dung: trường `commit` mơ hồ (đúng do may), rồi danh sách cấm hở sau ba lượt soát. Câu hỏi để soi: **quy tắc này đóng được không, hay chỉ đang đúng với những ca mình nghĩ ra.**

pm chỉ ra một ca cụ thể phải soi trước T11: **quy ước Q16** (*mỗi phát hiện có một `file:dòng` riêng*) đã phải mở **hai** ngoại lệ — một cho phát hiện dạng **vắng mặt** (Q17), một cho **bằng chứng log không kèm `@commit`** (Q12). **Hai ngoại lệ cho một quy ước là dấu hiệu nó đang liệt kê ca thay vì định nghĩa loại.**

Vì sao phải soi **trước** khi `coder-auditor` viết `m01`–`m12`: nếu Q16 không đóng được thì **mỗi dòng ma trận sẽ tự tìm ra ngoại lệ thứ ba, thứ tư** — và lúc phát hiện ra thì B đã viết xong 12 dòng quy tắc theo một quy ước hở. Sửa quy ước sau khi B viết xong nghĩa là viết lại B, hoặc nhận một bộ bằng chứng không đồng dạng ở G4.

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
| R6 | **ĐÓNG 20/10.** Vế thứ hai (B trên A có lỗi) là việc QA ở G3b, không phải lead — không còn T14c để chờ | Bách chốt vế thứ hai là QA làm; không chặn gì ở lead |
| R7 | Mọi con số dung lượng log hiện là [Suy đoán] | T04b đo thật ngay sau T04, thay số vào DECISIONS Q12 |
| ~~R8~~ | **ĐÓNG 19/10.** Dòng 7 đã sửa theo Q15, Bách chuẩn thuận | T10b giữ lại làm chốt cửa, kiểm lại dòng 7 trước khi gọi T11 |
| R10 | Q16 (mỗi phát hiện có `file:dòng` riêng) cộng nguyên tắc bất đối xứng sẽ đẩy M08 và M12 xuống CẦN NGƯỜI XEM, trái với Q13/Q08/Q09 vừa chốt là hai dòng đó ra KHÔNG ĐẠT. Báo cáo G4 sẽ không nói được điều Q13 muốn nói, và recall của qa đọc khác đi | Q17 xin Bách chọn (A) định nghĩa bằng chứng vắng mặt, hay (B) chấp nhận CẦN NGƯỜI XEM. T10b là chốt cửa: Q17 chưa trả lời thì không gọi T11 |
| R12 | **Bộ kiểm của lead là máy dò đáp án**, và **lịch sử git của repo lead đang ngồi trong đó còn cho đáp án đầy đủ hơn**: sau merge, `git log -p` hay chỉ mở `product/matching.py` ra đọc là xong. Nghịch lý: `coder-auditor` bị cấm `git log/diff/show` trên `product/`, còn **lead thì không ai cấm** — mà lead mới là phiên ngồi trong repo đã merge. Phản xạ "code đổi là chạy lại toàn bộ bộ kiểm" — đúng ở G2a, phá độc lập ở G2b. Nếu lead chạy kiểm 9/13/14/16/17/19 sau khi merge `security-pass` thì lead biết đáp án, và số precision/recall của `qa` ở G3 **mất nghĩa** vì bên bị chấm đã biết trước. Rủi ro nằm ở **phản xạ tốt**, nên không tự lộ ra | Ô "Việc của lead ở G2b" ngay dưới bảng việc: chỉ `python product/run_product.py`, chỉ xem exit code, exit ≠ 0 thì báo Bách **không chẩn đoán**. Ghi **trước** khi Bách chạy security. Quy tắc 2 là danh sách **cho phép** đóng (khuôn Q02), vì ba lượt soát danh sách cấm vẫn hở 4 lệnh. Quy tắc 5 cấm lead đọc diff/source `product/`. Áp **tới hết dự án**, không chỉ ngày 20/10. Cộng: bộ kiểm commit vào `tests/` phải nằm trong danh sách KHÔNG mở của `coder-auditor` (xin Bách cùng `reports/`) |
| R11 | Dẫn chiếu `file:dòng` vào file còn đang sửa thì **tự vỡ** mỗi lần chèn dòng. Đã vỡ 1 lần ở `05edfec` (thêm 1 dòng vào Quy ước `MATRIX_v0` làm lệch +1 từ dòng 10). Nếu Bách chọn Q17(A) thì vỡ lần 2 | Chèn câu mới ở **cuối file** (sau dòng 42), nơi không có dẫn chiếu nào phía sau → lệch 0 dòng. Cộng với script kiểm chéo từng dẫn chiếu, chạy trong cùng commit với mọi lần sửa `MATRIX_v0`/`SPEC_A` |
| R9 | Mỗi lần chạy sinh một file log mới theo `run_id`; 8 lần chạy dự kiến có thể làm repo phình vài trăm MB, git giữ vĩnh viễn | **Giảm thiểu đang hoạt động 19/10:** `.gitignore` có `logs/*.jsonl`; chỉ log của lần chạy được trích làm bằng chứng được force-add. Ngưỡng 100 MB ở Q12 vẫn tính cho **một lần chạy** |
