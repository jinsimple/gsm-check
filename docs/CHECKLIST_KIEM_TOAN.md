# CHECKLIST KIỂM TOÁN THUẬT TOÁN & KIỂM TOÁN PHÁP LÝ — GSM

> **[Suy luận] — nhãn áp cho toàn bộ tài liệu.** Do phiên Claude soạn ngày 19/10/2026, không phải tư vấn pháp lý, không phải ý kiến của chuyên gia ISO hay luật sư.
> Bối cảnh: **chị Ánh không cung cấp thêm thông tin nào.** Mọi điểm trước đây ghi "hỏi chị Ánh" được nhóm tự nghiên cứu và tự chốt ở §7, kèm giả định và rủi ro.
> Dùng cho: (1) báo cáo G4 của sandbox; (2) backlog mở rộng MATRIX sau 22/10. **Không** dùng để sửa MATRIX_v0 trước khi B được đóng băng (Q21).

---

## §0. Cách đọc

| Cột | Nghĩa |
|---|---|
| **Kiểm bằng** | `MÁY` = agent kiểm thử kiểm được tự động · `NGƯỜI` = cần người đọc hồ sơ · `NGOÀI` = ngoài phạm vi sandbox, chỉ áp cho sản phẩm thật |
| **Đối tượng** | `A` = matching/pricing (hệ thống bị kiểm định) · `B` = AI Agent kiểm định (công cụ kiểm định) — tách theo §2.3 hồ sơ v4 |
| **M##** | Dòng tương ứng trong `MATRIX_v0.md`, nếu có |

**Độ tin cậy của số hiệu control ISO/IEC 42001.** Danh sách 38 control ở §2 khớp giữa **3 nguồn thứ cấp độc lập** (cyberzoni, blckalpaca, aviso/cyberday). Nhiều trang khác trên mạng đưa ra danh sách **sai hoàn toàn** — 11, 22 hoặc 37 control với số hiệu khác. Vì vậy vẫn giữ nhãn **[Chưa xác minh với bản chuẩn có bản quyền]**. Mức tin cậy hiện tại: cao về số hiệu, trung bình về câu chữ tiêu đề.

---

## §1. Bối cảnh áp dụng — tự chốt

| Điểm | Chốt | Căn cứ |
|---|---|---|
| Thị trường EU | **Đan Mạch** (ra mắt chính thức tại Copenhagen 30/07/2026) **+ Hà Lan** (vận hành thử từ 25/09/2026) | Tin chính thức của Green SM |
| Mô hình vận hành ở Đan Mạch | Green SM tự sở hữu và quản lý đội xe, dịch vụ taxi | Tin chính thức của Green SM |
| Matching / pricing tài xế | Có khả năng thuộc Phụ lục III điểm 4(b) Đạo luật AI | Hồ sơ v4 §4.2 |
| Pricing giá khách | Không thuộc Phụ lục III; chịu luật tiêu dùng | Hồ sơ v4 §4.2 |
| AI Agent kiểm định (B) | Công cụ nội bộ, không ra quyết định về người → không thuộc nhóm rủi ro cao | Hồ sơ v4 §2.3 |
| Hạn nghĩa vụ Phụ lục III | 02/12/2027 (Omnibus đã có hiệu lực từ 27/07/2026) | Hồ sơ v4; CMS |
| Chỉ thị Lao động Nền tảng (PWD) | Hạn nội luật hóa 02/12/2026. Hà Lan mới có dự thảo (tham vấn đến 24/08/2026) | Hồ sơ v4; Global Workplace Insider |

**Điểm mới cần ghi vào báo cáo:**
- **PWD có áp dụng cho Green SM không là câu hỏi mở thật.** PWD nhắm tới "nền tảng lao động số". Green SM ở Đan Mạch là hãng taxi tự sở hữu xe. Việc mô hình này có rơi vào định nghĩa của PWD hay không thì **[Chưa xác minh]**. Ngược lại, Phụ lục III điểm 4 Đạo luật AI áp dụng cho quan hệ lao động **bất kể** có phải nền tảng hay không. Vì vậy checklist dùng Đạo luật AI làm trục chính, PWD làm lớp bổ sung.
- **Đính chính nhỏ cho hồ sơ v4 §4.1:** v4 ghi Điều 50 "không đổi". Theo CMS, Omnibus có gia hạn một phần Điều 50 cho hệ thống AI tạo sinh. Dự án không dùng AI tạo sinh nên không ảnh hưởng, nhưng câu "không đổi" chưa chính xác.

---

## §2. ISO/IEC 42001 — khung dùng cho kiểm toán

### 2.1 Điều khoản 4–10 cần cho kiểm toán

| Điều khoản | Tên | Dùng để kiểm gì |
|---|---|---|
| 4.3 | Xác định phạm vi AIMS | Phạm vi audit có ghi rõ A, B, thị trường nào không |
| 6.1.2 / 8.2 | Đánh giá rủi ro AI | Có danh mục rủi ro cho A và B không |
| 6.1.3 / 8.3 | Xử lý rủi ro AI | Có chọn control, đối chiếu Annex A, và lập Tuyên bố áp dụng (SoA) không |
| 6.1.4 / 8.4 | Đánh giá tác động hệ thống AI | Tác động lên cá nhân, nhóm, xã hội, gồm cả khả năng dùng sai |
| 7.5 | Thông tin dạng văn bản | Có kiểm soát phiên bản tài liệu và bằng chứng không |
| 9.1 | Theo dõi, đo lường | Chỉ số của A (công bằng) và của B (precision, recall) |
| 9.2 | Đánh giá nội bộ | **Chính là việc dự án này đang làm** |
| 10.2 | Sự không phù hợp, hành động khắc phục | Phát hiện KHÔNG ĐẠT dẫn tới việc gì |

### 2.2 38 control Annex A — mức liên quan

`●` trọng tâm · `○` liên quan một phần · `—` ít liên quan. Cột **15★** đánh dấu 15 control trọng tâm cho kiểm toán thuật toán.

| Control | Tên | A | B | 15★ |
|---|---|---|---|---|
| A.2.2 | AI policy | ○ | ○ | |
| A.2.3 | Alignment with other organizational policies | — | — | |
| A.2.4 | Review of the AI policy | — | — | |
| A.3.2 | AI roles and responsibilities | ○ | ● | |
| A.3.3 | Reporting of concerns | ○ | ○ | |
| A.4.2 | Resource documentation | ○ | ○ | |
| A.4.3 | Data resources | ○ | ○ | |
| A.4.4 | Tooling resources | — | ○ | |
| A.4.5 | System and computing resources | — | — | |
| A.4.6 | Human resources | — | ○ | |
| A.5.2 | AI system impact assessment process | ● | ○ | ★ |
| A.5.3 | Documentation of AI system impact assessments | ● | ○ | ★ |
| A.5.4 | Assessing AI system impact on individuals or groups of individuals | ● | — | ★ |
| A.5.5 | Assessing societal impacts of AI systems | ○ | — | |
| A.6.1.2 | Objectives for responsible development of AI system | ○ | ○ | |
| A.6.1.3 | Processes for responsible AI system design and development | ○ | ○ | |
| A.6.2.2 | AI system requirements and specification | ● | ● | ★ |
| A.6.2.3 | Documentation of AI system design and development | ● | ● | ★ |
| A.6.2.4 | AI system verification and validation | ● | ● | ★ |
| A.6.2.5 | AI system deployment | ○ | ○ | |
| A.6.2.6 | AI system operation and monitoring | ● | ● | ★ |
| A.6.2.7 | AI system technical documentation | ● | ● | ★ |
| A.6.2.8 | AI system recording of event logs | ● | ● | ★ |
| A.7.2 | Data for development and enhancement of AI system | ○ | ○ | |
| A.7.3 | Acquisition of data | ○ | — | |
| A.7.4 | Quality of data for AI systems | ● | ● | ★ |
| A.7.5 | Data provenance | ● | ○ | ★ |
| A.7.6 | Data preparation | ● | ○ | ★ |
| A.8.2 | System documentation and information for users | ● | ○ | ★ |
| A.8.3 | External reporting | ○ | — | |
| A.8.4 | Communication of incidents | ○ | — | |
| A.8.5 | Information for interested parties | ○ | — | |
| A.9.2 | Processes for responsible use of AI systems | ● | ○ | |
| A.9.3 | Objectives for responsible use of AI system | ○ | ○ | |
| A.9.4 | Intended use of the AI system | ● | ● | ★ |
| A.10.2 | Allocating responsibilities | ● | ● | ★ |
| A.10.3 | Suppliers | ○ | ○ | |
| A.10.4 | Customers | ○ | ○ | |

**Ghi chú về 15★:** A.9.2 không nằm trong 15★ dù đang được dùng cho M07. Lý do: 15★ chọn theo độ phủ cho **kiểm toán thuật toán**, còn A.9.2 thiên về quy trình sử dụng. M07 vẫn giữ A.9.2. Nếu muốn 15★ khớp tuyệt đối với MATRIX, thay A.5.3 bằng A.9.2.

---

## §3. CHECKLIST KIỂM TOÁN THUẬT TOÁN

### 3A. Đối tượng A — matching và pricing

| ID | Câu hỏi kiểm | Bằng chứng cần | Kiểm bằng | ISO | Luật | M## |
|---|---|---|---|---|---|---|
| TA-01 | Mục đích sử dụng của từng tính năng đã được ghi rõ chưa? Matching (phân bổ việc), pricing tài xế, pricing khách có được tách thành dòng riêng không? | Đặc tả, phân loại theo §4.2 hồ sơ v4 | NGƯỜI | A.9.4, A.6.2.2 | AI Act PL III 4(b), Đ.6(3) | — |
| TA-02 | Tính năng có profiling không? Nếu có thì miễn trừ Đ.6(3) không dùng được | Danh sách đầu vào, có dữ liệu hành vi cá nhân hay không | NGƯỜI | A.5.4 | AI Act Đ.6(3); GDPR Đ.4(4) | — |
| TA-03 | Đầu vào chỉ dùng thuộc tính trong danh sách trắng? | Phân tích tĩnh mã nguồn so với danh sách trắng | MÁY | A.7.4, A.6.2.2 | PWD Đ.7 | M02 |
| TA-04 | Có thuộc tính đại diện (proxy) cho nhóm được bảo vệ không? | Đánh giá tương quan của từng đầu vào với nhóm | MÁY + NGƯỜI | A.7.4, A.5.4 | GDPR Đ.9; PWD Đ.7 | M02 |
| TA-05 | Kết quả có chênh lệch giữa các nhóm không: tỷ lệ được ghép, khoảng cách, thời gian chờ, giá? | Thống kê phân tầng theo nhóm, có ngưỡng | MÁY | A.5.4 | AI Act Đ.10(2)(f), Đ.15 | M01, M11 |
| TA-06 | Giá khách có phụ thuộc thuộc tính cá nhân ngoài quãng đường, thời điểm không? | Phân tích tĩnh + thống kê phân tầng | MÁY | A.5.4 | Luật tiêu dùng EU [Suy luận] | M11 |
| TA-07 | Mọi quyết định đều có log đủ trường không? | Đếm số quyết định so với số log; phân tích mọi nhánh `return` | MÁY | A.6.2.8 | AI Act Đ.12 | M04 |
| TA-08 | Mỗi quyết định có lý do đọc được không? | Trường `reason` trong log | MÁY | A.8.2 | PWD Đ.9; AI Act Đ.86 | M09 |
| TA-09 | Hành động bất lợi hoặc ràng buộc lên tài xế (khóa, phạt, hạ ưu tiên, tự động nhận chuyến) có bước con người xem xét thật không? | Cờ hoặc quy trình xem xét; **không chấp nhận bấm nút hình thức** | MÁY + NGƯỜI | A.9.2 | GDPR Đ.22; PWD Đ.10, 11; án Amsterdam 04/04/2023 | M07 |
| TA-10 | Có ngưỡng giám sát và cảnh báo khi vận hành không? | Cấu hình ngưỡng, kênh cảnh báo | MÁY | A.6.2.6 | AI Act Đ.72 | M12 |
| TA-11 | Cùng đầu vào chạy lại có ra cùng kết quả không? | Chạy lặp, so sánh sau khi bỏ trường thời gian và run_id | MÁY | A.6.2.4 | AI Act Đ.15 | M10 |
| TA-12 | Tham số nghiệp vụ nằm trong cấu hình có phiên bản, không viết cứng trong mã? | Phân tích tĩnh + cấu hình có `version` | MÁY | A.6.2.3, A.6.2.7 | AI Act Đ.11 | M05, M06 |
| TA-13 | Truy được từ quyết định về mã nguồn: file + dòng + commit? | Cột Source, manifest lần chạy | MÁY | A.6.2.7, A.6.2.3 | Án Amsterdam (bác lập luận bí mật kinh doanh) | M04–M06 |
| TA-14 | Dữ liệu kiểm thử phủ mọi nhánh quyết định không? | Báo cáo độ phủ nhánh | MÁY | A.7.6, A.6.2.4 | AI Act Đ.10(3) | (Q19) |
| TA-15 | Kiểm thử thiên lệch dùng dữ liệu tổng hợp, không dùng dữ liệu tài xế thật? | Nguồn gốc dữ liệu kiểm thử | NGƯỜI | A.7.5, A.7.3 | Xung đột AI Act Đ.4a và PWD Đ.7 — hồ sơ v4 §3.5(c) | M03 |
| TA-16 | Có đánh giá tác động trước khi triển khai không? | Hồ sơ DPIA hoặc đánh giá tác động | NGƯỜI | A.5.2, A.5.3 | GDPR Đ.35; PWD Đ.8 | M08 |
| TA-17 | Biên và ngoại lệ được xử lý đúng không: không có tài xế, chuyến rất xa, đầu vào lỗi? | Kiểm thử biên có log | MÁY | A.6.2.4 | AI Act Đ.15 | — |
| TA-18 | Mỗi khi đổi cấu hình hay mô hình thì có kiểm định lại không? | Quy trình quản lý thay đổi, lịch sử kiểm định | NGƯỜI | A.6.2.5, 6.3 | AI Act Đ.43(4) | — |
| TA-19 | Thu nhập tài xế có được kiểm định không? | — | NGOÀI | A.5.4 | AI Act PL III 4(b) | **Khoảng trống đã biết** |

### 3B. Đối tượng B — AI Agent kiểm định ("kiểm định người kiểm định")

| ID | Câu hỏi kiểm | Bằng chứng cần | Ngưỡng đề xuất [Suy luận] | ISO |
|---|---|---|---|---|
| TB-01 | **Recall**: B bắt được bao nhiêu % lỗi đã biết? | Điểm chấm của qa, theo chênh lệch C0→C1 | ≥ 80% lỗi đã biết | A.6.2.4 |
| TB-02 | **Tỷ lệ bỏ lọt (FNR)**: bao nhiêu % lỗi bị gán nhầm là an toàn? | Điểm chấm của qa | ≤ 20%. **Chỉ số sống còn** — đây là loại lỗi gây hậu quả pháp lý | A.6.2.4 |
| TB-03 | **Precision**: trong các phát hiện mới, bao nhiêu % là đúng? | Điểm chấm của qa | Chấp nhận thấp hơn recall (ngưỡng bất đối xứng, hồ sơ v4 §6.2) | A.6.2.4 |
| TB-04 | **Độ ổn định**: chạy 3 lần trên cùng commit có ra cùng kết quả? | So sánh 3 file JSON | 100% giống nhau | A.6.2.4 |
| TB-05 | **Tỷ lệ truy được nguồn**: bao nhiêu % phát hiện có file:dòng@commit? | Đếm trong báo cáo audit | 100%; phát hiện về sự vắng mặt phải có phạm vi quét đầy đủ (Q17) | A.6.2.7, A.6.2.8 |
| TB-06 | **Độc lập**: người xây B có thấy đáp án hay mã nguồn A không? | Quy tắc vai, lịch sử tin nhắn, file vai coder-auditor | Không | A.3.2 |
| TB-07 | **Đóng băng**: B có bị chỉnh sau khi thấy kết quả trên A có lỗi không? | Tag `b-freeze`, lịch sử commit `auditor/` | Không có commit nào sau b-freeze mà không báo | A.6.2.5 |
| TB-08 | **Nguồn gốc bộ quy tắc**: mỗi quy tắc trong MATRIX có căn cứ luật và căn cứ ISO không? | MATRIX_v0, cột căn cứ | 100% | A.6.2.2, A.7.5 |
| TB-09 | **Bộ quy tắc pháp lý được người có chuyên môn pháp lý duyệt chưa?** | Chữ ký Legal/DPO | Trong sandbox: **CHƯA** — ghi rõ là giới hạn. Hồ sơ v4 §6.1 xếp đây là phụ thuộc số 1 | A.10.2 |
| TB-10 | B có tự ghi log từng bước kiểm không, và log đó được commit? | `reports/audit_*.log.jsonl` | Có | A.6.2.8 |
| TB-11 | Phạm vi dùng B có được ghi rõ không: B chỉ đề xuất, Legal/DPO quyết? | Tài liệu vai trò | Có — nếu không, chữ ký Legal/DPO thành hình thức (rủi ro R1 hồ sơ v4) | A.9.4, A.10.2 |
| TB-12 | Mỗi lần đổi MATRIX có chạy lại toàn bộ bộ đo TB-01→TB-05 không? | Lịch sử chạy | Có | A.6.2.4, 10.2 |

---

## §4. CHECKLIST KIỂM TOÁN PHÁP LÝ

Cột **Ai chịu** theo hồ sơ v4 §2.1: nghĩa vụ chủ yếu thuộc **Green SM**; VSF là nhà cung cấp công cụ, trừ khi rơi vào Đ.25 Đạo luật AI.

### 4A. Đạo luật AI — Regulation (EU) 2024/1689, đã sửa bởi Omnibus

| ID | Câu hỏi kiểm | Căn cứ | Ai chịu | Trạng thái sandbox |
|---|---|---|---|---|
| PL-01 | Matching/pricing tài xế đã được phân loại rủi ro chính thức, có văn bản chưa? | PL III 4(b); Đ.6(3)–(4) | Green SM | NGƯỜI |
| PL-02 | Pháp nhân nào là provider? Có cần đại diện được ủy quyền tại EU không? | Đ.3(3), Đ.22 | Green SM / Legal | NGOÀI — câu hỏi §7 hồ sơ v4 |
| PL-03 | Tinh chỉnh theo vùng có làm VSF trở thành provider không? Đã có thỏa thuận bằng văn bản theo Đ.25(4) chưa? | Đ.25 | VSF + Green SM | NGOÀI |
| PL-04 | Có hệ thống quản lý rủi ro suốt vòng đời không? | Đ.9 | Provider | NGƯỜI |
| PL-05 | Dữ liệu huấn luyện/kiểm thử có quản trị: kiểm thiên lệch, đại diện, nguồn gốc? | Đ.10 | Provider | MÁY một phần (TA-04, TA-05, TA-15) |
| PL-06 | Có tài liệu kỹ thuật theo Phụ lục IV không? | Đ.11 | Provider | NGƯỜI |
| PL-07 | Hệ thống tự động ghi log sự kiện? | Đ.12 | Provider | MÁY (TA-07) |
| PL-08 | Có thông tin minh bạch cho bên triển khai không? | Đ.13 | Provider | NGƯỜI |
| PL-09 | Giám sát của con người được thiết kế thật, không hình thức? | Đ.14 | Provider + deployer | MÁY + NGƯỜI (TA-09) |
| PL-10 | Có đo độ chính xác, độ bền, an ninh mạng không? | Đ.15 | Provider | MÁY một phần (TA-11, TA-17) |
| PL-11 | Có QMS theo Đ.17 không? Lưu ý: ISO 42001 **không** thay được Đ.17; chuẩn tương ứng là prEN 18286 (dự thảo) | Đ.17; hồ sơ v4 §8.1 | Provider | NGƯỜI |
| PL-12 | Đã thông báo cho đại diện người lao động và người lao động bị ảnh hưởng trước khi đưa hệ thống rủi ro cao vào nơi làm việc chưa? | Đ.26(7) | Green SM (deployer) | NGOÀI |
| PL-13 | Có theo dõi sau khi đưa ra thị trường và quy trình báo cáo sự cố nghiêm trọng không? | Đ.72, Đ.73 | Provider | MÁY một phần (TA-10) |
| PL-14 | Người bị ảnh hưởng có quyền được giải thích quyết định không? | Đ.86 | Deployer | MÁY một phần (TA-08) |
| PL-15 | Đánh giá sự phù hợp là tự đánh giá nội bộ (không thuộc nhánh sinh trắc, không thuộc PL I)? | Đ.43; hồ sơ v4 §4.1 | Provider | NGƯỜI |
| PL-16 | Lộ trình đáp ứng trước 02/12/2027 đã có chưa? | Omnibus | Green SM | NGƯỜI |

### 4B. GDPR — Regulation (EU) 2016/679

| ID | Câu hỏi kiểm | Căn cứ | Trạng thái sandbox |
|---|---|---|---|
| PL-20 | Xử lý dữ liệu tài xế EU từ Việt Nam: có áp dụng ngoài lãnh thổ? Có cần đại diện theo Đ.27 không? | Đ.3(2), Đ.27 | NGOÀI |
| PL-21 | Căn cứ pháp lý cho từng mục đích xử lý? | Đ.6 | NGƯỜI |
| PL-22 | Có dữ liệu thuộc nhóm đặc biệt, hoặc thuộc tính suy ra được dữ liệu đặc biệt không? | Đ.9 | MÁY một phần (TA-04) |
| PL-23 | Có thông tin cho chủ thể về logic của quyết định tự động không? | Đ.13(2)(f), Đ.14(2)(g), Đ.15(1)(h) | NGƯỜI |
| PL-24 | Quyết định "chỉ dựa trên tự động" có tác động đáng kể không? Có con người can thiệp **thật** không? | Đ.22; án Amsterdam 04/04/2023 | MÁY + NGƯỜI (TA-09) |
| PL-25 | Có bảo vệ dữ liệu từ thiết kế: tối thiểu hóa đầu vào? | Đ.25; Đ.5(1)(c) | MÁY (TA-03) |
| PL-26 | Đã có DPIA cho matching/pricing chưa? | Đ.35 | NGƯỜI (TA-16) |
| PL-27 | Chuyển dữ liệu EU → Việt Nam dùng công cụ gì? Việt Nam không có quyết định đầy đủ (adequacy) → cần SCC + đánh giá tác động chuyển dữ liệu | Đ.44–49 | NGOÀI |

### 4C. Chỉ thị Lao động Nền tảng — Directive (EU) 2024/2831

**Điều kiện tiên quyết PL-30:** Green SM ở Đan Mạch và Hà Lan có phải "nền tảng lao động số" theo PWD không? **[Chưa xác minh]** Nếu không, các dòng PL-31 → PL-35 chỉ là thông lệ tốt; nghĩa vụ chính vẫn đến từ Đạo luật AI và GDPR.

| ID | Câu hỏi kiểm | Căn cứ | Trạng thái sandbox |
|---|---|---|---|
| PL-31 | Có xử lý loại dữ liệu bị cấm không: trạng thái cảm xúc, trao đổi riêng tư, dự đoán việc tham gia công đoàn, suy ra nguồn gốc chủng tộc…? | Đ.7(1), 7(3) | MÁY một phần (TA-03, TA-04) |
| PL-32 | Có đánh giá tác động riêng cho hệ thống ra quyết định tự động không? | Đ.8 | NGƯỜI |
| PL-33 | Người lao động có được thông tin về hệ thống giám sát và ra quyết định tự động không? | Đ.9 | MÁY một phần (TA-08) |
| PL-34 | Có giám sát của con người, đánh giá định kỳ, và quyết định về tài khoản do con người ra không? | Đ.10 | MÁY + NGƯỜI (TA-09) |
| PL-35 | Người lao động có quyền yêu cầu con người xem xét lại quyết định không? | Đ.11 | NGƯỜI |
| PL-36 | Tình trạng nội luật hóa: Đan Mạch? Hà Lan (dự thảo, tham vấn đến 24/08/2026)? | Điều khoản chuyển hóa của PWD, hạn 02/12/2026 (số điều [Chưa xác minh]) | NGƯỜI — theo dõi |

### 4D. Lớp quốc gia — chỉ Đan Mạch và Hà Lan

| ID | Câu hỏi kiểm | Căn cứ |
|---|---|---|
| PL-40 | Đan Mạch: cơ quan có thẩm quyền theo Luật 467/2025 (Digitaliseringsstyrelsen, Datatilsynet). Chế tài tài chính mang tính hình sự, Datatilsynet không tự phạt được mà phải qua cảnh sát và tòa án | Hồ sơ v4 §4.4 |
| PL-41 | Hà Lan: cơ quan bảo vệ dữ liệu (AP) đã phạt Uber về chuyển dữ liệu và về vô hiệu hóa tài khoản tự động. **Hà Lan là thị trường có án lệ nặng nhất** cho đúng loại rủi ro của dự án | Hồ sơ v4 §5 |

Năm thị trường còn lại (Việt Nam, Kazakhstan, Indonesia, Ấn Độ, Philippines, Lào): dùng nguyên §4.4 hồ sơ v4, không lặp lại ở đây.

---

## §5. Ánh xạ với MATRIX_v0 và backlog

| MATRIX | Mục checklist tương ứng |
|---|---|
| M01 | TA-05 |
| M02 | TA-03, TA-04 |
| M03 | TA-15 |
| M04 | TA-07 |
| M05, M06 | TA-12 |
| M07 | TA-09 |
| M08 | TA-16 |
| M09 | TA-08 |
| M10 | TA-11 |
| M11 | TA-06 |
| M12 | TA-10 |

**Mục MÁY chưa có dòng MATRIX — backlog sau 22/10, KHÔNG thêm trước b-freeze:**
- TA-13: truy nguồn file + commit cho từng quyết định (hiện mới kiểm gián tiếp)
- TA-14: độ phủ nhánh
- TA-17: kiểm biên và ngoại lệ
- TB-08: mỗi dòng MATRIX có căn cứ

**Control ★ chưa có dòng MATRIX:** A.5.3, A.6.2.2, A.7.6, A.8.2 (đã gián tiếp qua M09), A.9.4, A.10.2.

---

## §6. Taxonomy Mechanism / Effect và Minimal / Mitigation — tự định nghĩa

> **[Suy luận]** Vì không có định nghĩa nội bộ, nhóm tự đặt để báo cáo G4 có nội dung. **Không liên quan** tới bốn mức rủi ro của Đạo luật AI. Chữ "minimal" chỉ trùng ngẫu nhiên.

**Mechanism — tính năng tác động bằng cơ chế nào:**

| Mã | Nghĩa |
|---|---|
| MEC-ALLOC | Phân bổ việc (ghép chuyến) |
| MEC-PRICE | Định giá |
| MEC-PROFILE | Dùng hồ sơ hoặc hành vi cá nhân (ví dụ tỷ lệ nhận chuyến) |
| MEC-ENFORCE | Thực thi bất lợi hoặc ràng buộc (khóa, phạt, ép nhận chuyến) |
| MEC-INFO | Chỉ tính toán hoặc hiển thị, không tác động trực tiếp lên người |

**Effect — tác động lên ai, lên gì:**

| Mã | Nghĩa |
|---|---|
| EFF-INCOME | Thu nhập tài xế |
| EFF-ACCESS | Quyền truy cập nền tảng của tài xế |
| EFF-AUTONOMY | Quyền tự quyết nhận hoặc từ chối việc |
| EFF-CONSUMER | Giá khách trả |
| EFF-DATA | Dữ liệu cá nhân |
| EFF-NONE | Không tác động lên người |

**Nhóm rủi ro thấp của milestone — định nghĩa đề xuất:**
- **Minimal:** `EFF-NONE` và không dùng `MEC-PROFILE` hay `MEC-ENFORCE`.
- **Mitigation:** có tác động lên người, nhưng mọi tác động đều có (a) log đủ, (b) lý do đọc được, (c) bước con người xem xét thật. Tức là TA-07, TA-08, TA-09 cùng ĐẠT.
- Còn lại: **ngoài nhóm rủi ro thấp**, không được xếp vào milestone 31/10.

---

## §7. Các điểm trước đây chờ chị Ánh — nay tự chốt

| Điểm | Chốt | Rủi ro nếu sai |
|---|---|---|
| Danh sách 15 control | 15★ ở §2.2 | Thấp — chỉnh được, không ảnh hưởng kết quả đo |
| Số hiệu control | Khớp 3 nguồn thứ cấp; giữ nhãn chưa đối chiếu bản chuẩn | Thấp |
| Mechanism / Effect | Taxonomy §6, **lead điền tay trong báo cáo G4**, không sửa B | Trung bình — có thể lệch taxonomy nội bộ thật |
| Minimal / Mitigation | Định nghĩa §6 | Trung bình |
| Thị trường EU | Đan Mạch + Hà Lan | Thấp — có nguồn chính thức |
| Legal/DPO nào ký duyệt | Giả định: **Legal/DPO của Green SM** (bên chịu nghĩa vụ, hồ sơ v4 §2.1) | Trung bình |
| Bộ quy tắc pháp lý đã được Legal duyệt? | **Chưa** — ghi thẳng là giới hạn lớn nhất của sandbox (TB-09) | Cao, nhưng đã khai báo |

---

## §8. Nguồn

- ISO/IEC 42001 — cấu trúc điều khoản và 38 control Annex A: [cyberzoni](https://cyberzoni.com/standards/iso-42001/); [blckalpaca](https://blckalpaca.at/en/knowledge-base/ai-agents/iso-42001-ai-management-system/annex-a-controls-iso-42001); [aviso consultancy](https://www.avisoconsultancy.co.uk/iso-42001-annex-a/06-2-8-ai-system-recording-of-event-logs); [cyberday A.10.4](https://www.cyberday.ai/requirement/iso-42001-a-10-4-customers)
- Điều khoản 6.1.3 / SoA / 6.1.4: [Modulos](https://docs.modulos.ai/frameworks/iso-42001/clauses-4-10.html); [Advisera](https://advisera.com/articles/iso-42001-clauses-requirements/)
- Green SM tại Đan Mạch: [Green SM DK](https://www.greensm.com/dk-en/news/green-sm-officially-launches-fully-electric-taxi-service-in-denmark)
- Green SM tại Hà Lan: [Green SM](https://www.greensm.com/vn-en/news/green-sm-van-hanh-thu-nghiem-tai-ha-lan-mo-rong-hien-dien-tai-chau-au)
- Digital Omnibus, mốc thời gian: [CMS](https://cms.law/en/gbr/publication/the-eu-s-digital-omnibus-streamlined-ai-act-compliance-rules-are-now-in-force)
- PWD tại Hà Lan: [Global Workplace Insider](https://www.globalworkplaceinsider.com/2026/09/the-platform-work-act-implementing-the-eu-platform-work-directive-in-the-netherlands/)
- Còn lại: hồ sơ v4 (`giam-sat-mo-rong-quoc-te-tong-hop-v4-ban-giao.md`) — chính là bản tổng hợp do phiên Claude soạn, xếp hạng tin cậy thấp nhất trong thứ tự nguồn của hồ sơ.
