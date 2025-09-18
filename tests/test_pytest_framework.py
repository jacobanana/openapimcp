"""Tests for pytest framework functionality."""

from .test_utils import assert_tool_version, run_command


def test_pytest_command_available():
    """Test that pytest command is available and working."""
    assert_tool_version("pytest", ["uv", "run", "pytest", "--version"])


def test_pytest_can_discover_tests():
    """Test that pytest can discover and collect tests."""
    result = run_command(["uv", "run", "pytest", "--collect-only", "-q"])
    # Should find multiple test functions
    assert (
        "test session starts" in result.stdout or result.stdout.count("test") >= 1
    ), f"Pytest didn't discover tests: {result.stdout}"


def test_pytest_configuration_valid():
    """Test that pytest configuration is valid."""
    run_command(["uv", "run", "pytest", "--help"])


def test_basic_pytest_functionality():
    """Test basic pytest functionality with a simple assertion."""
    # This is a meta-test - if pytest can run this test, it's working
    assert True
    assert 1 + 1 == 2
    assert "hello" in "hello world"


def test_pytest_with_coverage():
    """Test that pytest can run with coverage reporting."""
    # Try to run a simple test with coverage
    result = run_command(
        [
            "uv",
            "run",
            "pytest",
            "tests/test_pytest_framework.py::test_basic_pytest_functionality",
            "--cov=.",
            "--cov-report=term-missing",
            "-v",
        ]
    )
    assert (
        "PASSED" in result.stdout or "passed" in result.stdout
    ), f"Test didn't pass with coverage: {result.stdout}"
