# Báo cáo chấm B — commit `83229ff`

> Chấm bởi phiên `qa` cách ly, theo đáp án riêng không đưa vào repo (CLAUDE.md §3). File này chỉ chứa số đo.

## Phạm vi chấm

- B: đóng băng tại tag `b-freeze` (`cce80bf`), không đổi giữa hai commit A dưới đây (đã xác minh `git diff b-freeze <commit> -- auditor/` rỗng ở cả hai).
- A mốc nền (C0): `2abeafd` (trước merge `security-pass`).
- A được chấm (C1): `83229ff` (sau merge `security-pass`, `[security] hardening pass`).
- Tổng số mục lỗi cài được chấm: 6. Tổng số mục sạch được chấm: 3.

## Số đếm

| | Số lượng |
|---|---|
| TP (bắt đúng lỗi cài) | 4 |
| FN (bỏ sót lỗi cài) | 2 |
| FP (báo động giả trên mục sạch) | 0 |

## Công thức và kết quả

- precision = TP / (TP + FP) = 4 / (4 + 0) = **1.000**
- recall = TP / (TP + FN) = 4 / (4 + 2) = **0.667**
- FNR = FN / (TP + FN) = 2 / (4 + 2) = **0.333**

## So với mục tiêu đề xuất [Suy luận]

| Số đo | Mục tiêu | Kết quả | Đạt? |
|---|---|---|---|
| recall | ≥ 5/6 (0.833) | 0.667 | Không |
| FNR | ≤ 1/6 (0.167) | 0.333 | Không |
| precision | (không đặt mục tiêu cứng) | 1.000 | — |

## Độ ổn định

- Chạy `python auditor/run_audit.py` 3 lần liên tiếp trên cùng commit `83229ff` (cùng mã nguồn, cùng dữ liệu mock, seed cố định).
- So sánh cả 3 bản JSON xuất ra sau khi bỏ các trường đổi theo lần chạy (`ts`, `run_id`, `product_run_id`, và run_id nhúng trong tên file log): **3/3 bản giống hệt nhau** trên toàn bộ 12 dòng ma trận (cùng `result`, cùng cấu trúc evidence/note sau chuẩn hoá).
- Kết luận: ổn định tuyệt đối trong phạm vi 3 lần chạy đo được — không phát hiện sai khác do không xác định.

## Ghi chú phương pháp

- Chấm theo **tập bằng chứng** (`file:dòng`) của từng dòng ma trận, không chấm theo nhãn ĐẠT/KHÔNG ĐẠT/CẦN NGƯỜI XEM.
- Với mỗi dòng ma trận có bằng chứng dạng `file:dòng`, lấy tập bằng chứng ở C1 trừ tập bằng chứng ở C0 (phần tử mới). Số dòng được quy chiếu qua `git diff` giữa hai commit A để biết dòng nào thực sự là nội dung mới/đổi, dòng nào chỉ trùng số do dịch dòng từ các thay đổi khác — so khớp bằng **nội dung dòng**, không chỉ số dòng.
- Một dòng ma trận **đã** CẦN NGƯỜI XEM/KHÔNG ĐẠT trên A sạch (trước khi cài lỗi) mà tập bằng chứng ở C1 không có phần tử mới, hoặc phần tử mới không rơi vào vùng mã nguồn bị thay đổi của lỗi đang xét → **không** tính là bắt được lỗi đó qua dòng này (nhãn không đổi không tự động là TP, và cũng không bị tính là FP vì nhãn đó không phải do lần cài lỗi này sinh ra).
- Một dòng ma trận không có bằng chứng dạng `file:dòng` (chỉ có bằng chứng dạng số lượng/thống kê trong log của B) vẫn được xét TP nếu số liệu đó thay đổi theo đúng cơ chế của lỗi; ghi nhận riêng vì không kiểm được bằng ánh xạ dòng.
- FP được chấm trên 3 mục sạch: dòng ma trận tương ứng phải ra ĐẠT ở C1; cả 3 đều ĐẠT nên không có FP.
- Áp dụng phương pháp trên không đổi kết quả TP/FN so với lần chấm theo nhãn trước đó, nhưng xác nhận chắc hơn: 2 dòng ma trận vốn đã CẦN NGƯỜI XEM trên A sạch có sinh bằng chứng mới ở C1, nhưng bằng chứng mới đó rơi vào vị trí của (các) lỗi khác đã được một dòng ma trận khác bắt đúng, không rơi vào vị trí của lỗi còn bị bỏ sót.
