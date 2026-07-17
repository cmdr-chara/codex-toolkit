# Design Decisions and Justified Deviations

**Decision date:** 2026-07-17

## Repository fit

The target toolkit is intentionally compact and already includes `delegate-with-mission-cards`, a mission-card skill plus optional model-routed agents. This pack does not replace or silently fork that behavior.

- `multi-agent-work-coordinator` owns a repository-agnostic work graph, write-scope exclusivity, dependency waves, integration order, and acceptance evidence.
- `delegate-with-mission-cards` may remain the execution adapter that chooses specialized reader/writer roles and formats individual mission cards.
- When both are active, the coordinator produces the plan and ownership ledger; Mission Control dispatches the approved missions. The parent retains integration and release judgment.

## Progressive disclosure

Core skills avoid volatile version numbers. Current ecosystem observations are isolated in dated reference files under the relevant implementation skill. This permits refreshes without rewriting stable reasoning and safety rules.

## No runtime `shared/` folder

The brief permits `shared/` only for genuinely shared material. It is intentionally omitted because:

1. skills should remain installable independently;
2. a shared runtime file creates hidden coupling and broken partial installs;
3. the overlap rules are small enough to state explicitly in each relevant skill;
4. maintenance artifacts already live at the pack root.

## Scripts

Scripts exist only for deterministic inspection, overlap detection, report aggregation, drift heuristics, and validation. They are read-only, standard-library Python, path-bounded, and network-free. No script performs package installation, Git cleanup, code generation, or automatic source edits.

## Design-source adaptation

`product-design-director` and `screenshot-to-interface` use original wording and a new information architecture. Adapted concepts are limited to:

- infer context before selecting an aesthetic;
- calibrate direction through explicit axes rather than a default look;
- resist repetitive template-like compositions and meaningless visual chrome;
- audit an existing interface before changing it;
- treat a visual reference as an evidence source and verify fidelity iteratively;
- run a preflight review before declaring visual work complete.

These ideas are integrated with product-state modeling, accessibility, responsive behavior, provenance, asset handling, component boundaries, and evidence contracts not present as a cohesive system in the source. No substantial source prose or implementation code was copied. The required MIT notice is preserved in `THIRD_PARTY_NOTICES.md` and per-skill provenance references.

## Four implementation batches

1. Repository analysis and coordination: skills 1–3.
2. Evidence, diagnosis, and documentation: skills 4–6.
3. Product design and web delivery: skills 7–9.
4. Mobile architecture and platform delivery: skills 10–12.

A single section schema, evidence vocabulary, safety baseline, and handoff model is retained across all batches without mechanically duplicating paragraphs.

## Scope deviations

- The deliverable is a repository-ready additive pack rather than a direct modification of a live clone because direct Git cloning was unavailable in the execution environment. Repository trees, raw files, README files, and licenses were inspected through current web/raw sources; the limitation is recorded in the research ledger.
- The pack includes an append-only `skills/llms.txt` fragment instead of overwriting the target catalog.
- External URL availability is not asserted by the offline validator. The source ledger records URLs and the validator checks their presence, scheme, and dated-review metadata; source freshness still requires human or web-enabled review.
