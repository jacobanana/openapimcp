# Contributing to OpenAPI MCP CLI

## Development Setup

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup the project**:
   ```bash
   git clone <repository-url>
   cd openapimcp
   uv sync --dev
   ```

## Development Commands

### Code Formatting
```bash
# Check formatting
uv run python -m black --check .

# Apply formatting
uv run python -m black .
```

### Code Linting
```bash
# Check linting
uv run python -m ruff check .

# Fix auto-fixable issues
uv run python -m ruff check --fix .
```

### Testing
```bash
# Run all tests
uv run python -m pytest

# Run with coverage
uv run python -m pytest --cov=. --cov-report=term-missing

# Run specific test file
uv run python -m pytest tests/test_formatting.py -v
```

### Dependency Management
```bash
# Install/update dependencies
uv sync --dev

# Add new dependency
uv add <package-name>

# Add development dependency
uv add --dev <package-name>
```

### Pre-commit Hooks (Optional)
```bash
# Install pre-commit hooks
uv run python -m pre_commit install

# Run hooks manually
uv run python -m pre_commit run --all-files
```

### All-in-One Quality Check
```bash
# Run all quality checks
uv run python -m black --check . && uv run python -m ruff check . && uv run python -m pytest
```

## Code Style Guidelines

- **Line length**: 88 characters (Black default)
- **Import sorting**: Handled by Ruff
- **Code formatting**: Handled by Black
- **Linting**: Handled by Ruff with project-specific rules
- **Testing**: Use pytest with descriptive test names

## Project Structure

```
openapimcp/
├── main.py                 # Main CLI entry point
├── tests/                  # Test files
│   ├── test_*.py          # Test modules
│   └── __init__.py
├── pyproject.toml         # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks configuration
└── CONTRIBUTING.md        # This file
```

## Quality Standards

All code must:
- Pass Black formatting checks
- Pass Ruff linting checks
- Have test coverage for new functionality
- Pass all existing tests

Contributors can verify their changes meet these standards by running the quality check command above.