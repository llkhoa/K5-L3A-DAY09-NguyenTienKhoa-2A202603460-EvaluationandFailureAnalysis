# PRD v1.1 — nghiệm thu luồng hoàn tiền LogiX-VN

## Pilot và trách nhiệm

Giữ luồng hoàn tiền Lab 8. Mỗi ticket gắn với một claim; agent tra đơn theo principal và gửi toàn bộ đề xuất cho host kiểm tra approval, giới hạn tiền và số đã hoàn. Pilot chỉ xét các tình huống và hạn mức trong fixture cùng policy hiện hành. Yêu cầu thiếu mã đơn cần bổ sung thông tin; đơn ngoài quyền phải chuyển chuyên viên. Tranh chấp nhiều đơn và giải ngân thật nằm ngoài phạm vi đo.

## Điều kiện nghiệm thu

So với demo thủ công v1.0, CI chạy lại cùng item và seed, chặn khi vi phạm sàn tuyệt đối hoặc khi cận trên CI 95% của hiệu PR trừ baseline âm đối với metric có quy tắc đó. Dữ liệu từ `E-swarm-20261117-8c3d`, `E-fixed-20261117-8c3d`, `E-seeded_regression-20261117-8c3d`.

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

Tiền, approval, claim sở hữu và trạng thái đều chấm bằng code. Cột grader trong [taxonomy FM-01 đến FM-09](failure_taxonomy.md) ghi cách kiểm từng lỗi bằng event, label hoặc ledger. Giọng điệu có thể dùng judge đã hiệu chuẩn; helpful chưa đạt recall. [Audit judge](judge_audit.md).

## Quyết định release

Chạy `python -m lab9.gate --pr reports/eval_pr.json --baseline reports/baseline_v1.json` từ src. Eval owner (vai trò ledger/evaluation) giữ baseline đã duyệt, đối chiếu SHA và độ phủ item × seed. Exit 1 dừng merge; người phụ trách sửa lỗi và chạy lại. Nếu đề nghị ngoại lệ, Product và Eval owner phải ghi phạm vi, lý do, bằng chứng và thời hạn trên PR trước khi duyệt. Đây là quy trình đề xuất; nhóm chưa ký phê duyệt pilot.

## Bằng chứng và phiên bản tiếp theo

MockLLM chỉ chạy trên fixture; 14 item v1 cho CI rộng và replay judge chưa có held-out mới. Lên v2 khi thêm ca adversarial, đổi nhãn hoặc định nghĩa slice; thay metric hoặc ngưỡng cần tăng metric_spec_version và giải thích. Baseline v2, ngưỡng A/A và các lỗi chỉ lộ theo slice hoặc theo seed được ghi trong [eval card](eval_card.md).
