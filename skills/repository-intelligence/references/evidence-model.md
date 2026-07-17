# Repository Intelligence Evidence Model

Use the lightest evidence that can support the consequence of the decision.

## Evidence classes

| Class | Meaning | Examples | Reporting rule |
| --- | --- | --- | --- |
| Direct | Repository artifact explicitly establishes the fact | workspace manifest, import, route registration, schema reference, CODEOWNERS rule, deployment target | Cite exact path and relevant key/symbol |
| Corroborated inference | Multiple signals imply the conclusion, but no single artifact declares it | directory plus build target plus consumer imports; history plus reviewer policy | Name signals and explain inference |
| Hypothesis | Plausible but unverified relationship | dynamic plugin load, external consumer, runtime-only feature flag | State how to test it and never present as fact |
| Negative evidence | A bounded search found no signal | no import in scanned source roots | State query, roots, exclusions, and why absence is not universal proof |

## Confidence

- **High:** direct evidence or multiple independent corroborating signals; no material contradiction.
- **Medium:** strong inference with incomplete runtime/history/external visibility.
- **Low:** hypothesis, convention-based interpretation, or contradictory evidence.

Confidence measures support, not importance.

## Preferred evidence order

1. public contract, manifest, build/deploy declaration;
2. executable registration or call/import path;
3. focused test or generated-source input;
4. ownership policy and recent history;
5. documentation and naming convention.

Documentation may be stale. History indicates stewardship, not formal accountability. Generated output points back to its generator.

## Coverage record

Record:

```yaml
repository_root: /absolute/or/repo-relative/path
base_ref: optional
head_ref: optional
included_roots: []
excluded_roots: []
search_methods: []
history_available: true
build_metadata_available: true
runtime_evidence_available: false
external_consumers_visible: false
```

## Contradictions

Do not average contradictory evidence. List the conflict, identify which artifact is authoritative in production, and request validation when authority is unclear.
