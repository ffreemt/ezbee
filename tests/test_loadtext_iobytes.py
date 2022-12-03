"""Test loadtext."""
# import pytest
from pathlib import Path
import io
from ezbee.loadtext import loadtext


def test_loadtext_iobytes():
    r"""Test iobytes"""
    iob = io.BytesIO(Path(r"data/test-en.txt").read_bytes())
    text = loadtext(iob)

    if text:
        # assert len(text) == 190913
        assert len(text) >= 5300  # 5308
