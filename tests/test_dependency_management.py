"""Tests for dependency management with uv."""

import pytest

from .test_utils import assert_dependency_available


@pytest.mark.core
def test_core_dependencies_available():
    """Test that core project dependencies are available."""
    # Test that we can import the core dependencies
    assert_dependency_available(["click", "httpx"], "Core dependency import failed")

    # Verify the packages are installed
    import click
    import httpx

    assert hasattr(click, "command"), "Click should be properly installed"
    assert hasattr(httpx, "Client"), "HTTPX should be properly installed"


@pytest.mark.extended
def test_dev_dependencies_available():
    """Test that development dependencies are available."""
    # Test that we can import dev dependencies
    assert_dependency_available(["black", "pytest"], "Dev dependency import failed")

    # Verify the packages have expected functionality
    import black
    import pytest

    assert hasattr(black, "format_str"), "Black should be properly installed"
    assert hasattr(pytest, "main"), "Pytest should be properly installed"
