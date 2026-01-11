# Deliverable Planning Guidelines

## Overview

You will be given a **Deliverable work item ID** to plan. Your goal is to break down this deliverable into structured task work items and create them on the Azure DevOps (ADO) board.

This guide is for scenarios where:
- An Epic already exists with one or more deliverables
- You need to plan tasks for a specific deliverable
- The deliverable may already exist or just been created

### Context Sources

You will receive a **Deliverable work item ID** as the starting point. Gather context from:

1. **Deliverable Work Item** - Fetch using ADO MCP server to get:
   - Title and description
   - Objective and exit criteria
   - Current state and any comments

2. **Parent Epic** - Fetch the parent Epic to understand:
   - High-level goals and strategic context
   - Overall scope and constraints
   - Expected timeline and priorities

3. **Sibling Deliverables** - Fetch other deliverables under the same Epic to:
   - Understand what work has been done or is planned
   - Identify dependencies between deliverables
   - Avoid duplication and ensure proper sequencing
   - Learn from task patterns in completed deliverables

4. **User-Provided Context** - Direct input such as:
   - Specific requirements or constraints
   - Technical design decisions
   - Preferred implementation approaches

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

Use all available information (Deliverable + Epic + Sibling Deliverables + user context + AGENTS.md + selective codebase insights) to generate precise, context-aware tasks.

---

## Work Item Hierarchy

ADO work items follow a three-level hierarchy:

### 1. Epic (Quarter-Long Initiative)
- **Purpose:** High-level initiative, project, or major task
- **Duration:** Typically spans a quarter (3 months)
- **Scope:** Broad strategic goal or significant system change

### 2. Deliverable (Shippable Unit of Value)
- **Purpose:** Tangible outcome or product that provides standalone value
- **Duration:** 1-2 weeks of effort
- **Scope:** Must be independently shippable and demonstrable
- **Relationship:** Child of Epic (parent-child link)

### 3. Task (Atomic Work Unit) ← **YOU ARE CREATING THESE**
- **Purpose:** Single, focused unit of work
- **Duration:** 1-3 days for one person
- **Scope:** Atomic change - either code modification OR non-code activity (not both)
- **Relationship:** Child of Deliverable (parent-child link)
- **Types:**
  - **Code tasks:** Implemented by AI coding agents, require explicit boundaries
  - **Non-code tasks:** Configuration, manual operations

---

## Task Template

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
   - Set to the Deliverable ID you're planning for
   - Establishes parent-child relationship

---

## Decomposition Rules

### Core Principles

1. **Single Repository Boundary**
   - Each code task MUST track changes in exactly ONE repository
   - Cross-repo changes require separate tasks with explicit ordering

2. **Dependency-Driven Ordering**
   - Order tasks by **dependency**, NOT priority
   - Consider dependencies on tasks from sibling deliverables

3. **Size Constraints**
   - **Tasks:** 1-3 days maximum
     - If estimating >3 days, decompose further
     - If you can't explain a task in 3-4 lines, it's too big

4. **Clarity for AI Execution**
   - Every code task MUST have clear implementation boundaries
   - Reference AGENTS.md patterns for exit criteria
   - Testing requirements must be concrete, not vague

5. **Learn from Sibling Deliverables**
   - Review task patterns from other deliverables under the same Epic
   - Maintain consistency in task structure and granularity
   - Identify shared infrastructure or utilities already implemented

---

## Task Planning Workflow

### Step 1: Gather Context

1. **Fetch the Deliverable** using ADO MCP server:
   - Get title, description, objective, exit criteria
   - Understand what capability needs to be delivered

2. **Fetch Parent Epic** using ADO MCP server:
   - Get the Epic's title, description, and strategic goals
   - Understand the broader context and constraints

3. **Fetch Sibling Deliverables** using ADO MCP server:
   - Query all deliverables under the same Epic
   - Review their states (Done/Active/New) and tasks (if any exist)
   - Identify dependencies, patterns, and shared components

4. **Read AGENTS.md files** (if repos available):
   - Identify relevant repositories for the deliverable
   - Extract testing patterns, exit criteria, and boundaries

5. **Synthesize context:**
   - How does this deliverable fit into the Epic's goals?
   - What work from sibling deliverables can be leveraged?
   - What repositories will be modified?
   - What are the key technical constraints?

### Step 2: Generate Task List

1. **Identify task categories:**
   - Code changes (per repository)
   - Non-code activities (documentation, configuration, etc.)
   - Dependencies on other deliverables

2. **Apply decomposition rules:**
   - Each task is 1-3 days maximum
   - Each code task touches ONE repository
   - Clear boundaries and exit criteria

3. **Draft task descriptions:**
   - Use the Task Template for structure
   - Reference AGENTS.md patterns for exit criteria
   - Set explicit non-goals to establish boundaries

### Step 3: Present to User

Present the task list for review:

```
For Deliverable [ID]: [Title], I've identified [N] tasks:

Task 1: [Title] (Code change)
- Repository: [repo-name]
- Objective: [Brief description]
- Exit Criteria: [Concise list]
- Non-Goals: [Boundaries]

Task 2: [Title] (Non-code)
- Objective: [Brief description]
- Exit Criteria: [List]

...

Dependencies noted:
- Task X depends on Task Y from Deliverable Z

Are these tasks appropriate? Any adjustments needed?
```

### Step 4: Iterate with User

1. **Refine based on feedback:**
   - Adjust task scope and descriptions
   - Add missing tasks if prompted
   - Modify boundaries and exit criteria
   - Clarify dependencies

2. **Get explicit approval** before proceeding to creation

### Step 5: Create Tasks on ADO

1. **Use ADO MCP server** to create task work items:
   - Set parent relationship to the Deliverable ID
   - Populate all required fields
   - Maintain dependency order if tasks have prerequisites

2. **Confirm successful creation:**
   - Report task IDs to user
   - Provide links to created tasks
   - Confirm parent-child relationships established

---

## Good Task Examples

**Note:** The following examples use fictional repositories and systems for illustration purposes.

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

## Leveraging Sibling Deliverables

When reviewing sibling deliverables under the same Epic:

1. **Check Completion Status:**
   - Completed deliverables may have implemented shared utilities or patterns
   - Active deliverables may have dependencies your tasks need to respect

2. **Review Task Patterns:**
   - How were similar tasks structured in other deliverables?
   - What level of granularity was used?
   - What repositories were commonly touched?

3. **Identify Reusable Components:**
   - Shared libraries or utilities already implemented
   - Common patterns (authentication, error handling, logging)
   - Test fixtures or infrastructure

4. **Avoid Duplication:**
   - Don't recreate what already exists in sibling deliverables
   - Reference existing components in Non-Goals or Context

5. **Understand Dependencies:**
   - Tasks in your deliverable may depend on completion of tasks from other deliverables
   - Make these dependencies explicit in task descriptions or comments

---

## Tips for Success

1. **Start with context** - Thoroughly understand the deliverable, epic, and sibling work before planning tasks
2. **Be specific in boundaries** - Err on the side of over-specification for AI agents
3. **Leverage AGENTS.md** - These files encode team knowledge and standards
4. **Learn from siblings** - Review related deliverables for patterns and shared components
5. **Iterate with users** - Planning is collaborative, not dictatorial
6. **One repo per code task** - Simplifies execution and review
7. **Test requirements are mandatory** - Every code task needs clear testing criteria
8. **Make dependencies explicit** - Call out cross-deliverable dependencies clearly