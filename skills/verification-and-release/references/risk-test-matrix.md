# Risk and Test Matrix

## Risk dimensions

Assess consequence, exposure, novelty, coupling, detectability, and reversibility.

| Tier | Typical shape | Minimum evidence pattern |
| --- | --- | --- |
| Low | Local, reversible, no public contract or sensitive path | Diff review; nearest deterministic test/static check; focused manual check if UI |
| Medium | Multiple components or user journey; recoverable; bounded consumers | Static + focused unit/contract/integration evidence; negative path; affected-consumer inspection; representative environment |
| High | Auth/security/privacy/money/data integrity/public schema/migration/store or broad blast radius | Independent/adversarial review; old/new compatibility; failure/recovery and rollback rehearsal; representative E2E; observability and staged rollout |
| Critical | Irreversible or safety/regulatory impact; unknown external consumers; systemic infrastructure | Explicit authority and risk acceptance; formal controls; production-like rehearsal; rollback/restore or proven forward recovery; monitored canary; release owner sign-off |

## Failure-mode prompts

- stale or unauthorized data exposure;
- privilege escalation or tenant boundary break;
- duplicate/lost transaction or job;
- partial migration and mixed-version behavior;
- retry storms, race, deadlock, or idempotency failure;
- cache inconsistency or delayed invalidation;
- inaccessible keyboard/screen-reader flow;
- degraded startup, memory, latency, bundle, battery, or network use;
- missing telemetry or rollback after a silent failure;
- platform/store rejection or update-runtime mismatch.

## Evidence selection rule

For every credible high-consequence failure, name at least one pre-release detector and one post-release detector or explain why the failure cannot escape pre-release checks.
