"""Tests for pre-commit integration and style consistency."""

import subprocess
from pathlib import Path


def test_precommit_config_exists():
    """Test that pre-commit configuration file exists."""
    project_root = Path(__file__).parent.parent
    precommit_config = project_root / ".pre-commit-config.yaml"

    assert precommit_config.exists(), ".pre-commit-config.yaml should exist"

    # Check that the config file is not empty
    content = precommit_config.read_text()
    assert len(content) > 0, ".pre-commit-config.yaml should not be empty"
    assert "black" in content, "pre-commit config should include black"
    assert "ruff" in content, "pre-commit config should include ruff"


def test_precommit_command_available():
    """Test that pre-commit command is available."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "pre_commit", "--version"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Pre-commit command failed: {result.stderr}"
    assert (
        "pre-commit" in result.stdout.lower()
    ), f"Unexpected pre-commit version output: {result.stdout}"


def test_black_and_ruff_compatibility():
    """Test that Black and Ruff work together without conflicts."""
    project_root = Path(__file__).parent.parent

    # First run Black
    black_result = subprocess.run(
        ["uv", "run", "python", "-m", "black", "--check", "."],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Then run Ruff
    ruff_result = subprocess.run(
        ["uv", "run", "python", "-m", "ruff", "check", "."],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Both should pass
    assert (
        black_result.returncode == 0
    ), f"Black check failed: {black_result.stderr}\nstdout: {black_result.stdout}"
    assert (
        ruff_result.returncode == 0
    ), f"Ruff check failed: {ruff_result.stderr}\nstdout: {ruff_result.stdout}"


def test_style_consistency_across_files():
    """Test that all Python files follow consistent style."""
    project_root = Path(__file__).parent.parent

    # Get all Python files (excluding venv)
    python_files = list(project_root.glob("**/*.py"))
    python_files = [f for f in python_files if ".venv" not in str(f)]

    assert len(python_files) > 0, "Should find Python files to check"

    # Check each file individually with both tools
    for py_file in python_files:
        # Black check
        black_result = subprocess.run(
            ["uv", "run", "python", "-m", "black", "--check", str(py_file)],
            capture_output=True,
            text=True,
            cwd=project_root,
        )

        assert (
            black_result.returncode == 0
        ), f"Black formatting failed for {py_file}: {black_result.stderr}"

        # Ruff check
        ruff_result = subprocess.run(
            ["uv", "run", "python", "-m", "ruff", "check", str(py_file)],
            capture_output=True,
            text=True,
            cwd=project_root,
        )

        assert (
            ruff_result.returncode == 0
        ), f"Ruff linting failed for {py_file}: {ruff_result.stderr}"


def test_precommit_install_works():
    """Test that pre-commit can validate config (without actually installing)."""
    project_root = Path(__file__).parent.parent

    # Test pre-commit validate-config (doesn't actually install)
    result = subprocess.run(
        ["uv", "run", "python", "-m", "pre_commit", "validate-config"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # pre-commit validate-config should work
    assert (
        result.returncode == 0
    ), f"Pre-commit config validation failed: {result.stderr}\nstdout: {result.stdout}"
