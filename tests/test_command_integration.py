"""Tests for development command integration."""

import subprocess
from pathlib import Path


def test_format_command():
    """Test that formatting command works."""
    project_root = Path(__file__).parent.parent

    # Test black formatting command
    result = subprocess.run(
        ["uv", "run", "python", "-m", "black", "--check", "."],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert (
        result.returncode == 0
    ), f"Black format command failed: {result.stderr}\nstdout: {result.stdout}"


def test_lint_command():
    """Test that linting command works."""
    project_root = Path(__file__).parent.parent

    # Test ruff linting command
    result = subprocess.run(
        ["uv", "run", "python", "-m", "ruff", "check", "."],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert (
        result.returncode == 0
    ), f"Ruff lint command failed: {result.stderr}\nstdout: {result.stdout}"


def test_test_command():
    """Test that test command works."""
    project_root = Path(__file__).parent.parent

    # Test pytest command - just run a simple test to avoid recursion
    result = subprocess.run(
        ["uv", "run", "python", "-m", "pytest", "tests/test_formatting.py", "-v"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert (
        result.returncode == 0
    ), f"Pytest command failed: {result.stderr}\nstdout: {result.stdout}"
    assert "passed" in result.stdout.lower(), f"Tests didn't pass: {result.stdout}"


def test_install_command():
    """Test that dependency installation command works."""
    project_root = Path(__file__).parent.parent

    # Test uv sync command
    result = subprocess.run(
        ["uv", "sync", "--dev"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert (
        result.returncode == 0
    ), f"UV sync command failed: {result.stderr}\nstdout: {result.stdout}"


def test_coverage_command():
    """Test that test coverage command works."""
    project_root = Path(__file__).parent.parent

    # Test pytest with coverage
    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "-m",
            "pytest",
            "tests/test_formatting.py",
            "--cov=.",
            "--cov-report=term-missing",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert (
        result.returncode == 0
    ), f"Coverage command failed: {result.stderr}\nstdout: {result.stdout}"
    assert (
        "coverage" in result.stdout.lower()
    ), f"Coverage report not generated: {result.stdout}"


def test_all_tools_available_in_venv():
    """Test that all development tools are available in the virtual environment."""
    project_root = Path(__file__).parent.parent

    tools = [
        (["uv", "run", "python", "-m", "black", "--version"], "black"),
        (["uv", "run", "python", "-m", "ruff", "--version"], "ruff"),
        (["uv", "run", "python", "-m", "pytest", "--version"], "pytest"),
        (["uv", "run", "python", "-m", "coverage", "--version"], "coverage"),
    ]

    for command, tool_name in tools:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=project_root,
        )

        assert result.returncode == 0, f"{tool_name} command failed: {result.stderr}"
        assert (
            tool_name in result.stdout.lower()
        ), f"{tool_name} version check failed: {result.stdout}"
