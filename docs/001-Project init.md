# OpenAPI to MCP Server CLI Tool

We want to build a CLI tool that will create MCP servers based on OpenAPI specifications. The idea is to use it to hot load an api either from a file or a URL and serve that as an MCP server.

## Validate

```
openapimcp validate --api https://www.example.com/openapi.json
```

Reads and validates the OpenAPI spec. This should tell the user if there are any errors in the spec of if it's ok to proceed.
This should work for both local and hosted specs.


## Serve

1. Serve a hosted API spec:

```
openapimcp serve --api https://www.example.com/openapi.json --url https://www.example.com/api/v1
```

2. Serve a local API spec
```
openapimcp serve --api ./path/to/openapi.json --url https://www.example.com/api/v1
```

The --url argument should be optional. We should be able to derive the url from the spec if it's present.
If multiple urls are available in the spec, there should also be an argument to specify which one to use. For example `--server prod` or `--server dev`


## Describe

```
openapimcp describe --api https://www.example.com/openapi.json
```

Prints a formatted human readable description of what the MCP tools will be.