# Time-Sensitive Package and Platform Claim Review

Use this protocol before accepting a dated ecosystem reference as current.

## Scope

Review each named framework, package, service, store rule, or target SDK in:

- `skills/production-web-builder/references/web-ecosystem-*.md`
- `skills/flutter-production-builder/references/flutter-ecosystem-*.md`
- `skills/expo-react-native-builder/references/expo-react-native-ecosystem-*.md`
- `skills/mobile-architecture-director/references/platform-decision-matrix-*.md`

## Per-row review

Record:

```text
Item:
Target repository resolved version/range:
Framework/runtime peer compatibility:
Latest stable and release date:
Maintenance/release activity:
Advisories and fixed versions:
Deprecation/ownership status:
License and source:
Runtime/bundle/native/build/CI/service cost:
Built-in or existing-repository alternative:
Choose conditions:
Avoid conditions:
Primary source URLs:
Checked date:
Reviewer:
Decision and confidence:
```

## Failure conditions

Reject or mark unknown when:

- only a blog/listicle/popularity metric supports the choice;
- the target lockfile or peer graph contradicts the reference;
- the license is missing or incompatible with the project;
- a known advisory lacks a fixed/mitigated path;
- a package is deprecated, archived, unmaintained, or has unclear ownership and no explicit risk acceptance;
- runtime/binary/bundle/build/service cost was ignored;
- a built-in capability is sufficient and the added dependency has no concrete benefit;
- the reference's review date or scheduled security follow-up has passed.

## Platform decision check

A Flutter/Expo/native/other recommendation passes only when must-have constraints, disqualifiers, weighted evidence, prototypes for uncertain native/performance/offline/security claims, delivery ownership, and reconsideration triggers are recorded. Framework familiarity or popularity alone fails.
