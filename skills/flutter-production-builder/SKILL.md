---
name: flutter-production-builder
description: Build or audit a production Flutter application across architecture, state, routing, networking, serialization, persistence, offline-first behavior, platform integration, adaptive UI, accessibility, testing, performance, security, observability, and release. Use when Flutter is selected or already established. Do not use to choose Flutter versus Expo/native or to mandate packages independent of repository requirements.
---

# Flutter Production Builder

Implement Flutter from the app's actual contracts and supported platforms. Prefer Flutter/Dart capabilities and existing repository patterns before adding packages.

## Trigger boundary

Use this skill for:

- implementing a Flutter feature, screen flow, data layer, platform integration, or application;
- auditing Flutter architecture and production readiness;
- choosing state, routing, network, serialization, storage, offline, and test approaches conditionally;
- preparing Android/iOS and other supported Flutter targets for release.

Do not trigger for:

- choosing Flutter versus Expo/native—use `mobile-architecture-director`;
- a pure Dart package with no application/platform concerns;
- visual direction alone;
- blindly replacing an established state/routing/data architecture.

## Required inputs

Capture:

1. repository state, Flutter/Dart constraints, flavors, package manager state, and supported platforms/OS minimums;
2. product/design flows, adaptive behavior, accessibility and localization requirements;
3. backend/auth/data contracts, offline/sync expectations, and sensitive-data classification;
4. device/plugin/native integration requirements;
5. performance/resource targets and representative devices;
6. CI, signing, store/distribution, observability, feature flag, and rollback/update policy.

Inventory first:

```sh
python skills/flutter-production-builder/scripts/flutter_project_inventory.py . --format markdown
```

## Safety baseline

- Inspect and preserve uncommitted work.
- Read `pubspec.yaml`, `pubspec.lock`, analysis options, generated-file conventions, platform projects, and existing architecture before edits.
- Use repository-pinned Flutter tooling where present. Do not upgrade SDK/packages under an implementation task without routing the transition to `codebase-evolution-controller`.
- Do not edit generated serialization/router/database/platform files directly; change authoritative input and regenerate with the repository's recorded command.
- Never place secrets in Dart source, app assets, logs, crash reports, or compile-time defines that ship to clients.
- Do not assume emulator/simulator behavior proves real-device lifecycle, biometrics, storage, performance, notification, or background behavior.

## Workflow

### 1. Establish architecture and platform state

Map:

- app entry points, flavors/environments, routing, dependency construction, state/data layers;
- feature/domain boundaries and public models;
- network/auth, storage/database, sync, background, notifications, links, and native plugins;
- generated code inputs/outputs;
- platform manifests/entitlements/permissions and minimum versions;
- tests, golden policy, integration/device harness, CI/build/release scripts;
- observability and release identity.

Use Flutter's recommended separation of UI and data responsibilities as a lens, not a mandate to rewrite a working architecture.

### 2. Define feature and state contracts

For each journey specify:

- route/deep-link/back and restoration behavior;
- loading, empty, partial, stale, offline, retry, validation, success, error, permission, and destructive states;
- state ownership and lifetime: widget-local, route/feature, app/session, durable/server-owned;
- async cancellation, race, retry, idempotency, and process death/restart;
- adaptive layout, keyboard, orientation, dynamic type/text scale, localization, and accessibility;
- analytics/trace/error signals and user recovery.

Do not choose a state package before identifying state ownership and event/data flow.

### 3. Select packages conditionally

Read [`references/flutter-ecosystem-2026-07-17.md`](references/flutter-ecosystem-2026-07-17.md). For each new dependency record:

- current SDK/platform compatibility and resolved version;
- maintenance/release evidence and ecosystem fit;
- license and security/deprecation status;
- binary/runtime/build/code-generation cost;
- built-in/existing alternative;
- choose/avoid conditions and native fallback;
- generator/update/removal ownership.

Use `dart pub outdated` or repository tooling only after inspecting constraints and when network/package resolution is authorized. Package presence is not evidence it should be expanded.

### 4. Structure features and dependencies

- Keep widgets focused on presentation/interaction; isolate data sources, repositories, and platform services behind testable interfaces where complexity warrants it.
- Add a domain/use-case layer only for rules reused across screens/data sources or requiring independent testing.
- Use constructor/provider-based dependency composition visible from app/feature roots; avoid hidden service-locator reach unless the established system governs it.
- Separate transport/storage DTOs from UI/domain models when versioning or persistence makes the boundary material.
- Model async state explicitly and prevent stale responses from overwriting newer intent.
- Keep feature boundaries aligned with navigation/data ownership, not arbitrary “screens/widgets/utils” dumping grounds.

### 5. Routing and navigation

- Use `Navigator`/`Router` capabilities or the existing router for simple flows.
- Consider `go_router` for declarative URL/deep-link, nested navigation, redirects, and restoration needs that it demonstrably simplifies.
- Define authenticated/unauthenticated routing without flicker or unauthorized route construction.
- Test deep links, browser URL for Flutter web if supported, back gestures/buttons, nested stacks/tabs, state restoration, unknown routes, and notification links.
- Keep redirect logic pure/bounded and prevent loops.

### 6. Networking, authentication, and serialization

- Prefer `package:http` or existing client for simple HTTP; consider Dio when interceptors, cancellation, upload/download progress, or transport customization justify it.
- Centralize base URL, timeouts, headers, safe diagnostics, error classification, retry and idempotency policy.
- Do not retry non-idempotent effects blindly.
- Refresh credentials with one coordinated flow; prevent request storms and account crossover.
- Validate untrusted responses and version contracts. Use manual parsing for small stable payloads; code generation when repeated typed boundaries reduce drift.
- Keep tokens/secrets out of ordinary preferences and logs; backend authorization remains authoritative.

### 7. Persistence and offline-first behavior

Follow [`references/offline-and-data.md`](references/offline-and-data.md). Decide separately:

- ephemeral cache;
- user settings;
- secrets/credentials;
- relational/queryable application data;
- durable outbox and sync metadata;
- downloaded files/media.

Define source of truth, schema/version migration, encryption needs, conflict policy, retry/reconciliation, account isolation, logout/deletion, backup behavior, and storage limits. “Offline-first” requires usable reads and durable writes without network plus deterministic convergence—not merely cached responses.

### 8. Platform integration

- Prefer maintained first-party/federated plugins that support all required targets and current embedding/toolchain.
- Review native permissions, privacy usage strings/manifests, entitlements/capabilities, background modes, ProGuard/R8, Gradle/Xcode settings, and app lifecycle.
- Wrap plugins behind an application interface when failure modes, permissions, or platform differences are material.
- Test denied/restricted/permanently denied permission, unavailable hardware, interruption, background/foreground, process death, and device rotation.
- For unsupported native APIs, define platform channels/plugin ownership, thread/cancellation/error contracts, and native tests.

### 9. Adaptive, accessible, and localized UI

- Use layout constraints and available space rather than device-name breakpoints alone.
- Preserve platform navigation, text input, selection, back, menus, dialogs, safe areas, and system UI conventions where users rely on them.
- Verify semantics labels/roles/actions, traversal/focus order, screen-reader announcements, contrast, touch targets, text scaling, high contrast, reduce motion, and keyboard/switch access.
- Test long/RTL text, locale formats, font fallback, orientation, fold/large screen where supported, and virtual keyboard insets.
- Prefer semantic/native widgets; custom render/gesture controls require equivalent semantics and focus.

### 10. Testing

Use a risk-based pyramid:

- Dart unit tests for rules, state transitions, parsing, repositories, sync/conflict;
- widget tests for semantics, layout states, navigation interactions, and controlled platform/data boundaries;
- golden tests only for stable visual contracts with reviewed fonts/rendering and intentional update policy;
- integration tests for real app flows and Flutter/native/plugin boundaries;
- real-device tests for biometrics, notifications, storage, background, links, camera/media, performance, and platform accessibility.

Use fakes at owned interfaces; cover actual database/network/plugin integration elsewhere. Test migrations from released schema versions.

### 11. Performance and observability

- Profile release/profile mode on representative devices; debug timing is not release evidence.
- Inspect startup, frame build/raster time, shader/image work, memory, allocation, GC, list laziness, rebuild scope, network/storage, and background battery/data.
- Reduce work through architecture and lifecycle before adding memoization/cache complexity.
- Add structured error/crash, trace, and performance signals with release/environment identity and no sensitive payloads.
- Handle Flutter framework errors, async zone/isolate errors, native crashes, and expected domain errors distinctly.

### 12. Build and release

Use [`references/release-checklist.md`](references/release-checklist.md). At minimum:

1. run repository-approved format/analyze/tests and generation checks;
2. build each intended flavor/platform in release mode;
3. test install/upgrade from a released version and local-data migration;
4. validate signing, identifiers, versions, permissions/privacy, store assets/metadata, and symbol files;
5. run critical real-device journeys, accessibility, performance, offline, links/notifications, and failure recovery;
6. verify feature flags, observability, staged rollout, support, and rollback/forward-fix plan.

Return exact files, package decisions, generation, commands/results, device/build evidence, known gaps, and release handoff.

## Interaction boundaries

- `mobile-architecture-director` owns the platform choice.
- `product-design-director` and `screenshot-to-interface` own direction/reference evidence.
- `codebase-evolution-controller` owns Flutter/Dart/package/toolchain migrations.
- This skill owns feature-level Flutter verification; `verification-and-release` owns final gate.
- `documentation-synchronizer` owns user/developer/configuration/migration/release documentation.

## Failure handling

- If a package has stale or conflicting compatibility, do not force it; test built-in/existing alternatives or prototype the native boundary.
- If generated output drifts, inspect generator versions/inputs and stop before manual edits.
- If plugin behavior differs by platform, expose the difference in product state or platform adapter rather than pretending parity.
- If offline conflicts lack a product rule, block durable mutation design and request a conflict policy.
- If a release build fails but debug works, investigate tree shaking, permissions, minification, native configuration, and environment separately; do not disable release optimizations blindly.

## Stop conditions

Stop when required flows work across supported states/platforms, package/native choices are evidenced, data and migrations are safe, accessibility/performance/security/observability are checked on representative builds/devices, and remaining release risks are explicit. Hand final release judgment to `verification-and-release`.
