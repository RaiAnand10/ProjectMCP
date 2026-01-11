# Project MCP Server

A project-aware MCP (Model Context Protocol) server that provides project planning and sprint recap guidelines for GitHub Copilot to act as a project buddy in VS Code.

## Purpose

This MCP server provides structured guidelines for:
- Breaking down projects and epics into well-defined deliverables and tasks
- Planning deliverables by decomposing them into actionable tasks
- Raising pull requests with proper structure and validation
- Generating sprint recaps and iteration summaries
- Optimized for AI-assisted development with Azure DevOps integration

## Tools

### `get_project_planning_guide`
Returns comprehensive guidelines for decomposing projects/epics into work items.

**Parameters:** None

**Returns:** Project planning guidelines including:
- Hierarchy structure (Epic → Deliverable → Task)
- Decomposition rules (size, scope, independence)
- Best practices for AI-executable tasks
- Anti-patterns to avoid

### `get_sprint_recap_guide`
Returns guidelines for generating a sprint recap or iteration summary.

**Parameters:** None

**Returns:** Sprint recap guidelines including:
- Data collection process (iterations, work items, parent epics)
- How to structure highlights and lowlights
- Analysis guidelines for determining accomplishments
- Best practices for stakeholder communication

### `get_deliverable_planning_guide`
Returns guidelines for planning a deliverable work item by breaking it into tasks.

**Parameters:** None

**Returns:** Deliverable planning guidelines including:
- Context gathering from deliverable, parent epic, and sibling deliverables
- Task decomposition rules and templates
- Integration with AGENTS.md patterns
- Leveraging work from related deliverables

### `get_pr_raising_guide`
Returns guidelines for raising a Pull Request after completing implementation work.

**Parameters:** None

**Returns:** PR raising guidelines including:
- PR description structure (What/Why/Testing Done)
- Work item linkage and traceability
- Build validation and buddy build triggering
- Quality guidelines for reviewable PRs

## Installation

```bash
# Install the MCP package (required dependency)
pip install mcp

# Install this package directly
pip install -e /home/anandkuma/repos/ProjectMCP
```

## VS Code Configuration

Add to your `mcp.json` in VS Code:

```json
{
  "servers": {
    "project-mcp": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "project_mcp.server", "<ado_org>", "<ado_project>", "<ado_team>"]
    }
  }
}
```

## Usage

Once configured, you can use the tools in Copilot Chat:

**Get planning guidelines:**
> "Show me the project planning guidelines"

Copilot will call `get_project_planning_guide()` to get the decomposition rules and best practices for breaking down epics.

**Plan a deliverable:**
> "Help me plan deliverable #12345"
> "Break down this deliverable into tasks"

Copilot will call `get_deliverable_planning_guide()` to get instructions on fetching context and creating tasks.

**Generate a sprint recap:**
> "Create a sprint recap for the previous iteration"
> "Summarize what we accomplished last sprint"

Copilot will call `get_sprint_recap_guide()` to get instructions on how to query ADO and format the recap with highlights and lowlights.

**Raise a pull request:**
> "Create a PR for these changes"
> "I'm ready to raise a pull request"

Copilot will call `get_pr_raising_guide()` to get the PR description structure and build validation workflow.

## Customization

Edit the guide files in `src/project_mcp/data/` to customize the guidelines:
- `project_planning.md` - Epic decomposition into deliverables and tasks
- `deliverable_planning.md` - Deliverable decomposition into tasks
- `sprint_recap.md` - Sprint recap structure and analysis guidelines
- `pr_raising.md` - Pull request creation and validation workflow

## Project Structure

```
ProjectMCP/
├── pyproject.toml
├── README.md
└── src/
    └── project_mcp/
        ├── __init__.py
        ├── server.py
        └── ├── deliverable_planning.md
            ├── sprint_recap.md
            └── pr_raising.md
```

## Features

- ✅ Project planning and decomposition guidelines (Epic → Deliverables → Tasks)
- ✅ Deliverable planning guidelines (Deliverable → Tasks)
- ✅ Pull request raising guidelines with build validation
- ✅ Sprint recap genera

- ✅ Project planning and decomposition guidelines
- ✅ Sprint recap generation guidelines
- ✅ ADO context injection (org, project, team, area path)
- 🔄 Future: Direct ADO integration tools (WIQL, work item CRUD)
- 🔄 Future: Automated sprint detection
- 🔄 Future: Epic hierarchy analysis