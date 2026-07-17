---
name: repository-intelligence
description: Map a repository's architecture, ownership, dependency boundaries, risk hotspots, change impact, and likely edit conflicts with traceable evidence. Use when a task asks what exists, who or what owns it, what a proposed change can affect, or where parallel edits may collide. Do not use to delegate work, implement the change, diagnose a specific runtime failure, or approve a release.
---

# Repository Intelligence

Produce a decision-grade map before high-blast-radius work. Analyze; do not silently edit.

## Trigger boundary

Use this skill for requests such as:

- “Map the architecture and service boundaries before we change authentication.”
- “What consumes this schema, and what is the blast radius?”
- “Find ownership gaps, risky hubs, and likely merge-conflict surfaces.”
- “Explain where a new capability belongs without modifying the repository.”

Do not trigger for:

- assigning tasks or spawning agents—use `multi-agent-work-coordinator` after the map exists;
- explaining one observed failure—use `debugging-investigator`;
- executing a planned upgrade—use `codebase-evolution-controller`;
- a narrow symbol lookup that does not need architecture or impact reasoning.

## Required inputs

Obtain or state:

1. repository root and current working-tree state;
2. decision to inform or proposed change hypothesis;
3. base/head refs when impact is diff-driven;
4. depth and excluded areas, including generated or vendored code;
5. evidence constraints, such as unavailable history or missing build tooling.

If the change is unspecified, map the repository generally but label change-impact conclusions as provisional.

## Safety baseline

- Inspect `git status --short` before analysis. Never assume a clean tree.
- Do not checkout, reset, clean, stash, reformat, regenerate, or install dependencies.
- Treat uncommitted files as user work and include them in conflict analysis when relevant.
- Keep generated, vendored, cache, and dependency directories out of source statistics unless they are the subject.
- Never infer ownership solely from directory names or a single `git blame` line.

## Workflow

### 1. Frame the decision

Write a one-sentence intelligence question and an evidence threshold. Examples:

```text
Question: Which components, contracts, and operational surfaces can be affected by changing session token rotation?
Threshold: Every high-confidence edge must cite a manifest, import, call site, schema, CI/deploy file, owner rule, or history sample.
```

Separate the requested decision from interesting but irrelevant repository facts.

### 2. Establish repository state

Capture:

- repository root, current branch or detached state, and worktree changes;
- languages, manifests, workspaces/modules, lockfiles, build systems, CI, deployment, and infrastructure files;
- top-level source, test, documentation, migration, generated, and vendor boundaries;
- submodules, nested repositories, or packages with independent release cycles.

Use [`scripts/repo_signal_scan.py`](scripts/repo_signal_scan.py) for a fast, read-only first pass, then verify material findings manually.

```sh
python skills/repository-intelligence/scripts/repo_signal_scan.py . --format markdown
```

The script finds signals; it does not establish architecture by itself.

### 3. Build the component map

Identify components at the repository's natural granularity: deployable, package, service, application, plugin, domain module, or library. For each component record:

- purpose and externally observable responsibility;
- entry points and public contracts;
- source and test roots;
- runtime, build-time, and operational dependencies;
- data stores, queues, files, APIs, schemas, or generated artifacts it reads or writes;
- deployment unit and failure boundary;
- ownership evidence and confidence.

Prefer explicit boundaries in workspace manifests, module descriptors, build targets, deployment definitions, and public interfaces. Use directory shape only as supporting evidence.

### 4. Trace dependency boundaries

Trace both directions for the decision-relevant nodes:

- inbound consumers: imports, calls, event subscribers, schema users, CLI/API clients, tests, docs, deployment jobs;
- outbound dependencies: libraries, services, data contracts, environment/configuration, generated code, build plugins;
- temporal coupling: migration order, startup order, producer/consumer compatibility, background jobs, caches;
- hidden coupling: shared global state, convention-based discovery, reflection, code generation, string-based routes/topics, and copy-pasted schemas.

Distinguish static references from runtime relationships. Sample dynamic paths through tests, traces, configuration, or framework registration rather than claiming completeness from text search.

### 5. Determine ownership

Triangulate ownership from:

1. `CODEOWNERS` or equivalent policy;
2. component metadata and maintainers files;
3. recent path history and reviewers;
4. release/deployment responsibility;
5. documentation and on-call/runbook references.

Report policy ownership and observed stewardship separately. Flag orphaned, contested, or single-person surfaces. Do not publish personal conclusions unsupported by repository evidence.

### 6. Map change impact

For a proposed change, enumerate impact rings:

- **Ring 0 — direct:** files, symbols, contracts, manifests, migrations, and configuration explicitly changed;
- **Ring 1 — immediate consumers:** compile/import/call/schema/test/deploy consumers;
- **Ring 2 — behavioral dependents:** workflows, jobs, clients, caches, operational assumptions, documentation;
- **Ring 3 — ecosystem/external:** published APIs/packages, partner integrations, backward compatibility, store or infrastructure constraints.

For each impact item state mechanism, evidence, confidence, and verification needed. Absence of a search match is not proof of no consumer.

### 7. Locate risk hotspots

Score qualitatively; do not invent a numeric precision model. Raise risk for combinations of:

- high fan-in/fan-out or many deployment consumers;
- security, authentication, authorization, privacy, money, or destructive data behavior;
- public schemas/APIs or compatibility-sensitive serialization;
- lockfiles, shared build configuration, generated outputs, migrations, release metadata;
- weak tests, flaky checks, sparse ownership, or frequent emergency edits;
- runtime indirection, concurrency, distributed transactions, or difficult rollback;
- large recent churn coupled with concentrated defects.

State the evidence behind every hotspot. Churn alone is not risk; centrality alone is not defect likelihood.

### 8. Predict edit conflicts

Find likely write collisions before parallel work:

- shared manifests and lockfiles;
- central route, registry, dependency-injection, export, schema, migration, generated, and release files;
- common fixtures, snapshots, baselines, or golden images;
- overlapping source roots or code-generation inputs/outputs;
- independent changes that alter the same public contract despite separate files.

Recommend a single integration owner or serialized order for shared surfaces. Do not assign agents; hand the conflict map to `multi-agent-work-coordinator`.

### 9. Produce the intelligence report

Use the schema in [`references/output-schema.md`](references/output-schema.md). Include:

- scope, repository state, exclusions, and unknowns;
- component and dependency map;
- ownership map with evidence type;
- proposed-change impact rings;
- hotspots and conflict surfaces;
- verification targets and open questions;
- confidence per material conclusion.

Use exact file paths and symbols. For large maps, prioritize decision-relevant nodes and attach an inventory rather than burying the conclusion.

## Evidence rules

Apply [`references/evidence-model.md`](references/evidence-model.md):

- label direct evidence, corroborated inference, and hypothesis;
- cite path plus symbol/section/line range when practical;
- use at least two independent signals for high-consequence ownership or hidden-coupling claims;
- state search coverage and ignored directories;
- downgrade confidence when history, generated inputs, runtime configuration, or external consumers are unavailable.

## Handoffs

- To `multi-agent-work-coordinator`: component map, dependency edges, conflict surfaces, single-owner files, and suggested sequencing constraints.
- To `codebase-evolution-controller`: current/target contracts, consumers, compatibility boundaries, and rollback-sensitive nodes.
- To `debugging-investigator`: suspected causal paths and observability gaps, clearly labeled as hypotheses.
- To builders: placement options, invariants, consumers, and focused verification targets.

Do not hand off a directory list as an architecture map.

## Failure handling

- If the repository is too large, state a bounded slice and expand breadth-first from the changed contract.
- If build metadata conflicts with source shape, report both and identify which governs production.
- If code generation obscures ownership, trace generator inputs and generated consumers; never edit generated files as a recommendation without identifying regeneration.
- If evidence is missing, return an uncertainty register and the smallest actions that would resolve it.

## Stop conditions

Stop when the decision-relevant components and consumers are mapped, high-risk conclusions have traceable evidence, conflict surfaces are explicit, and remaining unknowns cannot be resolved from available repository data. Do not continue into delegation or implementation unless separately requested and routed.
