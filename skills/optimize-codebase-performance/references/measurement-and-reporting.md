# Performance Measurement and Reporting

Use one protocol for baseline and comparison unless the purpose is to measure the protocol itself.

## Measurement record

Capture:

- candidate revision and working-tree state;
- hardware, OS, runtime, dependencies, build mode, and resource limits;
- exact workload, input size, concurrency, cache state, and external dependencies;
- command or procedure, profiler settings, warm-up, sample count, and run order;
- metric, units, statistic, variance or range, and raw artifact location;
- background load, throttling, sampling overhead, and known confounders.

Use production-like builds for user-facing conclusions. Use microbenchmarks only to isolate a mechanism already connected to the critical path.

## Comparison rules

- Interleave or randomize baseline and candidate runs when environmental drift is material.
- Use multiple samples for timings; report median and a tail or peak statistic when outliers matter.
- Compare cold with cold and warm with warm.
- Treat changed hardware, data, concurrency, build flags, cache state, or dependencies as non-comparable unless modeled explicitly.
- Preserve raw values and rejected runs; explain exclusions before seeing the desired outcome.

For lower-is-better metrics:

    reduction percent = (baseline - candidate) / baseline * 100

For higher-is-better metrics:

    increase percent = (candidate - baseline) / baseline * 100

Do not calculate a percentage from a zero baseline. Report absolute delta and units in every case.

## Result table

| Batch | Workload | Metric | Baseline | Candidate | Absolute delta | Relative change | Variance or confidence | Correctness | Trade-off |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Label the conclusion:

- Comparable: same material conditions; causal claim is supported.
- Directional: conditions differ or noise prevents a precise causal estimate.
- Inconclusive: evidence cannot distinguish improvement from variation.
- Regressed: target or important secondary metric worsened materially.

Include negative results and the next smallest experiment only when another experiment is justified.
