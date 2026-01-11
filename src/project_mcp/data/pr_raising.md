# PR Raising Guidelines

## Overview

You have completed implementation work on a task and are ready to raise a Pull Request (PR). This guide covers creating a well-structured PR with proper description, work item linkage, and build validation.

### Context Sources

You will have context from one or more of:

1. **Task Work Item** - If execution started with a task ID, use the task's objective, exit criteria, and parent deliverable/epic context
2. **Implementation Context** - Code changes made, files modified, and approaches taken during implementation
3. **Discussion History** - Any iterations, design decisions, or trade-offs discussed during implementation
4. **User-Provided Context** - Direct description of the feature or change from the user

**Important:** Read the repository's `AGENTS.md` file to locate:
- **Buddy Build URL** - The test/validation pipeline to trigger for PR validation (REQUIRED)
- **Release Pipeline URL** - For reference only (not triggered during PR)
- PR-specific requirements, review policies, or conventions

---

## PR Requirements

### Mandatory Elements

Every PR MUST include:

1. **Structured Description** - Follow the PR Description Template (see below)
2. **Work Item Link** - Link to the originating task work item for traceability
3. **Build Validation** - Trigger buddy build and update PR with results
4. **Clear Title** - Concise, action-oriented (under 72 characters)

### PR Title Conventions

- **Use imperative mood** - "Add retry logic" not "Added retry logic"
- **Be specific** - Describe the change, not the activity
- **Include component/area** when relevant for clarity

**Good Examples:**
- `Add retry logic for metrics API calls`
- `Fix null reference in cluster health endpoint`
- `Refactor authentication to support multiple providers`

**Bad Examples:**
- `Task 5678` (no description of change)
- `Updates` (too vague)
- `WIP: Adding some stuff` (not ready for PR)

---

## PR Description Template

### Required Sections

```markdown
## What
[1-2 sentences describing WHAT this PR does - the concrete change being made]

## Why
[1-2 sentences explaining WHY this change is needed - the motivation, problem being solved, or goal being achieved]

## Testing Done
[To be populated with build/test results - initially set to "[Pending build validation]"]
```

### Conditional Section

Include this section ONLY if there were non-trivial discussions, iterations, or design decisions:

```markdown
## Coding/Design Considerations
- [Alternative approaches considered and why they were rejected]
- [Trade-offs made and their rationale]
- [Edge cases discussed and how they're handled]
- [Technical debt introduced intentionally with justification]
```

**Omit "Coding/Design Considerations"** if the change was straightforward with no significant design discussions.

---

## PR Creation Workflow

### Step 1: Read AGENTS.md and Gather Context

1. **Read the repository's `AGENTS.md`:**
   - Locate the **Buddy Build URL** (required for build validation)
   - Note any PR-specific requirements, review policies, or conventions
   - Identify testing requirements or coverage expectations

2. **Gather context from available sources:**
   - **Task Work Item:** Objective → "Why", Exit Criteria → validates "What" coverage, Parent context → broader motivation
   - **Implementation:** Files changed → "How", Key decisions → "Coding/Design Considerations"
   - **Discussion History:** Clarifications/iterations → "Coding/Design Considerations", Requirements → validates completeness

### Step 2: Compose PR Description

1. **Draft the description** following the PR Description Template
2. **Populate required sections:**
   - **What:** 1-2 sentences on the concrete change
   - **Why:** 1-2 sentences on motivation and problem solved
   - **Testing Done:** Initially set to "[Pending build validation]"

3. **Add Coding/Design Considerations ONLY if applicable:**
   - Include if there were non-trivial discussions, alternatives considered, or trade-offs made
   - Omit if the change was straightforward

**Example Description:**

```markdown
## What
Implement retry logic for API calls in the data-fetcher service with exponential backoff.

## Why
API calls to the upstream metrics service occasionally fail due to transient network issues, causing data gaps in dashboards. Adding retry logic improves reliability without requiring infrastructure changes.

## Coding/Design Considerations
- Considered using a library like `tenacity` but opted for a lightweight custom implementation to avoid adding dependencies
- Chose exponential backoff (base 2) over linear to balance quick recovery with avoiding thundering herd
- Circuit breaker threshold set to 5 failures based on observed P99 latency patterns

## Testing Done
[Pending build validation]
```

### Step 3: Create PR and Link Work Item

1. **Create the PR** using ADO MCP server:
   - Set PR title to concise, action-oriented summary (under 72 characters)
   - Set PR description to the composed content
   - Target the appropriate base branch (typically `main` or `master`)

2. **Link the work item** using ADO MCP server:
   - Create link between PR and originating task work item
   - Link type: "Pull Request" association
   - Enables traceability from work item to code change

### Step 4: Trigger Buddy Build and Update PR

1. **Trigger the buddy build** using ADO MCP server:
   - Use the buddy build URL from `AGENTS.md`
   - Pass the PR branch as the source branch
   - Capture the **pipeline run URL** from the response

2. **Update the PR description** to replace "[Pending build validation]":
   ```markdown
   ## Testing Done
   - Buddy build triggered: [Pipeline Run URL](url-here)
   - Status: Running
   ```

### Step 5: Confirm Completion

Report to the user:
- PR URL for review
- Work item link confirmation
- Build status and pipeline URL

**Example:**
```
PR created successfully:
- PR: https://dev.azure.com/org/project/_git/repo/pullrequest/1234
- Linked to Task #5678
- Buddy build running: https://dev.azure.com/org/project/_build/results?buildId=9999
```

---

## Quality Guidelines

1. **Keep PRs focused** - One logical change per PR; split large changes into multiple PRs
2. **Write for reviewers** - Description should provide context without requiring code examination
3. **Link work items** - Always link to the task for traceability
4. **Explain the "Why"** - Motivation is often more important than mechanics
5. **Update build status** - Keep "Testing Done" section current as builds complete
6. **Document design decisions** - Capture non-obvious choices in "Coding/Design Considerations"