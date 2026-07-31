---
name: optimize-codebase-performance
description: Measure, diagnose, propose, and execute bounded performance improvements for latency, throughput, CPU, memory, GPU, I/O, startup, database, bundle, rendering, or infrastructure cost while preserving correctness. Use when a user asks to profile a critical path, explain a bottleneck, reduce resource use, or optimize measured performance. Do not use for unmeasured cleanup, incorrect behavior whose cause is unknown, version migrations, general platform audits, or final release approval.
---
# Optimize Codebase Performance

Optimize a measured critical path, not code that merely looks inefficient. Separate diagnosis and proposal from authorized implementation.

## Trigger boundary

Use this skill for:

- profiling user-visible or system-visible latency, startup, throughput, or resource consumption;
- locating CPU, memory, GPU, database, network, I/O, bundle, or rendering bottlenecks;
- producing a reproducible performance proposal;
- implementing approved optimization batches and verifying comparable before/after results.

Do not trigger for:

- cleanup without a named performance path and metric;
- incorrect output, crashes, races, leaks, or regressions whose cause is unknown - use debugging-investigator first;
- dependency, runtime, schema, or platform migrations - use codebase-evolution-controller;
- general web, Flutter, or Expo production audits without a performance decision - use the relevant builder;
- deciding whether the integrated candidate can ship - use verification-and-release.

## Required inputs

Obtain or state:

1. critical path and affected user or system outcome;
2. target metric and whether lower or higher is better;
3. representative workload, input shape, concurrency, and cache state;
4. environment, hardware, runtime, build mode, and dependency state;
5. success threshold, correctness invariants, and acceptable trade-offs;
6. available profiler, telemetry, benchmark, test, and operational evidence;
7. time, compute, production-safety, privacy, and cost constraints;
8. whether the user approved a previously proposed optimization batch.

If the target is vague, select the nearest observable path and metric but keep conclusions provisional until the user confirms relevance.

## Safety baseline

- Inspect repository and environment state before measurement. Preserve uncommitted and unrelated user work.
- Treat profile, speed up, optimize, reduce, and improve requests as diagnosis and proposal authorization only at first.
- Do not edit repository or infrastructure files until the user separately approves a concrete proposal produced by this skill.
- Limit approval to named batches, files, settings, workloads, trade-offs, and verification. Re-propose materially different work.
- Prefer local, sanitized, read-only measurement. Do not upload private code, traces, profiles, or customer data without authorization.
- Do not run high-cost, destructive, production-load, permission-changing, or externally billable experiments without explicit authorization.
- Never trade correctness, security, privacy, accessibility, observability, or maintainability for an unproven or marginal gain.
- Never claim improvement from non-comparable measurements.

## Workflow

### Stage 1 - measure and propose

#### 1. Define the performance contract

Record:

    Critical path:
    User/system outcome:
    Metric and direction:
    Workload:
    Environment/build:
    Success threshold:
    Correctness invariants:
    Budget and exclusions:

Separate cold from warm behavior, development from production builds, and small fixtures from representative inputs. Do not optimize a proxy unless its relationship to the desired outcome is established.

#### 2. Establish a trustworthy baseline

Follow [the measurement and reporting protocol](references/measurement-and-reporting.md). Prefer existing telemetry, benchmarks, traces, or performance tests. Otherwise create the smallest repeatable measurement that does not alter product behavior.

Record exact command or procedure, candidate identity, warm-up policy, sample count, statistic, units, variance, background load, and raw artifact location. Use median plus tail/peak values when the path is noisy or users experience outliers.

Return BLOCKED when no safe measurement can represent the requested path. Return MEASURED when the baseline answers the request and no change is yet justified.

#### 3. Attribute cost and test hypotheses

Use [the bottleneck playbook](references/bottleneck-playbook.md) for the relevant layers only. Trace the critical path and distinguish work that is:

- performed too early, too often, in excessive volume, or unnecessarily serially;
- shaped poorly for lookup, query, allocation, transfer, rendering, or concurrency;
- amplified by cache, retry, queue, lifecycle, build, deployment, or infrastructure behavior.

For every candidate state:

    Hypothesis: <measured cost> is caused by <specific mechanism>.
    Evidence: <profile, trace, plan, counter, or controlled comparison>.
    Falsifier: <result that would reject the mechanism>.
    Smallest experiment: <bounded measurement or code/config change>.

Static analysis, scanner output, and generic advice are leads, not proof. Retire contradicted hypotheses explicitly.

#### 4. Rank bounded optimization batches

Rank candidates by expected impact, evidence strength, correctness risk, reversibility, complexity, and measurement cost. Prefer removing, deferring, batching, or narrowing proven work before adding caches, concurrency, dependencies, or architecture.

For each proposed batch state:

1. mechanism and supporting evidence;
2. exact files, settings, or boundaries;
3. expected metric movement and trade-offs;
4. correctness and nonfunctional invariants;
5. implementation steps;
6. focused tests and comparable remeasurement protocol;
7. rollback or rejection condition;
8. excluded adjacent optimization.

#### 5. Produce the proposal and stop

Return NO_JUSTIFIED_CHANGE when evidence does not support a worthwhile intervention. Return AWAITING_APPROVAL when one or more bounded batches are ready. Stop without editing and request explicit approval.

### Stage 2 - execute approved batches

#### 6. Validate approval and comparability

Confirm that approval clearly accepts the proposal. Re-check repository, workload, environment, and baseline identity. If any factor that affects comparability changed materially, refresh the baseline or return to Stage 1.

#### 7. Implement one measured batch at a time

For each approved batch:

1. make the smallest proposed edit;
2. run focused correctness and contract checks;
3. repeat the same measurement protocol;
4. compare with baseline and the immediately previous accepted batch;
5. inspect secondary metrics and stated trade-offs;
6. accept, revise within scope, or reject the batch from evidence.

Do not keep a change that fails correctness, materially worsens an important secondary metric, produces an inconsistent result, or adds unjustified complexity. Preserve negative results so the same experiment is not repeated without new evidence.

Any optimization outside the approved mechanism or boundaries requires a new proposal and approval.

#### 8. Verify and report

Run proportionate correctness, static, integration, and platform checks in addition to performance measurement. Report baseline and optimized values with units, sample/statistic information, absolute delta, percentage change when valid, confidence limits or variance where available, trade-offs, failed experiments, and residual bottlenecks.

Return OPTIMIZED only when approved batches preserve correctness and comparable evidence supports the result. Return NO_JUSTIFIED_CHANGE when all approved experiments are rejected. Return BLOCKED when safe proof requires unavailable environment, data, access, or authorization.

## Output contract

Lead with the state: MEASURED, AWAITING_APPROVAL, OPTIMIZED, NO_JUSTIFIED_CHANGE, or BLOCKED.

Include:

- target path, metric, workload, and environment;
- baseline and evidence quality;
- bottleneck hypotheses and falsification results;
- ranked proposal or implemented batches;
- correctness and comparable before/after evidence;
- negative results, trade-offs, and residual risk;
- explicit approval request when awaiting edits.

Do not report a percentage when the baseline is zero or conditions are not comparable. Report throughput gains separately from lower-is-better reductions.

## Handoffs

- To repository-intelligence: the critical path crosses unknown components or consumers that require broader mapping.
- To debugging-investigator: the primary problem is wrong behavior, a crash, race, leak, or unexplained regression rather than a bounded performance cost.
- To codebase-evolution-controller: the justified remedy requires a dependency, runtime, schema, storage, or platform transition.
- To the relevant builder: the approved change requires platform-specific architecture, device, browser, or store integration beyond the measured batch.
- To verification-and-release: provide benchmark, correctness, operational, and residual-risk evidence for the final release decision.
- To a security workflow: a proposed cache, batching boundary, tenancy change, or shared state creates a security or privacy decision.

## Failure handling

- If measurement is noisy, increase samples or improve control before editing; do not select the best run.
- If production-like data is unavailable, use a sanitized representative fixture and label external validity limits.
- If tooling changes the workload materially, use lower-overhead evidence or triangulate with counters and controlled comparisons.
- If baseline and optimized conditions differ, label the result directional and do not claim causality.
- If the bottleneck is outside repository scope, report the owner, evidence, and smallest external experiment without changing it.
- If approval is ambiguous, remain AWAITING_APPROVAL; urgency is not edit permission.

## Stop conditions

Stop Stage 1 when the critical path is measured or explicitly blocked, material hypotheses have evidence, and each justified edit is a bounded proposal awaiting approval. Stop Stage 2 when approved batches are accepted or rejected through comparable evidence and correctness checks, or when further work needs a new decision, environment, budget, or authorization.
