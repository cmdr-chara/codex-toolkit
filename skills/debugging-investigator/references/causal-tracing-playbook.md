# Causal Tracing Playbook

Select the signal that exposes the disputed state transition.

| Suspected mechanism | Useful evidence | Common trap |
| --- | --- | --- |
| Wrong branch/config/flag | evaluated value, source, version, targeting reason | logging configured value but not effective value |
| Data/schema mismatch | schema/version, field presence, serialized bytes or sanitized shape | inspecting only producer or only consumer |
| Cache inconsistency | key, namespace, version, hit/miss, age, invalidation event | logging values that expose sensitive payloads |
| Retry/idempotency | attempt ID, operation key, side-effect ledger, response class | treating duplicate logs as duplicate effects without IDs |
| Race/order | monotonic sequence, lock/state transitions, scheduler/thread/task IDs | relying on wall-clock order across hosts |
| Resource leak | acquisition/release counters, heap/file/socket/task lifecycle | profiling only after restart or debug-only behavior change |
| Timeout/cancellation | deadline propagation, remaining budget, cancellation owner | measuring one layer while hidden queueing consumes budget |
| Database/query | query shape/plan, transaction boundaries, row counts, lock waits | logging full sensitive queries or testing unlike production data |
| UI/mobile lifecycle | mount/focus/background state, event subscription, render/commit timing | assuming emulator lifecycle equals device behavior |

## Instrumentation rules

- Decide the question and expected outcomes first.
- Correlate across boundaries with an existing safe identifier or a new opaque one.
- Prefer structured fields over free-form messages.
- Bound cardinality and sampling.
- Avoid secrets, personal content, and full payloads.
- State lifetime and removal/retention owner for temporary instrumentation.
- Confirm instrumentation does not materially alter timing for race/performance defects.
