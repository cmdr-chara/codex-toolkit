# Cross-Layer Bottleneck Playbook

Read only the sections relevant to the measured critical path. A pattern is a hypothesis source, not proof.

## Application and runtime

Inspect algorithms, repeated parsing or transformation, allocation and copying, synchronization, serialization, logging, cleanup, and work performed before it is needed. Verify hot functions and call counts with a profiler, trace, counter, or controlled input comparison.

Prefer removing or narrowing work before replacing algorithms. Preserve ordering, numeric behavior, error semantics, and cancellation.

## Database and external services

Inspect query count and plans, rows scanned, payload size, N+1 access, connection pools, retries, timeouts, batching, and independent calls executed serially. Preserve authorization, tenant scope, filtering, soft deletion, pagination, transaction behavior, and rate limits.

Do not add caching until key scope, invalidation, bounds, consistency, and permission isolation are proven.

## Memory and lifecycle

Inspect peak resident memory, allocation rate, retained objects, unbounded collections, cache growth, duplicate buffers, resource ownership, and teardown. Distinguish a leak from intentional retention or allocator behavior through repeated lifecycle evidence.

Avoid a lower wall-time result that creates unacceptable peak memory or cleanup risk.

## Frontend and rendering

Inspect bundle and import cost, network waterfalls, hydration, render frequency, derived work, long lists, image decoding, layout and paint, animation frame time, and main-thread blocking. Measure a production-like build and the actual interaction.

Preserve accessibility semantics, focus, responsive behavior, visual output, and event ordering. Memoization without a measured render cost is not evidence.

## GPU and media

Inspect utilization, memory, transfers, synchronization, kernel or shader duration, batching, decode and encode stages, and pipeline stalls. Record device, driver, precision, resolution, and thermal state. Do not generalize one device result without labeling the limit.

## Infrastructure and cost

Inspect worker and pool sizing, queue depth, concurrency, autoscaling, container limits, storage and network behavior, cold starts, build images, and observability overhead. Model throughput, tail latency, reliability, and cost together.

Do not change production capacity, purchasing, permissions, or deployment settings without separate authorization and rollback controls.

## Candidate ranking

Rank with these questions:

1. Does runtime evidence place meaningful cost here?
2. Does the mechanism explain the observed workload shape?
3. Can the smallest change falsify the hypothesis?
4. Is the change reversible and behavior-preserving?
5. Which secondary metric or operational risk could worsen?
6. Is the expected gain worth the verification and maintenance cost?
