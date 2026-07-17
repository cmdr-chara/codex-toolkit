# Work Graph Schema

The ownership checker consumes JSON in this shape:

```json
{
  "version": 1,
  "objective": "Introduce session rotation without breaking existing clients",
  "repository_state": "branch and worktree summary",
  "single_owner_surfaces": [
    "package-lock.json",
    "db/migrations/**",
    "src/api/schema/**"
  ],
  "missions": [
    {
      "id": "M1",
      "objective": "Define backward-compatible token contract",
      "kind": "writer",
      "dependencies": [],
      "read_scope": ["src/auth/**", "src/api/**", "tests/auth/**"],
      "write_scope": ["src/auth/contracts.ts", "tests/auth/contracts.test.ts"],
      "produces": ["versioned token contract and focused tests"],
      "invariants": ["existing token remains readable during rollout"],
      "forbidden": ["package-lock.json", "db/migrations/**"],
      "acceptance_evidence": ["old and new token fixtures pass"],
      "integration_checks": ["auth consumer suite"],
      "stop_when": ["contract requires a schema decision not supplied"]
    }
  ],
  "integration_order": ["M1", "M2", "M3"],
  "final_checks": ["focused integration suite", "working-tree ownership audit"]
}
```

## Rules

- Mission IDs are unique and dependencies reference existing IDs.
- The dependency graph is acyclic unless a documented manual loop is intentionally serialized outside concurrent execution.
- Writer `write_scope` entries are repository-relative paths or glob patterns.
- Two writers may not have overlapping write scopes.
- A path listed in `single_owner_surfaces` may match at most one writer.
- Read overlap is allowed. Write/read overlap is expected but must respect dependency order when the reader consumes an in-flight output.
- Generated inputs and outputs are assigned together unless the generator contract makes separation safe and a single regeneration owner is named.
- Integration order includes every writer or explains why a node has no integration artifact.

## Status ledger

```text
ID | state | owner | dependencies | owned writes | evidence | integration result
```

Allowed states: `PLANNED`, `READY`, `RUNNING`, `PASS`, `PARTIAL`, `BLOCKED`, `ACCEPTED`, `REWORK`, `REJECTED`, `CANCELLED`.
