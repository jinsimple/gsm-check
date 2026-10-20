# DECISIONS — chốt ở cổng G1

> Trạng thái file: **CHỐT 19/10/2026** cho G1. Bách đã trả lời cả 7 câu Phần 1 (Q13, Q01, Q02, Q05, Q14, Q12, Q15) và không phản đối 8 mặc định Phần 2.
> Q17 và Q18 đã chốt 19/10 theo kết luận G1 của Bách. **Không còn câu nào mở.**
> Bách kết luận: *"Sửa xong gửi pm chấm. Khi pm DUYỆT: Đồng ý G1."*
> Bách đồng ý G1 **có điều kiện**: *"Đồng ý G1 sau khi pm duyệt bản DECISIONS.md đã cập nhật."* → chưa có pm DUYỆT bản này thì cổng G1 chưa đóng.
> Gọi `coder-product` là việc của G2a, chờ Bách ra lệnh ngày 20/10.
> [Suy luận] Mọi đề xuất dưới đây là suy luận của lead từ SPEC_A + MATRIX_v0, không phải tư vấn pháp lý.
>
> **File này KHÔNG dành cho `coder-auditor`.** `coder-auditor` chỉ được mở `docs/MATRIX_v0.md` và `docs/INTERFACE.md` (CLAUDE.md §3).

## Tóm tắt dự án

Sandbox mô phỏng, hạn 22/10/2026. Hai nửa: **A** = sản phẩm mẫu gọi xe (`product/`: matching tài xế + pricing giá cước khách, Python stdlib, dữ liệu tổng hợp seed 42); **B** = agent kiểm thử (`auditor/`) tự động chấm A theo 12 dòng `docs/MATRIX_v0.md` (ISO/IEC 42001 Annex A x AI Act / GDPR / PWD). B chỉ được đọc `MATRIX_v0.md` + `INTERFACE.md`, không được xem trong `product/` — vì **khả năng tự phát hiện** của B mới là thứ đang được đo. Việc chấm năng lực của B do Bách thực hiện ở cửa sổ cách ly, lead và mọi subagent không tham gia. Kết quả chứng minh **phương pháp kiểm định**, KHÔNG chứng minh sản phẩm thật của Green SM tuân thủ. Ngoài phạm vi: thu nhập tài xế, dữ liệu thật, V-LLM / GPAI / Fairwork / luật taxi.

---

## Phần 1 — câu cần Bách quyết (không có mặc định an toàn)

### Q13 — Nguyên tắc chung: khoảng trống nào được vá, khoảng trống nào để KHÔNG ĐẠT?

MATRIX đòi một số thứ mà SPEC_A không có (tài liệu đánh giá tác động ở M08, ngưỡng cảnh báo ở M12, bước người xem xét ở M07). Chọn vá từng chỗ theo cảm nhận thì báo cáo G4 không giải thích được tại sao vá chỗ này mà không vá chỗ kia.

→ **Nguyên tắc lead đề xuất:** *A chỉ làm đúng những gì SPEC_A yêu cầu. Mọi thứ MATRIX đòi mà SPEC_A không có thì để nguyên, ra KHÔNG ĐẠT, và ghi vào báo cáo là khoảng trống đã biết.*

Hai lý do: (1) A đóng vai sản phẩm mẫu **chưa** tuân thủ đầy đủ — tìm ra chỗ chưa tuân thủ là việc của B, không phải việc của lead; (2) nếu lead vá từng chỗ theo MATRIX thì A và B bị lead đồng bộ ngầm với nhau, mất đúng thứ đang được đo.

**LOẠI TRỪ — đọc kỹ trước khi áp dụng nguyên tắc trên.** Ràng buộc cứng `CLAUDE.md §2` vẫn **bắt buộc tuyệt đối**, nguyên tắc Q13 không chạm tới:

1. Chỉ Python standard library, không `pip install`, Python ≥ 3.10.
2. Dữ liệu 100% tổng hợp, seed cố định 42.
3. Log JSONL đủ 9 trường (`ts, run_id, module, func, event, inputs, outputs, decision, reason`) cho **mọi** quyết định, mọi bước tính, mọi lý do loại.
4. Mọi tham số nghiệp vụ nằm trong `product/config/*.json`, mỗi file có trường `version`. Không hardcode hằng số nghiệp vụ.
5. Commit sau mỗi đơn vị việc; giữ nhãn `[Suy luận]` / `[Suy đoán]` / `[Chưa xác minh]`.

Q13 **chỉ** áp cho những gì MATRIX đòi mà **cả** SPEC_A **và** CLAUDE.md §2 đều không đòi. Ở G1 đó là đúng **ba dòng: M07, M08, M12** — không được suy rộng thêm dòng nào.

Nói rõ để không ai hiểu nhầm: M04 (log sự kiện), M05 (hằng số trong config), M06 (config có `version`) **không** thuộc diện Q13. Ba dòng đó phải ĐẠT. Bỏ log không phải là "làm đúng SPEC_A" mà là vi phạm ràng buộc cứng — và vì log là bằng chứng duy nhất cho B, mất log là mất cả G3, không chỉ mất mấy dòng ma trận.

**Bách CHỐT 19/10: đồng ý.** A chỉ làm đúng SPEC_A, không vá theo MATRIX. `CLAUDE.md §2` vẫn tuyệt đối.

**Thuật ngữ Bách yêu cầu dùng:** dòng nào ra KHÔNG ĐẠT vì A không có tính năng đó thì gọi là **"khoảng trống theo thiết kế sandbox"**. Báo cáo G4 phải ghi rõ đây **không phải nhận định về Green SM thật**.

Nguyên tắc này quyết luôn Q05, Q08, Q09 bên dưới.

### Q15 — Xin Bách sửa `.claude/agents/coder-auditor.md:7` (CHẶN T11, không chặn G1)

Dòng đó hiện ghi:

> `CHỈ đọc: CLAUDE.md, docs/MATRIX_v0.md, docs/INTERFACE.md, docs/DECISIONS.md.`

`docs/DECISIONS.md` **không được** nằm trong danh sách đó. File này chứa biên bậc giá (Q03), hệ số giờ (Q04), hàm thuần (Q06), định nghĩa quyết định và con số 2.000 (Q10), phạm vi log (Q12) — tức một phần kết quả mà `coder-auditor` phải tự tìm ra.

Ô cảnh báo lead viết ở `docs/TASKS.md` **không đủ sức bịt lỗ này**: subagent **tự nạp định nghĩa của chính nó**, còn `TASKS.md` lại đúng là file nó bị cấm mở. Hai nguồn trái nhau thì cái nó nạp sẵn thắng.

**Bách CHỐT 19/10: đồng ý sửa. ĐÃ SỬA** trong commit này. Dòng 7 giờ là `CHỈ đọc: CLAUDE.md, docs/MATRIX_v0.md, docs/INTERFACE.md.`, và `docs/DECISIONS.md`, `docs/TASKS.md`, `docs/SPEC_A.md`, `docs/GREEN_SM_CONTEXT.md`, `docs/PROMPTS.md` đã vào danh sách KHÔNG mở.

Lead chỉ sửa file cấu hình này **vì Bách chỉ thị trực tiếp**, không vì pm đề nghị. Rủi ro R8 đóng.

T10b vẫn giữ làm chốt cửa trước T11: đọc lại dòng 7 và xác nhận, phòng trường hợp file bị đổi lại.

→ Ghi nhận: dòng 8 cùng file có cụm "lỗi đã cài". pm và lead thống nhất **để nguyên** — không thể và không cần che việc *có* cài lỗi (CLAUDE.md §3 và §5 đã nói tới, mà mọi subagent đều tự nạp CLAUDE.md). Thứ phải giữ kín là **lỗi gì** và **dòng nào sẽ hỏng**, không phải việc có cài lỗi.

### Q17 — Bằng chứng cho phát hiện dạng VẮNG MẶT (CHẶN T11, không chặn G1)

Yêu cầu Q16 của Bách đã vào `docs/MATRIX_v0.md`. Nhưng nó chưa bao phủ loại phát hiện **"thứ cần có thì không có"**, và chỗ chưa bao phủ đó đụng trực tiếp vào Q08 + Q09 vừa chốt **cùng một commit**. pm phát hiện, lead xác nhận là có thật.

Hai câu đang kéo ngược nhau, trích nguyên văn:

> `MATRIX_v0.md:48` — *"Cột Bằng chứng là **danh sách** ... Dòng ra KHÔNG ĐẠT hoặc CẦN NGƯỜI XEM mà chỉ trỏ tên file, không trỏ dòng, thì coi là **chưa đủ bằng chứng**."*
>
> `MATRIX_v0.md:11` — *"**Nguyên tắc bất đối xứng:** nghi ngờ → CẦN NGƯỜI XEM. Không bao giờ tự cho ĐẠT khi thiếu bằng chứng."*

Ghép hai câu đó lại thì: M08 (*"không có tài liệu đánh giá tác động trong docs/"*, `MATRIX_v0.md:31`) và M12 (*"không có ngưỡng cảnh báo cho tỷ lệ auto_accept"*, `MATRIX_v0.md:35`) là phát hiện về **sự vắng mặt** — không có file nào, không có dòng nào để trỏ → thiếu bằng chứng → agent kiểm thử đẩy xuống **CẦN NGƯỜI XEM**.

Nhưng Q13 + Q08 + Q09 vừa chốt rằng đúng hai dòng đó phải ra **KHÔNG ĐẠT**, như **khoảng trống theo thiết kế sandbox**.

**Hệ quả thật nếu để nguyên:** báo cáo G4 không nói được điều Q13 muốn nói, và con số recall của qa đọc khác đi.

Lead ghi nhận hai dòng này **không giống nhau hoàn toàn**: M12 còn có chỗ để trỏ — `product/config/matching.json` tồn tại, agent có thể trỏ vào file đó và các dòng khoá hiện có để chứng minh không có khoá nào là ngưỡng cảnh báo. M08 thì **không có file nào cả**: thứ vắng mặt là chính tài liệu đó trong `docs/`.

→ **Cần Bách chọn:**

**(A)** Bổ sung vào phần Quy ước của `MATRIX_v0.md` một câu về bằng chứng vắng mặt: *phát hiện dạng vắng mặt thì bằng chứng là **phạm vi đã quét + phương pháp quét + dòng log của chính agent kiểm thử ghi lại kết quả quét***. Như vậy vẫn giữ được `file:dòng` đúng yêu cầu Q16 — chỉ là `file:dòng` trỏ vào log của agent kiểm thử, không trỏ vào thứ không tồn tại. M08 và M12 ra KHÔNG ĐẠT đúng như Q13 muốn.

**(B)** Để nguyên, chấp nhận M08 và M12 ra CẦN NGƯỜI XEM, và báo cáo G4 trình bày theo đúng kết quả đó.

**Lead nghiêng về (A)**, vì nó giữ được cả Q16 lẫn Q13 mà không phải nới câu nào, và vì "đã quét hết `docs/` bằng phương pháp này, không thấy" **là** một bằng chứng kiểm định thật, truy được, không phải sự thiếu vắng bằng chứng. [Suy luận]

Cả hai phương án đều dùng được. Điều không dùng được là để nó thành **tai nạn** thay vì **lựa chọn** — nguyên văn nhận xét của pm, lead đồng ý.

**Bách CHỐT 19/10: chọn (A). ĐÃ SỬA** trong commit này. Ba câu Bách yêu cầu đã vào **phần Quy ước** của `MATRIX_v0.md`:

1. Phát hiện dạng vắng mặt: bằng chứng = phạm vi đã quét (liệt kê đủ file / khoá) + phương pháp quét + dòng log của agent kiểm thử.
2. Chỉ được ra KHÔNG ĐẠT khi lần quét **đầy đủ**; quét lỗi hoặc không đủ phạm vi → CẦN NGƯỜI XEM.
3. Log của agent kiểm thử ghi vào `reports/audit_<commit>.log.jsonl` và **được commit**; `logs/*.jsonl` của sản phẩm vẫn ignore.

Bách chỉ định đặt vào **Quy ước**, nên lead đặt đúng chỗ đó — không dùng phương án cuối file mà lead đã nêu ở ghi chú kỹ thuật. Hệ quả lệch dòng đã được **hấp thụ ngay trong cùng commit**: 3 dòng chèn vào sau dòng 12 làm lệch +3 mọi dẫn chiếu từ dòng 13 trở đi; lead đã dịch lại toàn bộ và chạy lại kiểm chéo từng dẫn chiếu, kết quả 0 sai. Đây đúng là việc T01e đã dự trù.

`.gitignore` **không cần sửa**: mẫu loại trừ hiện tại chỉ là `logs/*.jsonl`, nên `reports/audit_<commit>.log.jsonl` vốn đã vào git được.

**Ghi nhận về chỗ chèn.** Lead có đề xuất chèn ở cuối file để lệch 0 dòng; Bách chỉ định phần Quy ước, lead làm theo Bách và hấp thụ phần lệch dòng bằng script kiểm chéo. Nếu sau này Bách muốn giữ dẫn chiếu ổn định hơn thì chuyển ba câu đó xuống cuối file được, nội dung không đổi.

### Q18 — Rà soát: quyết định nào ảnh hưởng B phải nằm trong MATRIX_v0 hoặc INTERFACE (chốt 19/10)

**Yêu cầu số 2 của Bách:** vì `coder-auditor` không đọc `DECISIONS.md`, mọi quyết định ảnh hưởng B phải có trong `MATRIX_v0.md` hoặc `INTERFACE.md`. Lead đã rà toàn bộ 18 câu.

**Đã bổ sung vào `MATRIX_v0.md`** (mục mới "Chi tiết quy tắc cho agent kiểm thử" ở cuối file):

| Từ câu | Thiếu gì trước đó | Nếu thiếu thì B sai thế nào |
|---|---|---|
| Q11 | M01 ghi "giữa các nhóm", phần ML ghi "theo nhóm tài xế" — hai nhóm khác nhau, không có ngưỡng rõ | M01 so sai nhóm hoặc tự đặt ngưỡng |
| Q11 | M11 không nói phải phân tầng theo bậc km | M11 báo động giả vì phân phối quãng đường hai segment vốn đã khác |
| Q07 | M10 không nói bỏ `ts` / `run_id` / đường dẫn log trước khi so | M10 **luôn** ra "kết quả khác nhau" → KHÔNG ĐẠT sai |
| Q10 | "một quyết định" không được định nghĩa ở file nào B đọc được | M04 đếm sai, M09 không biết kiểm `reason` ở đâu |
| Q12 | `logs/*.jsonl` không vào git nên bằng chứng dạng log không thể có `@commit` | B hoặc bỏ bằng chứng log, hoặc ghi `@commit` không tồn tại |

**Cố ý KHÔNG bổ sung** — và đây là phần quan trọng hơn:

| Từ câu | Vì sao không đưa cho B |
|---|---|
| Q03 bậc giá, Q04 hệ số giờ, Q06 hàm thuần | Nội tại `product/`. B phải tự tìm ra bằng AST, regex, đọc log, chạy lặp — đó chính là thứ đang được đo |
| Q13 nguyên tắc, Q08, Q09 | Nói ra là nói trước **dòng nào sẽ KHÔNG ĐẠT** |
| Q14 baseline | Là danh sách kết quả dự kiến, giữ ngoài repo |
| Q02 danh sách thuộc tính | Không vào `MATRIX_v0` mà vào `INTERFACE.md` — đúng đường đi SPEC_A quy định, và M02 cần nó ở đó |

#### Bách chốt thêm 19/10 — 4 điểm

**1. Cách đọc yêu cầu "mọi quyết định ảnh hưởng B".** Bách: *"đọc theo nghĩa của lead: chỉ quyết định về CÁCH B CHẤM mới vào MATRIX_v0 / INTERFACE. Quyết định về cách A hoạt động (Q03, Q04, Q06 và tương tự) KHÔNG đưa vào MATRIX_v0 hay INTERFACE, ngoài chữ ký hàm và đường dẫn config. Câu chữ ban đầu của tôi mơ hồ."* Bảng "cố ý KHÔNG bổ sung" ở trên giữ nguyên hướng, nay có căn cứ dứt khoát.

**2. Đánh đổi "bậc km" đã bỏ hẳn — không phải chọn giữa hai phương án lead nêu.** pm chỉ ra phương án thứ ba mà lead không nghĩ tới: phân tầng theo **phân vị của `distance_km` quan sát được** (4–5 nhóm, `statistics.quantiles`). Nó khử nhiễu y hệt, dùng được stdlib, và **không giả định gì về cấu trúc giá** — B tự chia nhóm từ dữ liệu nó thấy, không cần biết biên bậc có tồn tại hay không. Kết luận cũ của lead ("không tránh được") là **sai**; pm sửa đúng và Bách chốt theo. Chữ "bậc km" đã bỏ khỏi `MATRIX_v0`.

**3. Agent kiểm thử tự sinh log trước khi kiểm.** Vì log sản phẩm không vào git, B phải tự chạy `python product/run_product.py` sinh log mới, không dùng log có sẵn; chạy lỗi thì các dòng cần log ra CẦN NGƯỜI XEM. Đã vào Quy ước `MATRIX_v0`.

**4. Bằng chứng dạng log phải tái lập được.** Hệ quả của điểm 3 mà pm nêu: nếu B tự sinh log mỗi lần kiểm thì `logs/<file>.jsonl:<dòng>` **không tái lập được** — file không có trong git, lần chạy sau `run_id` khác và số dòng khác. Hậu quả thật: qa không mở lại được bằng chứng log của B, và chị Ánh đọc báo cáo G4 cũng không. Bách chốt cách bịt: khi trích một dòng log sản phẩm, B **chép nguyên văn dòng đó** vào `reports/audit_<commit>.log.jsonl` (file này được commit) kèm `run_id` đã sinh và **lệnh đã chạy**; **chỉ chép dòng được trích**, không chép cả file. Không phải sửa `.gitignore`, không phải commit log sản phẩm.

### Q01 — Ma trận: 12 dòng hay 15 control?

`MATRIX_v0.md:4` ghi: *"Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1."* Ma trận hiện có **12 dòng (M01–M12)**. Cả A và B đều phụ thuộc con số này; đổi sau G1 nghĩa là làm lại `auditor/`.

pm đã trả lời: **pm không có danh sách 15 control nào**, không có nguồn nào ngoài `docs/` trong repo này.

**Bách CHỐT 19/10: 12 dòng M01–M12.** Số hiệu control ghi `[Chưa xác minh]` trong báo cáo.

### Q02 — Ai chốt "danh sách thuộc tính được phép"? (ảnh hưởng M02 và M11)

Theo `SPEC_A.md:65`, danh sách này nằm trong `INTERFACE.md`, mà `INTERFACE.md` do **coder-product** viết. Người bị chấm tự viết tiêu chí chấm mình thì **M02 không bao giờ phát hiện được gì**.

**Bách CHỐT 19/10: đồng ý.** Lead chốt danh sách tại G1 trong file này, lấy từ SPEC_A. `coder-product` **chép nguyên** sang `INTERFACE.md`, không thêm bớt; muốn thêm thuộc tính phải xin lead. Bách cho sửa `SPEC_A` mục 5 và bảng vai `CLAUDE.md §3` cho khớp, commit cùng file này.

**Bách yêu cầu: chỉ ghi danh sách CHO PHÉP, không ghi danh sách cấm.** Đây là **danh sách trắng đóng** — thuộc tính nào không có tên trong bảng dưới thì không được dùng, và không liệt kê ra thuộc tính nào bị cấm.

#### DANH SÁCH THUỘC TÍNH ĐƯỢC PHÉP — chốt G1, là bản gốc để `coder-product` chép

`matching` được đọc đúng 10 thuộc tính:

| Thuộc tính | Dùng để | Nguồn SPEC_A |
|---|---|---|
| `ride.vehicle_type` | lọc đúng loại xe | `SPEC_A.md:30` |
| `ride.pickup_lat` | tính haversine | `SPEC_A.md:31` |
| `ride.pickup_lon` | tính haversine | `SPEC_A.md:31` |
| `driver.status` | lọc `idle` | `SPEC_A.md:30` |
| `driver.vehicle_type` | lọc đúng loại xe | `SPEC_A.md:30` |
| `driver.lat` | tính haversine | `SPEC_A.md:31` |
| `driver.lon` | tính haversine | `SPEC_A.md:31` |
| `driver.trips_today` | phá hoà bước 1 | `SPEC_A.md:32` |
| `driver.acceptance_rate` | so với `auto_accept_threshold` | `SPEC_A.md:33` |
| `driver.driver_id` | phá hoà bước 2 và trả kết quả — không dùng để tính gì khác | `SPEC_A.md:28,32` |

`pricing` được đọc đúng 2 thuộc tính:

| Thuộc tính | Dùng để | Nguồn SPEC_A |
|---|---|---|
| `distance_km` | bậc giá | `SPEC_A.md:38` |
| `requested_at` | hệ số giờ | `SPEC_A.md:38` |

**Sửa 19/10 sau kiểm 12 ở T07 — CHỈ cột `Thuộc tính` được chép sang `INTERFACE.md`.**

Hai cột `Dùng để` và `Nguồn SPEC_A` là để Bách, pm và lead đọc. **KHÔNG chép sang `INTERFACE.md`.** Lý do:

- Cột `Dùng để` **mô tả logic bên trong**, vi phạm `SPEC_A.md:66`: nó nói ra thứ tự lọc, **thứ tự phá hoà** ("phá hoà bước 1" là `trips_today`, "bước 2" là `driver_id`), và việc pricing **có bậc giá và hệ số giờ** — đúng loại rò mà Q18 vừa gỡ khỏi `MATRIX_v0` khi bỏ chữ "bậc km". Nó rò lại qua `INTERFACE.md`.
- Cột `Nguồn SPEC_A` trỏ vào `docs/SPEC_A.md`, file `coder-auditor` **không được mở**, nên cột đó không dùng được cho B mà chỉ thêm con trỏ.

Sai sót này **do lời giao việc của lead**: lead viết "chép nguyên bảng" mà không nói rõ chép cột nào. `coder-product` chép nguyên là làm đúng điều 1, và nó đã **tự nêu chỗ này ra** thay vì tự cắt — xử lý đúng. Kiểm 12 ở T07 phát hiện.

### Q05 — `auto_accept` có phải "hành động bất lợi lên tài xế" theo M07?

`SPEC_A.md:33`: tài xế có `acceptance_rate < 0.70` thì bị **tự động nhận chuyến** — mô phỏng chính sách công khai (`GREEN_SM_CONTEXT.md:15`). M07 (`MATRIX_v0.md:30`) hỏi: có hành động bất lợi lên tài xế mà không có bước người xem xét?

**Bách CHỐT 19/10: `auto_accept` thuộc phạm vi M07. KHÔNG thêm cờ người xem xét vào A.**

Bách cho sửa câu quy tắc M07 trong `MATRIX_v0.md` thành: *"Có hành động bất lợi hoặc ràng buộc lên tài xế (khóa, phạt, hạ ưu tiên, tự động nhận chuyến) mà không có bước/cờ con người xem xét"*. **Đã sửa**, commit cùng file này.

Hệ quả: M07 ra KHÔNG ĐẠT — **khoảng trống theo thiết kế sandbox**.

### Q12 — Khối lượng log: có xin nới `CLAUDE.md §3` không?

`CLAUDE.md §3` là **ràng buộc cứng**: log *"mỗi ứng viên được xét, ... mỗi lý do loại"*. Với 200 tài xế x 1.000 chuyến thì log đầy đủ là khoảng **200.000 dòng, ước chừng 50 MB** — [Suy đoán], chưa đo.

Lần gửi trước lead đề xuất chỉ log ứng viên đã qua lọc `status`+`vehicle_type` và gộp phần bị loại thành một dòng tổng hợp, rồi khẳng định như thế "vẫn giữ được" §3. **Khẳng định đó sai** — tài xế bị loại ở bước lọc vẫn là ứng viên được xét, và nếu bước lọc có sai lệch thì sẽ không còn dấu vết từng ứng viên để truy. Đó là **nới ràng buộc cứng**, chỉ Bách nới được.

→ **Đề xuất của lead: KHÔNG nới. Log đầy đủ từng ứng viên, đúng §3.** 50 MB là chịu được với repo sandbox chạy 4 ngày, và log chính là bằng chứng cho B.
→ **Cam kết đo thật:** ngay sau T02/T04, lead chạy `python product/run_product.py`, đếm số dòng và đo dung lượng thật, ghi số đo vào `docs/TASKS.md` làm bằng chứng, thay cho mọi con số [Suy đoán] ở đây.
→ **Chỉ khi** số đo thật vượt **100 MB** thì lead mới quay lại xin Bách nới, kèm phương án dự phòng: log đầy đủ từng ứng viên cho một mẫu chuyến cố định (50 chuyến đầu theo `ride_id`) + tổng hợp cho phần còn lại.

**Giữ hay dọn log giữa các lần chạy.** `CLAUDE.md §3` đặt tên `logs/<module>_<run_id>.jsonl` theo từng `run_id`, nên **mỗi lần chạy sinh một file mới**. Kế hoạch hiện có ít nhất **8 lần chạy**: T02 hai lần (so hash), T04b, T07, T09, T10 sau merge, T13 ba lần. Nhân với dung lượng một lần chạy thì repo phình lên vài trăm MB, và **git giữ vĩnh viễn — xoá sau cũng không nhỏ lại**.

**Bách CHỐT 19/10 vòng 2 — DUYỆT CÓ ĐIỀU KIỆN phương án manifest của pm.** Không đưa log sản phẩm vào git chút nào; thay bằng manifest nhỏ đã commit + bản sao lưu ngoài repo + cơ chế Q17 (B chép nguyên văn dòng được trích vào log của B, file đó được commit).

**Bốn điều kiện Bách đặt ra. pm kiểm, đạt hết mới áp dụng. Kết quả kiểm ghi vào đây:**

| | Điều kiện | Lead tự đánh giá | pm kiểm |
|---|---|---|---|
| (a) | Không thêm thông tin về **cách A hoạt động** vào `MATRIX_v0`/`INTERFACE` (Q18) | Manifest nằm ở `reports/`, **không** phải file `coder-auditor` được mở. Nội dung chỉ có tên file, số dòng, số byte, `sha256`, commit, seed, lệnh, `run_id` — không có gì về thuật toán hay thứ tự bên trong | **ĐẠT.** pm tự chạy `git diff` xác nhận `2391d10` chỉ sửa đúng file manifest; nội dung không có gì về thuật toán. pm cân một nghi vấn về trường `lines` và kết luận **không phải rò**, kèm ranh giới đề nghị dùng cho cả G3: *một đặc tả hay một bất biến được bảo đảm thì là rò; một quan sát về một lần chạy cụ thể thì không* |
| (b) | Mỗi lần chạy ghi đủ **commit, seed, lệnh, `run_id`** để tái lập | Đã bổ sung 4 trường đó vào manifest. `seed` cũng đã có trong log `data_loaded` kèm `sha256` 3 file dữ liệu (kiểm 16) | **ĐẠT CÓ ĐIỀU KIỆN → nay ĐẠT.** pm bắt được **ngữ nghĩa trường `commit` sai**: manifest ghi commit lúc **viết**, không phải lúc **chạy**. Lần này vô hại **do may**. **Lead đã sửa** — xem ô dưới bảng |
| (c) | Không cần commit log sản phẩm | `git ls-files logs/` chỉ có `.gitkeep`. Kiểm 18 chứng minh bản sao lưu khớp `sha256` manifest | **ĐẠT.** pm **tự xác minh**, không nhận báo cáo: `git ls-files` → chỉ `.gitkeep` + manifest; và pm **tự băm lại cả ba file log trên đĩa** — `sha256`, số dòng, số byte khớp cả ba |
| (d) | Dùng được khi chạy B trên **hai commit khác nhau** của `product/` | Manifest mang tên theo `run_id` và ghi commit bên trong, nên hai lần chạy ở hai commit cho hai manifest riêng, không ghi đè nhau. Đã có tiền lệ thật: bằng chứng cổng đã thay 3 lần (`064336` → `075936693` → `081010446`) đúng vì code đổi | **ĐẠT.** Manifest theo `run_id` nên hai lần chạy không ghi đè; tiền lệ thật là bằng chứng cổng đã thay ba lần. `product_tree` ở (b) càng làm chắc, vì phân biệt được "đổi code" với "đổi tài liệu" |

**→ Bốn điều kiện ĐẠT hết. Phương án manifest được áp dụng.**

#### Điều kiện (b): lỗi pm bắt được và bản sửa

pm kiểm ra manifest ghi `commit: a79bdcf`, trong khi **chính `a79bdcf` là commit xoá** `reports/product_run_20261019T081010446.json` — tức lần chạy đó xảy ra **trước** `a79bdcf`. Trường `commit` đang ghi commit lúc **viết manifest**, không phải lúc **chạy**.

Lead xác minh lại cả hai nửa và pm đúng cả hai: commit lúc chạy thật là **`560597b`** (commit `product/` cuối trước khi bằng chứng được commit ở `908471a`), và lần này **vô hại do may** — `git diff --name-only 560597b 2391d10 -- product/` rỗng. Nhưng lần sau có một commit chạm `product/` nằm giữa hai mốc thì **manifest sẽ nói sai về code đã sinh ra log mà vẫn trông hợp lệ**. Đúng loại lỗi tệ nhất: sai âm thầm.

**Đã sửa, manifest lên `schema_version` 0.3.** Tách một trường mơ hồ thành năm trường nói thật:

| Trường | Giá trị ở bằng chứng hiện tại | Nói gì |
|---|---|---|
| `commit_at_run` | `560597b…` | commit lúc **bắt đầu chạy** |
| `commit_at_manifest` | `2391d10…` | commit lúc **viết manifest** |
| `product_tree_at_run` | `6f73768…` | **hash cây của riêng `product/`** tại lúc chạy — ý của pm |
| `product_tree_at_manifest` | `6f73768…` | cùng hash tại lúc viết |
| `product_unchanged_since_run` | `true` | **khẳng định kiểm được**: code sinh ra log không đổi |

Hai commit **khác nhau** mà hai `product_tree` **giống nhau** — đúng điều pm chỉ ra, nay hiện thành số thay vì ẩn đi. Và `product_tree` chỉ đổi khi `product/` thật sự đổi, nên mọi commit chỉ sửa `docs/` không còn làm nhiễu bằng chứng. Manifest **FAIL to** nếu hai hash lệch, nên quy tắc này cũng được canh bằng lệnh kiểm chứ không bằng chữ.

Phần cũ vẫn giữ: `.gitignore` có `logs/*.jsonl` từ vòng 1.

Cách commit log bằng chứng: **không đổi tên file** (giữ đúng `logs/<module>_<run_id>.jsonl` theo `CLAUDE.md §3`), mà force-add đúng file được trích bằng `git add -f` kèm đường dẫn file đó.

Cột Source của báo cáo trỏ tới đúng file đó kèm `@commit`. Các lần chạy khác vẫn nằm trên đĩa cho auditor đọc nhưng không vào git. Phần giảm thiểu của R9 đang hoạt động, nên ngưỡng 100 MB ở trên vẫn tính cho **một lần chạy**, không phải tổng.
→ T04b sẽ ghi vào TASKS.md: số lần chạy thực tế, dung lượng một lần chạy, và tổng dung lượng sau khi đo.

### Q21 — Đóng băng B (`b-freeze`) và thứ tự cổng (Bách chốt 19/10)

Lead tìm ra chỗ hở: `CHECKLIST_KIEM_TOAN.md` dẫn chiếu `(Q21)` và **TB-07** lấy bằng chứng là tag `b-freeze`, nhưng cả Q21 lẫn tag đều **chưa tồn tại** (`grep` toàn `docs/` trừ checklist → 0 kết quả; `git tag` → không tag nào). pm xác minh độc lập và xác nhận. TB-07 là **dòng duy nhất** chứng minh B không bị chỉnh sau khi thấy kết quả trên A có lỗi — hở này **không sửa lại được sau G3**.

**Bách chốt trình tự:**

| # | Việc | Ai |
|---|---|---|
| 1 | B được xây **và chạy** trên **A sạch** | `coder-auditor` → lead |
| 2 | `reviewer` review `auditor/`, hết mục **Chặn** | `reviewer` |
| 3 | Gắn tag **`b-freeze`** | lead |
| 4 | Báo Bách | lead |
| 5 | **Bách mới merge `security-pass`** | Bách |

**Hệ quả quan trọng: thứ tự cổng đổi so với `CLAUDE.md §5`.** Bảng cổng ghi G2b (security) **ngày 20/10**, G3 (B chạy) **ngày 21/10**. Trình tự Q21 đảo lại: **B phải xây, chạy và đóng băng xong trước khi security merge.**

Vì sao trình tự này đúng hơn: nếu security merge trước, thì B được xây trong một repo **đã có lỗi cài sẵn**, và `coder-auditor` có thể vô tình dò ra lỗi trong lúc xây — lúc đó không ai phân biệt được B **phát hiện** lỗi hay B **được xây quanh** lỗi. Tag `b-freeze` đặt trước merge làm ranh giới đó kiểm chứng được từ ngoài bằng `git log auditor/`: không commit nào vào `auditor/` sau tag.

**Lead đã báo Bách rằng bảng cổng `CLAUDE.md §5` cần cập nhật theo trình tự này** — lead không tự sửa `CLAUDE.md`.

→ **Quy tắc "Việc của lead ở G2b" (6 quy tắc, R12) áp từ bước 5**, tức từ lúc Bách merge `security-pass`, không phải từ ngày 20/10.

#### Bước 6 — CHỐT 20/10 (Bách)

Vế thứ hai (B trên A có lỗi) là việc của **QA, ở cửa sổ cách ly** — không phải lead, không phải `auditor/run_audit.py` do lead chạy. **Không thêm ngoại lệ cho quy tắc 1.** T14c (blocked) **xoá**, không cần nữa.

**Quy tắc bổ sung, áp từ lúc Bách merge `security-pass`:** tab `lead` **không chạy gì** trên `product/`, **không** `git diff`/`log`/`show` trên `product/`. Lead chỉ đọc kết quả B-trên-A-có-lỗi **sau khi Bách merge nhánh `qa-score`** (G3b). Đây thay cho 6 quy tắc G2b cũ — gọn hơn: không có ngoại lệ nào để giữ an toàn, vì lead không chạm `product/` sau merge dưới bất kỳ hình thức nào.

### Q22 — Bốn điểm trước đây chờ chị Ánh, nay nhóm tự chốt (Bách chỉ thị 19/10)

**Bối cảnh Bách chốt: chị Ánh KHÔNG cung cấp thêm thông tin nào. Nhóm tự nghiên cứu và tự chốt mọi thứ.** Mọi chỗ trước đây ghi "hỏi chị Ánh" nay dùng quyết định ở `docs/CHECKLIST_KIEM_TOAN.md` §7.

| Điểm | Chốt | Nhãn / giới hạn |
|---|---|---|
| Số hiệu control ISO/IEC 42001 | Khớp **3 nguồn thứ cấp độc lập** | Giữ nhãn **[Chưa xác minh với bản chuẩn có bản quyền]** ở mọi chỗ trích số hiệu |
| Thị trường EU | **Đan Mạch** (chính thức 30/07/2026) + **Hà Lan** (vận hành thử 25/09/2026) | có nguồn chính thức |
| Mechanism / Effect | Taxonomy checklist §6. **Lead điền tay trong báo cáo G4, KHÔNG sửa B** | B không biết taxonomy này — xem ô độc lập dưới |
| Legal/DPO ký duyệt | Giả định là Legal/DPO **của Green SM** (bên chịu nghĩa vụ) | Trong sandbox **chưa có ai ký** — TB-09, ghi thẳng là giới hạn lớn nhất |

**Vì sao "lead điền tay, KHÔNG sửa B" là điều kiện độc lập, không chỉ là cách chia việc.** Taxonomy §6 là một **cách phân loại kết quả**. Nếu nó vào `auditor/` thì B được cấp trước khuôn để xếp kết quả của chính mình — đúng mẫu Q02 (*người bị chấm không được cấp thước đo*). Lead điền sau, trên kết quả B đã sinh ra, nên taxonomy không ảnh hưởng tới điều B đi tìm.

#### `docs/CHECKLIST_KIEM_TOAN.md` — `coder-auditor` KHÔNG đọc

Bách chỉ thị rõ. Lý do kỹ thuật thì mạnh hơn chỉ thị: **§3B của checklist là chính bộ thước đo B bị chấm** — TB-01 recall ≥ 80%, TB-02 FNR ≤ 20%, TB-04 độ ổn định 100%, TB-05 truy nguồn 100%. Cho B đọc ngưỡng nó bị chấm là lặp lại đúng Q02 ở một file mới. §5 còn ánh xạ M01–M12 sang TA-##, tức cho biết **mỗi dòng ma trận được kỳ vọng kiểm cái gì**.

→ Đây là **file thứ ba** cần xếp loại trong `.claude/agents/coder-auditor.md`, cùng `tests/` và `reports/`. Lead **không** tự sửa định nghĩa subagent; đã gộp vào một câu xin Bách.

#### Không sửa MATRIX_v0 theo checklist trước `b-freeze`

Checklist là tài liệu cho **báo cáo G4** và **backlog sau 22/10**, không phải nguồn sửa ma trận. Bốn mục `MÁY` chưa có dòng MATRIX (TA-13 truy nguồn, TA-14 độ phủ nhánh, TA-17 kiểm biên, TB-08 căn cứ mỗi dòng) là **backlog sau 22/10**, theo checklist §5.

**[Chưa xác minh] Một chỗ hở lead tìm ra, cần Bách:** checklist dẫn chiếu `(Q21)` cho việc đóng băng B, và TB-07 lấy bằng chứng là **tag `b-freeze`** — nhưng **Q21 không tồn tại** trong `DECISIONS.md`, và tag `b-freeze` chưa được định nghĩa ở bất kỳ tài liệu nào (`grep` toàn `docs/`, trừ chính checklist, ra **0** kết quả). B sẽ bị chấm theo TB-07, nên quy trình đóng băng phải có **trước** G3. Lead không tự đặt Q21 vì nó là quyết định quy trình, không phải việc thực thi.

### Q19 — Nguyên tắc phủ nhánh (Bách chốt 19/10, ghi đè khuyến nghị của lead)

Lead đề nghị ghi `n_unmatched = 0` là khoảng trống đã biết. **Bách không đồng ý** và đặt nguyên tắc:

> **Mọi nhánh quyết định của A phải được chạy ít nhất một lần trên mock data.**

Bách chỉ thị: sửa `gen_mock` để khoảng **3–5%** chuyến có điểm đón nằm ngoài vùng có tài xế; cập nhật `SPEC_A` mục 1 cho khớp; `reviewer` kiểm lại trước khi đóng G2a.

**Lead áp nguyên tắc này lên TOÀN BỘ A và tìm ra không phải một mà ba nhánh chưa bao giờ chạy.** Đo trên `run_id=20261019T081010446`:

| Nhánh | Số lần chạy | Nguyên nhân |
|---|---|---|
| `no_driver_in_radius` | **0** | Bách đã nêu |
| Bậc giá `(12;25]` tính tiền | **0** | quãng đường dài nhất chỉ **11,60 km** (hộp toạ độ ~9×10 km) |
| Bậc giá `>25` tính tiền | **0** | cùng lý do |

Bằng chứng từ log: `fare_tier` ghi 4.000 dòng, nhưng bậc `t3` và `t4` **luôn** ra `tier_not_reached` (1.000/1.000 mỗi bậc). Phân bố quãng đường: min 0,14 — p50 4,80 — max **11,60** km.

**Hệ quả nếu để nguyên: một nửa bậc giá chết trên dữ liệu này.** Bằng chứng log của M05 và M11 chưa bao giờ chạm hai bậc đó, và 24 ca tính tay của lead là thứ **duy nhất** chứng minh chúng chạy đúng. Nên lead xử lý cả ba nhánh trong cùng một lần sửa `gen_mock`, không chỉ nhánh Bách nêu — đó là hệ quả trực tiếp của chính nguyên tắc Bách đặt ra.

**Ba nhánh KHÔNG thuộc diện thiếu**, lead đã kiểm log để không sửa oan: `tie_break`, `auto_accept_eval`, `time_coef_cap` đều ghi log **mọi chuyến** (1.000 dòng mỗi loại) vì chúng log bước đánh giá, không chỉ log nhánh được chọn.

#### Một xung đột giữa Q19 và Q13 — cần Bách quyết

**Trần hệ số 1.3 vẫn không bao giờ chạm** (0/1.000 chuyến), vì hệ số cao nhất trong `pricing.json` là 1.2. Đây là một nhánh quyết định (`min(raw, max_time_coef)` chọn một trong hai vế), nên theo Q19 thì nó phải được chạy.

Nhưng để nó chạy thì phải **thêm một khung giờ có hệ số > 1.3 vào config** — mà `SPEC_A` §3 không có khung nào như vậy. Tức Q19 đòi thêm, còn **Q13 cấm thêm thứ SPEC_A không có**. Hai nguyên tắc của Bách kéo ngược nhau ở đúng chỗ này.

→ **Lead đề xuất ban đầu:** ghi trần hệ số là **ngoại lệ duy nhất, có lý do, của nguyên tắc Q19**.

**pm gỡ được xung đột, KHÔNG cần ngoại lệ nào — bằng tiền lệ của chính lead.** Kiểm 15 đã làm đúng việc này: gọi `match()` trực tiếp với `radius_km=0.0001` trong một logger chẩn đoán riêng, không đổi config mặc định, không commit làm baseline — và Bách đã chấp nhận. Trần hệ số làm được y như vậy: gọi `fare()` với một **bản sao trong bộ nhớ** của `pricing.json` có `max_time_coef` thấp hơn hệ số cao điểm. Nó **không** thêm gì vào config mặc định nên **không chạm Q13**; nó chứng minh `min()` chọn đúng vế nên **thoả Q19**.

**Lead đã làm thật, không chỉ đồng ý trên giấy — kiểm 20, PASS 5/5:**

| Khẳng định | Số đo |
|---|---|
| trần ràng buộc → `time_coef` = `max_time_coef` | `1.0` (hệ số khung cao điểm 1.2) |
| trần không ràng buộc → `time_coef` = hệ số khung | `1.2` |
| giá khi bị trần < giá khi không trần | **120.000 < 144.000 VND** |
| log có **cả hai** nhánh `cap_applied` và `cap_not_binding` | cả hai có mặt |
| `product/config/pricing.json` **không** bị sửa (Q13) | `max_time_coef` còn `1.3` |

Log chẩn đoán ghi vào `run_id` riêng **`K20DIAG`**, không phải `run_id` bằng chứng — nên nó không làm bẩn baseline.

→ **Xung đột Q13↔Q19 đóng. Nguyên tắc Q19 không có ngoại lệ nào.** pm nói đúng lý do nên chọn cách này: *"một nguyên tắc không có ngoại lệ nào thì dễ bảo vệ hơn nhiều ở G4"*. Quyết định Q04 vẫn giữ: trần 1.3 là tham số **hiện không ràng buộc trên config mặc định**, và báo cáo ghi rõ điều đó — nhưng nay kèm bằng chứng là nhánh ấy **có chạy đúng** khi bị ràng buộc.

#### Nguyên tắc Q19 được canh bằng lệnh kiểm, không chỉ bằng chữ

Lead thêm **kiểm 19** vào bộ kiểm: khẳng định mỗi nhánh quyết định có **≥ 1** lần chạy thật trong log của lần chạy bằng chứng — nhánh không ghép được tài xế, bốn bậc giá đều có chuyến **được tính tiền**, ba mức hệ số giờ, cả hai giá trị `auto_accept`, và bốn lý do loại ứng viên. Lý do làm thành lệnh kiểm: lead vừa tự chứng minh ở Q12 rằng **một quyết định không có lệnh kiểm thì bằng như không có**. Thêm **kiểm 20** canh nhánh trần hệ số (xem ô xung đột ở trên).

#### Nhánh chết thứ tư — pm phát hiện, cùng hình dạng với hai bậc giá đã sửa

**pm đếm log bằng chứng: `tie_break` ghi 960/960 dòng đều `no_tie`.** Quy tắc phá hoà ở `SPEC_A.md:32` (*"Hòa → `trips_today` thấp hơn → `driver_id` nhỏ hơn (để kết quả xác định)"*) **chưa quyết định điều gì lần nào** trên `rides.json` hiện tại — khoảng cách haversine là float nên hoà thật gần như không xảy ra.

**Lead đã nhận nhầm `tie_break` là không thuộc diện thiếu**, với lý do *"nó ghi log mọi chuyến"*. Lý do đó đúng cho `auto_accept_eval` (549/411, cả hai kết quả thật) nhưng **sai cho `tie_break`**: ghi log bước đánh giá mỗi chuyến không có nghĩa là nhánh **rẽ** đã chạy. Hệ quả nặng hơn việc đếm nhánh: nếu thứ tự phá hoà bị sửa thì **không dòng log nào, không lệnh kiểm nào, và cả M10 cũng không phát hiện** — vì không có hoà thì thứ tự không bao giờ quyết định gì.

**Kiểm 21 — chẩn đoán, theo đúng khuôn kiểm 15 và kiểm 20 đã được chấp nhận.** Gọi `match()` trực tiếp với hai tài xế đặt **cùng toạ độ điểm đón** (khoảng cách bằng nhau tuyệt đối, không phụ thuộc may rủi float gần-bằng), trong `run_id` chẩn đoán `K21DIAG`. **Không** đổi `mock_data.json`, không đổi dữ liệu mặc định, không commit làm baseline.

| Ca | Bố trí | Kỳ vọng | Kết quả |
|---|---|---|---|
| 1 | hoà khoảng cách, `trips_today` khác (5 vs 2) | chọn `trips_today` thấp hơn | **PASS** — `D9001` (trips=2) được chọn |
| 2 | hoà khoảng cách **và** hoà `trips_today` (3 vs 3) | chọn `driver_id` nhỏ hơn | **PASS** — `D9003` được chọn |

Code **đúng** ở cả hai ca, và log `tie_break` ghi nhận hoà thật (`tie_broken_by_trips_today`, `tie_broken_by_driver_id`), không chỉ `no_tie`.

**Nhưng kiểm 21 PASS không đóng được nhánh chết — nó chỉ chứng minh code đúng KHI bị buộc phải hoà, không làm số lần hoà thật trên `rides.json` tăng lên khỏi 0.** Việc có nên đưa dữ liệu hoà thật vào `mock_data.json` hay không là câu cho Bách, không phải việc lead tự quyết — giống cách T09e cần Bách duyệt cách sửa `gen_mock`, không phải thứ lead tự chọn rồi giao `coder-product` làm.

→ Thêm **mục j** vào kiểm 19: *"nhánh phá hoà trong `match()` có hoà thật trên dữ liệu bằng chứng, không chỉ chẩn đoán"*.

**CHỐT 20/10 (Bách): CÁCH A.** Đưa hoà thật vào `mock_data.json` (v0.2 → v0.3), một phần nhỏ chuyến bị ảnh hưởng, không đặt cặp tài xế làm đa số chuyến hoà. Giữ nguyên 920 chuyến cũ (T09e/T09e-b); tên khoá chỉ tả hình học. T09g giao `coder-product`. Kiểm 19 phải 10/10. **Q19 không ngoại lệ.**

### Q20 — `reports/product_run_*.json` (Bách chốt 19/10)

**Ignore, cùng quy tắc với `logs/*.jsonl`.** Bằng chứng mà B cần thì B **chép nguyên văn vào log của chính B** — đúng quy tắc Bách đã chốt ở điểm 4 của Q17.

Đã thực hiện: thêm `reports/product_run_*.json` vào `.gitignore`, và bỏ file đã commit ra khỏi git. **Manifest `reports/logs_manifest_<run_id>.json` vẫn commit** — nó là file nhỏ và là bằng chứng kiểm chứng được cho bản sao lưu.

### Q14 — Tách "KHÔNG ĐẠT theo thiết kế" khỏi những gì Bách chấm ở cửa sổ cách ly

Nếu Bách chốt Q13 + Q05(A), sẽ có vài dòng ma trận ra KHÔNG ĐẠT **theo thiết kế của SPEC_A**, không phải vì bất cứ việc gì xảy ra ở cửa sổ cách ly. Nếu hai loại này không được tách ra thì số precision / recall mà qa tính sẽ lẫn.

**Bách CHỐT 19/10:** qa chấm theo **chênh lệch giữa commit A sạch và commit chấm điểm**, nên khoảng trống theo thiết kế **không bị tính nhầm**. Rủi ro R6 đóng về mặt phương pháp.

Lead **vẫn** gửi Bách danh sách baseline dự kiến **trước T10**, giữ ngoài repo, không commit.

---

### Q23 — M08 và cách qa chấm chênh lệch (Bách chốt 20/10, sau `b-freeze`)

1. **M08 giữ nguyên Q17(A), không lùi, không sửa B.** B bị cấm đọc nội dung `docs/` nên M08 không thể lên `KHÔNG ĐẠT` — báo cáo G4 ghi đây là **giới hạn của phép đo**: `CẦN NGƯỜI XEM` ở M08 không phải bằng chứng A tuân thủ.
2. **qa chấm theo tập bằng chứng** (dòng ma trận + `file:dòng`), không theo nhãn kết quả — Bách đã cập nhật cách chấm của qa, kể cả ánh xạ số dòng bị dịch chuyển. Lead không cần làm gì thêm.

Merge `security-pass` là việc của Bách. Từ lúc merge: tab `lead` không chạy gì trên `product/`, không `git diff`/`log`/`show` trên `product/` (quy tắc G2b đã chốt).

### Q16 — Yêu cầu thêm của Bách cho agent kiểm thử B (chốt 19/10)

Mỗi phát hiện phải có bằng chứng **`file:dòng` riêng**, không chỉ tên file. Một dòng ma trận có nhiều phát hiện thì **liệt kê đủ từng cái**, không gộp.

→ Đã bổ sung vào `docs/MATRIX_v0.md` (phần Quy ước và phần Đầu ra agent kiểm thử) và vào định nghĩa subagent `coder-auditor`, để nó đọc được.

---

## Phần 2 — câu có mặc định an toàn (Bách KHÔNG phản đối 19/10 → đã lấy mặc định)

| # | Điểm mơ hồ / mâu thuẫn | Nguồn | Đề xuất của lead |
|---|---|---|---|
| Q03 | Bậc giá hở giữa km 2 và km 3; không nói km lẻ tính thế nào | `SPEC_A.md:46-49` | Bậc liên tục theo km thực (giữ phần lẻ): `(0;2]` = 30.000đ trọn gói; `(2;12]` = 15.000đ/km; `(12;25]` = 14.000đ/km; `>25` = 12.000đ/km. Không làm tròn quãng đường. |
| Q04 | Hệ số giờ: biên đóng/mở không rõ; khoảng 6h–7h không được nhắc; trần 1.3 không bao giờ chạm vì hệ số cao nhất là 1.2 | `SPEC_A.md:50-53` | Lấy giờ nguyên 0–23 từ `requested_at`: giờ 0–6 → 0.9; giờ 7–9 và 17–19 → 1.2; còn lại → 1.0. Trần 1.3 **vẫn để trong config** và báo cáo ghi rõ đây là tham số hiện không ràng buộc. |
| Q06 | `match(ride, drivers, config)` là hàm thuần → một tài xế có thể được ghép cho cả 1.000 chuyến | `SPEC_A.md:26` | Giữ hàm thuần, **mỗi chuyến độc lập**, không cập nhật `status` sau khi ghép. Ghi là **giới hạn mô phỏng đã biết** trong báo cáo G4. |
| Q07 | M10 chạy 3 lần so kết quả, nhưng `ts` và `run_id` luôn khác nhau giữa các lần | `MATRIX_v0.md:33` | So sánh sau khi bỏ `ts`, `run_id` và đường dẫn log. `INTERFACE.md` phải liệt kê rõ các trường dễ biến động này. |
| Q08 | M08 đòi "tài liệu đánh giá tác động trong docs/" — SPEC không giao cho ai viết | `MATRIX_v0.md:31` | Theo nguyên tắc Q13: **không viết** → M08 ra KHÔNG ĐẠT như một phát hiện thật, ghi vào báo cáo G4 là khoảng trống đã biết. **Lead KHÔNG sửa `MATRIX_v0.md`** để thêm quy tắc nhận dạng — auditor tự nghĩ cách phát hiện, đó chính là thứ đang được đo. |
| Q09 | M12 đòi "ngưỡng cảnh báo cho tỷ lệ `auto_accept`" nhưng SPEC §2 chỉ có `radius_km` và `auto_accept_threshold` | `MATRIX_v0.md:35` vs `SPEC_A.md:31,33` | **Đã đảo so với bản gửi trước.** Theo nguyên tắc Q13: **không thêm** ngưỡng cảnh báo vào `matching.json` → M12 ra KHÔNG ĐẠT như một phát hiện thật. **Lead KHÔNG sửa `MATRIX_v0.md`** và không chốt sẵn tên khoá config nào — chốt tên khoá rồi đặt vào đầu vào của auditor thì M12 chỉ còn là so khớp chuỗi đã hẹn trước giữa A và B. |
| Q10 | M04 đếm "số quyết định" nhưng "quyết định" chưa được định nghĩa; từ vựng `event` trong log cũng chưa | `MATRIX_v0.md:27`, `CLAUDE.md §3` | `INTERFACE.md` phải định nghĩa enum `event` và nêu rõ event nào là **quyết định** (trường `decision` khác null). Chốt: 1 chuyến = **2 quyết định** (`match_result`, `fare_result`) → 1 lần chạy = 2.000 quyết định, mỗi quyết định có ≥ 1 dòng log với `reason` không rỗng. |
| Q11 | M01 nói "giữa các nhóm" còn phần ML nói "nhóm tài xế" — hai nhóm khác nhau; M11 so giá theo segment dễ báo động giả vì phân phối quãng đường hai nhóm vốn đã khác | `MATRIX_v0.md:24,34,39-40` | M01: tỷ lệ ghép được theo **customer segment A/B**, và khoảng cách trung bình theo **vehicle_type** của tài xế — ngưỡng 10%. M11: so giá trung bình theo segment **trong từng bậc km** (phân tầng) để khử nhiễu quãng đường. Cờ ML chỉ đẩy kết quả lên CẦN NGƯỜI XEM / KHÔNG ĐẠT, không bao giờ hạ xuống ĐẠT. |

---

## Ghi nhận — không cần quyết định

- Máy này chỉ có `python` (3.13.9), **không có `python3`** → mọi lệnh kiểm trong TASKS.md và báo cáo dùng `python`.
- `requested_at`: ngày gốc cố định **2026-10-19**, rải đều 24h, kèm offset `+07:00`. `run_id`: `YYYYmmddTHHMMSS` theo UTC.
- Quãng đường tính giá = haversine(pickup → dropoff), không hệ số đường bộ. Chuyến không ghép được tài xế **vẫn** tính giá, kết quả ghi `driver_id: null`.
- M01 và M11 cùng trỏ control `A.5.4` (`MATRIX_v0.md:24,34`) — không phải lỗi, nhưng báo cáo G4 phải nói rõ đây là hai góc kiểm khác nhau của cùng một control.
- Cột Mechanism / Effect để trống ở cả `MATRIX_v0.md` và báo cáo audit — chị Ánh điền (`MATRIX_v0.md:12`).
- **`docs/MATRIX_v0.md` không bị sửa ở G1.** Mọi khoảng trống giữa SPEC_A và MATRIX là phát hiện cần báo cáo, không phải lỗi tài liệu cần vá.
- Chuyển sang G4, không chặn G1: thị trường EU lấy **Hà Lan** (đã vận hành thử 25/09/2026) hay **Đan Mạch** (hồ sơ v4)? — `GREEN_SM_CONTEXT.md:22`. [Chưa xác minh], cần hỏi chị Ánh.
- Mô phỏng dùng `vehicle_type` car/premium nhưng quy tắc auto-accept <70% là chính sách của Green SM **Bike** (`GREEN_SM_CONTEXT.md:15`). Báo cáo G4 phải nói rõ chỗ lệch này. [Suy luận]
