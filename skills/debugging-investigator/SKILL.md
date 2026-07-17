---
name: debugging-investigator
description: Diagnose a concrete failure through controlled reproduction, ranked hypotheses, minimally invasive instrumentation, causal tracing, and falsification, then recommend the smallest explanatory fix and regression test. Use when observed behavior is wrong and the cause is uncertain. Do not use for planned upgrades, broad refactors, feature design, or release approval.
---

# Debugging Investigator

Convert symptoms into a defensible causal explanation. Evidence precedes edits.

## Trigger boundary

Use this skill for:

- a reproducible or reported crash, incorrect result, regression, hang, leak, race, flaky test, or production incident;
- a failure that crosses components and needs trace/causal analysis;
- ranking competing explanations and designing discriminating experiments;
- recommending a minimal fix and regression coverage after cause is established.

Do not trigger for:

- a known framework/dependency migration—use `codebase-evolution-controller`;
- preventive architecture mapping without a symptom—use `repository-intelligence`;
- implementing an already-understood bug fix unless investigation evidence must be reconstructed;
- deciding whether the final integrated release can ship.

## Required inputs

Collect:

1. exact observed behavior and expected behavior;
2. first/last known versions, timestamp, environment, frequency, and affected scope;
3. reproduction steps, request/input identifiers, logs/traces/crash/test output;
4. repository state and recent relevant changes;
5. safety constraints for production data, traffic, secrets, and instrumentation;
6. what has already been tried and its result.

Normalize relative terms. Replace “after the last deploy” with exact candidate, deployment, and time when available.

## Safety baseline

- Preserve the working tree and production state; do not reset, clean, or mutate data to make reproduction easier.
- Redact secrets, personal data, tokens, and customer payloads from evidence.
- Use read-only inspection and isolated fixtures before live experiments.
- Add instrumentation behind the narrowest safe scope and remove or document it after use.
- Do not disable security, authorization, integrity checks, rate limits, or safeguards merely to reach the symptom.
- Never claim root cause from temporal correlation alone.

## Workflow

### 1. Write the failure statement

Use:

```text
Given <preconditions/input>, in <environment/version>,
when <action/event> occurs,
the system produces <observed result>,
but the contract requires <expected result>.
Frequency/scope:
First/last known:
User/operational impact:
```

Separate primary symptom from downstream noise. A timeout may be the symptom; a retry storm and queue growth may be consequences.

### 2. Establish evidence integrity

Verify candidate/version, clock/timezone, correlation identifiers, sampling, log level, and whether the evidence came from the same request/process/build. Preserve raw artifacts before summarizing. Identify gaps such as truncated stack traces, missing spans, or client/server clock skew.

### 3. Reproduce or bound the symptom

Prefer the smallest representative environment:

1. existing failing test or captured input;
2. isolated component/integration harness;
3. local or staging reproduction with production-like configuration;
4. narrowly controlled production observation when no safe substitute exists.

Vary one condition at a time. Record attempts including non-reproductions. If reproduction is intermittent, measure the condition space—load, timing, order, data shape, device, region, feature flag, dependency version—rather than looping blindly.

If direct reproduction is impossible, bound the failure with positive and negative examples and continue with explicit lower confidence.

### 4. Construct the timeline and causal path

Trace from trigger to symptom across:

- input validation and normalization;
- state transitions and feature/configuration decisions;
- calls, messages, jobs, retries, caches, locks, and transactions;
- serialization/deserialization and schema/version boundaries;
- resource limits, cancellation, timeouts, lifecycle, and cleanup;
- output rendering/delivery and client interpretation.

Use repository paths plus runtime evidence. Static code reachability is not proof a branch executed.

### 5. Build and rank hypotheses

Use [`references/hypothesis-ledger.md`](references/hypothesis-ledger.md). Each hypothesis must state:

- causal mechanism, not merely a component name;
- observations it explains and observations it conflicts with;
- expected evidence if true and if false;
- cheapest safe discriminating experiment;
- current confidence and reason.

Start with several plausible mechanisms. Include configuration, data, environment, concurrency, dependency, and observability explanations where credible. Do not anchor on the latest change without comparison evidence.

### 6. Instrument discriminating points

Follow [`references/causal-tracing-playbook.md`](references/causal-tracing-playbook.md). Add the minimum signal needed to distinguish hypotheses:

- structured event at a state transition;
- correlation/causation identifier across boundaries;
- value shape, version, branch decision, duration, queue depth, retry count, or resource lifecycle;
- assertion/invariant in a safe test or nonproduction environment;
- profile, heap, thread, query, network, or scheduler evidence when the mechanism requires it.

Define expected output before running the experiment. Logging everything increases noise and data exposure without necessarily increasing information.

### 7. Run falsification experiments

For each experiment record setup, controlled variable, candidate/version, raw evidence, result, and hypothesis update. Favor tests that can disprove the leading explanation. Repeat only when the mechanism is probabilistic, and state sample size and conditions without inventing statistical confidence.

Retire hypotheses explicitly. If evidence contradicts all current hypotheses, expand the causal boundary rather than forcing a fit.

### 8. Establish the root-cause chain

A complete chain links:

```text
trigger → violated assumption/defect → state transition → propagated effect → observed symptom
```

Also explain why safeguards/tests/monitoring did not catch it. Distinguish:

- root defect;
- enabling condition;
- trigger;
- amplifiers;
- user-visible and operational effects.

Require that the chain predicts both failing and nonfailing cases.

### 9. Recommend the minimal explanatory fix

Choose the smallest change that breaks the causal chain while preserving contracts. Compare alternatives for correctness, blast radius, compatibility, observability, and rollback. Avoid broad upgrades/refactors unless evidence shows the current version or architecture is the cause and a narrow remedy is unavailable.

Before implementation, identify:

- files/contracts affected;
- invariant restored;
- new failure modes;
- rollback or disable path;
- whether the change is a migration requiring `codebase-evolution-controller`.

### 10. Design regression evidence

Create a test that fails for the established mechanism, not only the original incidental input. Include:

- smallest deterministic reproduction;
- boundary/negative case that must remain valid;
- appropriate integration level for the failed contract;
- concurrency/timing harness when relevant;
- assertion that would fail if the causal defect returns;
- observability assertion when detection was part of the gap.

Run the regression against the unfixed behavior when practical or otherwise prove its pre-fix failure from a preserved fixture/candidate.

## Output contract

Return:

- failure statement and impact;
- evidence inventory and reproduction status;
- timeline/causal path;
- ranked hypothesis ledger with experiments;
- root-cause chain and confidence;
- minimal-fix recommendation with alternatives and risks;
- regression-test design;
- observability/prevention gaps;
- unknowns and next discriminating action if cause remains unresolved.

## Handoffs

- To `repository-intelligence` when the causal boundary or consumer graph is unknown and broader mapping is required.
- To `codebase-evolution-controller` when the proven remedy changes versions, schema, or public compatibility.
- To the relevant builder for a bounded fix and feature-level verification.
- To `verification-and-release` with regression and residual-risk evidence after integration.
- To `documentation-synchronizer` when behavior, troubleshooting, runbooks, or known limitations change.

## Failure handling

- If evidence is contradictory, preserve both paths and test candidate identity, configuration, clock, and sampling before code theories.
- If production instrumentation is unsafe, use sampled metadata, sanitized fixtures, existing telemetry, or a controlled shadow environment.
- If the symptom disappears after an unrelated restart, investigate state/resource lifecycle; do not declare it fixed.
- If a proposed fix works but the causal mechanism remains unexplained, classify it as mitigation, not root-cause resolution.
- If the issue is actively harming data or security, prioritize containment and evidence preservation, then resume causal analysis.

## Stop conditions

Stop with `DIAGNOSED` when one causal chain explains and predicts the evidence and a regression test targets it. Stop with `BOUNDED` when the failure is narrowed and the next required evidence is unavailable. Never manufacture certainty; state confidence and the unresolved alternative.
