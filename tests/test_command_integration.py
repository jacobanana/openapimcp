"""Tests for development command integration."""

import pytest

from .test_utils import run_command


@pytest.mark.extended
def test_format_command():
    """Test that formatting command works."""
    run_command(["uv", "run", "black", "--check", "."])


@pytest.mark.extended
def test_lint_command():
    """Test that linting command works."""
    run_command(["uv", "run", "ruff", "check", "."])
