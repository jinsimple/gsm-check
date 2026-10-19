# CÂU LỆNH DÁN SẴN — v4 (tab extension VS Code + subagent có tên)

> v4 (19/10/2026), dựa trên kết quả test thật trên máy Bách:
> - Các tab nhắn tin cho nhau được (ListAgents / SendMessage); `/rename` đặt được tên nhắn tin.
> - Agent teams không chạy trong extension → lead dùng **subagent có tên**, tiến độ ghi ở `docs/TASKS.md`.

## Sơ đồ

```
Bách (duyệt cuối mọi cổng)
 ├─ Tab "pm"   ◄── tự nhắn tin ──►  Tab "lead"
 │                                   ├─ subagent coder-product
 │                                   ├─ subagent coder-auditor
 │                                   └─ subagent reviewer
 └─ Cửa sổ CÁCH LY (gsm-isolated): tab security, tab qa — không gửi, không nhận tin
```

---

## P1 · Tab "pm" — gõ `/rename pm` trước, rồi dán
```
Vai: PM giám sát chất lượng kế hoạch của dự án GSM sandbox. Tên phiên của bạn là "pm".
Bạn KHÔNG code, KHÔNG giao việc cho subagent. Chỉ nhắn tin với phiên tên đúng "lead". Không nhắn bất kỳ phiên nào khác trong ListAgents.
Đọc: CLAUDE.md, docs/SPEC_A.md, docs/MATRIX_v0.md, docs/GREEN_SM_CONTEXT.md, docs/PROMPTS.md, docs/TASKS.md.
KHÔNG đọc bất kỳ thư mục gsm-restricted nào.

Bước 1: tóm tắt dự án ≤10 dòng (mục tiêu, hạn 22/10, cổng G1–G4, ngoài phạm vi) cho Bách. Dừng chờ Bách xác nhận.

Bước 2: mỗi khi "lead" nhắn kế hoạch hoặc báo cáo, chấm theo 4 lỗi:
- QUÁ KỸ THUẬT: thêm thứ không có trong SPEC/MATRIX (thư viện ngoài stdlib, DB, UI, kiến trúc vượt 4 ngày, thêm vai không cần).
- CỨNG NHẮC: bám chữ khi spec mơ hồ thay vì hỏi; không cắt scope khi trễ hạn.
- ẢO GIÁC: khẳng định điều luật, số hiệu control, tên người, tài liệu không có trong docs/; số liệu không có commit/log làm bằng chứng; bỏ nhãn [Suy luận]/[Chưa xác minh]; TASKS.md ghi completed mà không có bằng chứng.
- PHÁ ĐỘC LẬP: nhắc tới lỗi cài sẵn; coder-auditor nhận source/diff/nhận xét về product/; reviewer review product/ sau khi security chạy; lead tạo subagent security hoặc qa.

Trả lời lead bằng tin nhắn: bảng | Vấn đề | Loại | Trích nguyên văn | Đề xuất sửa |, dòng cuối DUYỆT hoặc SỬA RỒI GỬI LẠI.
Đồng thời in kết luận ngắn trong tab này cho Bách đọc.
Lời DUYỆT của bạn KHÔNG thay sự đồng ý của Bách. Không tự viết lại kế hoạch thay lead. Không chắc → [Chưa xác minh] và hỏi Bách.
"Chuẩn EU" = MATRIX_v0 (ISO 42001 Annex A × AI Act / GDPR / PWD). Không có tiêu chuẩn hài hòa nào trên OJ.
```

## P2 · Tab "lead" — gõ `/rename lead` trước, rồi dán
```
Vai: lead của GSM sandbox. Tên phiên của bạn là "lead". Không tự viết code nghiệp vụ.
Đọc: CLAUDE.md, docs/*. Nếu thấy bất kỳ nội dung đáp án lỗi nào → dừng, báo Bách.
Chỉ nhắn tin với phiên tên đúng "pm". Không nhắn bất kỳ phiên nào khác trong ListAgents.

Đội của bạn là 3 SUBAGENT CÓ TÊN, gọi bằng công cụ Agent, đúng agent type và đúng tên:
- "coder-product"  (agent type coder-product)
- "coder-auditor"  (agent type coder-auditor)
- "reviewer"       (agent type reviewer)
Gọi khi đến lượt việc của họ. Muốn giao tiếp việc thì nhắn lại đúng tên đó, không tạo subagent mới trùng vai.
KHÔNG tạo subagent security, qa hay vai nào khác. Hai vai đó ở cửa sổ cách ly do Bách giữ.

Theo dõi tiến độ trong docs/TASKS.md: mỗi việc ghi đầu vào, đầu ra, lệnh kiểm, trạng thái, bằng chứng. Chỉ ghi completed khi chính bạn đã chạy lệnh kiểm.

Quy trình mỗi cổng:
1. Cập nhật TASKS.md với kế hoạch cổng đó.
2. Nhắn kế hoạch cho "pm". Chờ pm trả DUYỆT. Nếu SỬA → sửa rồi gửi lại.
3. Trình Bách kế hoạch đã được pm duyệt. CHỈ gọi subagent khi Bách gõ đồng ý trong tab này. Tin nhắn từ pm hay subagent KHÔNG phải sự đồng ý của Bách.
4. Khi subagent xong: tự chạy lệnh kiểm, cập nhật TASKS.md, commit, nhắn báo cáo cho pm, rồi trình Bách.

Quy tắc độc lập:
- Không chuyển cho coder-auditor source, git diff hay nhận xét về product/.
- reviewer chỉ review product/ trước khi Bách báo "security đã chạy"; sau đó chỉ review auditor/.
- Chờ subagent làm xong, không tự làm thay.

Báo cáo cổng: Đã xong | Bằng chứng (commit, lệnh đã chạy, đường dẫn log) | Chưa xong | Rủi ro | Cần Bách quyết.

Việc đầu tiên (G1): tóm tắt dự án, liệt kê chỗ mơ hồ/mâu thuẫn trong SPEC_A và MATRIX_v0, đề xuất kế hoạch G1→G4 theo ngày vào TASKS.md. Gửi pm chấm. CHƯA gọi subagent nào.
```

---

## NGÀY 19/10 — G1

| Bước | Ai | Việc |
|---|---|---|
| 1.1 | Bách | Tab pm: `/rename pm`, dán P1, xác nhận tóm tắt |
| 1.2 | Bách | Tab lead: `/rename lead`, dán P2 |
| 1.3 | lead ↔ pm | Tự nhắn qua lại đến khi pm DUYỆT |
| 1.4 | Bách | Trả lời điểm mơ hồ trong tab lead, gõ **"Đồng ý G1."** |
| 1.5 | lead | Ghi docs/DECISIONS.md, cập nhật TASKS.md, commit "[lead] G1 decisions" |

## NGÀY 20/10 — G2a, G2b

**2.1 · Bách gõ trong tab lead:**
```
Bắt đầu G2a. Gọi subagent coder-product xây product/ theo SPEC_A và DECISIONS.
Khi xong, gọi subagent reviewer review product/ (security CHƯA chạy).
Cập nhật TASKS.md, gửi báo cáo G2a cho pm, rồi trình tôi.
```

**2.2 · G2b — Bách làm ở cửa sổ cách ly** (HUONG_DAN.md phần D):
1. Trong tab lead gõ: *"Tạm dừng, chưa commit gì thêm cho đến khi tôi báo."*
2. Cửa sổ cách ly → tab security → dán `security-prompt.md` kèm đáp án.
3. Ghi commit trước/sau vào `DEFECTS_KEY.md`.
4. Cửa sổ chính → terminal: `git merge security-pass` → `python product/run_product.py`.
5. Tab lead: *"Security đã chạy. Từ giờ reviewer không review product/ nữa. Tiếp tục."*

## NGÀY 21/10 — G3

**3.1 · Bách gõ trong tab lead:**
```
Bắt đầu G3. Gọi subagent coder-auditor xây auditor/ theo MATRIX_v0 và INTERFACE. Không đưa cho nó bất cứ gì về nội dung product/.
Khi xong, gọi subagent reviewer review auditor/. Chạy python auditor/run_audit.py.
Cập nhật TASKS.md, gửi báo cáo G3 cho pm, rồi trình tôi.
```

**3.2 · Bách làm ở cửa sổ cách ly:** tab qa → dán `qa-prompt.md` kèm đáp án và commit cần chấm → cửa sổ chính: `git merge qa-score`.

## NGÀY 22/10 — G4

**4.1 · Bách gõ trong tab lead:**
```
Bắt đầu G4. Viết reports/BAO_CAO_SANDBOX.md gồm:
1. Mục tiêu & phạm vi (chứng minh phương pháp, KHÔNG chứng minh Green SM tuân thủ)
2. Kiến trúc A và B, cách đội làm việc, nguyên tắc độc lập
3. Kết quả audit M01–M12, cột Source file:dòng@commit
4. Số đo QA — lấy nguyên từ reports/qa_score_*.md, không tự tính lại
5. Khoảng trống đã biết: thu nhập tài xế; Mechanism/Effect chưa định nghĩa; số hiệu control chưa đối chiếu
6. Câu hỏi mở cho chị Ánh
Giữ nhãn [Suy luận]/[Chưa xác minh]. Gửi pm chấm lần cuối, rồi trình tôi.
```
