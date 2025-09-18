"""Tests for pre-commit integration and style consistency."""

import pytest

from .test_utils import get_project_root


@pytest.mark.core
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
