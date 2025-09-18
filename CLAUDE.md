# OpenAPI to MCP server CLI tool

This project is a python based CLI tool that will take OpenAPI specs and host them as MCP Servers.

**Stack:**
- python 3.11 or greater
- [FastMCP](https://gofastmcp.com/integrations/openapi)
- Click
- [HTTPX](https://www.python-httpx.org/) (asynchronous)

**Tooling:**
- uv
- pytest
- black
- ruff

**Packaging:**
- distribute as wheels (easy installation with pipx)
- distribute as docker image