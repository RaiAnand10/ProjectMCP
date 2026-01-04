# Project Planning Guidelines

## Overview

You will be given a project/task to plan along with contextual information. Your goal is to decompose this high-level initiative into structured work items and create them on the Azure DevOps (ADO) board.

### Context Sources

You will always receive an **Epic work item ID** as the starting point for planning. The Epic may contain:
- Title and high-level description
- Objectives and expected outcomes

Additionally, the user may provide **supplementary context** directly, such as:
- Specific requirements or constraints
- Technical design decisions

**Important:** If repos are available in the workspace, scan for and read ALL `AGENTS.md` files across all repositories. These files contain:
- Repository overview and architecture
- Exit criteria patterns for code changes
- Testing requirements and validation approaches
- Boundaries and constraints for AI agents
- Other dependent repositories or artifacts

**Codebase Scanning Strategy:**
- **AGENTS.md is mandatory** - Always read these files first when available
- **Deeper codebase scan is conditional** - If AGENTS.md is:
  - Missing testing requirements or patterns
  - Not present in a critical repository
  
  Then perform a high-level scan to understand:
  - Directory structure and key modules
  - Existing patterns (test structure, error handling, etc.)
  - Integration points between components
  
- **Balance thoroughness with efficiency** - Don't scan everything by default; use AGENTS.md as the primary source and scan code only when needed to fill gaps

Use all available information (Epic details + user-provided context + AGENTS.md + selective codebase insights) to generate precise, context-aware work items.

---

## Work Item Hierarchy

ADO work items follow a three-level hierarchy:

### 1. Epic (Quarter-Long Initiative)
- **Purpose:** High-level initiative, project, or major task
- **Duration:** Typically spans a quarter (3 months)
- **Scope:** Broad strategic goal or significant system change
- **Examples:** "Mature kubectl-ai with DK8S context awareness", "Implement ADO work item automation for Project MCP"

### 2. Deliverable (Shippable Unit of Value)
- **Purpose:** Tangible outcome or product that provides standalone value
- **Duration:** 1-2 weeks of effort
- **Scope:** Must be independently shippable and demonstrable
- **Relationship:** Child of Epic (parent-child link)
- **Examples:** "Deliver MCP server tools to read DK8S metrics and trends", "Deliver ADO work item query capability in Project MCP"

### 3. Task (Atomic Work Unit)
- **Purpose:** Single, focused unit of work
- **Duration:** 1-3 days for one person
- **Scope:** Atomic change - either code modification OR non-code activity (not both)
- **Relationship:** Child of Deliverable (parent-child link)
- **Types:**
  - **Code tasks:** Implemented by AI coding agents, require explicit boundaries
  - **Non-code tasks:** Configuration, manual operations

---

## Work Item Templates

### Deliverable Template

**Required Fields:**

1. **Title** (One-liner)
   - Focus on the **outcome or capability being delivered**, not the activity
   - Use clear, specific language describing what will exist after completion
   - Consider starting with "Deliver" for consistency, but prioritize clarity over convention
   - ✅ Good: "Deliver MCP server tools to read DK8S metrics and trends" (outcome: tools exist)
   - ✅ Good: "ADO work item query capability in Project MCP" (outcome: capability exists)
   - ❌ Bad: "Add metrics tools" (describes activity, not outcome)
   - ❌ Bad: "Improve error handling" (vague, no specific capability described)

2. **Description** (Structured)
   ```markdown
   ## Objective
   [Brief summary of what we want to achieve and why it matters]

   ## Exit Criteria
   [High-level feature/capability that will be live after this deliverable]
   - [What will users/systems be able to do - e.g., "kubectl-ai can retrieve DK8S cluster health across regions"]
   - [What artifact/capability will exist - e.g., "MCP tools available for querying ADO work items"]

   ## Context
   [Additional background that is NOT covered in Objective: links to design docs, dependencies on other work, technical constraints, or related systems]
   ```

3. **Parent**
   - Set to the Epic ID
   - Establishes parent-child relationship in ADO

---

### Task Template

**Required Fields:**

1. **Title** (One-liner)
   - Be specific and action-oriented
   - Include component/file/area when relevant
   - ✅ Good: "Implement get_cluster_health() tool in dk8s-mcp-server"
   - ❌ Bad: "Cluster health"

2. **Description** (Structured)

   **For ALL tasks:**
   ```markdown
   ## Objective
   [Detailed description of what needs to be implemented and why. This should be 3-4 lines covering:
   - What capability/feature is being built
   - Why it's needed (context from Epic/Deliverable)
   - High-level approach or architectural fit]
   ```

   **For CODE CHANGE tasks (additional sections):**
   ```markdown
   ## Repository
   [Name of the repository where changes will be made]

   ## Exit Criteria
   - [Concise list of what needs to be implemented with tests added, passing, and validated as per AGENTS.md requirements]
   - [Keep this high-level to avoid hallucination - specific test scenarios will be determined during implementation]

   ## Explicit Non-Goals
   - [What should NOT be changed/touched - set clear boundaries]
   - [Features out of scope]
   ```

   **For NON-CODE tasks:**
   ```markdown
   ## Exit Criteria
   - [What artifacts/documents/setup will be produced]
   ```

3. **Parent**
   - Set to the corresponding Deliverable ID
   - Establishes parent-child relationship

---

## Decomposition Rules

### Core Principles

1. **Single Repository Boundary**
   - Each code task MUST track changes in exactly ONE repository
   - Cross-repo changes require separate tasks with explicit ordering

2. **Dependency-Driven Ordering**
   - Order deliverables and tasks by **dependency**, NOT priority

3. **Size Constraints**
   - **Deliverables:** 1-2 weeks maximum
     - If estimating >2 weeks, break into multiple deliverables
     - Each deliverable should provide standalone value
   - **Tasks:** 1-3 days maximum
     - If estimating >3 days, decompose further
     - If you can't explain a task in 3-4 lines, it's too big

4. **Clarity for AI Execution**
   - Every code task MUST have clear implementation boundaries
   - Reference AGENTS.md patterns for exit criteria
   - Testing requirements must be concrete, not vague

---

## Work Item Creation Workflow

### Phase 1: Deliverable Planning

1. **Generate deliverable list**
   - Based on epic context and AGENTS.md insights
   - Include title, description, acceptance criteria for each

2. **Present to user**
   ```
   "I've identified [N] deliverables for this epic:

   Deliverable 1: [Title]
   - Objective: [Summary]
   - Exit Criteria: [List]

   Deliverable 2: [Title]
   ...

   Do these deliverables look correct? Any refinements needed?"
   ```

3. **Iterate with user**
   - Discuss scope, ordering, dependencies
   - Refine descriptions based on feedback
   - Adjust breakdown if deliverables are too large/small
   - Get explicit approval before creating work items

4. **Create deliverables on ADO**
   - Use ADO MCP server to create work items
   - Set parent relationships to Epic
   - Confirm successful creation

### Phase 2: Task Planning (Per Deliverable)

**For EACH deliverable** (one at a time):

1. **Generate task list**
   - Distinguish code vs. non-code tasks
   - Apply decomposition rules
   - Reference AGENTS.md for exit criteria and boundaries

2. **Present to user**
   ```
   "For Deliverable [N]: [Title], I've identified [M] tasks:

   Task 1: [Title] (Code change)
   - Repository: [repo-name]
   - Objective: [Brief description]
   - Exit Criteria: [Concise list]
   - Non-Goals: [Boundaries]

   Task 2: [Title] (Non-code)
   - Objective: [Brief description]
   - Exit Criteria: [List]

   ...

   Are these tasks appropriate? Any adjustments needed?"
   ```

3. **Iterate with user**
   - Refine task scope and descriptions and add missing tasks if prompted
   - Adjust boundaries and exit criteria
   - Get explicit approval before creating work items

4. **Create tasks on ADO**
   - Use ADO MCP server to create work items
   - Set parent relationship to Deliverable
   - Confirm successful creation

5. **Repeat for next deliverable**
   - Move to next deliverable only after current one's tasks are approved and created

---

## Good Task Examples

**Note:** The following examples use fictional repositories (dk8s-mcp-server, kubectl-ai) and systems (MTP Data Mart, Geneva) for illustration purposes.

### Code Change Task Example
```markdown
Title: Implement get_cluster_health() tool in dk8s-mcp-server

Description:
## Objective
Add an MCP tool to dk8s-mcp-server that retrieves current DK8S cluster health status across all regions and returns a structured summary with component-level breakdown. This enables kubectl-ai to understand platform state during incident triage and determine whether problems are isolated or indicative of broader system degradation. The implementation should query the MTP Data Mart's dk8s_cluster_health view, handle authentication using existing service principal configuration, and follow established MCP protocol patterns from the codebase.

## Repository
dk8s-mcp-server

## Exit Criteria
- get_cluster_health() tool implemented and registered in MCP server catalog
- Tool queries MTP Data Mart and returns cluster health with region and component-level status
- Authentication and error handling implemented per AGENTS.md patterns
- Tests added and passing per AGENTS.md requirements

## Explicit Non-Goals
- Do NOT implement historical trend analysis (separate task)
- Do NOT add alerting or notification logic
- Do NOT query Geneva directly - use Data Mart abstraction only
```

### Non-Code Task Example
```markdown
Title: Document kubectl-ai MCP integration architecture and troubleshooting runbook

Description:
## Objective
Create comprehensive documentation for kubectl-ai MCP server integration to support team onboarding and operational troubleshooting. The MCP integration adds architectural complexity (server lifecycle, tool discovery, network communication) that requires clear documentation covering connection flows, tool invocation mechanics, and common failure scenarios. Documentation should include architecture diagrams, troubleshooting steps with log analysis examples, and reference queries demonstrating MCP tool usage.

## Exit Criteria
- Architecture documentation created with diagrams and tool invocation flows
- Troubleshooting runbook covers common failure scenarios with resolution steps
- Documentation reviewed by team and merged to main branch
```

---

## Integration with AGENTS.md

When AGENTS.md files are available in repositories, use them to inform task planning:

1. **Exit Criteria** - Reference the mandatory exit criteria patterns from AGENTS.md (e.g., "all tests passing per AGENTS.md requirements") rather than repeating the full checklist

2. **Build and Test Commands** - Include specific build/test commands from AGENTS.md when relevant to the task

3. **Repository Structure** - Use AGENTS.md to understand where code should be added and what patterns to follow

4. **Related Dependencies** - Identify related repositories or artifacts mentioned in AGENTS.md that should be included in Non-Goals or Context

---

## Tips for Success

1. **Start with the big picture** - Understand the epic goal before decomposing
2. **Think in deliverables** - What can be shipped independently?
3. **Make dependencies explicit** - Don't assume implicit ordering
4. **Be specific in boundaries** - Err on the side of over-specification for AI agents
5. **Leverage AGENTS.md** - These files encode team knowledge and standards
6. **Iterate with users** - Planning is collaborative, not dictatorial
7. **One repo per code task** - Simplifies execution and review
8. **Test requirements are mandatory** - Every code task needs clear testing criteria