"""Test color_map."""
from ezbee.color_map import color_map


def test_color_map():
    """Test color_map."""
    assert "background" in color_map("1.")
    assert "background" in color_map(0.21)

    assert "wrap_text" in color_map("")
    assert "wrap_text" in color_map("a")
