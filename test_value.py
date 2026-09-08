from pathlib import Path


def test_value_is_one_before_fixture_task() -> None:
    assert Path(__file__).with_name("value.txt").read_text(encoding="utf-8").strip() == "1"
