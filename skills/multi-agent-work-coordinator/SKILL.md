---
name: multi-agent-work-coordinator
description: Plan and govern safe parallel repository work using a dependency graph, exclusive write ownership, overlap detection, integration order, and evidence-based acceptance of subagent results. Use when multiple bounded work items can proceed independently after repository boundaries are known. Do not use for repository discovery, role/model routing alone, tightly coupled work, or tasks too small or ambiguous to verify independently.
---

# Multi-Agent Work Coordinator

Parallelize execution without parallelizing accountability. The parent owns the work graph, integration, validation, and final judgment.

## Trigger boundary

Use this skill for:

- splitting a mapped feature across independent packages, tests, and documentation;
- coordinating multiple agents while preventing shared-file collisions;
- sequencing migrations or generated outputs through explicit dependency waves;
- auditing a proposed agent plan for overlap, missing acceptance evidence, or unsafe integration.

Do not trigger when:

- repository boundaries and consumers are unknown—run `repository-intelligence` first;
- one agent can complete the work with less briefing and review overhead;
- tasks require continuous edits to the same files or unresolved product decisions;
- the request is only to choose specialized Mission Control roles—the existing `delegate-with-mission-cards` skill can dispatch after this skill defines the work graph.

## Required inputs

Require:

1. one objective and concrete acceptance criteria;
2. current repository state and an intelligence map or equivalent evidence;
3. candidate work items with likely read/write surfaces;
4. single-owner surfaces, sequence constraints, and integration checks;
5. available agent capabilities and any access restrictions.

If the repository map is stale relative to the working tree, refresh the affected slice before assigning work.

## Safety baseline

- Inspect and preserve uncommitted user work.
- Do not use Git cleanup, force operations, destructive migrations, or unreviewed generated output.
- Give every writer an exclusive write scope. “Coordinate later” is not a valid collision strategy.
- Keep lockfiles, schemas, migrations, central registries, generated artifacts, release metadata, and shared configuration under one writer or the parent integrator.
- Agents may read outside their write scope only as stated. They must stop before editing outside it.
- Never accept completion solely from an agent's prose; inspect artifacts and rerun proportionate checks in the integrated state.

## Workflow

### 1. Decide whether parallelism is justified

Parallelize only when all are true:

- objective and acceptance criteria are stable;
- work can be partitioned by artifact or decision boundary;
- dependencies can be represented as an acyclic graph or explicit serialized loop;
- each result has independent evidence;
- briefing, review, and merge cost is lower than sequential execution.

Keep work parent-owned when it is small, destructive, product-judgment-heavy, credential-bound, or too intertwined to isolate.

### 2. Create the work graph

Define nodes using [`references/work-graph-schema.md`](references/work-graph-schema.md). Every node needs:

- unique ID and objective;
- decision or artifact produced;
- dependencies and readiness conditions;
- allowed read scope and exclusive write scope;
- invariants and forbidden surfaces;
- acceptance evidence and integration checks;
- stop/escalation conditions;
- expected return format.

Do not use vague nodes such as “handle backend.” Split by verifiable outcome, not job title.

### 3. Assign ownership

Create an ownership ledger before dispatch:

```text
surface | owner mission | why single-owner | consumers | integration point
```

Use the most specific practical paths. A writer that owns `src/**` prevents useful concurrency and hides uncertainty. A writer that owns one file while its code generator owns the output elsewhere is incomplete.

Treat semantic collisions as overlap even when paths differ: two missions changing opposite ends of the same API, schema, feature flag, or serialization format require an explicit compatibility contract and order.

### 4. Detect overlap

Run the conservative checker against the work-graph JSON:

```sh
python skills/multi-agent-work-coordinator/scripts/ownership_check.py work-plan.json
```

Resolve every reported collision by:

1. assigning the shared surface to one mission;
2. moving it to a parent integration mission;
3. splitting by generated input versus generated output with one regeneration owner;
4. serializing the dependent missions;
5. redesigning the boundary.

Do not waive a collision because agents use separate branches; the integration conflict still exists.

### 5. Form execution waves

A mission is `READY` only when all dependencies and inputs are available. Launch the smallest useful wave, normally two to four missions. Favor parallel readers and independent leaf writers.

Order examples:

- contract definition → independent consumers → generated artifacts → integrated verification;
- investigation readers → decision owner → isolated implementers → integration owner;
- source changes → one lockfile/generated-output owner → docs → release evidence.

Do not permit recursive delegation unless the graph explicitly models it and the parent can observe ownership transitively.

### 6. Dispatch bounded work

A dispatch must include the exact node, repository-state warning, and return contract. If the toolkit's Mission Control bundle is installed, use [`references/mission-control-adapter.md`](references/mission-control-adapter.md) to translate approved nodes into role-specific mission cards. Otherwise use any agent mechanism that preserves the same boundaries.

Agents must return:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- files read and changed;
- concise result/diff summary;
- commands/checks run and exact outcomes;
- evidence against each acceptance criterion;
- deviations, assumptions, and residual risks;
- whether they stayed within write ownership.

### 7. Review each handoff

Classify each result:

- `ACCEPTED`: artifacts and evidence satisfy the node;
- `REWORK`: bounded correction needed;
- `BLOCKED`: dependency or environment prevents completion;
- `REJECTED`: ownership, safety, or correctness breach invalidates the result.

Verify:

1. objective and scope match;
2. every changed file is owned;
3. unrelated user changes remain intact;
4. material claims are corroborated;
5. tests target the behavior, not only implementation details;
6. downstream assumptions remain valid.

Do not launch dependent nodes from `PARTIAL` output unless the graph is revised explicitly.

### 8. Integrate in declared order

The parent or designated single integration mission resolves shared surfaces. Before combining results:

- refresh worktree state and detect new user changes;
- compare actual changed files with the ledger;
- apply contract/schema changes before dependent consumers;
- regenerate only from reviewed inputs and one owner;
- reconcile tests and docs against final behavior;
- rerun checks against the integrated tree, not isolated agent states.

A clean textual merge is not evidence of semantic compatibility.

### 9. Close the graph

A graph is complete only when every node is accepted, intentionally cancelled, or recorded blocked; integration checks pass or are explicitly unavailable; and residual risks have owners. Hand the integrated evidence to `verification-and-release` for a release decision when shipping is in scope.

## Evidence by risk

- **Low:** owned diff, nearest deterministic check, and scope review.
- **Medium:** focused tests, static checks, affected-consumer inspection, and integrated rerun.
- **High:** negative/adversarial paths, compatibility or rollback evidence, independent review, and full relevant integrated suite.

Risk is driven by consequence and reversibility, not line count.

## Handoffs and interaction boundaries

- `repository-intelligence` supplies architecture and conflict evidence; this skill does not replace it.
- `codebase-evolution-controller` owns migration staging and rollback; this skill may parallelize approved stages without redefining them.
- builders own feature-level verification; this skill checks their evidence and integrated interactions.
- `verification-and-release` owns the final release gate.
- `delegate-with-mission-cards` is an optional dispatch adapter, not a prerequisite and not a second planner.

## Failure handling

- If overlap cannot be eliminated, serialize or keep the work under one owner.
- If an agent broadens scope, stop and reassess rather than retroactively expanding ownership.
- If a dependency changes mid-wave, pause affected nodes and version the graph.
- If integration checks fail, reopen the responsible nodes based on evidence; do not assign blame by last writer.
- If available agents cannot meet access or verification needs, keep the node parent-owned.

## Stop conditions

Stop when parallelism is no longer beneficial, ownership cannot be made exclusive, the graph depends on unresolved product/architecture decisions, or all nodes and integration evidence are closed. Never delegate final product tradeoffs, release judgment, or user communication.
