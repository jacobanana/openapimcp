"""CLI interface for OpenAPI MCP tool."""

import click
import httpx
import fastmcp
from importlib.metadata import version as get_version
from . import __version__


@click.group()
@click.version_option(version=__version__, prog_name="openapimcp")
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="Enable verbose output for debugging."
)
@click.pass_context
def cli(ctx, verbose):
    """OpenAPI to MCP server CLI tool.

    Transform OpenAPI specifications into MCP (Model Context Protocol) servers
    for enhanced AI model integration and tooling.

    Use 'openapimcp COMMAND --help' for help on specific commands.
    """
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose

    if verbose:
        click.echo("Verbose mode enabled.")


@click.group("serve")
def serve_commands():
    """Commands for serving OpenAPI specifications as MCP servers."""
    pass


@click.group("validate")
def validate_commands():
    """Commands for validating OpenAPI specifications."""
    pass


@serve_commands.command("start")
@click.option(
    "--spec", "-s",
    required=True,
    type=click.Path(exists=True),
    help="Path to the OpenAPI specification file."
)
@click.option(
    "--port", "-p",
    default=8000,
    type=int,
    help="Port to serve the MCP server on (default: 8000)."
)
@click.pass_context
def serve_start(ctx, spec, port):
    """Start an MCP server from an OpenAPI specification."""
    if ctx.obj.get('verbose'):
        click.echo(f"Starting MCP server for spec: {spec}")
        click.echo(f"Port: {port}")

    click.echo("🚧 Coming soon: MCP server functionality")
    click.echo(f"Will serve OpenAPI spec '{spec}' on port {port}")


@validate_commands.command("spec")
@click.argument("spec_file", type=click.Path(exists=True))
@click.pass_context
def validate_spec(ctx, spec_file):
    """Validate an OpenAPI specification file."""
    if ctx.obj.get('verbose'):
        click.echo(f"Validating OpenAPI spec: {spec_file}")

    click.echo("🚧 Coming soon: OpenAPI validation")
    click.echo(f"Will validate spec file: {spec_file}")


# Add command groups to main CLI
cli.add_command(serve_commands)
cli.add_command(validate_commands)


@cli.command()
def info():
    """Display information about the OpenAPI MCP tool."""
    click.echo("OpenAPI MCP CLI Tool")
    click.echo(f"Version: {__version__}")
    click.echo("Transform OpenAPI specs into MCP servers for AI integration.")
    click.echo()
    click.echo("Core Dependencies:")
    try:
        click.echo(f"  • Click: {get_version('click')}")
    except Exception:
        click.echo("  • Click: Available")

    try:
        click.echo(f"  • HTTPX: {get_version('httpx')}")
    except Exception:
        click.echo("  • HTTPX: Available")

    try:
        click.echo(f"  • FastMCP: {get_version('fastmcp')}")
    except Exception:
        click.echo("  • FastMCP: Available")
    click.echo()
    click.echo("Ready to process OpenAPI specifications!")


if __name__ == "__main__":
    cli()