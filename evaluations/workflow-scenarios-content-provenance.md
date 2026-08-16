# Supplemental End-to-End Workflow Scenario

**Information checked:** 2026-08-16

## 17. `content-provenance-hygiene` — Inspect and sanitize a user-owned PDF

**Situation:** A user owns a PDF exported from a design tool and wants to understand which provenance/document metadata is present, remove only the requested metadata classes, keep visible content intact, and retain the original. The optional local sanitation service is configured, but its PDF capabilities must be checked at runtime.

**Inputs:** exact PDF artifact; ownership/authorization context; inspect-versus-clean intent; preservation invariants; requested metadata scope; configured service URL/auth environment; `/health`, `/capabilities`, and `/openapi.json` evidence when relevant.

**Expected workflow:**

1. Freeze the target, output strategy, working-tree/user-file state, requested metadata scope, and visible-content invariants.
2. Resolve the explicitly configured service and check `/health`; do not install or start third-party infrastructure silently.
3. Query `/capabilities` before promising PDF-specific inspection or rebuild behavior.
4. Call `/inspect` first and classify findings as confirmed, probable, informational, or not detected rather than inferring provenance from file origin.
5. Build the smallest deterministic remediation plan for the confirmed requested findings and state any collateral metadata/container consequences.
6. Stop at `AWAITING_APPROVAL` if the discovered operation exceeds the user's original deterministic scope, such as broad metadata stripping or a materially lossy rebuild.
7. For an already-approved bounded cleanup, call `/clean` with only the required options and write a separate output by default.
8. Re-inspect the output; compare target findings, file integrity, visible-content invariants, and unexpected metadata loss.
9. Report `INSPECTED`, `AWAITING_APPROVAL`, `SANITIZED`, or `BLOCKED` without claiming that the result proves human authorship or erases the artifact's real history.

**Expected artifacts:** target/authorization record; service capability evidence; pre-clean provenance-hygiene findings; bounded remediation plan; cleaned artifact when authorized; post-clean inspection; before/after side-effect record; residual unknowns and final state.

**Verification:** the original remains available; inspection precedes mutation; optional capabilities are runtime-verified; the cleaned artifact still parses/opens; the approved target finding is absent or reduced on re-inspection; visible content is preserved for metadata-only operations; no detector-evasion or authorship claim is introduced.

**Stop/escalate:** stop when the service is unavailable, the required format capability is absent, evidence is ambiguous, authorization is unclear, the requested operation becomes authorship/detector evasion, or sanitation would widen into substantive text/image editing. Hand unknown service corruption to `debugging-investigator` and integrated release judgment to `verification-and-release`.
