# PR Raising Guidelines

## Overview

You have completed implementation work on a task and are ready to raise a Pull Request (PR). This guide covers creating a well-structured PR with proper description, work item linkage, and build validation.

### Context Sources

You will have context from one or more of:

1. **Task Work Item** - If execution started with a task ID, use the task's objective, exit criteria, and parent deliverable/epic context
2. **Implementation Context** - Code changes made, files modified, and approaches taken during implementation
3. **Discussion History** - Any iterations, design decisions, or trade-offs discussed during implementation
4. **User-Provided Context** - Direct description of the feature or change from the user
5. **Repository Context** - Use ADO MCP server to get repository details (default branch, repo ID, build pipelines)

**Optional:** Read the repository's `AGENTS.md` file if available for:
- PR-specific requirements, review policies, or conventions
- Testing requirements or coverage expectations

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
[Populate with available testing information - include what's applicable, omit what's not]
- Unit tests: [If tests were added, mention what was tested]
- Local validation: [If local build/testing was done, include command snippets and key results]
- Build validation: [Initially "Pending", will be updated with buddy build status]
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

### Step 1: Get Repository Details and Gather Context

1. **Get repository details** using ADO MCP server:
   - Fetch the repository information for the current repository
   - Identify the **default branch** (this will be the PR base branch)
   - Identify the **repository ID** (needed for build pipeline discovery and work item linking)

2. **Identify buddy build pipeline** using ADO MCP server (optional):
   - Query available build pipelines for the project and repository
   - Attempt to identify the buddy build by name patterns:
     - Look for builds with names containing: "buddy", "validation", "CI", "test"
     - Exclude builds with: "official", "release", "pr" (case-insensitive)
   - If multiple candidates exist, prefer the one with "buddy" in the name
   - Note the **pipeline ID** for triggering if found
   - **If no clear buddy build is identified, proceed without it** - this is not blocking

3. **Gather context from available sources:**
   - **Task Work Item:** Objective → "Why", Exit Criteria → validates "What" coverage, Parent context → broader motivation
   - **Implementation:** Files changed and key decisions → "Coding/Design Considerations"
   - **Discussion History:** Clarifications/iterations → "Coding/Design Considerations", Requirements → validates completeness
   - **AGENTS.md (optional):** PR conventions, review policies, testing requirements

### Step 2: Compose PR Description

1. **Draft the description** following the PR Description Template
2. **Populate required sections:**
   - **What:** 1-2 sentences on the concrete change
   - **Why:** 1-2 sentences on motivation and problem solved
   - **Testing Done:** Include applicable items (omit if not done):
     - Unit tests added (what scenarios were covered)
     - Local build and testing (commands run, key output snippets)
     - Build validation status:
       - If buddy build was identified: "Pending"
       - If buddy build could not be identified: "Unable to locate buddy build pipeline for this repository"

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
- Unit tests: Added tests for retry logic (success after retries, max attempts reached, circuit breaker activation)
- Local validation:
  ```bash
  pytest tests/test_retry_handler.py -v
  # All 12 tests passed
  ```
- Build validation: Pending
```

### Step 3: Create PR and Link Work Item

1. **Create the PR** using ADO MCP server:
   - Set PR title to concise, action-oriented summary (under 72 characters)
   - Set PR description to the composed content
   - Set base branch to the **default branch** from Step 1
   - Set source branch to the current working branch

2. **Link the work item** using ADO MCP server:
   - Create a link between the PR and the originating task work item
   - Provide necessary identifiers: project, repository, PR, and work item
   - This enables traceability from work item to code change

### Step 4: Trigger Buddy Build and Update PR (if buddy build was found)

**Note:** Only perform this step if a buddy build pipeline was successfully identified in Step 1.

1. **Trigger the buddy build** using ADO MCP server:
   - Run the buddy build pipeline identified in Step 1
   - Set source branch to the PR branch (source branch from Step 3)
   - Capture the **build ID** and **pipeline run URL** from the response

2. **Update the PR description** to replace "Pending" in build validation:
   - Edit the PR description using ADO MCP server
   - Update the "Build validation" line in Testing Done section:
   ```markdown
   ## Testing Done
   - Unit tests: [Keep existing content if present]
   - Local validation: [Keep existing content if present]
   - Build validation: Buddy build triggered [Pipeline Run #{buildId}](pipeline-run-url) - Status: Running
   ```

**If no buddy build was found:** Skip this step. The PR description already notes that the buddy build pipeline could not be located.

### Step 5: Confirm Completion

Report to the user:
- PR URL for review
- Work item link confirmation
- Build status (if triggered) or note that buddy build was not found

**Example (with buddy build):**
```
PR created successfully:
- PR: https://dev.azure.com/org/project/_git/repo/pullrequest/1234
- Linked to Task #5678
- Buddy build running: https://dev.azure.com/org/project/_build/results?buildId=9999
- Testing Done section includes: unit tests, local validation, and build status
```

**Example (without buddy build):**
```
PR created successfully:
- PR: https://dev.azure.com/org/project/_git/repo/pullrequest/1234
- Linked to Task #5678
- Note: Could not identify buddy build pipeline for this repository
- Testing Done section includes: unit tests and local validation
```

---

## Quality Guidelines

1. **Keep PRs focused** - One logical change per PR; split large changes into multiple PRs
2. **Write for reviewers** - Description should provide context without requiring code examination
3. **Link work items** - Always link to the task for traceability
4. **Explain the "Why"** - Motivation is often more important than mechanics
5. **Update build status** - Keep "Testing Done" section current as builds complete
6. **Document design decisions** - Capture non-obvious choices in "Coding/Design Considerations"