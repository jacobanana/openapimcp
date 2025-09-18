"""Tests for code linting compliance."""

import pytest

from .test_utils import assert_linting_compliance


@pytest.mark.extended
def test_ruff_linting_compliance():
    """Test that all Python files pass Ruff linting."""
    assert_linting_compliance(["uv", "run", "ruff", "check"], "Ruff")
