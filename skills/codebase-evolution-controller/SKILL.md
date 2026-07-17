---
name: codebase-evolution-controller
description: Control dependency upgrades, framework migrations, schema or API transitions, compatibility windows, staged rollouts, rollback, and removal of legacy paths using current evidence. Use when a repository must move from a known current state to a defined target state without breaking consumers. Do not use to diagnose an unexplained failure, perform an ordinary feature change, or make the final release-readiness decision.
---

# Codebase Evolution Controller

Treat evolution as a controlled state transition, not a version-number edit.

## Trigger boundary

Use this skill for:

- upgrading a framework, runtime, SDK, compiler, database, or major dependency;
- migrating API, event, storage, serialization, or configuration contracts;
- planning dual-read/dual-write, compatibility adapters, canaries, or phased client transitions;
- removing a deprecated path after measurable exit criteria are met.

Do not trigger for:

- finding why the current system fails—use `debugging-investigator` first;
- adding a feature that does not change a compatibility boundary;
- package shopping without a concrete repository and decision;
- approving a release—hand integrated evidence to `verification-and-release`.

## Required inputs

Capture:

1. repository state and relevant component/consumer map;
2. current state, desired target, business/technical reason, and deadline;
3. supported runtimes/platforms and external consumers;
4. production data/configuration and deployment topology;
5. rollback constraints, maintenance window, and acceptable compatibility period;
6. current primary-source evidence for target compatibility and security.

If target state is not specified, compare feasible targets and recommend one with evidence; do not silently choose “latest.”

## Safety baseline

- Inspect and preserve uncommitted work.
- Read manifests and lockfiles before proposing commands. Never assume package manager, workspace, or build mode.
- Do not run automatic upgrade, code-mod, formatter, migration, or generator tools without first recording scope, expected changes, version, and rollback.
- Never edit generated outputs without identifying and running the authoritative generator.
- Back up or snapshot production data through the system's established mechanism before irreversible transitions; do not invent a backup command.
- Avoid destructive database or Git commands. Rehearse rollback against representative data where consequence warrants it.

## Workflow

### 1. Define the transition contract

Write:

```text
Current state:
Target state:
Reason:
Must remain compatible with:
Can change:
Cannot change:
Success measures:
Compatibility window:
Rollback point and trigger:
Legacy-removal criteria:
```

A migration is incomplete without an exit condition for temporary compatibility code.

### 2. Establish a reproducible baseline

Before changing versions or contracts:

- record manifests, lockfiles, toolchain/runtime versions, generated inputs, and deployment images;
- run the nearest reliable build/test/static checks in the current state;
- capture representative contract fixtures, schemas, API responses, migration checksums, or storage samples;
- record known failures separately from migration regressions;
- inventory manifests with [`scripts/manifest_inventory.py`](scripts/manifest_inventory.py).

```sh
python skills/codebase-evolution-controller/scripts/manifest_inventory.py . --format markdown
```

If the baseline cannot pass, define an explicit “no worse than baseline” comparison and isolate known failures.

### 3. Gather compatibility evidence

Use primary sources and the rubric in [`references/compatibility-evidence.md`](references/compatibility-evidence.md). Verify:

- current and target framework/runtime support ranges;
- direct and transitive peer constraints;
- breaking changes, removed APIs, migration guides, security advisories, and deprecation status;
- toolchain, operating-system, browser, device, store, database, and infrastructure requirements;
- license changes and deployment/runtime cost where dependencies change;
- maintenance activity and whether built-in capabilities now replace a dependency.

Popularity is context, not proof. Record source URL and checked date for every material version/package claim.

### 4. Map the compatibility surface

From the repository map, enumerate:

- public/internal APIs, schemas, events, storage formats, and CLI/configuration;
- generated code and generator compatibility;
- deployment jobs, images, caches, feature flags, observability, and rollback tooling;
- internal and external consumers by upgrade cadence;
- test fixtures, snapshots, docs, examples, and operational runbooks.

Classify each as `unchanged`, `adapter`, `dual-path`, `coordinated cutover`, `data rewrite`, or `retired`.

### 5. Choose the transition pattern

Select by risk and reversibility:

- **in-place compatible upgrade:** behavior and contracts remain compatible; fast rollback exists;
- **expand/contract:** add compatible shape, migrate consumers/data, then remove old shape;
- **adapter/strangler:** isolate old/new APIs behind a stable boundary;
- **dual-read:** read both formats while new writes converge;
- **dual-write:** only with idempotency, reconciliation, observability, and a defined source of truth;
- **shadow/canary:** execute new behavior on a controlled subset before cutover;
- **coordinated stop-the-world:** only when compatibility is impossible and an approved maintenance boundary exists.

Do not use dual-write by default; it creates consistency and rollback complexity.

### 6. Build stages and gates

Use [`references/migration-plan-template.md`](references/migration-plan-template.md). Every stage needs:

- entry assumptions and exact artifact/version changes;
- owned write surfaces;
- compatibility guarantee;
- data or traffic movement;
- focused verification and observability;
- rollback action and latest safe rollback point;
- promotion criteria and blocker criteria.

Prefer small coherent transitions that leave the repository runnable. Separate mechanical changes from behavior changes when it improves diagnosis and review.

### 7. Implement or direct the migration

For each stage:

1. refresh repository state;
2. change the minimum authoritative files;
3. update generated artifacts through reviewed generators;
4. add compatibility code before migrating dependents;
5. update tests for old and new behavior during the window;
6. update telemetry before traffic or data cutover;
7. record exact commands and results;
8. inspect the diff for unrelated churn.

When package manager output changes broadly, explain why each lockfile class changed and reject unexpected registry, source, or transitive shifts until reviewed.

### 8. Verify across layers

At minimum consider:

- build/type/static analysis in every supported target;
- focused unit/contract/integration tests for old and new paths;
- serialization/schema/data round trips and forward/backward compatibility;
- representative migration and rollback on a safe copy of data;
- performance/resource regressions where runtime/toolchain changed;
- security checks and known-advisory resolution;
- deployment, startup, health, observability, and operational procedures;
- external client or platform compatibility.

Feature-level verification stays with the implementing team; produce an evidence package for the final release gate.

### 9. Roll out and observe

Define:

- cohort or environment order;
- metrics, traces, logs, data reconciliation, and user-impact signals;
- automatic/manual rollback triggers;
- pause duration or sample threshold justified by traffic and risk;
- ownership during the rollout;
- behavior when old and new versions coexist.

Do not call a rollout reversible after the first irreversible data write unless a tested reverse transform or restore path exists.

### 10. Contract and remove legacy paths

Remove adapters, flags, old dependencies, data columns, and compatibility tests only after stated exit evidence is met. Verify no remaining consumer, configuration, documentation, dashboard, alert, or rollback procedure requires the old path.

## Handoffs

- From `repository-intelligence`: consumers, boundaries, conflict surfaces, and ownership.
- From `debugging-investigator`: established root cause when an upgrade is the minimal remedy.
- To `documentation-synchronizer`: user/developer migration guides, configuration, API, runbook, and deprecation updates.
- To `verification-and-release`: stage evidence, residual risks, rollout/rollback readiness, and legacy-removal status.
- To `multi-agent-work-coordinator`: approved stage graph and exclusive surfaces when parallel execution is safe.

## Failure handling

- If primary sources conflict, do not guess; pin the unresolved matrix and prototype the smallest compatibility case.
- If automated migration output is unexpectedly broad, stop, restore through ordinary file review/version control without discarding user work, and narrow the tool scope.
- If rollback fails in rehearsal, block rollout or redefine the last reversible point.
- If external consumers are unknown, lengthen the compatibility window or add version negotiation rather than assuming coordinated adoption.
- If a security fix requires urgent movement, retain evidence and rollback discipline; urgency changes sequencing, not truth requirements.

## Output contract

Return:

- transition contract and source-checked compatibility matrix;
- staged plan with owners, gates, and rollback points;
- exact files/versions changed when implementation occurred;
- baseline and per-stage verification results;
- rollout/observability plan;
- residual risks, blockers, and legacy-removal criteria.

## Stop conditions

Stop and escalate when target compatibility is unsupported, data loss cannot be bounded, rollback is fictional, required consumers cannot coexist, or credentials/production access are unavailable. Complete when the target state is verified, rollout evidence satisfies promotion criteria, documentation is synchronized, and temporary paths have explicit owners and removal dates or criteria.
