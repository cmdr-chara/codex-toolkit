---
name: review-and-refactor-code
description: Review a defined diff or code area for actionable defects and integration risks, assess structural problems, and plan or execute behavior-preserving refactors through traceable evidence and incremental verification. Use when a user asks for code review, change-risk analysis, maintainability assessment, cleanup, decomposition, or refactoring. Do not use for general repository mapping, unknown runtime failures, version or schema migrations, security-only review, platform-wide production audits, or final release approval.
---
# Review and Refactor Code

Find defects that matter, distinguish them from optional design improvements, and change structure only after an approved proposal.

## Trigger boundary

Use this skill for:

- reviewing a branch, commit, pull request, working-tree diff, or bounded code area;
- identifying defects introduced by a change and tracing affected consumers;
- assessing whether a structural refactor is justified and feasible;
- planning or performing behavior-preserving decomposition, deduplication, or boundary cleanup.

Do not trigger for:

- broad architecture, ownership, or blast-radius mapping without a defined review/refactor decision - use repository-intelligence;
- a concrete failure whose cause is unknown - use debugging-investigator;
- dependency, framework, runtime, schema, or public API transitions - use codebase-evolution-controller;
- security as the primary review decision - use the applicable security review workflow;
- a platform-wide web or mobile production audit - use the relevant builder;
- deciding whether an integrated candidate can ship - use verification-and-release.

## Required inputs

Obtain or state:

1. repository root and current working-tree state;
2. review or refactor scope, including base/head refs when diff-driven;
3. intended behavior, contracts, and acceptance criteria;
4. generated, vendored, migration, or lockfile boundaries;
5. relevant tests, build commands, and known baseline failures;
6. compatibility, performance, security, and operational constraints;
7. whether the user has approved a previously proposed edit batch.

If scope is too broad to support file-level evidence, select a bounded slice and explain the coverage limit.

## Safety baseline

- Inspect repository state before analysis. Preserve uncommitted and unrelated user work.
- Do not checkout, reset, clean, stash, regenerate, reformat broadly, or install dependencies during review.
- Treat review, refactor, cleanup, and improvement requests as analysis authorization only at first.
- Do not edit repository files until the user separately approves a concrete proposal produced by this skill.
- Limit approval to the named files, invariants, slices, and verification plan. Re-propose materially different work.
- Never label style preference, hypothetical risk, or missing proof as a defect.
- Do not remove pre-existing dead code unless it is inside the approved scope and its replacement is verified.

## Workflow

### Stage 1 - inspect and propose

#### 1. Freeze the decision and scope

Record:

    Mode: review | refactor proposal | approved refactor execution
    Scope:
    Base/head or working-tree state:
    Intended behavior:
    Critical contracts:
    Exclusions:
    Evidence limits:

For a diff review, inspect both changed lines and enough surrounding consumers to determine whether behavior can break. For a refactor request, identify the structural pain and the behavior that must remain fixed.

#### 2. Establish the evidence surface

Inspect:

- changed files, renames, deletions, generated outputs, manifests, schemas, and configuration;
- callers, callees, imports, registrations, routes, events, data contracts, and side effects;
- tests that exercise the affected behavior, including negative and boundary cases;
- recent path history when it explains intent or compatibility;
- build, deployment, documentation, and operational consumers when the change reaches them.

Search is evidence of a reference, not proof of runtime execution. Label facts, corroborated inferences, and unresolved hypotheses.

#### 3. Review for actionable defects

Use [the finding contract](references/finding-contract.md). A finding must include:

- the smallest useful file and line location;
- the violated contract and observable failure;
- the input, state, environment, or sequence that triggers it;
- evidence connecting the reviewed change to the failure;
- a feasible correction and any validation needed;
- priority P0 through P3 and confidence.

Report no finding when the concern is speculative, pre-existing but unrelated, purely stylistic, or already prevented by surrounding behavior. Keep optional improvements separate from defects.

#### 4. Assess refactor value and feasibility

Use [the behavior-parity guide](references/behavior-parity.md). Map:

- public and internal interfaces;
- callers and dependency direction;
- state, I/O, exceptions, ordering, timing, and cleanup effects;
- compatibility surfaces and generated sources;
- characterization evidence and gaps.

Prefer the smallest structural change that reduces demonstrated complexity or risk. Reject abstraction without a second real use, file splitting without a clearer boundary, and rewrites whose behavior cannot be bounded.

#### 5. Produce the proposal and stop

For each proposed slice, state:

1. objective and evidence;
2. files and contracts affected;
3. invariants that must remain true;
4. characterization or regression tests required before editing;
5. implementation steps and temporary adapters;
6. focused and broader verification;
7. rollback or safe stopping point;
8. excluded adjacent cleanup.

Return REVIEWED when analysis is complete and no edit is justified. Return AWAITING_APPROVAL when a concrete edit proposal is ready. Stop without editing and request explicit approval.

### Stage 2 - execute an approved refactor

#### 6. Validate approval and baseline

Confirm that approval names or clearly accepts the proposal. Re-inspect the working tree for changes since the proposal. If scope, behavior, or repository state materially changed, return to Stage 1.

Run or add the approved characterization evidence before structural edits. Record baseline failures without hiding or repairing unrelated problems.

#### 7. Refactor in safe slices

For each approved slice:

1. preserve public behavior and compatibility boundaries;
2. make the minimum structural edit;
3. keep the tree buildable and testable;
4. run focused checks immediately;
5. inspect the diff for accidental behavior or formatting changes;
6. continue only when the slice preserves its invariants.

Use adapters only when they reduce transition risk, and define their removal condition. Remove imports, variables, helpers, and files made obsolete by the approved change; leave unrelated pre-existing cleanup alone.

#### 8. Verify and report

Run the repository's proportionate check ladder: characterization/regression tests, focused static checks, affected integration tests, and the broadest relevant standard check available. Report commands, candidate state, results, skipped checks, baseline failures, and residual uncertainty.

Return REFACTORED only when approved slices and required checks complete. Return BLOCKED when behavior parity, repository state, or required evidence prevents safe completion.

## Output contract

Lead with the state: REVIEWED, AWAITING_APPROVAL, REFACTORED, or BLOCKED.

Include only applicable sections:

- scope and repository state;
- findings ordered by priority;
- optional improvements, clearly separated;
- refactor proposal or implemented slices;
- behavior-parity evidence;
- verification results and residual risk;
- explicit approval request when awaiting edits.

If there are no actionable findings, say so and identify material evidence gaps. Do not fill the report with praise or low-value observations.

## Handoffs

- To repository-intelligence: unresolved architecture, ownership, or broad consumer mapping needed before a safe proposal.
- To debugging-investigator: a reported or discovered failure needs reproduction and causal isolation.
- To codebase-evolution-controller: the justified change crosses dependency, framework, schema, runtime, or public compatibility states.
- To the relevant platform builder: approved behavior changes or platform-specific production work exceed structural refactoring.
- To verification-and-release: integrated refactor evidence and residual risk when a release decision is requested.
- To a security workflow: authentication, authorization, privacy, trust-boundary, or exploitability review is primary.

## Failure handling

- If no reliable base exists, review the explicit working tree or bounded files and state that historical causality is unavailable.
- If the diff is too large, prioritize public contracts and high-consequence paths, then request a narrower continuation.
- If tests are absent, propose characterization at the nearest stable boundary before refactoring.
- If generated code obscures the change, trace its source and regeneration path; do not refactor generated output directly.
- If behavior changes are necessary, separate them into a new proposal rather than disguising them as refactoring.
- If approval is ambiguous, remain AWAITING_APPROVAL; do not infer permission from urgency.

## Stop conditions

Stop Stage 1 when the requested scope has evidence-backed findings, the refactor decision is justified or rejected, and any edit proposal is specific enough to approve. Stop Stage 2 when approved slices preserve stated invariants and required checks pass, or when the next safe action needs new evidence or authorization.
