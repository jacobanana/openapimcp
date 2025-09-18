"""Tests for code formatting compliance."""

import subprocess
import sys
from pathlib import Path


def test_black_formatting_compliance():
    """Test that all Python files are formatted with Black."""
    project_root = Path(__file__).parent.parent

    # Run black in check mode to verify formatting
    result = subprocess.run(
        [sys.executable, "-m", "black", "--check", "--diff", str(project_root)],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Black returns 0 if all files are formatted, 1 if changes are needed
    assert result.returncode == 0, (
        f"Black formatting check failed. Files need formatting:\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )


def test_black_command_available():
    """Test that black command is available and working."""
    result = subprocess.run(
        [sys.executable, "-m", "black", "--version"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Black command failed: {result.stderr}"
    assert (
        "black" in result.stdout.lower()
    ), f"Unexpected black version output: {result.stdout}"
