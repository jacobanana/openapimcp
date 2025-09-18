"""Tests for code formatting compliance."""

from .test_utils import assert_formatting_compliance, assert_tool_version


def test_black_formatting_compliance():
    """Test that all Python files are formatted with Black."""
    assert_formatting_compliance(["uv", "run", "black", "--check", "--diff"], "Black")


def test_black_command_available():
    """Test that black command is available and working."""
    assert_tool_version("black", ["uv", "run", "black", "--version"])
