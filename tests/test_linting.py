"""Tests for code linting compliance."""

from .test_utils import assert_linting_compliance, assert_tool_version, run_command


def test_ruff_linting_compliance():
    """Test that all Python files pass Ruff linting."""
    assert_linting_compliance(["uv", "run", "ruff", "check"], "Ruff")


def test_ruff_command_available():
    """Test that ruff command is available and working."""
    assert_tool_version("ruff", ["uv", "run", "ruff", "--version"])


def test_ruff_format_available():
    """Test that ruff format command is available (but we use Black for formatting)."""
    result = run_command(["uv", "run", "ruff", "format", "--help"])
    assert (
        "format" in result.stdout.lower()
    ), f"Ruff format help output unexpected: {result.stdout}"
