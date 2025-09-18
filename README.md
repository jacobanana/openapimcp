# OpenAPI MCP CLI Tool

Transform OpenAPI specifications into MCP (Model Context Protocol) servers for enhanced AI model integration and tooling.

## Installation

Install the CLI tool using pipx (recommended):

```bash
pipx install openapimcp
```

Or using pip:

```bash
pip install openapimcp
```

## Quick Start

1. **Display help information:**
   ```bash
   openapimcp --help
   ```

2. **Check version:**
   ```bash
   openapimcp --version
   ```

3. **View tool information and dependencies:**
   ```bash
   openapimcp info
   ```

4. **Start an MCP server (coming soon):**
   ```bash
   openapimcp serve start --spec path/to/openapi.yaml --port 8000
   ```

5. **Validate an OpenAPI spec (coming soon):**
   ```bash
   openapimcp validate spec path/to/openapi.yaml
   ```

## Features

- CLI Foundation: Professional command-line interface with help and version information
- Dependency Management: Automatic handling of FastMCP, Click, and HTTPX dependencies
- Extensible Architecture: Command groups ready for OpenAPI and MCP functionality
- MCP Server Generation: Transform OpenAPI specs into MCP servers (coming soon)
- OpenAPI Validation: Validate OpenAPI specifications (coming soon)

## Requirements

- Python 3.11 or higher
- FastMCP, Click, and HTTPX (automatically installed)

## Development

This project uses modern Python packaging with uv for dependency management:

```bash
# Install dependencies
uv sync --dev

# Run the CLI in development
uv run openapimcp --help

# Run tests
uv run pytest -m core

# Format code
uv run black .

# Lint code
uv run ruff check .
```

## License

MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## Roadmap

- OpenAPI specification parsing and validation
- MCP server generation from OpenAPI specs
- Support for multiple OpenAPI versions (3.0, 3.1)
- Plugin system for custom transformations
- Docker support for containerized MCP servers

## Support

- GitHub Issues: Report bugs or request features
- Documentation: View the docs

Built with care for the AI development community.