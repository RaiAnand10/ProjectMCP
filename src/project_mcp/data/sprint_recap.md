# Sprint Recap Guidelines

## Overview

Generate a sprint recap summarizing the previous iteration's accomplishments and challenges. The recap should provide stakeholders with a clear view of what was delivered, what's in progress, and any blockers or concerns.

---

## Data Collection Process

### Step 1: Get Iterations

1. Use the ADO MCP server to query the team's iterations
2. Identify the **previous iteration** - the last iteration

### Step 2: Query Work Items

1. Use ADO MCP server to retrieve all work items from the previous iteration
2. Work items will include:
   - **Deliverables** (parent items representing shippable units of value)
   - **Tasks** (child items representing atomic work units)

### Step 3: Get Parent Epics

1. For all Deliverables, fetch their relations to find parent links
2. Use the ADO MCP server to batch fetch all parent Epics in a single query for efficiency
3. Create a **short form** of each Epic title to use as the subject/feature name:
   - Remove common prefixes like "Epic:", "Initiative:", etc.
   - Use the most descriptive 2-4 words
   - Example: "Mature kubectl-ai with DK8S context awareness" → "kubectl-ai DK8S Integration"

### Step 4: Group by Epic

1. Group all deliverables by their parent Epic
2. For deliverables **without an Epic parent**, perform logical grouping:
   - Group by common themes (infrastructure, observability, security, etc.)
   - Use the deliverable's own title as the subject if unique

### Step 5: Analyze Completion Status

For each **Deliverable**:

1. **Check State:** Done/Closed = complete, Active/New = incomplete (verify closure reason isn't "Won't Fix" or "Cut")

2. **Examine Child Tasks (Primary Source of Highlights):**
   - Fetch all child tasks for the Deliverable
   - Look for completed tasks with tangible outcomes - these are often the real highlights even if the parent Deliverable is still open
   - A Deliverable may be "Active" but still have significant completed work worth highlighting

3. **Check Comments:** Scan for progress updates, blockers, or scope changes that inform the narrative

---

## Recap Structure

### Highlights

Summarize 2-4 key accomplishments from the sprint. Each highlight should be:
- **1-2 sentences** (3 max) covering what was achieved and why it matters
- Focused on **outcomes and impact**, not just activities
- Written for stakeholders who may not know technical details
- **Never mention individual owner/assignee names** — this is a team recap, not individual attribution

**Format:**
```
**[Epic Short Name]:** [What was accomplished across deliverables under this epic]. [Impact or next steps]. [Any relevant context].
```

**Example:**
```
**USNat Buildout:** USNat DK8s subscriptions and clusters have been mapped to follow UAE topology, with priority on dedicated clusters. A plan is set to align USSec with this new structure. Subscription creation can begin, but cluster creation is blocked due to issues with the ClusterProvisioning pipeline (see lowlights).

**DK8s Compute Capacity Optimization:** Deployed a proof of concept for the ResourceRecommender service in staging. This service will offer dynamic compute capacity recommendations for USSec and USNat, replacing static overrides managed by AdmissionAdjuster.
```

### Lowlights

Summarize 1-3 challenges, blockers, or concerns. Each lowlight should be:
- **1-2 sentences** (3 max) explaining the issue and its impact
- Honest about problems without assigning blame
- Include context on timeline or severity if relevant

**Format:**
```
**[Issue/Blocker Name]:** [What the problem is]. [Impact on the team or project]. [Any known timeline or mitigation].
```

**Example:**
```
**ClusterProvisioning Pipeline:** ClusterProvisioning has been broken in USSec and USNat for over a month due to several breaking changes and a lack of automated testing. This issue is blocking service migrations to dedicated clusters in USSec and the upcoming USNat buildout.
```

---

## Analysis Guidelines

### Determining Highlights

**Only include items with tangible, shipped outcomes.** Look for:
- Deliverables marked as **Done** or **Closed** with actual artifacts delivered
- Deployments to staging or production environments
- Merged code, published docs, or completed configurations
- Proof of concepts that are running (not just planned)

**Exclude from highlights:**
- Items that are "in progress" without a shipped component
- Work that has been "committed" but not started or completed
- Planning activities without deliverables

### Determining Lowlights

Look for:
- Deliverables that were planned but not started or significantly delayed
- Tasks blocked by external dependencies
- Recurring issues or technical debt causing problems
- Scope changes or unexpected complexity discovered mid-sprint

---

## Output Format

```markdown
# Sprint Recap: [Iteration Name] ([Date Range])

## Highlights

**[Epic 1 Short Name]:** [1-2 sentence summary of progress under this epic]

**[Epic 2 Short Name]:** [1-2 sentence summary of progress under this epic]

**[Logical Group Name]:** [1-2 sentence summary for ungrouped deliverables]

## Lowlights

**[Epic/Issue Short Name]:** [1-2 sentence summary]

**[Blocker Name]:** [1-2 sentence summary]
```

---

## Tips for Quality Recaps

1. **Be specific** - Use concrete numbers, feature names, and environments
2. **Connect to business value** - Explain why accomplishments matter
3. **Be honest about challenges** - Lowlights help set expectations and surface blockers
4. **Keep it scannable** - Busy stakeholders should grasp the sprint in 30 seconds
5. **Celebrate wins** - Even small progress on important initiatives deserves mention