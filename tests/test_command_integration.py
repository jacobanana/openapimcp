"""Tests for development command integration."""

from .test_utils import assert_tool_version, run_command


def test_format_command():
    """Test that formatting command works."""
    run_command(["uv", "run", "black", "--check", "."])


def test_lint_command():
    """Test that linting command works."""
    run_command(["uv", "run", "ruff", "check", "."])


def test_test_command():
    """Test that test command works."""
    # Test pytest command - just run a simple test to avoid recursion
    result = run_command(["uv", "run", "pytest", "tests/test_formatting.py", "-v"])
    assert "passed" in result.stdout.lower(), f"Tests didn't pass: {result.stdout}"


def test_install_command():
    """Test that dependency installation command works."""
    run_command(["uv", "sync", "--dev"])


def test_coverage_command():
    """Test that test coverage command works."""
    # Test pytest with coverage
    result = run_command(
        [
            "uv",
            "run",
            "pytest",
            "tests/test_formatting.py",
            "--cov=.",
            "--cov-report=term-missing",
        ]
    )
    assert (
        "coverage" in result.stdout.lower()
    ), f"Coverage report not generated: {result.stdout}"


def test_all_tools_available_in_venv():
    """Test that all development tools are available in the virtual environment."""
    tools = [
        (["uv", "run", "black", "--version"], "black"),
        (["uv", "run", "ruff", "--version"], "ruff"),
        (["uv", "run", "pytest", "--version"], "pytest"),
        (["uv", "run", "coverage", "--version"], "coverage"),
    ]

    for command, tool_name in tools:
        assert_tool_version(tool_name, command)
