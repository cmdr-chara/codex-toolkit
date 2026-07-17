# Compatibility Evidence Rubric

**Stable rubric; version claims belong in a dated migration record.**

## Source order

1. official framework/platform release notes, support policy, migration guide, and security advisory;
2. official package registry metadata and repository releases;
3. target repository manifests, lockfiles, and generated metadata;
4. maintained compatibility matrices or conformance tests;
5. community reports only as leads for reproduction, never as sole compatibility proof.

## Record for every changed dependency

| Field | Required evidence |
| --- | --- |
| Current and target | Exact package/runtime identifier and resolved version |
| Compatibility | Supported framework/runtime/platform ranges and peers |
| Maintenance | Latest stable release date and recent release/repository signal |
| Adoption fit | Existing repository use and ecosystem integration; not popularity alone |
| License | Registry/repository license and whether it changed |
| Security/deprecation | Official advisories, unsupported versions, replacement guidance |
| Runtime/bundle cost | Material binary, startup, memory, network, build, or bundle effect |
| Built-in alternative | Whether framework/platform capability is sufficient |
| Choose when | Repository-specific conditions that justify it |
| Avoid when | Conditions that make it unnecessary or risky |
| Sources | URLs plus `Information checked: YYYY-MM-DD` |

## Compatibility matrix

```markdown
| Surface | Current | Target | Compatible coexistence | Required change | Evidence | Confidence |
| Runtime/toolchain | | | | | | |
| Direct dependencies | | | | | | |
| Generated code | | | | | | |
| Data/schema | | | | | | |
| API/events | | | | | | |
| CI/deploy | | | | | | |
| Supported clients/platforms | | | | | | |
```

## Security handling

- Use the advisory's affected and fixed ranges, not a blog summary alone.
- Check transitive resolution in the actual lockfile.
- Record mitigations separately from fixes.
- Recheck immediately before release when the advisory or scheduled patch date is newer than the migration record.
