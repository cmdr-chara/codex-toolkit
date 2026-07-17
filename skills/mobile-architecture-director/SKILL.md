---
name: mobile-architecture-director
description: Select and shape an evidence-based mobile approach among Flutter, Expo/React Native, native iOS/Android, Kotlin Multiplatform, web-container, and other viable options using product, team, device, security, offline, performance, accessibility, and distribution constraints. Use when platform choice or mobile architecture direction is unresolved. Do not use to implement an already selected Flutter or Expo application.
---

# Mobile Architecture Director

Choose the platform that best satisfies the product's hard constraints and organizational ability to operate it. Do not convert team preference into architecture evidence.

## Trigger boundary

Use this skill for:

- deciding Flutter versus Expo/React Native versus native or another approach;
- reviewing whether an existing mobile platform choice still fits new constraints;
- defining shared/native boundaries, delivery model, offline/data architecture, and prototype risks before implementation;
- producing a mobile architecture decision record with disqualifiers and validation.

Do not trigger for:

- implementing Flutter—use `flutter-production-builder` after selection;
- implementing Expo/React Native—use `expo-react-native-builder` after selection;
- general web responsive work;
- a choice already constrained by an approved platform decision unless new evidence invalidates it.

## Required inputs

Capture:

1. target users, countries, devices, OS/platform minimums, and accessibility obligations;
2. core flows, UI/brand demands, release cadence, and expected product lifetime;
3. device APIs, background execution, widgets/extensions, media, graphics, maps, payments, identity, notifications, and deep links;
4. offline duration, sync/conflict, local data sensitivity, and backend contracts;
5. latency, startup, animation, memory, battery, binary/download, and reliability needs;
6. app-store, enterprise, web/desktop, over-the-air update, and compliance constraints;
7. team skills, hiring, ownership, CI/build infrastructure, native support, and migration budget;
8. existing code/assets and the amount that is genuinely reusable.

Replace “cross-platform” with the exact surfaces that must share behavior, UI, domain logic, or release timing.

## Safety baseline

- Inspect and preserve the repository, prototypes, approved product decisions, and uncommitted user work; do not replace an existing app merely to simplify the comparison.
- Do not select from popularity, one benchmark, or a preferred language alone.
- Verify current platform/framework support from primary sources and date the record.
- Treat third-party plugin/native-module compatibility as a prototype question, not a promise.
- Do not assume over-the-air updates can change native code or bypass store policy.
- Do not reduce security to “use secure storage”; model trust, data, device compromise, transport, auth, and backend authorization.
- Never claim feature parity without platform-specific acceptance criteria.

## Workflow

### 1. Define hard gates

List must-have, non-negotiable requirements that can disqualify an option:

- required OS/device/API unavailable or immature;
- platform-specific extension/widget/service or background mode central to the product;
- hard performance/graphics/media/latency constraint;
- regulated security, cryptography, identity, or attestation requirement;
- app-store/enterprise/distribution/update restriction;
- accessibility or platform-convention requirement;
- unsupported minimum OS or hardware;
- team cannot own required native code and no credible partner exists.

Test each gate with current official evidence. Do not score a disqualified option into first place.

### 2. Model the product architecture

Map:

- navigation and screen/state graph;
- data sources, local database, cache, sync, conflicts, and background work;
- authentication/session, secrets, privacy, permissions, and device trust;
- device/native integrations and platform-specific UX;
- observability, support, feature flags, updates, and rollback;
- build/signing/distribution environments;
- shared versus platform-specific code candidates.

Use [`references/mobile-nonfunctional-requirements.md`](references/mobile-nonfunctional-requirements.md) to expose hidden requirements.

### 3. Compare viable options

Use the dated [`references/platform-decision-matrix-2026-07-17.md`](references/platform-decision-matrix-2026-07-17.md). Evaluate at least:

- Flutter;
- Expo/React Native;
- separate native Swift/SwiftUI and Kotlin/Jetpack Compose;
- Kotlin Multiplatform with native UI when shared domain/data is valuable;
- Capacitor/PWA/web container only when web reuse and native constraints fit;
- another approach only with equivalent evidence.

For each option record:

- hard-gate result;
- product and UX fit;
- native integration maturity and fallback;
- offline/data/security design;
- performance and accessibility risk;
- release/build/update/store operations;
- team fit and total ownership cost;
- migration/reversibility and lock-in;
- unknowns requiring a spike.

### 4. Weight criteria explicitly

Weights must come from product and organizational consequence. Use a 1–5 scale only to make assumptions visible; do not pretend the total is objective.

```text
criterion | weight | option evidence | score | confidence | disqualifier/unknown
```

Run sensitivity: if a small weight change reverses the decision, the choice is not robust and needs a prototype or stakeholder decision.

### 5. Design proof spikes

Prototype the smallest high-risk unknown, such as:

- required camera/BLE/NFC/background/extension integration on real devices;
- 60/120 Hz interaction or complex list/media workload;
- cold start, memory, binary, battery, and network behavior;
- secure auth/biometric/keychain/keystore flow and account recovery;
- offline edits, conflicts, background sync, and data migration;
- accessibility with screen reader, dynamic type/font scale, keyboard/switch, and platform navigation;
- build/signing/store/update pipeline;
- monorepo/native-module compatibility.

Define acceptance thresholds, device/OS matrix, and evidence before building the spike. Throwaway prototypes must not become production architecture by inertia.

### 6. Choose shared and native boundaries

Decide what should be shared:

- domain rules and API models;
- persistence/sync;
- UI components and design tokens;
- navigation/state;
- analytics/observability;
- tests and release tooling.

Maximize shared value, not shared line count. Keep platform-specific behavior where native convention, API, accessibility, performance, or release ownership requires it.

### 7. Define the operating model

Specify:

- repository/monorepo shape and ownership;
- version and dependency update policy;
- native-module/plugin review and fallback;
- CI, signing, secrets, build profiles, environments, and artifact retention;
- beta/store tracks, phased rollout, updates, crash/metric monitoring, and rollback;
- OS/framework support cadence and deprecation policy;
- accessibility, performance, security, and privacy gates;
- incident and store-review ownership.

A platform choice without an operating model transfers risk to delivery.

### 8. Produce the decision record

Return:

```markdown
Decision: <platform/architecture>
Status: PROPOSED | VALIDATED | BLOCKED
Information checked: YYYY-MM-DD
Hard gates:
Options considered:
Weighted comparison and confidence:
Prototype evidence:
Shared/native boundaries:
Data/offline/security architecture:
Build/update/distribution model:
Key risks and mitigations:
Why rejected options lost:
Reconsideration/revisit triggers:
Implementation handoff:
```

Choose `BLOCKED` when a hard-gate unknown lacks evidence. Do not hide uncertainty inside a numeric score.

## Handoffs

- To `flutter-production-builder`: Flutter version/support evidence, platform scope, architecture boundaries, NFRs, native integration prototypes, and release model.
- To `expo-react-native-builder`: Expo/RN/SDK evidence, native modules, New Architecture compatibility, update/runtime policy, NFRs, and store model.
- To native/KMP/web teams: equivalent architecture decision and prototype evidence.
- To `product-design-director`: unresolved product/platform UX tradeoffs.
- To `verification-and-release`: platform-level acceptance, build/store, rollout, and rollback evidence after implementation.

## Failure handling

- If no option passes a hard gate, redesign the product constraint, split platforms, or budget native work; do not pick the least-bad unsupported option silently.
- If plugin/module claims conflict, reproduce on the target framework and device versions.
- If team-cost data is unknown, state staffing/ownership assumptions and compare scenarios.
- If web/desktop scope dominates, evaluate those targets separately rather than forcing one mobile framework to optimize every platform.
- If the decision is politically fixed, record it as a constraint and still expose technical risks and mitigations.

## Stop conditions

Stop when hard gates are tested, the choice is robust to reasonable weighting, critical unknowns have prototype evidence or block status, operating ownership is defined, and an implementation-ready handoff exists. Do not proceed into platform code under this skill.
