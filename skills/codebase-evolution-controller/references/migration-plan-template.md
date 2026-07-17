# Migration Plan Template

```markdown
# Evolution Plan: <current> → <target>

Information checked: YYYY-MM-DD

## Transition contract
- Reason:
- Current state:
- Target state:
- Must remain compatible with:
- Success measures:
- Compatibility window:
- Last reversible point:
- Legacy-removal criteria:

## Baseline
| Check/artifact | Command or source | Result | Known issue |

## Compatibility evidence
| Surface/package | Current | Target | Change/security/license notes | Built-in alternative | Choose/avoid | Sources |

## Consumer and data map
| Consumer/data set | Current contract | Transition mode | Owner | Cutover evidence |

## Stages
### Stage N — <name>
- Entry conditions:
- Authoritative files:
- Changes:
- Compatibility guarantee:
- Data/traffic action:
- Verification:
- Observability:
- Rollback procedure:
- Promotion criteria:
- Blockers:

## Rollout
| Cohort/environment | Start gate | Signals | Pause/decision | Rollback trigger | Owner |

## Legacy contraction
| Temporary path | Removal evidence | Earliest removal | Owner | Verification |

## Residual risk and release handoff
- Evidence package:
- Unknowns:
- Risks requiring acceptance:
```
