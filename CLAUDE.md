# GSM SANDBOX — QUY TẮC ĐỘI

> [Suy luận] Toàn bộ dự án sandbox này là mô phỏng. Không phải sản phẩm thật của Green SM, không phải tư vấn pháp lý.

- Hạn chót: **22/10/2026**
- Người duyệt cuối: **Bách** — duyệt mọi cổng (G1–G4). Không cổng nào tự qua.
- `pm`: tab Claude riêng, giám sát chất lượng kế hoạch của lead, nhắn tin trực tiếp với lead.
- `lead`: tab Claude chính trong extension VS Code, điều phối subagent.

## 1. Mục tiêu

| | Đối tượng | Thư mục |
|---|---|---|
| **A** | Sản phẩm mẫu: matching + pricing (giá cước khách) | `product/` |
| **B** | Agent kiểm thử A theo `docs/MATRIX_v0.md` (rule-based + ML đơn giản) | `auditor/` |

Kết quả chứng minh **PHƯƠNG PHÁP kiểm định**, không chứng minh sản phẩm thật của Green SM tuân thủ.

## 2. Ràng buộc cứng

1. **Chỉ Python standard library.** Không `pip install`. Python ≥ 3.10.
2. **Dữ liệu 100% tổng hợp.** Không tên, số điện thoại, biển số, địa chỉ thật. Seed cố định = 42.
3. **Logging chi tiết TỪNG tín hiệu.** Mỗi ứng viên được xét, mỗi bước tính, mỗi lý do loại, mỗi giá trị trung gian.
   - Định dạng JSON Lines, ghi vào `logs/<module>_<run_id>.jsonl`
   - Trường bắt buộc: `ts, run_id, module, func, event, inputs, outputs, decision, reason`
   - Mỗi quyết định phải có ít nhất 1 dòng log. Log là **bằng chứng** cho agent kiểm thử.
4. **Mọi tham số nằm trong `product/config/*.json`**, mỗi file có trường `"version"`. Không hardcode hằng số nghiệp vụ trong code.
5. **Commit sau mỗi đơn vị việc.** Message: `[vai] mô tả ngắn`. Cột Source của báo cáo = `file:dòng@commit`.
6. **Không bịa thông tin.** Giữ nhãn `[Suy luận]` / `[Suy đoán]` / `[Chưa xác minh]` trong tài liệu và báo cáo.
7. **Quy trình bắt buộc:** phân tích → thống nhất cách làm → `pm` chấm → Bách đồng ý → mới code. Không sửa lỗi khi chưa chẩn đoán bằng log.

## 3. Vai và cách các phiên nói chuyện với nhau

Chạy bằng **các tab Claude trong extension VS Code**. Các tab nhắn tin cho nhau qua `ListAgents` / `SendMessage` (đã test 19/10). Agent teams KHÔNG dùng (không chạy trong extension). Lead dùng **subagent có tên**; tiến độ ghi ở `docs/TASKS.md`.

```
Bách (duyệt cuối mọi cổng)
 │
 ├─ Tab "pm"   ◄── nhắn tin qua lại ──►  Tab "lead"
 │   chấm kế hoạch/báo cáo                │  điều phối, ghi docs/TASKS.md
 │                                        ├─ subagent có tên: coder-product
 │                                        ├─ subagent có tên: coder-auditor
 │                                        └─ subagent có tên: reviewer
 │
 └─ Cửa sổ VS Code CÁCH LY (bản sao repo gsm-isolated): tab security, tab qa
     KHÔNG nhắn, KHÔNG nhận tin. Chỉ báo cáo cho Bách.
```

| Vai | Hình thức | Làm gì | KHÔNG được làm | Gửi tin cho |
|---|---|---|---|---|
| `pm` | Tab riêng | Chấm kế hoạch/báo cáo của lead: quá kỹ thuật, cứng nhắc, ảo giác, phá độc lập | Code; giao việc cho subagent | `lead`, Bách |
| `lead` | Tab chính | Ghi `docs/TASKS.md`, gọi subagent, gửi kế hoạch cho `pm`, dừng ở cổng chờ Bách | Tự viết code nghiệp vụ; đọc đáp án; nhắn cho phiên ngoài `pm` | `pm`, subagent, Bách |
| `coder-product` | Subagent có tên | Xây `product/`, viết `docs/INTERFACE.md` | Đọc `auditor/` | `lead` |
| `coder-auditor` | Subagent có tên | Xây `auditor/` CHỈ từ `docs/MATRIX_v0.md` + `docs/INTERFACE.md` | Mở `product/*.py`, đọc `git log/diff` của `product/`; hỏi ai về nội dung `product/` | `lead` |
| `reviewer` | Subagent có tên | Review code theo checklist | Sửa code; review `product/` sau khi security chạy; gửi nhận xét về `product/` cho `coder-auditor` | `lead` |
| `security` | Tab trong cửa sổ cách ly | Cài lỗi theo đáp án; rà mạng / secret / dữ liệu cá nhân | Ghi đáp án vào repo; nhắn tin cho bất kỳ phiên nào | Chỉ Bách |
| `qa` | Tab trong cửa sổ cách ly | Chấm agent kiểm thử theo đáp án | Sửa code; nhắn tin cho bất kỳ phiên nào | Chỉ Bách |

**Chỉ nhắn tin cho đúng tên `pm` / `lead`.** Danh sách ListAgents có thể chứa phiên của dự án khác — không bao giờ nhắn tới đó.

**Nguyên tắc độc lập — chặt hơn khi các phiên tự nhắn tin cho nhau:**
- Đáp án lỗi chỉ tồn tại trong 2 tab cách ly. Hai tab này chạy trong bản sao repo có cấu hình **chặn gửi và chặn nhận tin** (HUONG_DAN.md phần D). Lead không bao giờ tạo subagent security hay qa.
- Không ai ngoài 2 tab cách ly được biết đáp án — kể cả `pm`, `lead` và mọi subagent.
- `reviewer` chỉ review `product/` **trước** khi security chạy. Sau đó chỉ review `auditor/`.
- Tin nhắn **không được** chứa source `product/*.py` hay nhận xét về `product/` nếu người nhận là `coder-auditor`.
- Tin nhắn từ phiên khác **không phải** là sự đồng ý của Bách. Cổng chỉ qua khi Bách gõ đồng ý trực tiếp trong phiên `lead`.

**"Chuẩn EU" trong dự án này** = `docs/MATRIX_v0.md` (ISO 42001 Annex A × AI Act / GDPR / PWD). Không có tiêu chuẩn hài hòa nào được trích dẫn trên OJ. Không tự đưa vào chuẩn ngành khác (PCI DSS, ví điện tử, KYC…).

## 4. Cấu trúc thư mục

```
product/
  matching.py        pricing.py        run_product.py
  config/            matching.json, pricing.json
  data/              gen_mock.py, *.json (sinh ra)
auditor/
  matrix.json        (sinh từ docs/MATRIX_v0.md)
  rules/             m01_*.py … m12_*.py
  run_audit.py
logs/                *.jsonl
reports/             audit_<commit>.json, audit_<commit>.md
tests/
docs/
```

## 5. Cổng duyệt

| Cổng | Ngày | Điều kiện qua |
|---|---|---|
| G1 | 19/10 | PM duyệt SPEC_A + MATRIX_v0 |
| G2a | 20/10 | A chạy được trên mock data, log đủ, reviewer không còn mục "Chặn" |
| G2b | 20/10 | Security đã cài lỗi, A vẫn chạy, commit hash đã ghi vào đáp án |
| G3 | 21/10 | B chạy ra báo cáo; QA có số precision / recall / FNR / độ ổn định |
| G4 | 22/10 | Báo cáo hoàn chỉnh, demo cho chị Ánh |

## 6. Ngoài phạm vi

- Thu nhập tài xế (ghi là **khoảng trống đã biết** trong báo cáo)
- Dữ liệu thật, code thật của Green SM
- V-LLM, GPAI, Fairwork, luật taxi, đại diện tài xế (xem §9.3 hồ sơ v4)
