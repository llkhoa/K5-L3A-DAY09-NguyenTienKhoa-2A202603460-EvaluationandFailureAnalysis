# Hiệu chuẩn judge trên nhãn replay

FAIL là lớp dương. Dùng ngưỡng κ ≥ 0,60, precision ≥ 0,80, recall ≥ 0,70; cả ba phải đạt.

| Tiêu chí | n | TP / FP / FN / TN | κ | Precision | Recall | Tỷ lệ lỗi quan sát → Rogan–Gladen | Quyết định |
|---|---:|---|---:|---:|---:|---|---|
| tone_ok | 100 | 24 / 4 / 6 / 66 | 0,757 | 0,857 | 0,800 | 28% → 30% | Đủ sàn để đánh giá giọng điệu trên tập replay. |
| helpful | 100 | 9 / 0 / 21 / 70 | 0,375 | 1,000 | 0,300 | 9% → 30% | Loại khỏi gate: bỏ sót 21 trong 30 lỗi. |

| Case | Judge / người | Phán quyết audit và thay đổi rubric |
|---|---|---|
| H-008 | PASS / FAIL | Theo người. Với khách chưa quen, thêm ví dụ “anh check giúp em … nha” cho mức quá suồng sã. |
| H-017 | PASS / FAIL | Theo người trong ngữ cảnh khách lớn tuổi của nhãn. Chấm đại từ xưng hô trong ngữ cảnh, kể cả khi câu mở đầu bằng “Dạ”. |
| H-029 | PASS / FAIL | Theo người. “Không cần nhắn thêm” chặn trao đổi; xét toàn câu sau lời chào lịch sự. |
| H-042 | FAIL / PASS | Theo người. Câu ngắn vẫn nêu kết quả và thời gian; đưa vào ví dụ đạt mà không cần lời xin lỗi. |
| H-051 | FAIL / PASS | Theo người. Thêm “refund” vào danh sách thuật ngữ CS cho phép nếu thông điệp vẫn rõ. |
| H-063 | PASS / FAIL | Theo người. Lời hứa “sẽ hoàn thêm” vượt kết quả hệ thống; tách cam kết chưa được xác nhận thành tiêu chí riêng. |
| HL-015 | PASS / FAIL | Nhãn người đánh dấu sai tiền dù câu lịch sự. Dùng ledger để chấm tiền; CSV thiếu ledger để audit lại con số độc lập. |

Chạy `python -m lab9.judge --csv data/eval/judge_tone_public.csv --audit 6`, sau đó thay tên tệp bằng `judge_helpful_public.csv`. Hiệu chỉnh tỷ lệ lỗi toàn tập không sửa được từng verdict sai. Cần thu nhãn người mới giữ riêng để đo khả năng tổng quát trước pilot.
