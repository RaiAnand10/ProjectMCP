# Project MCP Server

A project-aware MCP (Model Context Protocol) server that provides project planning guidelines for GitHub Copilot to act as a project buddy in VS Code.

## Purpose

This MCP server provides structured guidelines for breaking down projects and epics into well-defined deliverables and tasks, optimized for AI-assisted development.

## Tools

### `get_project_planning_guide`
Returns comprehensive guidelines for decomposing projects/epics into work items.

**Parameters:** None

**Returns:** Project planning guidelines including:
- Hierarchy structure (Epic → Deliverable → Task)
- Decomposition rules (size, scope, independence)
- Best practices for AI-executable tasks
- Anti-patterns to avoid

## Installation

```bash
# Install the MCP package (required dependency)
pip install mcp

# Install this package directly
pip install -e /home/anandkuma/repos/ProjectMCP
```

## VS Code Configuration

Add to your VS Code `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "project-mcp": {
        "command": "python",
        "args": ["-m", "project_mcp.server"]
      }
    }
  }
}
```

Or run the installed command directly:

```json
{
  "mcp": {
    "servers": {
      "project-mcp": {
        "command": "project-mcp"
      }
    }
  }
}
```

## Usage

Once configured, you can use the tool in Copilot Chat:

**Get planning guidelines:**
> "Show me the project planning guidelines"

Copilot will call `get_project_planning_guide()` to get the decomposition rules and best practices.

## Customization

Edit `src/project_mcp/data/project_planning.md` to modify the project planning guidelines.

## Project Structure

```
ProjectMCP/
├── pyproject.toml
├── README.md
└── src/
    └── project_mcp/
        ├── __init__.py
        ├── server.py
        └── data/
            └── project_planning.md
```

## Future Additions

- ADO integration tools (WIQL, work item CRUD)
- Sprint detection and planning helpers
- Epic hierarchy analysis
- Context storage and retrieval
