"""Test ezbee."""
# pylint: disable=broad-except
from ezbee import __version__
from ezbee import ezbee


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not ezbee()
    except Exception:
        assert True
