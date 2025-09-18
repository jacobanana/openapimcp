# Breakdown – OpenAPI MCP CLI

## Checklist

- [x] **ID:** 001
  **Title:** Set up project structure and dependencies
  **Type:** technical
  **Description:** Create the Python project structure with proper packaging configuration, install core dependencies (FastMCP, Click, HTTPX), and set up development tooling (uv, pytest, black, ruff). Establish the basic CLI entry point and package structure to support the three main commands. 
  **DoR:** Inputs=project requirements; Outputs=working Python package with CLI skeleton; Acceptance hint=can run `openapimcp --help`; Deps=none

- [ ] **ID:** 002
  **Title:** Implement OpenAPI spec loading and parsing
  **Type:** technical
  **Description:** Create a core module to load OpenAPI specifications from both local files and remote URLs using HTTPX. Handle JSON and YAML formats, implement proper error handling for network failures and malformed specs. This foundational capability will be used by all three commands. 
  **DoR:** Inputs=file path or URL; Outputs=parsed OpenAPI spec object; Acceptance hint=can load specs from file and URL; Deps=001

- [ ] **ID:** 003
  **Title:** Implement validate command
  **Type:** functional
  **Description:** Build the validate command that loads an OpenAPI spec and performs comprehensive validation checks. Report any schema errors, missing required fields, or structural issues in a user-friendly format. This gives users confidence before proceeding to serve the API. 
  **DoR:** Inputs=OpenAPI spec path/URL; Outputs=validation report with pass/fail status; Acceptance hint=reports specific validation errors; Deps=002

- [ ] **ID:** 004
  **Title:** Implement describe command
  **Type:** functional
  **Description:** Create the describe command that analyzes an OpenAPI spec and generates a human-readable summary of what MCP tools will be created. Show endpoints, methods, parameters, and brief descriptions in a formatted output that helps users understand the resulting MCP server capabilities. 
  **DoR:** Inputs=OpenAPI spec path/URL; Outputs=formatted description of MCP tools; Acceptance hint=shows clear summary of endpoints and tools; Deps=002

- [ ] **ID:** 005
  **Title:** Implement server URL resolution
  **Type:** technical
  **Description:** Create logic to determine the base URL for API calls from the OpenAPI spec's servers array. Handle cases where URL is provided via command line, derived from spec, or multiple servers are available. Implement server selection by name (e.g., `--server prod`) when multiple options exist. 
  **DoR:** Inputs=OpenAPI spec + optional URL/server args; Outputs=resolved base URL; Acceptance hint=correctly selects server URL; Deps=002

- [ ] **ID:** 006
  **Title:** Implement basic MCP server with STDIO transport
  **Type:** functional
  **Description:** Build the core serve command that converts OpenAPI endpoints into MCP tools and runs an MCP server using STDIO transport. Each OpenAPI endpoint becomes an MCP tool that can make HTTP requests to the actual API. Use FastMCP for the MCP server implementation. 
  **DoR:** Inputs=OpenAPI spec + base URL; Outputs=running MCP server on STDIO; Acceptance hint=MCP client can connect and see tools; Deps=005

- [ ] **ID:** 007
  **Title:** Add HTTP transport support
  **Type:** technical
  **Description:** Extend the serve command to support streamable HTTP transport in addition to STDIO. Add the `--transport` argument with STDIO as default. Implement proper HTTP server setup while maintaining the same MCP tool functionality. 
  **DoR:** Inputs=transport type argument; Outputs=MCP server on specified transport; Acceptance hint=works with both STDIO and HTTP; Deps=006

- [ ] **ID:** 008
  **Title:** Implement dynamic tool generation from OpenAPI operations
  **Type:** technical
  **Description:** Create comprehensive mapping from OpenAPI operations to MCP tools, handling different HTTP methods, path parameters, query parameters, request bodies, and response schemas. Generate proper tool schemas that MCP clients can understand and use effectively. 
  **DoR:** Inputs=OpenAPI operations; Outputs=MCP tool definitions; Acceptance hint=tools match OpenAPI spec exactly; Deps=006

- [ ] **ID:** 009
  **Title:** Add authentication and headers support
  **Type:** technical
  **Description:** Implement support for API authentication schemes defined in OpenAPI specs (API keys, bearer tokens, basic auth). Allow passing authentication credentials via command line arguments or environment variables, and properly forward them in HTTP requests to the target API. 
  **DoR:** Inputs=auth scheme from spec + credentials; Outputs=authenticated HTTP requests; Acceptance hint=can call protected endpoints; Deps=008

- [ ] **ID:** 010
  **Title:** Package for distribution
  **Type:** technical
  **Description:** Set up packaging configuration for wheel distribution via PyPI and Docker image creation. Ensure the CLI tool can be easily installed with pipx and run as a Docker container. Include proper entry points and metadata for both distribution methods. 
  **DoR:** Inputs=working CLI tool; Outputs=wheel package + Docker image; Acceptance hint=can install with pipx and run in Docker; Deps=009