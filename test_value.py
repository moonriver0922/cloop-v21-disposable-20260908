from pathlib import Path


def test_value_is_two() -> None:
    assert Path(__file__).with_name("value.txt").read_text(encoding="utf-8").strip() == "2"
