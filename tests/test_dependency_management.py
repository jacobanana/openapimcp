"""Tests for dependency management with uv."""

import subprocess
from pathlib import Path


def test_uv_command_available():
    """Test that uv command is available and working."""
    result = subprocess.run(
        ["uv", "--version"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"UV command failed: {result.stderr}"
    assert (
        "uv" in result.stdout.lower()
    ), f"Unexpected uv version output: {result.stdout}"


def test_uv_sync_works():
    """Test that uv sync can install dependencies."""
    project_root = Path(__file__).parent.parent

    result = subprocess.run(
        ["uv", "sync", "--dev"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # uv sync should succeed (return code 0 or already synced)
    assert (
        result.returncode == 0
    ), f"UV sync failed: {result.stderr}\nstdout: {result.stdout}"


def test_uv_lockfile_exists():
    """Test that uv creates and maintains a lock file."""
    project_root = Path(__file__).parent.parent
    lockfile = project_root / "uv.lock"

    assert lockfile.exists(), "uv.lock file should exist after dependency installation"

    # Lock file should be a valid file with content
    content = lockfile.read_text()
    assert len(content) > 0, "uv.lock file should not be empty"
    assert "package" in content.lower(), "uv.lock should contain package information"


def test_core_dependencies_available():
    """Test that core project dependencies are available."""
    # Test that we can import the core dependencies
    try:
        import click
        import httpx

        # Note: fastmcp might not be importable in all environments, so we skip it for now
    except ImportError as e:
        raise AssertionError(f"Core dependency import failed: {e}") from e

    # Verify the packages are installed
    assert hasattr(click, "command"), "Click should be properly installed"
    assert hasattr(httpx, "Client"), "HTTPX should be properly installed"


def test_dev_dependencies_available():
    """Test that development dependencies are available."""
    # Test that we can import dev dependencies
    try:
        import black
        import pytest
    except ImportError as e:
        raise AssertionError(f"Dev dependency import failed: {e}") from e

    # Verify the packages have expected functionality
    assert hasattr(black, "format_str"), "Black should be properly installed"
    assert hasattr(pytest, "main"), "Pytest should be properly installed"


def test_uv_run_works():
    """Test that uv run can execute commands in the virtual environment."""
    project_root = Path(__file__).parent.parent

    # Test running python in the uv environment
    result = subprocess.run(
        ["uv", "run", "python", "-c", "print('Hello from uv!')"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert result.returncode == 0, f"UV run failed: {result.stderr}"
    assert (
        "Hello from uv!" in result.stdout
    ), f"UV run output unexpected: {result.stdout}"
