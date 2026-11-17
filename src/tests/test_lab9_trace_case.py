import pytest

pytestmark = pytest.mark.student


@pytest.mark.parametrize("shape, correct", [("seeded_regression", False), ("fixed", True)])
def test_c002_ticket_cannot_replace_db_delay(shape, correct):
    from lab9.trace_case import investigate

    case = investigate(shape, "C-002", 11)
    trial = case["trial"]
    kept_db = all(e["kind"] != "model_override" for e in trial["events"])
    assert kept_db is correct
    assert (trial["snapshot"]["refund_vnd"] == case["label"]["refund_vnd"]) is correct
    assert trial["lab8_pass"] is correct
