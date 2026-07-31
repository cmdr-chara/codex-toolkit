# Review Finding Contract

Use this contract to decide whether a concern belongs in a code-review result.

## Admission test

Include a finding only when all are true:

1. The reviewed change or bounded target contains the cause or makes the failure reachable.
2. A concrete input, state, environment, or event sequence exposes the problem.
3. The result violates an observable behavior, compatibility, safety, data, or operational contract.
4. The location is precise enough for an author to act on.
5. A feasible correction or decisive verification exists.

Exclude style preference, speculative future risk, unrelated pre-existing defects, and behavior prevented by surrounding code.

## Priority

| Priority | Meaning |
| --- | --- |
| P0 | Immediate catastrophic impact such as active data loss, severe security compromise, or service-wide outage. |
| P1 | High-confidence defect likely to affect critical behavior or many users; should block integration. |
| P2 | Real defect with bounded impact or a less common trigger; should normally be fixed before release. |
| P3 | Low-impact but actionable correctness or maintainability defect with a concrete failure mode. |

Priority reflects consequence and reach, not fix size. Keep optional refactor opportunities outside this scale.

## Finding shape

    [P1-P3] Short imperative title
    Location: path plus the tightest useful line or symbol
    Contract: expected behavior
    Trigger: input/state/sequence
    Impact: observable failure and affected consumer
    Evidence: why the reviewed code causes it
    Correction: smallest feasible direction
    Confidence: high | medium | low, with reason when not high

Keep the body concise. Cite surrounding consumers only when needed to prove impact.

## Review completion

After findings, state:

- reviewed scope and refs;
- material areas not inspected;
- tests or runtime evidence used;
- whether no findings means clean evidence or limited coverage.
