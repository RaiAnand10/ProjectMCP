"""Main MCP server implementation."""

import asyncio
from pathlib import Path
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize the MCP server
server = Server("project-mcp")

# Path to data directory
DATA_DIR = Path(__file__).parent / "data"


def load_text_file(filename: str) -> str:
    """Load a text file from the data directory."""
    filepath = DATA_DIR / filename
    if filepath.exists():
        return filepath.read_text(encoding="utf-8")
    return ""


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools."""
    return [
        Tool(
            name="get_project_planning_guide",
            description="Returns the project planning guidelines for breaking down "
                        "projects/epics into work items. Use this to understand how to "
                        "decompose work into the right hierarchy and granularity.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    
    if name == "get_project_planning_guide":
        content = load_text_file("project_planning.md")
        
        if content:
            return [TextContent(
                type="text",
                text=content
            )]
        else:
            return [TextContent(
                type="text",
                text="Project planning guide not found."
            )]
    
    else:
        return [TextContent(
            type="text",
            text=f"Unknown tool: {name}"
        )]


async def run_server():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def main():
    """Entry point."""
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
