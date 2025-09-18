"""Tests for dependency management with uv."""

from .test_utils import (
    assert_dependency_available,
    assert_tool_version,
    get_project_root,
    run_command,
)


def test_uv_command_available():
    """Test that uv command is available and working."""
    assert_tool_version("uv", ["uv", "--version"])


def test_uv_sync_works():
    """Test that uv sync can install dependencies."""
    run_command(["uv", "sync", "--dev"])


def test_uv_lockfile_exists():
    """Test that uv creates and maintains a lock file."""
    project_root = get_project_root()
    lockfile = project_root / "uv.lock"

    assert lockfile.exists(), "uv.lock file should exist after dependency installation"

    # Lock file should be a valid file with content
    content = lockfile.read_text()
    assert len(content) > 0, "uv.lock file should not be empty"
    assert "package" in content.lower(), "uv.lock should contain package information"


def test_core_dependencies_available():
    """Test that core project dependencies are available."""
    # Test that we can import the core dependencies
    assert_dependency_available(["click", "httpx"], "Core dependency import failed")

    # Verify the packages are installed
    import click
    import httpx

    assert hasattr(click, "command"), "Click should be properly installed"
    assert hasattr(httpx, "Client"), "HTTPX should be properly installed"


def test_dev_dependencies_available():
    """Test that development dependencies are available."""
    # Test that we can import dev dependencies
    assert_dependency_available(["black", "pytest"], "Dev dependency import failed")

    # Verify the packages have expected functionality
    import black
    import pytest

    assert hasattr(black, "format_str"), "Black should be properly installed"
    assert hasattr(pytest, "main"), "Pytest should be properly installed"


def test_uv_run_works():
    """Test that uv run can execute commands in the virtual environment."""
    # Test running python in the uv environment
    result = run_command(["uv", "run", "python", "-c", "print('Hello from uv!')"])
    assert (
        "Hello from uv!" in result.stdout
    ), f"UV run output unexpected: {result.stdout}"
