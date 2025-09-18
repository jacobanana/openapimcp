"""Tests for pytest framework functionality."""

import subprocess
import sys
from pathlib import Path


def test_pytest_command_available():
    """Test that pytest command is available and working."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--version"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Pytest command failed: {result.stderr}"
    assert (
        "pytest" in result.stdout.lower()
    ), f"Unexpected pytest version output: {result.stdout}"


def test_pytest_can_discover_tests():
    """Test that pytest can discover and collect tests."""
    project_root = Path(__file__).parent.parent

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert result.returncode == 0, f"Pytest collection failed: {result.stderr}"
    # Should find multiple test functions
    assert (
        "test session starts" in result.stdout or result.stdout.count("test") >= 1
    ), f"Pytest didn't discover tests: {result.stdout}"


def test_pytest_configuration_valid():
    """Test that pytest configuration is valid."""
    project_root = Path(__file__).parent.parent

    # Run pytest with config validation
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--help"],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert result.returncode == 0, f"Pytest config validation failed: {result.stderr}"


def test_basic_pytest_functionality():
    """Test basic pytest functionality with a simple assertion."""
    # This is a meta-test - if pytest can run this test, it's working
    assert True
    assert 1 + 1 == 2
    assert "hello" in "hello world"


def test_pytest_with_coverage():
    """Test that pytest can run with coverage reporting."""
    project_root = Path(__file__).parent.parent

    # Try to run a simple test with coverage
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/test_pytest_framework.py::test_basic_pytest_functionality",
            "--cov=.",
            "--cov-report=term-missing",
            "-v",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    # Coverage might not be 100% but pytest should run successfully
    assert (
        result.returncode == 0
    ), f"Pytest with coverage failed: {result.stderr}\nstdout: {result.stdout}"
    assert (
        "PASSED" in result.stdout or "passed" in result.stdout
    ), f"Test didn't pass with coverage: {result.stdout}"
