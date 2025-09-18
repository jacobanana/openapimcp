"""Tests for code formatting compliance."""

import pytest

from .test_utils import assert_formatting_compliance


@pytest.mark.extended
def test_black_formatting_compliance():
    """Test that all Python files are formatted with Black."""
    assert_formatting_compliance(["uv", "run", "black", "--check", "--diff"], "Black")
