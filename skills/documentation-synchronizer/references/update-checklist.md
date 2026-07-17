# Documentation Update Checklist

## Factual

- Names, paths, flags, fields, defaults, limits, versions, and platforms match authoritative artifacts.
- Removed/deprecated behavior is clearly scoped and searchable old terminology is addressed.
- Examples include prerequisites, expected result, and material failure/rollback behavior.
- Security, privacy, permission, and data-retention statements are verified.

## Structural

- User, developer, API, architecture, configuration, migration, operations, and release surfaces were considered.
- Generated source is edited instead of generated output, or the repository explicitly permits direct edits.
- Cross-links lead to one authoritative explanation rather than divergent copies.
- Versioned docs do not accidentally update unsupported branches.

## Executable/visual

- Documentation build/parsing succeeds.
- Internal links and anchors resolve; external links are checked when tooling/network permits.
- Snippets compile, type-check, run, or are compared with source-generated output.
- Screenshots are current, legible, free of sensitive data, and have useful alt text.
- Diagrams have a text explanation and match component/deployment boundaries.

## Release

- Migration and rollback order is unambiguous.
- Changelog/release notes reflect user-visible behavior under repository policy.
- External docs, localization, support, and operator handoffs have owners.
- Validation gaps are stated rather than hidden.
