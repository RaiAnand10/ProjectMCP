"""Main MCP server implementation."""

import argparse
import asyncio
from dataclasses import dataclass
from pathlib import Path
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize the MCP server
server = Server("project-mcp")

# Path to data directory
DATA_DIR = Path(__file__).parent / "data"

# Mapping from team name to area path
TEAM_AREA_PATH_MAP: dict[str, str] = {
    "DK8S Observability": r"OS\Microsoft Security\Microsoft Threat Protection (MTP)\OneSOC (1SOC)\Infra and Developer Platform (SCIP-IDP)\Defender K8S Platform\DK8S Observability",
}


@dataclass
class ServerConfig:
    """Server configuration parsed from command-line arguments."""
    ado_org: str
    ado_project: str
    ado_team: str


# Global config populated at startup
config: ServerConfig | None = None


def parse_args() -> ServerConfig:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Project MCP Server for Azure DevOps project planning"
    )
    parser.add_argument(
        "ado_org",
        help="The name of the Azure DevOps organization"
    )
    parser.add_argument(
        "ado_project",
        help="The name of the Azure DevOps project"
    )
    parser.add_argument(
        "ado_team",
        help="The name of the Azure DevOps team"
    )
    
    args = parser.parse_args()
    return ServerConfig(
        ado_org=args.ado_org,
        ado_project=args.ado_project,
        ado_team=args.ado_team
    )


def get_area_path(ado_team: str | None) -> str | None:
    """Get the area path for a given team name."""
    if not ado_team:
        return None
    return TEAM_AREA_PATH_MAP.get(ado_team)


def load_text_file(filename: str) -> str:
    """Load a text file from the data directory."""
    filepath = DATA_DIR / filename
    if filepath.exists():
        return filepath.read_text(encoding="utf-8")
    return ""


def build_context_header(ado_org: str, ado_project: str, ado_team: str) -> str:
    """Build a context header with ADO organization, project, team, and area path information."""
    lines = ["## ADO Context\n"]
    lines.append(f"- **Organization:** {ado_org}")
    lines.append(f"- **Project:** {ado_project}")
    lines.append(f"- **Team:** {ado_team}")
    
    area_path = get_area_path(ado_team)
    if area_path:
        lines.append(f"- **Area Path:** {area_path}")
    
    lines.append("\n---\n")
    
    return "\n".join(lines)


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
        ),
        Tool(
            name="get_sprint_recap_guide",
            description="Returns guidelines for generating a sprint recap. Use this when "
                        "asked to create a sprint summary, iteration recap, or review of "
                        "what was accomplished in the previous sprint. The guide explains "
                        "how to query ADO for iteration data and format highlights/lowlights.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_pr_raising_guide",
            description="Returns guidelines for raising a Pull Request after completing "
                        "implementation work. Use this when ready to create a PR. The guide "
                        "covers PR description structure (What/Why/How/Testing Done), linking "
                        "work items, triggering buddy builds, and updating the PR with build status.",
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
    
    # Build context header for all tools
    context_header = build_context_header(
        config.ado_org, config.ado_project, config.ado_team
    )
    
    if name == "get_project_planning_guide":
        content = load_text_file("project_planning.md")
        
        if content:
            full_content = context_header + content
            return [TextContent(
                type="text",
                text=full_content
            )]
        else:
            return [TextContent(
                type="text",
                text="Project planning guide not found."
            )]
    
    elif name == "get_sprint_recap_guide":
        content = load_text_file("sprint_recap.md")

        if content:
            full_content = context_header + content
            return [TextContent(
                type="text",
                text=full_content
            )]
        else:
            return [TextContent(
                type="text",
                text="Sprint recap guide not found."
            )]

    elif name == "get_pr_raising_guide":
        content = load_text_file("pr_raising.md")

        if content:
            full_content = context_header + content
            return [TextContent(
                type="text",
                text=full_content
            )]
        else:
            return [TextContent(
                type="text",
                text="PR raising guide not found."
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
    global config
    config = parse_args()
    asyncio.run(run_server())


if __name__ == "__main__":
    main()