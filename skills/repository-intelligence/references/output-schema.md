# Repository Intelligence Output Schema

```markdown
# Repository Intelligence: <decision>

## Scope and state
- Root:
- Branch/ref:
- Working-tree changes:
- Included:
- Excluded:
- Decision informed:

## Executive map
<5–12 decision-relevant findings>

## Components
| Component | Responsibility | Entry/public contracts | Dependencies | Deploy/failure boundary | Owner evidence | Confidence |

## Dependency and data edges
| From | To | Mechanism | Contract/artifact | Runtime/build/ops | Evidence | Confidence |

## Ownership
| Surface | Policy owner | Observed steward | Gap/conflict | Evidence |

## Change-impact rings
| Ring | Surface/consumer | Impact mechanism | Risk | Required verification | Evidence | Confidence |

## Hotspots
| Surface | Why risky | Consequence | Mitigation/inspection | Evidence |

## Edit-conflict surfaces
| Surface | Candidate changes | Collision mechanism | Single owner or order |

## Unknowns and contradictions
| Question | Why material | Current evidence | Resolution action |

## Handoff package
- Invariants:
- Single-owner surfaces:
- Sequence constraints:
- Focused verification targets:
```

Keep machine-generated inventory separate from the executive map. Exact paths are mandatory; diagrams are optional and must have a text equivalent.
