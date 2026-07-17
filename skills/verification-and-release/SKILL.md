---
name: verification-and-release
description: Build a risk-based verification strategy and decide whether an integrated change is ready to release from traceable test, CI, coverage, operational, security, compatibility, and rollback evidence. Use when the question is what must be proven or whether a completed change can ship. Do not use to implement the feature, diagnose an unknown failure, or treat a green checkmark as sufficient evidence by itself.
---

# Verification and Release

Issue a release decision only from evidence proportional to consequence, novelty, and reversibility.

## Trigger boundary

Use this skill for:

- designing a verification plan from a diff, migration, or release candidate;
- auditing CI/test evidence and identifying material gaps;
- deciding `READY`, `CONDITIONAL`, or `BLOCKED` for a release;
- defining rollout, monitoring, rollback, and post-release checks.

Do not trigger for:

- implementing product behavior or writing the initial feature tests;
- investigating why a test or production symptom fails—use `debugging-investigator`;
- executing an upgrade—use `codebase-evolution-controller`;
- reviewing a tiny local edit when no release decision or broader evidence strategy is requested.

## Required inputs

Collect or explicitly mark unavailable:

1. integrated diff or release candidate identifier and repository state;
2. intended behavior, acceptance criteria, and affected users/consumers;
3. architecture/change-impact evidence and risk-sensitive surfaces;
4. CI runs, local checks, coverage or test map, and known baseline failures;
5. deployment topology, feature flags, migrations, observability, and rollback mechanism;
6. security, privacy, compliance, platform, and compatibility constraints;
7. release scope, cohort, timing, and responsible owner.

A list of commands without the exact artifact/ref and result is not release evidence.

## Safety baseline

- Inspect current worktree and candidate identity before running checks.
- Do not discard, clean, stash, rewrite, or auto-fix user work.
- Do not mark a check passed when it was skipped, filtered, flaky, retried to green without analysis, or run against a different revision.
- Do not expose secrets in logs, screenshots, or evidence bundles.
- Do not perform production deployment or rollback merely because this skill recommends it; use the project's authorized release mechanism and owner.
- Treat irreversible schema/data changes as release blockers until restore or forward-recovery evidence exists.

## Workflow

### 1. Freeze the candidate and claim set

Record:

```text
Candidate ref/artifact:
Working-tree state:
Change summary:
Behavioral claims:
Nonfunctional claims:
Supported environments/consumers:
Release mode:
```

Every check must prove or challenge a claim. Avoid undirected “run everything” plans that still miss the critical path.

### 2. Map change to risk

Use repository/change-impact evidence to classify:

- direct files and behavior;
- public contracts and consumers;
- authentication, authorization, privacy, money, data integrity, destructive operations;
- concurrency, distributed systems, caches, migrations, and background work;
- performance, accessibility, SEO, observability, and platform/store constraints;
- reversibility and blast radius.

Assign a risk tier using [`references/risk-test-matrix.md`](references/risk-test-matrix.md). Record why; line count and developer confidence do not determine risk.

### 3. Build the evidence matrix

For each material claim select evidence across relevant layers:

| Layer | Purpose |
| --- | --- |
| Static | Syntax, types, lint rules, policy/configuration, dependency and secret checks |
| Unit/component | Local logic, state transitions, boundary values, accessibility semantics |
| Contract/schema | Producer/consumer compatibility, serialization, generated clients, migrations |
| Integration | Real subsystem boundaries, storage, network, queues, auth, framework behavior |
| End-to-end | Critical user/operational journeys in a representative environment |
| Nonfunctional | Performance, resource, accessibility, security, reliability, observability |
| Operational | Build artifact, deploy/startup, health, flags, dashboards, alerts, rollback |

Do not require every layer mechanically. Require the smallest set that can detect the credible failure modes.

### 4. Challenge the test strategy

For each risk ask:

- What failure would users or operators observe?
- Which test or signal detects it before release?
- Can the test pass while the failure still exists?
- Is the environment representative enough?
- Does the evidence cover negative paths, partial failure, retries, concurrency, and recovery?
- Is the assertion behavioral or coupled to implementation details?
- Does changed code lack a test because it is trivial, untestable, or simply omitted?

Coverage percentage is a locator, not a verdict. Inspect uncovered changed branches and critical paths; do not set a universal percentage gate without repository policy.

### 5. Collect and normalize results

Capture exact command, environment, candidate, start/end, status, totals, failed/skipped/flaky counts, and artifact links or paths. Use [`scripts/summarize_test_reports.py`](scripts/summarize_test_reports.py) to aggregate JUnit XML and LCOV summaries without changing reports:

```sh
python skills/verification-and-release/scripts/summarize_test_reports.py \
  --junit build/test-results --lcov coverage/lcov.info --format markdown
```

Correlate CI jobs with the candidate ref. A passing previous commit, cancelled matrix leg, or allowed failure does not prove this candidate.

### 6. Evaluate evidence quality

Classify each item:

- `PASS`: relevant, current, representative, and complete enough;
- `FAIL`: expected claim contradicted;
- `GAP`: no evidence for a material risk;
- `STALE`: wrong ref/version/environment;
- `FLAKY`: result is nondeterministic or passed only after unexplained retry;
- `NOT_APPLICABLE`: reason documented and reviewed.

A failure in a critical path blocks release until resolved or explicitly accepted by an authorized owner with containment. Do not relabel it “known issue” without scope evidence.

### 7. Verify operational readiness

Check applicable release controls:

- reproducible build artifact and provenance;
- configuration, secrets references, permissions, and environment validation;
- schema/data migration ordering and compatibility with mixed versions;
- health/readiness/startup behavior and capacity headroom;
- feature flag defaults, targeting, kill switch, and stale-flag owner;
- metrics, traces, logs, dashboards, alerts, and diagnostic identifiers;
- rollback or forward-fix procedure, authority, time limit, and data implications;
- runbooks, support notes, user/admin communication, and migration docs;
- store, signing, privacy manifest, platform policy, or deployment adapter checks where applicable.

A rollback command that has not been validated against the candidate's state transition is a hypothesis.

### 8. Define rollout and post-release verification

Specify cohorts/environments, promotion intervals or sample thresholds, signals, owners, and stop/rollback conditions. Include synthetic or manual checks for high-value journeys immediately after release. Account for delayed jobs, cache expiry, asynchronous migrations, and mobile/store uptake when relevant.

### 9. Issue the decision

Use [`references/release-evidence-schema.md`](references/release-evidence-schema.md).

- **READY:** all critical claims have current evidence; operational and rollback controls are credible; residual risks are bounded and owned.
- **CONDITIONAL:** no uncontained critical failure, but named noncritical evidence or operational conditions must be satisfied before or during a constrained rollout.
- **BLOCKED:** failed critical evidence, material unknown, unsafe compatibility/data transition, missing rollback/observability, or candidate identity mismatch.

State the minimum actions that can change the decision. Never use “looks good” as a release status.

## Interaction boundaries

- Implementing skills own focused tests and checks for the behavior they change.
- `verification-and-release` owns the integrated evidence model and release gate.
- `debugging-investigator` explains failed or flaky evidence when cause is unknown.
- `codebase-evolution-controller` supplies migration stages, compatibility, rollout, and rollback evidence.
- `documentation-synchronizer` closes release-blocking user, API, migration, configuration, and runbook gaps.
- `multi-agent-work-coordinator` may gather evidence in parallel; this skill accepts or rejects the integrated evidence.

## Failure handling

- If CI is unavailable, substitute locally reproducible evidence only when environment differences are bounded; otherwise record a gap.
- If tests are flaky, estimate neither probability nor safety from a few retries. Isolate cause or block the affected claim.
- If a full suite is too expensive, select risk-targeted shards and document untested space and compensating rollout controls.
- If production-like data cannot be used, create representative sanitized fixtures and state limitations.
- If rollback is impossible, require stronger pre-release evidence, smaller cohorts, and forward-recovery design; high-risk irreversible changes may remain blocked.

## Stop conditions

Stop when each material claim has a classified evidence state, critical gaps have an owner and action, operational controls are evaluated, and a traceable verdict is issued. Do not continue into deployment without an explicit authorized release action.
