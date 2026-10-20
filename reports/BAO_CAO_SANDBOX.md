# Báo cáo sandbox GSM — kiểm định phương pháp cho matching + pricing

> **[Suy luận]** Kết quả kiểm định phương pháp cho `product/` (A) và `auditor/` (B), dự án sandbox GSM. `security-pass` merge tại `83229ff`, `qa-score` merge tại `a3453cb`.

## 1. Mục tiêu & phạm vi

Dự án này chứng minh **một phương pháp kiểm định thuật toán**: dùng một agent AI (B) để tự động rà soát một sản phẩm mẫu (A — matching + pricing taxi) theo một ma trận quy tắc (`MATRIX_v0.md`) ánh xạ từ ISO/IEC 42001 + Đạo luật AI EU + GDPR + Chỉ thị Lao động Nền tảng (PWD).

**Không chứng minh**: sản phẩm thật của Green SM có tuân thủ hay không. A là mô phỏng, 100% dữ liệu tổng hợp (seed 42), không dùng code hay dữ liệu thật của Green SM (`CLAUDE.md §2`, `§6`).

Thước đo thành công: B có phát hiện được lỗi cài sẵn có chủ đích không (`security`, cửa sổ cách ly), ở mức recall/FNR/precision nào, và B có độc lập với người xây A hay không.

## 2. Kiến trúc A và B, cách đội làm việc, nguyên tắc độc lập

| | A | B |
|---|---|---|
| Vai trò | Sản phẩm bị kiểm định — matching + pricing | Agent kiểm định — đọc A, không đọc đáp án |
| Thư mục | `product/` | `auditor/` |
| Xây bởi | subagent `coder-product` | subagent `coder-auditor` |
| Nguồn cho phép đọc | `docs/SPEC_A.md`, `docs/DECISIONS.md` Q02 (danh sách thuộc tính), `CLAUDE.md` | **CHỈ** `docs/MATRIX_v0.md` + `docs/INTERFACE.md` |

**Đội**: `lead` (điều phối, không viết code nghiệp vụ, ghi `docs/TASKS.md`), `pm` (chấm kế hoạch/báo cáo, 4 mốc: G2a, `b-freeze`, kết quả sau merge, G4), `security`/`qa` (cửa sổ cách ly riêng của Bách, không nhắn tin với ai).

**Nguyên tắc độc lập** (`CLAUDE.md §3`), cơ chế thực hiện:

- `coder-auditor` không đọc `product/*.py` bằng mắt, không `git log/diff/show` trên `product/`, không đọc `DECISIONS.md`/`TASKS.md`/`SPEC_A.md`/`CHECKLIST_KIEM_TOAN.md`/`tests/` — chỉ `ast.parse`, `regex`, đọc log JSONL, hoặc tự chạy lại `product/run_product.py`.
- `reviewer` chỉ review `product/` **trước** khi security chạy; sau đó chỉ review `auditor/`.
- B được **đóng băng** (`git tag b-freeze`) **trước** khi security cài lỗi — không phải sau. Thứ tự này đảm bảo B không thể được xây "quanh" lỗi đã biết (xem mục 7, khoảng trống Q21/thứ tự cổng).
- Từ lúc Bách merge `security-pass`: `lead` không chạy gì trên `product/`, không `git diff/log/show` trên `product/` — vì bộ kiểm riêng của `lead` (`tests/`) là một máy dò đáp án chính xác (R12).
- Bằng chứng log là **chính B tự sinh**, không dùng log cũ: mỗi dòng trích dẫn một dòng log sản phẩm làm bằng chứng được **chép nguyên văn** vào `reports/audit_<commit>.log.jsonl` (file có commit), kèm `run_id` + lệnh đã chạy — để bằng chứng tái lập được dù `logs/*.jsonl` không vào git.

## 3. Kết quả audit M01–M12 (B chạy trên A sạch, tại `b-freeze` = `cce80bf`)

Nguồn: `reports/audit_8869ebd.md` (hash cây `auditor/` giống `b-freeze`, đã kiểm `d8638d0`). Độ ổn định (TB-04): 3 lần chạy B@`b-freeze`, so JSON sau chuẩn hoá — giống hệt (xem T13, `docs/TASKS.md`).

| ID | Control (ISO 42001) | Luật | Kết quả | Source (ví dụ) |
|---|---|---|---|---|
| M01 | A.5.4 | AI Act PL III 4(b); PWD Đ.8 | **ĐẠT** | chênh lệch tỷ lệ ghép theo `customer_segment` 0,58%; khoảng cách theo `vehicle_type` 4,52% — cả hai < 10% |
| M02 | A.7.4 | PWD Đ.7 | **ĐẠT** | `product/matching.py` — không truy cập thuộc tính ngoài whitelist 10 thuộc tính (Q02) |
| M03 | A.7.5 | GDPR Đ.5(1)(c) | **ĐẠT** | quét regex 4 file `data/`+`config/`, không khớp SĐT/email/CCCD/CMND |
| M04 | A.6.2.8 | AI Act Đ.12 | **ĐẠT** | 2000/2000 quyết định có log, `reason` không rỗng |
| M05 | A.6.2.3 | AI Act Đ.11 | **CẦN NGƯỜI XEM** | `matching.py:26` (`6371.0088`), `pricing.py:24` (`1e-09`) — **[Chưa xác minh]** heuristic, 2 hằng số này thực chất là bán kính Trái Đất và epsilon làm tròn, không phải hằng số nghiệp vụ. Nguồn: `docs/TASKS.md:382-383` — danh sách miễn của kiểm 14, khớp tên file + giá trị + ngữ cảnh kèm lý do, vào repo tại commit `100f2a0` (19/10, **trước** khi security chạy). B không có quyền biết điều này |
| M06 | A.6.2.7 | AI Act Đ.11 | **ĐẠT** | cả 3 file config có `version` |
| M07 | A.9.2 | GDPR Đ.22; PWD Đ.10 | **CẦN NGƯỜI XEM** | `auto_accept` có thật (554/1000 quyết định), nhưng B chỉ quét được **từ khoá** cho bước xem xét con người, không xác nhận được cơ chế thật |
| M08 | A.5.2 | GDPR Đ.35; PWD Đ.8 | **CẦN NGƯỜI XEM** | xem mục 5 — **giới hạn của phép đo**, không phải A tuân thủ |
| M09 | A.8.2 | PWD Đ.9 | **ĐẠT** | 2000/2000 dòng quyết định có `reason` |
| M10 | A.6.2.4 | AI Act Đ.15 | **ĐẠT** | 3 lần chạy `run_product.py`, giống hệt sau khi bỏ trường biến động |
| M11 | A.5.4 (pricing) | Luật tiêu dùng EU [Suy luận] | **ĐẠT** | `fare()` không đọc `segment`/`customer`, không `open`/`load` file ngoài hợp đồng |
| M12 | A.6.2.6 | AI Act Đ.72 [Suy luận] | **KHÔNG ĐẠT** | quét đủ 3 config + 5 file `.py`: không có ngưỡng cảnh báo cho tỷ lệ `auto_accept` **tổng hợp** (chỉ có ngưỡng từng chuyến) |

Kết quả B chạy trên A **có lỗi** (sau merge `security-pass`) — do qa chạy ở cửa sổ cách ly, so với kết quả trên A sạch ở bảng trên để tính TB-01/02/03. Số đo: xem mục 4.

## 4. Số đo QA

Nguyên văn từ `reports/qa_score_83229ff.md` (qa chấm, merge `a3453cb`) — không tự tính lại.

- Phạm vi: B đóng băng tại `b-freeze` (`cce80bf`), không đổi giữa C0=`2abeafd` và C1=`83229ff` (`git diff b-freeze <commit> -- auditor/` rỗng ở cả hai). 6 mục lỗi cài + 3 mục sạch được chấm.
- Chấm theo **tập bằng chứng** (`file:dòng`), không theo nhãn ĐẠT/KHÔNG ĐẠT/CNX — ánh xạ qua `git diff` giữa C0/C1 theo nội dung dòng, không chỉ số dòng (Q23).

| | Số lượng |
|---|---|
| TP (bắt đúng lỗi cài) | 4 |
| FN (bỏ sót lỗi cài) | 2 |
| FP (báo động giả trên mục sạch) | 0 |

| Số đo | Kết quả | Mục tiêu riêng của qa [Suy luận] | So mục tiêu §3B (≥80% / ≤20%) | Đạt? |
|---|---|---|---|---|
| precision | **1.000** | (không đặt mục tiêu cứng) | — | — |
| recall | **0.667** | ≥ 0.833 (5/6) | ≥ 0.80 | Không đạt cả hai |
| FNR | **0.333** | ≤ 0.167 (1/6) | ≤ 0.20 | Không đạt cả hai |

Lưu ý: `0.833`/`0.167` là mục tiêu **riêng qa đặt**, chặt hơn ngưỡng gốc của checklist §3B (`CHECKLIST_KIEM_TOAN.md:133-134`: recall ≥ 80%, FNR ≤ 20%). Dù dùng ngưỡng nào, kết luận không đổi: 0.667 không đạt.

Độ ổn định (qa, trên `83229ff`): chạy `run_audit.py` 3 lần, so JSON sau chuẩn hoá — **3/3 giống hệt** toàn bộ 12 dòng ma trận. Khớp hướng với TB-04 ở mục 8 (lead tự chạy trên `b-freeze`).

Ghi chú của qa (nguyên văn, không diễn giải lại): 2 dòng ma trận đã CNX trên A sạch có sinh bằng chứng mới ở C1, nhưng bằng chứng đó rơi vào vị trí của (các) lỗi đã được dòng khác bắt đúng — không rơi vào vị trí của 2 lỗi còn bị bỏ sót, nên không tính thêm TP.

### Vì sao sót 2 lỗi (FN=2) — phần quan trọng nhất của báo cáo này

**Bách xác nhận: cả 2 lỗi bị sót nằm TRONG vùng 12 dòng ma trận** (`docs/DECISIONS.md` Q24, hỏi và trả lời **sau** khi `qa-score` đã merge — không mở trước hoặc trong lúc đo, không làm bẩn tính mù của phép đo). Vậy FN = 2 **không phải** do `MATRIX_v0` thiếu dòng — giả thuyết "độ phủ ma trận" ở bản nháp trước là sai, sửa lại ở đây.

Với lỗi nằm trong vùng, nguyên nhân tách thành hai tầng khác hẳn nhau về việc phải sửa gì:

- **(i) Câu quy tắc trong `MATRIX_v0` quá yếu** để bắt loại lỗi đó, dù `auditor/rules/mXX.py` hiện thực đúng câu chữ. Việc sửa là sửa **ma trận** — thuộc backlog sau 22/10 — và theo TB-12, đổi `MATRIX_v0` thì phải chạy lại toàn bộ TB-01→TB-05.
- **(ii) Câu quy tắc đủ mạnh, nhưng `auditor/rules/mXX.py` hiện thực yếu hơn câu chữ** của `MATRIX_v0`. Việc sửa là sửa **B**, và phải đo lại với một bộ lỗi **mới** (bộ lỗi hiện tại đã dùng để chấm, không dùng lại được để kiểm bản B đã sửa).

Phân biệt (i)/(ii) được bằng cách đọc câu quy tắc của dòng đó trong `MATRIX_v0` rồi so với hiện thực tại `b-freeze` — **không cần biết đáp án là lỗi gì**. Đây đúng loại lỗi "hình thức của quy tắc" (câu chữ đúng nhưng cách đóng không phủ hết, hoặc hiện thực không theo sát câu chữ) mà đội đã bắt **bốn lần** ở G1–G3 (Q02, Q19, R12, manifest).

**Mức độ nặng còn phụ thuộc dòng nào bị sót, theo hai ca — cả hai là ứng viên [Chưa xác minh], chưa biết ca nào đúng:**
- Nếu rơi vào M05, M07 hoặc M08 (ba dòng vốn đã CẦN NGƯỜI XEM trên A sạch): tín hiệu ở đó yếu từ đầu, M08 bị bịt hoàn toàn (mục 5) — đây là **giới hạn đã khai báo trước khi đo**, không phải phát hiện mới.
- Nếu rơi vào một trong 8 dòng ra ĐẠT: dòng đó ra **ĐẠT trên chính A có lỗi** — một **vacuous pass**: quy tắc chạy xong và báo an toàn đúng tại chỗ có lỗi. Ca này nặng hơn nhiều vì nói về phương pháp chấm, không chỉ về một dòng.

**MỞ ĐÁP ÁN SAU THÍ NGHIỆM (`docs/DECISIONS.md` Q24, chốt 20/10 — hỏi/trả lời SAU khi `qa-score` đã chấm xong):** Bách đã xác định nội bộ 2 dòng ma trận cụ thể bị sót và ca tương ứng — **chọn giữ dạng tổng quát, không công khai số dòng cụ thể** trong báo cáo này. Tách hẳn khỏi phần đo phía trên để người đọc phân biệt đâu là kết quả mù, đâu là giải thích khi đã biết đáp án.

## 5. Khoảng trống đã biết

- **Thu nhập tài xế**: ngoài phạm vi (`CLAUDE.md §6`).
- **M08 không bao giờ lên `KHÔNG ĐẠT`** (Q23, Bách chốt 20/10): B bị cấm đọc nội dung `docs/` nên không thể xác nhận có/không có tài liệu đánh giá tác động. `CẦN NGƯỜI XEM` ở M08 là **giới hạn của phép đo** do chính nguyên tắc độc lập tạo ra, không phải bằng chứng A có/không có DPIA.
- **M05, M07 là CẦN NGƯỜI XEM trên A sạch, không phải trên A có lỗi** — nếu security cài lỗi đúng vùng này, nhãn kết quả không đổi (CNX→CNX). Bách đã chỉ thị qa chấm theo **tập bằng chứng** (`file:dòng`), không theo nhãn, để không mất khả năng phát hiện (Q23). **Precision của M05 trên A sạch = 0/2**: cả 2 bằng chứng trích (`6371.0088`, `1e-09`) đều là hằng số toán học/làm tròn, không phải hằng số nghiệp vụ (xác nhận riêng bởi `reviewer`/`lead`) — cả hai là dương tính giả trên A sạch.
- **Tên người thật xuất hiện trong repo (dọn sau G4)**: tên của người duyệt nội dung pháp lý bên ngoài dự án (tên nêu trong `CLAUDE.md`, không lặp lại ở đây) xuất hiện trong lịch sử 7 commit và trong comment `auditor/rules/m07_adverse_action_review.py:13`. Lúc repo còn public, đây lộ qua web; Bách đã chuyển repo Private nên hết nguy ngay lúc này. Kế hoạch: dọn comment đó **sau khi G4 hoàn tất** (không sửa `auditor/` trong lúc còn chờ G3b).
- **Mechanism/Effect, Minimal/Mitigation**: taxonomy tự định nghĩa (`CHECKLIST_KIEM_TOAN.md §6`), lead điền tay, không đưa vào B.
- **Số hiệu control ISO/IEC 42001**: khớp 3 nguồn thứ cấp, chưa đối chiếu bản chuẩn có bản quyền.
- **Giới hạn mô phỏng đã biết**: `match()` là hàm thuần, không cập nhật `status` tài xế sau khi ghép — một tài xế có thể "thắng" nhiều chuyến trong mock data.
- **Trần hệ số giờ 1.3** không chạm trên config mặc định (hệ số cao nhất là 1.2) — đã kiểm bằng chẩn đoán riêng (kiểm 20), không phải trên dữ liệu bằng chứng.

## 6. Giả định đã tự chốt và rủi ro

> Bối cảnh: người duyệt pháp lý bên ngoài dự án không cung cấp thêm thông tin nào. Nhóm tự nghiên cứu và tự chốt, nguồn: `docs/CHECKLIST_KIEM_TOAN.md §7`.

| Điểm | Chốt | Rủi ro nếu sai |
|---|---|---|
| Danh sách 15 control trọng tâm | §2.2 checklist | Thấp — chỉnh được, không ảnh hưởng kết quả đo |
| Số hiệu control | Khớp 3 nguồn thứ cấp độc lập | Thấp |
| Mechanism / Effect | Taxonomy §6, lead điền tay, không sửa B | Trung bình — có thể lệch taxonomy nội bộ thật |
| Minimal / Mitigation | Định nghĩa §6 | Trung bình |
| Thị trường EU | Đan Mạch (chính thức 30/07/2026) + Hà Lan (thử 25/09/2026) | Thấp — có nguồn chính thức |
| Legal/DPO ký duyệt | Giả định: Legal/DPO của Green SM | Trung bình |
| Bộ quy tắc pháp lý đã được Legal duyệt? | **Chưa** — giới hạn lớn nhất của sandbox | Cao, nhưng đã khai báo (TB-09) |

## 7. Việc cần người có thẩm quyền pháp lý

Sáu mục nhóm **không có thẩm quyền quyết** — cần Legal/DPO hoặc luật sư, không lượng kiểm thử nào thay được:

| Mục | Câu hỏi |
|---|---|
| TB-09 | Bộ quy tắc pháp lý (MATRIX_v0) đã được người có chuyên môn pháp lý duyệt chưa? — **Chưa**, trong sandbox |
| PL-02 | Pháp nhân nào là provider theo Đạo luật AI? Có cần đại diện được ủy quyền tại EU? |
| PL-03 | Tinh chỉnh theo vùng có làm VSF trở thành provider không? |
| PL-20 | Xử lý dữ liệu tài xế EU từ Việt Nam có áp dụng ngoài lãnh thổ không? |
| PL-27 | Chuyển dữ liệu EU → Việt Nam dùng công cụ gì (SCC + đánh giá tác động)? |
| PL-30 | Green SM ở Đan Mạch/Hà Lan có phải "nền tảng lao động số" theo PWD không? |

## 8. Chấm kết quả B theo checklist §3B (TB-01 → TB-12)

| TB | Tên | Số đo | Nguồn |
|---|---|---|---|
| TB-01 | Recall | **0.667 — Không đạt** cả ngưỡng §3B (≥0.80) và mục tiêu riêng của qa (≥0.833) (4/6 lỗi cài bắt được) | qa, mục 4 |
| TB-02 | FNR | **0.333 — Không đạt** cả ngưỡng §3B (≤0.20) và mục tiêu riêng của qa (≤0.167) (2/6 lỗi bị bỏ sót) — chỉ số sống còn; lý do sót xem mục 4 "Vì sao sót 2 lỗi" | qa, mục 4 |
| TB-03 | Precision | **1.000** — 0 báo động giả trên 3 mục sạch | qa, mục 4 |
| TB-04 | Độ ổn định | **ĐẠT** — 3 lần chạy B@`b-freeze` giống hệt sau chuẩn hoá | T13 |
| TB-05 | Truy nguồn | **ĐẠT** — 100%, mỗi phát hiện có `file:dòng`[`@commit`] riêng | T11/T12 |
| TB-06 | Độc lập | **ĐẠT** — `reviewer` grep toàn `auditor/`, không rò nội dung bị cấm. **Rủi ro đã quản lý**: có một quãng repo ở chế độ public với nhánh `security-pass` đã đẩy, nên diff đáp án đọc được từ ngoài; không ảnh hưởng phép đo vì B đã đóng băng tại `b-freeze` trước khi security chạy. Bách đã chuyển repo Private | T14 |
| TB-07 | Đóng băng | **ĐẠT** — theo đúng ngưỡng §3B ("không có commit nào sau `b-freeze` **mà không báo**"), không theo nghĩa "không commit nào". Có **đúng một** commit chạm `auditor/` sau `b-freeze` (`cce80bf`): `0ad269b`, **sau khi Bách đã duyệt G4**, do Bách yêu cầu trực tiếp — chỉ đổi 1 dòng docstring (`m07_adverse_action_review.py:13`) để bỏ tên người thật. Hành vi B không đổi: chứng minh bằng AST giống hệt sau khi bỏ node docstring (`tests/kiem22_m07_docstring.py`, PASS), và `git diff --name-only b-freeze HEAD -- auditor/` ra đúng 1 file. Lead đã tự khai commit này cho `pm` trước khi `pm` tự phát hiện bằng lệnh kiểm | T14b, `tests/kiem22_m07_docstring.py` |
| TB-08 | Nguồn gốc quy tắc | **ĐẠT** — mỗi dòng MATRIX có cột control+luật | `matrix.json` |
| TB-09 | Legal/DPO duyệt | **CHƯA** — giới hạn khai báo | mục 6 |
| TB-10 | Log của B commit | **ĐẠT** — `reports/audit_<commit>.log.jsonl` | — |
| TB-11 | Phạm vi dùng B rõ | **ĐẠT** — tài liệu vai trò `CLAUDE.md §3` | — |
| TB-12 | Chạy lại bộ đo khi đổi MATRIX | **[Chưa xác minh]** — chưa có lần đổi MATRIX sau `b-freeze` để kiểm | — |

Ngưỡng ở checklist §3B (recall ≥ 80%, FNR ≤ 20%) là **[Suy luận]** của chính checklist, không phải chuẩn ngành.
