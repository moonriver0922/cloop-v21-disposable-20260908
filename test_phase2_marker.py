from pathlib import Path


def test_phase2_marker_complete() -> None:
    assert (
        Path(__file__).with_name("phase2_marker.txt").read_text(encoding="utf-8").strip()
        == "LOOP_PHASE_2_COMPLETE"
    )
