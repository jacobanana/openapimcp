"""Tests for code linting compliance."""

import subprocess
import sys
from pathlib import Path


def test_ruff_linting_compliance():
    """Test that all Python files pass Ruff linting."""
    project_root = Path(__file__).parent.parent

    # Run ruff check to verify linting
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", str(project_root)],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Ruff returns 0 if no issues, non-zero if issues found
    assert result.returncode == 0, (
        f"Ruff linting check failed. Issues found:\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )


def test_ruff_command_available():
    """Test that ruff command is available and working."""
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "--version"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Ruff command failed: {result.stderr}"
    assert (
        "ruff" in result.stdout.lower()
    ), f"Unexpected ruff version output: {result.stdout}"


def test_ruff_format_available():
    """Test that ruff format command is available (but we use Black for formatting)."""
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--help"],
        capture_output=True,
        text=True,
    )

    # Ruff format help should work
    assert result.returncode == 0, f"Ruff format help failed: {result.stderr}"
    assert (
        "format" in result.stdout.lower()
    ), f"Ruff format help output unexpected: {result.stdout}"
