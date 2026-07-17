# Hypothesis Ledger

```markdown
| ID | Causal mechanism | Explains | Conflicts with | Evidence if true | Evidence if false | Discriminating experiment | Result | Confidence/state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | | | | | | | | ACTIVE |
```

Allowed states: `ACTIVE`, `SUPPORTED`, `WEAKENED`, `REJECTED`, `SUPERSEDED`, `UNTESTABLE`.

## Ranking rules

Rank by explanatory coverage, consistency with timing and nonfailing cases, prior evidence in this system, and experiment cost/risk. Do not rank by narrative appeal.

A useful hypothesis states a mechanism:

- Weak: “the cache is broken.”
- Testable: “a cache key omits tenant ID, so a warm entry from tenant A is returned for tenant B until TTL expiry.”

## Experiment record

```text
Experiment ID:
Hypotheses distinguished:
Candidate/environment:
Controlled variable:
Expected result per hypothesis:
Safety/data handling:
Raw artifact:
Observed result:
Interpretation:
New confidence/state:
```
