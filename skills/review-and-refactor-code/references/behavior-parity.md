# Behavior-Parity Refactoring

Use this reference when a structural proposal or approved refactor must preserve externally observable behavior.

## Build the parity ledger

Record the affected contract at the nearest stable boundary:

| Surface | Before evidence | Invariant | Verification |
| --- | --- | --- | --- |
| Inputs | Accepted shapes, defaults, invalid cases | Same acceptance and normalization | Characterization or unit tests |
| Outputs | Values, schema, ordering, formatting | Same observable result | Golden or contract tests |
| Errors | Type, message contract, status, retryability | Same caller-visible failure semantics | Negative tests |
| Side effects | Writes, events, logs, cleanup | Same count, order, and lifetime | Integration tests, spies, or fixtures |
| Timing and state | Sequencing, cancellation, concurrency | No new race or lifecycle gap | Targeted harness |
| Compatibility | Imports, API, config, serialization | Existing consumers continue to work | Consumer and build checks |

Do not preserve an accidental implementation detail unless callers or tests rely on it as a contract.

## Design safe slices

Prefer this order:

1. Add missing characterization evidence.
2. Introduce the new internal boundary behind the existing interface.
3. Move one responsibility at a time.
4. Redirect callers in bounded groups.
5. Remove a compatibility adapter only after all callers and tests prove it unused.
6. Delete artifacts made obsolete by this refactor and nothing unrelated.

Each slice must have one purpose, a reversible stopping point, and a check that would detect behavior drift.

## Reject unsafe proposals

Re-propose or stop when:

- the change mixes feature behavior with structure;
- public compatibility would change without a migration plan;
- the target boundary cannot be characterized;
- the design adds abstraction without reducing demonstrated coupling or complexity;
- generated or vendored output is treated as authored source;
- verification cost exceeds the stated value and risk reduction.

## Handoff evidence

Report the parity ledger, approved slices, checks per slice, adapter removal conditions, intentional behavior changes kept out of scope, and any invariant that remains unproven.
