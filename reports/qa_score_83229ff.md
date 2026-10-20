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

- TP/FN được chấm theo cặp (C0, C1): một mục lỗi cài được tính TP khi có dòng ma trận chuyển từ ĐẠT ở C0 sang KHÔNG ĐẠT/CẦN NGƯỜI XEM ở C1 **với bằng chứng mới trỏ đúng vị trí cụ thể** của lỗi đó (không chỉ trùng tên file); nếu dòng ma trận không đổi trạng thái và không có bằng chứng mới gắn với lỗi cụ thể, tính là FN dù trạng thái đang là CẦN NGƯỜI XEM từ trước.
- FP được chấm trên 3 mục sạch: dòng ma trận tương ứng phải ra ĐẠT ở C1; cả 3 đều ĐẠT nên không có FP.
