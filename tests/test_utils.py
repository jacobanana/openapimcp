"""Shared test utilities to eliminate code duplication."""

import subprocess
from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def run_command(
    command: list[str],
    cwd: Path | None = None,
    check_returncode: bool = True,
    error_message: str | None = None,
) -> subprocess.CompletedProcess:
    """Run a command and optionally check its return code."""
    if cwd is None:
        cwd = get_project_root()

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=cwd,
    )

    if check_returncode:
        default_error = f"Command {' '.join(command)} failed: {result.stderr}\nstdout: {result.stdout}"
        assert result.returncode == 0, error_message or default_error

    return result


def assert_tool_version(tool_name: str, command: list[str]) -> None:
    """Assert that a tool command returns version information containing the tool name."""
    result = run_command(command, error_message=f"{tool_name} command failed")

    assert (
        tool_name.lower() in result.stdout.lower()
    ), f"Unexpected {tool_name} version output: {result.stdout}"


def assert_formatting_compliance(tool_command: list[str], tool_name: str) -> None:
    """Assert that all Python files pass formatting compliance checks."""
    project_root = get_project_root()

    run_command(
        tool_command + [str(project_root)],
        error_message=f"{tool_name} formatting check failed. Files need formatting",
    )


def assert_linting_compliance(tool_command: list[str], tool_name: str) -> None:
    """Assert that all Python files pass linting checks."""
    project_root = get_project_root()

    run_command(
        tool_command + [str(project_root)],
        error_message=f"{tool_name} linting check failed. Issues found",
    )


def get_python_files(exclude_venv: bool = True) -> list[Path]:
    """Get all Python files in the project."""
    project_root = get_project_root()
    python_files = list(project_root.glob("**/*.py"))

    if exclude_venv:
        python_files = [f for f in python_files if ".venv" not in str(f)]

    return python_files


def assert_dependency_available(module_names: list[str], error_context: str) -> None:
    """Assert that Python modules can be imported."""
    try:
        for module_name in module_names:
            __import__(module_name)
    except ImportError as e:
        raise AssertionError(f"{error_context}: {e}") from e
