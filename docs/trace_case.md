# C-002@11 — lần ghi đè đầu tiên

Run `E-seeded_regression-20261117-8c3d`, item E-002. Nhãn yêu cầu denied và 0đ. Ledger có một giao dịch 20.000đ, reply cũng báo 20.000đ. Vì vậy grader đối chiếu reply với ledger vẫn pass, còn RefundAmountCorrect và TrialPass đều fail.

| Bước | seeded_regression | fixed, cùng claim và seed |
|---|---|---|
| 1 | Handoff điều tra chỉ đọc cho claim. | Cùng phạm vi. |
| 2 | Investigator đọc được O-202, DB ghi trễ 2 ngày. | Cùng dữ kiện. |
| **3** | **model_override** ghi `{"delay_days": 5}`, lấy số trên ticket thay DB (FM-03). | Quote 0đ, lý do no_entitlement. |
| Sau đó | Bước 4 quote 20.000đ, bước 5 đọc lịch sử 0đ, bước 6 báo đã hoàn. | Bước 4 trả lời từ chối, ledger không có giao dịch. |

Trong thư mục `src`, chạy `python -m lab9.trace_case --shape seeded_regression --claim C-002 --seed 11`, lặp lại với `--shape fixed`. Test `tests/test_lab9_trace_case.py::test_c002_ticket_cannot_replace_db_delay` kiểm sự kiện ghi đè, ledger và verdict trên cả hai shape. Trace xác định thao tác sai đầu tiên quan sát được; không cho biết suy luận nội bộ của một model thật.
