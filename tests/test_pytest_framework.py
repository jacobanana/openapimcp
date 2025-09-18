"""Tests for pytest framework functionality."""

import pytest


@pytest.mark.core
def test_basic_pytest_functionality():
    """Test basic pytest functionality with a simple assertion."""
    # This is a meta-test - if pytest can run this test, it's working
    assert True
    assert 1 + 1 == 2
    assert "hello" in "hello world"
