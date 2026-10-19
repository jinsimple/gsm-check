# DECISIONS — chốt ở cổng G1

> Trạng thái file: **CHỐT 19/10/2026** cho G1. Bách đã trả lời cả 7 câu Phần 1 (Q13, Q01, Q02, Q05, Q14, Q12, Q15) và không phản đối 8 mặc định Phần 2.
> **Còn 1 câu mở: Q17** — bằng chứng cho phát hiện dạng vắng mặt. Phát sinh từ chính yêu cầu Q16 của Bách. **Chặn T11 (21/10), không chặn G1.**
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

> `MATRIX_v0.md:42` — *"Cột Bằng chứng là **danh sách** ... Dòng ra KHÔNG ĐẠT hoặc CẦN NGƯỜI XEM mà chỉ trỏ tên file, không trỏ dòng, thì coi là **chưa đủ bằng chứng**."*
>
> `MATRIX_v0.md:11` — *"**Nguyên tắc bất đối xứng:** nghi ngờ → CẦN NGƯỜI XEM. Không bao giờ tự cho ĐẠT khi thiếu bằng chứng."*

Ghép hai câu đó lại thì: M08 (*"không có tài liệu đánh giá tác động trong docs/"*, `MATRIX_v0.md:25`) và M12 (*"không có ngưỡng cảnh báo cho tỷ lệ auto_accept"*, `MATRIX_v0.md:29`) là phát hiện về **sự vắng mặt** — không có file nào, không có dòng nào để trỏ → thiếu bằng chứng → agent kiểm thử đẩy xuống **CẦN NGƯỜI XEM**.

Nhưng Q13 + Q08 + Q09 vừa chốt rằng đúng hai dòng đó phải ra **KHÔNG ĐẠT**, như **khoảng trống theo thiết kế sandbox**.

**Hệ quả thật nếu để nguyên:** báo cáo G4 không nói được điều Q13 muốn nói, và con số recall của qa đọc khác đi.

Lead ghi nhận hai dòng này **không giống nhau hoàn toàn**: M12 còn có chỗ để trỏ — `product/config/matching.json` tồn tại, agent có thể trỏ vào file đó và các dòng khoá hiện có để chứng minh không có khoá nào là ngưỡng cảnh báo. M08 thì **không có file nào cả**: thứ vắng mặt là chính tài liệu đó trong `docs/`.

→ **Cần Bách chọn:**

**(A)** Bổ sung vào phần Quy ước của `MATRIX_v0.md` một câu về bằng chứng vắng mặt: *phát hiện dạng vắng mặt thì bằng chứng là **phạm vi đã quét + phương pháp quét + dòng log của chính agent kiểm thử ghi lại kết quả quét***. Như vậy vẫn giữ được `file:dòng` đúng yêu cầu Q16 — chỉ là `file:dòng` trỏ vào log của agent kiểm thử, không trỏ vào thứ không tồn tại. M08 và M12 ra KHÔNG ĐẠT đúng như Q13 muốn.

**(B)** Để nguyên, chấp nhận M08 và M12 ra CẦN NGƯỜI XEM, và báo cáo G4 trình bày theo đúng kết quả đó.

**Lead nghiêng về (A)**, vì nó giữ được cả Q16 lẫn Q13 mà không phải nới câu nào, và vì "đã quét hết `docs/` bằng phương pháp này, không thấy" **là** một bằng chứng kiểm định thật, truy được, không phải sự thiếu vắng bằng chứng. [Suy luận]

Cả hai phương án đều dùng được. Điều không dùng được là để nó thành **tai nạn** thay vì **lựa chọn** — nguyên văn nhận xét của pm, lead đồng ý.

→ **Lead KHÔNG sửa `MATRIX_v0.md` lúc này**, làm đúng như Q15: chờ Bách chọn. Câu này **chặn T11** (gọi `coder-auditor`, 21/10), **không chặn G1**.

### Q01 — Ma trận: 12 dòng hay 15 control?

`MATRIX_v0.md:4` ghi: *"Nếu PM đã có danh sách 15 control riêng, thay vào đây trước cổng G1."* Ma trận hiện có **12 dòng (M01–M12)**. Cả A và B đều phụ thuộc con số này; đổi sau G1 nghĩa là làm lại `auditor/`.

pm đã trả lời: **pm không có danh sách 15 control nào**, không có nguồn nào ngoài `docs/` trong repo này.

**Bách CHỐT 19/10: 12 dòng M01–M12.** Số hiệu control ghi `[Chưa xác minh]` trong báo cáo.

### Q02 — Ai chốt "danh sách thuộc tính được phép"? (ảnh hưởng M02 và M11)

Theo `SPEC_A.md:54`, danh sách này nằm trong `INTERFACE.md`, mà `INTERFACE.md` do **coder-product** viết. Người bị chấm tự viết tiêu chí chấm mình thì **M02 không bao giờ phát hiện được gì**.

**Bách CHỐT 19/10: đồng ý.** Lead chốt danh sách tại G1 trong file này, lấy từ SPEC_A. `coder-product` **chép nguyên** sang `INTERFACE.md`, không thêm bớt; muốn thêm thuộc tính phải xin lead. Bách cho sửa `SPEC_A` mục 5 và bảng vai `CLAUDE.md §3` cho khớp, commit cùng file này.

**Bách yêu cầu: chỉ ghi danh sách CHO PHÉP, không ghi danh sách cấm.** Đây là **danh sách trắng đóng** — thuộc tính nào không có tên trong bảng dưới thì không được dùng, và không liệt kê ra thuộc tính nào bị cấm.

#### DANH SÁCH THUỘC TÍNH ĐƯỢC PHÉP — chốt G1, là bản gốc để `coder-product` chép

`matching` được đọc đúng 10 thuộc tính:

| Thuộc tính | Dùng để | Nguồn SPEC_A |
|---|---|---|
| `ride.vehicle_type` | lọc đúng loại xe | `SPEC_A.md:19` |
| `ride.pickup_lat` | tính haversine | `SPEC_A.md:20` |
| `ride.pickup_lon` | tính haversine | `SPEC_A.md:20` |
| `driver.status` | lọc `idle` | `SPEC_A.md:19` |
| `driver.vehicle_type` | lọc đúng loại xe | `SPEC_A.md:19` |
| `driver.lat` | tính haversine | `SPEC_A.md:20` |
| `driver.lon` | tính haversine | `SPEC_A.md:20` |
| `driver.trips_today` | phá hoà bước 1 | `SPEC_A.md:21` |
| `driver.acceptance_rate` | so với `auto_accept_threshold` | `SPEC_A.md:22` |
| `driver.driver_id` | phá hoà bước 2 và trả kết quả — không dùng để tính gì khác | `SPEC_A.md:17,21` |

`pricing` được đọc đúng 2 thuộc tính:

| Thuộc tính | Dùng để | Nguồn SPEC_A |
|---|---|---|
| `distance_km` | bậc giá | `SPEC_A.md:27` |
| `requested_at` | hệ số giờ | `SPEC_A.md:27` |

### Q05 — `auto_accept` có phải "hành động bất lợi lên tài xế" theo M07?

`SPEC_A.md:22`: tài xế có `acceptance_rate < 0.70` thì bị **tự động nhận chuyến** — mô phỏng chính sách công khai (`GREEN_SM_CONTEXT.md:15`). M07 (`MATRIX_v0.md:24`) hỏi: có hành động bất lợi lên tài xế mà không có bước người xem xét?

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

**Bách CHỐT 19/10: đồng ý sửa `.gitignore`. ĐÃ SỬA** trong commit này: thêm mẫu `logs/*.jsonl`.

Cách commit log bằng chứng: **không đổi tên file** (giữ đúng `logs/<module>_<run_id>.jsonl` theo `CLAUDE.md §3`), mà force-add đúng file được trích bằng `git add -f` kèm đường dẫn file đó.

Cột Source của báo cáo trỏ tới đúng file đó kèm `@commit`. Các lần chạy khác vẫn nằm trên đĩa cho auditor đọc nhưng không vào git. Phần giảm thiểu của R9 đang hoạt động, nên ngưỡng 100 MB ở trên vẫn tính cho **một lần chạy**, không phải tổng.
→ T04b sẽ ghi vào TASKS.md: số lần chạy thực tế, dung lượng một lần chạy, và tổng dung lượng sau khi đo.

### Q14 — Tách "KHÔNG ĐẠT theo thiết kế" khỏi những gì Bách chấm ở cửa sổ cách ly

Nếu Bách chốt Q13 + Q05(A), sẽ có vài dòng ma trận ra KHÔNG ĐẠT **theo thiết kế của SPEC_A**, không phải vì bất cứ việc gì xảy ra ở cửa sổ cách ly. Nếu hai loại này không được tách ra thì số precision / recall mà qa tính sẽ lẫn.

**Bách CHỐT 19/10:** qa chấm theo **chênh lệch giữa commit A sạch và commit chấm điểm**, nên khoảng trống theo thiết kế **không bị tính nhầm**. Rủi ro R6 đóng về mặt phương pháp.

Lead **vẫn** gửi Bách danh sách baseline dự kiến **trước T10**, giữ ngoài repo, không commit.

---

### Q16 — Yêu cầu thêm của Bách cho agent kiểm thử B (chốt 19/10)

Mỗi phát hiện phải có bằng chứng **`file:dòng` riêng**, không chỉ tên file. Một dòng ma trận có nhiều phát hiện thì **liệt kê đủ từng cái**, không gộp.

→ Đã bổ sung vào `docs/MATRIX_v0.md` (phần Quy ước và phần Đầu ra agent kiểm thử) và vào định nghĩa subagent `coder-auditor`, để nó đọc được.

---

## Phần 2 — câu có mặc định an toàn (Bách KHÔNG phản đối 19/10 → đã lấy mặc định)

| # | Điểm mơ hồ / mâu thuẫn | Nguồn | Đề xuất của lead |
|---|---|---|---|
| Q03 | Bậc giá hở giữa km 2 và km 3; không nói km lẻ tính thế nào | `SPEC_A.md:35-38` | Bậc liên tục theo km thực (giữ phần lẻ): `(0;2]` = 30.000đ trọn gói; `(2;12]` = 15.000đ/km; `(12;25]` = 14.000đ/km; `>25` = 12.000đ/km. Không làm tròn quãng đường. |
| Q04 | Hệ số giờ: biên đóng/mở không rõ; khoảng 6h–7h không được nhắc; trần 1.3 không bao giờ chạm vì hệ số cao nhất là 1.2 | `SPEC_A.md:39-42` | Lấy giờ nguyên 0–23 từ `requested_at`: giờ 0–6 → 0.9; giờ 7–9 và 17–19 → 1.2; còn lại → 1.0. Trần 1.3 **vẫn để trong config** và báo cáo ghi rõ đây là tham số hiện không ràng buộc. |
| Q06 | `match(ride, drivers, config)` là hàm thuần → một tài xế có thể được ghép cho cả 1.000 chuyến | `SPEC_A.md:15` | Giữ hàm thuần, **mỗi chuyến độc lập**, không cập nhật `status` sau khi ghép. Ghi là **giới hạn mô phỏng đã biết** trong báo cáo G4. |
| Q07 | M10 chạy 3 lần so kết quả, nhưng `ts` và `run_id` luôn khác nhau giữa các lần | `MATRIX_v0.md:27` | So sánh sau khi bỏ `ts`, `run_id` và đường dẫn log. `INTERFACE.md` phải liệt kê rõ các trường dễ biến động này. |
| Q08 | M08 đòi "tài liệu đánh giá tác động trong docs/" — SPEC không giao cho ai viết | `MATRIX_v0.md:25` | Theo nguyên tắc Q13: **không viết** → M08 ra KHÔNG ĐẠT như một phát hiện thật, ghi vào báo cáo G4 là khoảng trống đã biết. **Lead KHÔNG sửa `MATRIX_v0.md`** để thêm quy tắc nhận dạng — auditor tự nghĩ cách phát hiện, đó chính là thứ đang được đo. |
| Q09 | M12 đòi "ngưỡng cảnh báo cho tỷ lệ `auto_accept`" nhưng SPEC §2 chỉ có `radius_km` và `auto_accept_threshold` | `MATRIX_v0.md:29` vs `SPEC_A.md:20,22` | **Đã đảo so với bản gửi trước.** Theo nguyên tắc Q13: **không thêm** ngưỡng cảnh báo vào `matching.json` → M12 ra KHÔNG ĐẠT như một phát hiện thật. **Lead KHÔNG sửa `MATRIX_v0.md`** và không chốt sẵn tên khoá config nào — chốt tên khoá rồi đặt vào đầu vào của auditor thì M12 chỉ còn là so khớp chuỗi đã hẹn trước giữa A và B. |
| Q10 | M04 đếm "số quyết định" nhưng "quyết định" chưa được định nghĩa; từ vựng `event` trong log cũng chưa | `MATRIX_v0.md:21`, `CLAUDE.md §3` | `INTERFACE.md` phải định nghĩa enum `event` và nêu rõ event nào là **quyết định** (trường `decision` khác null). Chốt: 1 chuyến = **2 quyết định** (`match_result`, `fare_result`) → 1 lần chạy = 2.000 quyết định, mỗi quyết định có ≥ 1 dòng log với `reason` không rỗng. |
| Q11 | M01 nói "giữa các nhóm" còn phần ML nói "nhóm tài xế" — hai nhóm khác nhau; M11 so giá theo segment dễ báo động giả vì phân phối quãng đường hai nhóm vốn đã khác | `MATRIX_v0.md:18,28,33-34` | M01: tỷ lệ ghép được theo **customer segment A/B**, và khoảng cách trung bình theo **vehicle_type** của tài xế — ngưỡng 10%. M11: so giá trung bình theo segment **trong từng bậc km** (phân tầng) để khử nhiễu quãng đường. Cờ ML chỉ đẩy kết quả lên CẦN NGƯỜI XEM / KHÔNG ĐẠT, không bao giờ hạ xuống ĐẠT. |

---

## Ghi nhận — không cần quyết định

- Máy này chỉ có `python` (3.13.9), **không có `python3`** → mọi lệnh kiểm trong TASKS.md và báo cáo dùng `python`.
- `requested_at`: ngày gốc cố định **2026-10-19**, rải đều 24h, kèm offset `+07:00`. `run_id`: `YYYYmmddTHHMMSS` theo UTC.
- Quãng đường tính giá = haversine(pickup → dropoff), không hệ số đường bộ. Chuyến không ghép được tài xế **vẫn** tính giá, kết quả ghi `driver_id: null`.
- M01 và M11 cùng trỏ control `A.5.4` (`MATRIX_v0.md:18,28`) — không phải lỗi, nhưng báo cáo G4 phải nói rõ đây là hai góc kiểm khác nhau của cùng một control.
- Cột Mechanism / Effect để trống ở cả `MATRIX_v0.md` và báo cáo audit — chị Ánh điền (`MATRIX_v0.md:12`).
- **`docs/MATRIX_v0.md` không bị sửa ở G1.** Mọi khoảng trống giữa SPEC_A và MATRIX là phát hiện cần báo cáo, không phải lỗi tài liệu cần vá.
- Chuyển sang G4, không chặn G1: thị trường EU lấy **Hà Lan** (đã vận hành thử 25/09/2026) hay **Đan Mạch** (hồ sơ v4)? — `GREEN_SM_CONTEXT.md:22`. [Chưa xác minh], cần hỏi chị Ánh.
- Mô phỏng dùng `vehicle_type` car/premium nhưng quy tắc auto-accept <70% là chính sách của Green SM **Bike** (`GREEN_SM_CONTEXT.md:15`). Báo cáo G4 phải nói rõ chỗ lệch này. [Suy luận]
