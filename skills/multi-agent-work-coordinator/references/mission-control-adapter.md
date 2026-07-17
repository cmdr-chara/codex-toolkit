# Optional Mission Control Adapter

The target toolkit already provides `delegate-with-mission-cards`, which selects specialized reader/writer roles and supplies mission-card formats. Keep responsibilities separate.

## Translation

1. Build and validate the work graph with `multi-agent-work-coordinator`.
2. Select only `READY` nodes.
3. Pass each node's objective, scopes, evidence, invariants, and stop conditions into the existing reader or writer mission-card shape.
4. Let Mission Control choose the lightest capable installed role.
5. Return results to the coordinator for ownership audit, acceptance classification, dependency release, and integration.

## Coordinator-owned fields

- decomposition and node IDs;
- dependencies and waves;
- exclusive write ownership;
- semantic overlap controls;
- integration order;
- acceptance and graph closure.

## Mission-Control-owned fields

- installed role selection and model routing;
- role-specific dispatch wording;
- per-agent execution within the approved node.

## Prohibitions

- Do not copy or hard-code model names from the optional bundle into this portable skill.
- Do not let a role expand its write scope.
- Do not create a second ledger with conflicting mission states.
- Do not treat agent self-reported success as coordinator acceptance.
