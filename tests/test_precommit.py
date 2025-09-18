"""Tests for pre-commit integration and style consistency."""

from .test_utils import (
    assert_tool_version,
    get_project_root,
    get_python_files,
    run_command,
)


def test_precommit_config_exists():
    """Test that pre-commit configuration file exists."""
    project_root = get_project_root()
    precommit_config = project_root / ".pre-commit-config.yaml"

    assert precommit_config.exists(), ".pre-commit-config.yaml should exist"

    # Check that the config file is not empty
    content = precommit_config.read_text()
    assert len(content) > 0, ".pre-commit-config.yaml should not be empty"
    assert "black" in content, "pre-commit config should include black"
    assert "ruff" in content, "pre-commit config should include ruff"


def test_precommit_command_available():
    """Test that pre-commit command is available."""
    assert_tool_version("pre-commit", ["uv", "run", "pre-commit", "--version"])


def test_black_and_ruff_compatibility():
    """Test that Black and Ruff work together without conflicts."""
    # First run Black
    run_command(["uv", "run", "black", "--check", "."])
    # Then run Ruff
    run_command(["uv", "run", "ruff", "check", "."])


def test_style_consistency_across_files():
    """Test that all Python files follow consistent style."""
    python_files = get_python_files(exclude_venv=True)
    assert len(python_files) > 0, "Should find Python files to check"

    # Check each file individually with both tools
    for py_file in python_files:
        # Black check
        run_command(["uv", "run", "black", "--check", str(py_file)])
        # Ruff check
        run_command(["uv", "run", "ruff", "check", str(py_file)])


def test_precommit_install_works():
    """Test that pre-commit can validate config (without actually installing)."""
    # Test pre-commit validate-config (doesn't actually install)
    run_command(["uv", "run", "pre-commit", "validate-config"])
