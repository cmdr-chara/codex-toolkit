---
name: documentation-synchronizer
description: Detect documentation drift caused by code, API, schema, configuration, migration, UI, deployment, or operational changes and update all affected user and maintainer surfaces consistently. Use when behavior or contracts changed and documentation must be mapped, edited, and validated. Do not use to invent product behavior, write unrelated marketing copy, or replace implementation verification.
---

# Documentation Synchronizer

Treat documentation as a distributed contract with users, developers, operators, and integrators.

## Trigger boundary

Use this skill for:

- identifying docs affected by an implementation or migration diff;
- synchronizing user guides, API references, configuration, examples, architecture, runbooks, and release notes;
- auditing stale commands, options, screenshots, generated docs, or cross-links;
- verifying a documentation-only change against current code and public contracts.

Do not trigger for:

- deciding what the product should do;
- visual brand/campaign copy unrelated to repository behavior;
- a code change with no externally or operationally meaningful documentation surface;
- generating API docs by editing generated output instead of its source.

## Required inputs

Obtain:

1. changed files/diff and final intended behavior;
2. repository documentation map and audience/release context;
3. authoritative sources for APIs, schemas, config, CLI, environment, and defaults;
4. supported versions and migration/deprecation policy;
5. documentation tooling, generators, link/check commands, and localization policy;
6. known generated, translated, versioned, or externally hosted documentation boundaries.

If behavior is ambiguous, stop and return the exact implementation question. Do not resolve ambiguity through prose.

## Safety baseline

- Inspect worktree state and preserve unrelated edits.
- Do not rewrite all docs to normalize style; update only impacted surfaces and necessary consistency links.
- Do not edit generated docs directly unless the repository explicitly treats them as source.
- Never copy secrets, production identifiers, private URLs, or personal data into examples.
- Mark destructive examples clearly and provide safe prerequisites; do not invent executable commands.
- Keep version-specific instructions scoped and dated where they can become stale.

## Workflow

### 1. Extract the contract delta

Summarize changes under applicable categories:

- behavior and user flow;
- public/internal API, event, schema, serialization;
- CLI command, flag, output, exit code;
- configuration, environment variable, secret reference, default;
- installation, dependency, compatibility, migration, deprecation;
- architecture, ownership, build/deploy/runtime operation;
- UI state, accessibility behavior, screenshot, or terminology;
- troubleshooting, observability, failure recovery, and rollback.

Distinguish newly introduced behavior, changed behavior, removed behavior, and correction of previously inaccurate docs.

### 2. Map documentation surfaces

Use [`references/doc-surface-map.md`](references/doc-surface-map.md). Search beyond `docs/`:

- root/package READMEs and install guides;
- inline API comments and generated-doc sources;
- OpenAPI/GraphQL/protobuf/schema descriptions;
- CLI help, `--help` snapshots, sample config, `.env.example`;
- examples, tutorials, fixtures, templates, code snippets;
- architecture decisions, diagrams, ownership, contributor docs;
- runbooks, dashboards/alert links, deployment/rollback guides;
- changelog, release notes, deprecation and migration guides;
- UI labels, empty/error/help states, screenshots, alt text;
- localization source and translation workflows.

Use the read-only heuristic scanner as a starting point:

```sh
python skills/documentation-synchronizer/scripts/doc_drift_scan.py . --base HEAD~1 --format markdown
```

Or provide an explicit changed-file list when history is unavailable:

```sh
python skills/documentation-synchronizer/scripts/doc_drift_scan.py . \
  --files src/config.ts api/openapi.yaml deploy/service.yml --format markdown
```

The scanner suggests surfaces; it cannot determine semantic drift.

### 3. Establish authority and audience

For each fact identify the authoritative artifact and audiences. Examples:

- runtime default → code/config schema, not an old README;
- API field → source schema and compatibility policy;
- install command → current package manager/installer and supported runtime;
- operational procedure → deployed topology and approved runbook;
- UX label/state → shipped component and product terminology.

Do not propagate a possibly stale sentence into more files. Correct the source and references.

### 4. Build the impact plan

Create:

```text
changed contract | audience | authoritative source | doc surfaces | update type | validation
```

Classify update type as `add`, `change`, `remove`, `deprecate`, `migrate`, `regenerate`, `link`, or `no change—reason`.

Prioritize release-blocking surfaces: unsafe migration steps, incompatible API/config instructions, missing security/privacy behavior, and invalid operational recovery.

### 5. Update coherently

Apply the smallest coherent set of changes:

- align terminology, names, defaults, supported versions, and examples;
- show prerequisites, expected result, failure behavior, and rollback where needed;
- document old/new behavior through the compatibility window;
- keep snippets executable and scoped to the repository's actual tools;
- use relative links when repository portability matters;
- add accessible alt text and update screenshots only when the visual change affects comprehension;
- update changelog/release notes according to repository policy, not automatically for every edit;
- route generated content through its generator and review the resulting diff.

Do not conceal limitations or unsupported cases in vague prose.

### 6. Cross-surface consistency review

Compare all affected surfaces for:

- exact command/flag/environment names and case;
- defaults, ranges, required/optional status, and version support;
- API request/response/error examples;
- schema and generated-client descriptions;
- user-facing labels versus screenshots and help text;
- migration ordering, mixed-version behavior, rollback, and data implications;
- architecture diagrams versus actual components and ownership;
- release notes versus the final integrated behavior.

Search for removed terms and old examples, including aliases and previous names.

### 7. Validate

Use [`references/update-checklist.md`](references/update-checklist.md). Run repository-provided checks where available:

- Markdown/MDX parser, formatter, style or spelling policy;
- internal and external link checker;
- documentation build and generated-doc diff;
- snippet/type/compile/test harness;
- CLI help or API schema comparison;
- screenshot/visual check when changed;
- localization key and untranslated-content checks.

If a command cannot be run, state why and inspect the closest deterministic source. A rendered page is not enough if its snippet is invalid.

### 8. Report the synchronized set

Return:

- contract delta;
- surfaces reviewed and changed;
- authoritative evidence for each material fact;
- validation commands/results;
- generated or localization follow-ups;
- intentionally unchanged surfaces with reason;
- residual drift risk and owner.

## Interaction boundaries

- Builders and `codebase-evolution-controller` own behavior; this skill documents the verified result.
- `repository-intelligence` can map documentation ownership and component links.
- `verification-and-release` decides whether missing or invalid documentation blocks release.
- `product-design-director` owns voice/direction for experience design; this skill maintains factual consistency.

## Failure handling

- If docs conflict with code, verify intended behavior with implementation evidence before choosing a side.
- If generated docs differ unexpectedly, inspect generator version/input and stop before manual patching.
- If external docs cannot be edited, prepare an exact handoff and mark repository references that would otherwise mislead.
- If localization cannot be completed, follow repository fallback/release policy and state untranslated risk.
- If an example requires credentials or destructive actions, replace with safe placeholders and explicit setup rather than publishing real values.

## Stop conditions

Stop when all affected audiences and surfaces are accounted for, material facts trace to authoritative artifacts, validation is recorded, and remaining external/generated/localized work has an owner. Do not mark synchronized while known contradictory instructions remain.
