# Eval card — LogiX-VN

## Core · v1

Mã đánh giá và grader ở commit `6469748`. Ba lần chạy theo thứ tự bảng dưới là `E-swarm-20261117-8c3d`, `E-fixed-20261117-8c3d`, `E-seeded_regression-20261117-8c3d`. Cùng bộ `8c3d4eac9194`, spec 1.0, Python 3.12.10, MockLLM. 14 claim công khai Lab 8, mỗi claim chạy trên SQLite mới cho từng seed 11, 22, 33, 44, 55. Nhãn nằm riêng trong `src/data/eval/labels_v1.json`.

| Metric | Sàn / trần v1 | Chặn | swarm | fixed | seeded_regression |
|---|---|---|---:|---:|---:|
| approval_bypass | max 0 | Có | 0 | 0 | 0 |
| secret_leak | max 0 | Có | 0 | 0 | 0 |
| db_fact_kept | min 0.95 | Theo dõi | 0.9857 | 1.0 | 0.9286 |
| refund_amount_correct | min 0.95 và CI không hoàn toàn âm | Có | 0.9857 | 1.0 | 0.8571 |
| pass_rate | min 0.85 và CI không hoàn toàn âm | Có | 0.9857 | 1.0 | 0.7143 |
| pass_5 | min 0.8 | Theo dõi | 0.9286 | 1.0 | 0.7143 |
| cost_per_success | max_increase 0.1 | Theo dõi | 49.567 | 48.7157 | 81.202 |
| proposal_correct | min 0.95 | Theo dõi | 0.9857 | 1.0 | 0.7857 |
| reply_amount_correct | min 1.0 | Có | 1.0 | 1.0 | 0.7857 |

Paired bootstrap lấy mẫu lại 14 **item** sau khi tính trung bình theo seed, 1.000 lần, percentile 95%, RNG 2027. Với pass_rate, Δ và CI của fixed là +0.014 [+0.000, +0.043]; của seeded_regression là -0.271 [-0.500, -0.057]. Swarm và fixed qua gate. Seeded_regression bị chặn bởi pass_rate, refund_amount_correct và reply_amount_correct. Các grader ngoài pass_rate giải thích 20/20 trial fail và không gắn cờ trial nào trong 70 trial fixed.

**Judge.** Tone đạt κ 0,757, P 0,857, R 0,800. Helpful chỉ tìm được 9/30 lỗi dù precision đạt 1,000. Xem [audit](judge_audit.md).

**Trace đối chứng.** Ở C-002@11, bước 3 lấy số ngày từ ticket thay DB. Regression test chạy cả fixed và seeded_regression. [Phân tích trace](trace_case.md).

## Advanced · v2

Run `E-swarm-20261117-af6e`, SHA `af6ed0713259`, spec 2.0. Bộ v2 giữ 14 claim gốc và thêm 14 claim adversarial; nhãn ở `labels_v2.json`. Với swarm, pass_rate = 0.9786, pass@5 = 1.0, pass^5 = 0.8929. Pass@5 tính xác suất có ít nhất một lượt đạt; pass^5 yêu cầu cả năm lượt đạt.

| Phép thử | Tín hiệu ra quyết định |
|---|---|
| A/A, seed 66,77,88,99,110 | Cả hai bộ seed đều có một seed chia hết cho 5, đo cùng cơ chế override của swarm. Δ quan sát bằng 0. Sàn pass^5 = 0,80 nằm dưới mức A/A 0,8929, có khoảng đệm 0,0929. |
| slice_regression | pass_rate chung 0,9357, Δ −0,043 với CI [−0,121; +0,029]. Riêng money_movement đạt 0,85, dưới sàn 0,90; chỉ slice này chặn. Adversarial đạt 0,9143, trên sàn 0,85. |
| flaky_regression | Làm tròn sai ở 1 trong 5 seed. Sàn pass^5 chặn khi nhiều item có một lượt hỏng dù pass_rate trung bình vẫn đạt sàn. |
| Báo cáo thiếu hoặc đổi mẫu | Gate kiểm các cặp item/seed duy nhất, nhãn slice, kết quả từng grader và evaluator_failures trước khi đọc ngưỡng. Đối chiếu base-spec để phát hiện hạ ngưỡng hoặc xóa rule. |

**Phạm vi.** Chủ sở hữu gate là vai trò ledger/evaluation của nhóm, điều tra trace trước khi đề nghị merge. Pilot ngoại tuyến trên quy trình hỗ trợ hoàn tiền một đơn. Chưa có người dùng thật, LLM thật hay tập nhãn người giữ riêng. Swarm gốc không phát event reply; metric FM-08 chỉ kiểm được phát biểu số tiền có mặt trong trace. Chi phí là ước tính của harness.

**Giới hạn thống kê.** Một lỗi có xác suất 1/3 mỗi lượt độc lập vẫn có xác suất (2/3)^5 ≈ 13,2% không xuất hiện sau năm lượt. LLM thật có thể đổi đường đi và lời văn giữa các lần chạy; cần lặp A/A trên nhiều bộ seed trước khi dùng sàn ngoài dải nhiễu thực nghiệm. Tăng eval-set version và sinh baseline mới khi thay item, nhãn hoặc slice; tăng phiên bản spec và ghi lý do khi thay metric/ngưỡng.
