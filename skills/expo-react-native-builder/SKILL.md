---
name: expo-react-native-builder
description: Build or audit a production Expo and React Native application across Expo Router, development builds, native modules, state/data, persistence, offline behavior, animation/gestures, accessibility, testing, performance, security, observability, EAS builds/updates, and store release. Use when Expo/React Native is selected or already established. Do not use to choose the mobile platform or to assume Expo Go and a package list are production architecture.
---

# Expo React Native Builder

Build against the selected Expo SDK and React Native architecture, real devices, native constraints, and store/update policy. Prefer Expo/RN capabilities and existing repository choices before dependencies.

## Trigger boundary

Use this skill for:

- implementing an Expo/React Native app or feature;
- auditing routing, native modules, data/offline, performance, accessibility, EAS, and release readiness;
- choosing state/data/storage/animation/test packages conditionally within an established Expo/RN app;
- upgrading implementation patterns within the current supported SDK without changing the platform decision.

Do not trigger for:

- deciding Expo/RN versus Flutter/native—use `mobile-architecture-director`;
- a web-only React task;
- a bare React Native migration or SDK upgrade whose central problem is version compatibility—use `codebase-evolution-controller` with this skill as implementation guidance;
- treating Expo Go as the production development/runtime environment.

## Required inputs

Capture:

1. repository state, Expo SDK/RN/React/Node/package-manager versions and monorepo shape;
2. app config, routes, development build, native directories/prebuild policy, EAS build/update/submit profiles;
3. product/design flows, platform conventions, accessibility/localization requirements;
4. backend/auth/data/offline/sync and sensitive-data contracts;
5. native modules/device APIs, permissions, extensions/widgets/background needs;
6. supported OS/devices, performance/resource targets, and real-device matrix;
7. testing, CI, observability, signing/store, update runtime, rollout, and rollback policy.

Inventory first:

```sh
python skills/expo-react-native-builder/scripts/expo_project_inventory.py . --format markdown
```

## Safety baseline

- Inspect and preserve uncommitted work.
- Read `package.json`, lockfile, app config, `eas.json`, native projects, config plugins, and existing architecture before edits.
- Use `npx expo install` or repository tooling for SDK-compatible Expo package resolution when authorized; do not force arbitrary versions.
- Do not run prebuild, install pods, regenerate native projects, or upgrade SDK/RN without reviewing expected native diffs and rollback.
- Never ship secrets in `EXPO_PUBLIC_*`, app config, JS bundle, AsyncStorage, logs, updates, or source maps.
- Test native modules, storage, biometrics, notifications, background, links, memory, and performance in development/release builds on real devices.

## Workflow

### 1. Establish runtime and native ownership

Map:

- Expo SDK, RN, React, Node, package manager, lockfile, New Architecture, and duplicate dependency risks;
- Expo Router/routes/layouts/deep links and navigation state;
- app config, config plugins, prebuild/native directories, custom native modules;
- development builds and environments;
- EAS Build, Update runtime/version/channel/branch policy, Submit, credentials/signing;
- state/data/storage/offline/background/push/links;
- tests, CI/workflows, observability, release identity.

For SDK 55+, New Architecture cannot be disabled. Verify every native dependency against the selected SDK/RN and architecture.

### 2. Define feature, navigation, and lifecycle contracts

For each flow specify:

- route, modal/tab/stack, deep/universal/app link, notification entry, back and restoration behavior;
- loading, empty, stale, offline, retry, validation, success, error, unauthorized, permission, and destructive states;
- state ownership: component, URL/route, feature/session client state, server cache, durable local source;
- app foreground/background/inactive, screen focus/blur, process death, update/reload, and account switching;
- keyboard/safe area/orientation/font scale/localization and accessibility;
- analytics/trace/error signals and recovery.

Do not tie long-lived subscriptions or requests solely to component mount when screen focus/app lifecycle owns them.

### 3. Use development builds for production work

Expo Go is useful for constrained exploration but is not the production development environment for store apps. Create and use development builds when the app needs:

- custom native modules/config plugins;
- production-like app identifiers, permissions, links, notifications, credentials, or runtime;
- accurate New Architecture/native dependency behavior;
- release-like performance and update testing.

Keep build profiles/environment inputs explicit. Test both clean install and upgrade paths.

### 4. Select packages conditionally

Read [`references/expo-react-native-ecosystem-2026-07-17.md`](references/expo-react-native-ecosystem-2026-07-17.md). For every new package record:

- SDK/RN/New Architecture/platform compatibility and resolved version;
- maintenance/release evidence and adoption fit;
- license, security/deprecation, native code and service terms;
- JS/native/binary/startup/memory/build/runtime cost;
- Expo/RN/native/existing alternative;
- choose/avoid conditions, config plugin/prebuild and rollback impact.

Avoid multiple routers, server-state caches, global-state stores, animation engines, or storage layers without a migration boundary.

### 5. Routing and navigation

- Prefer Expo Router in Expo apps when file-based routes, deep links, layouts, typed routes, and web integration fit.
- Use React Navigation directly when an existing non-Router architecture or specialized integration requires it; do not layer duplicate navigation ownership.
- Guard protected screens at a trusted data/session boundary and prevent unauthorized content flashes.
- Test deep/universal/app links, notifications, nested tabs/stacks/modals, hardware/system back, gestures, web URLs if supported, unknown routes, and state restoration.
- Keep route params serializable and version-compatible across persisted state/updates.

### 6. State, server data, and forms

- Keep local UI state local; use URL/route state for shareable navigation state.
- Use server-state tooling only for cache/freshness/retry/invalidation/optimistic/offline needs the framework/app does not already own.
- Use one client-state strategy for genuinely cross-tree independent state; do not mirror server cache into it.
- Define query keys, auth/account isolation, cancellation, stale response control, and mutation reconciliation.
- Prefer native form semantics/components and focused state; add form/schema packages only for demonstrable complexity.
- Validate and authorize on the server. Client validation improves UX, not trust.

### 7. Persistence, offline, and background work

Follow [`references/offline-updates-and-security.md`](references/offline-updates-and-security.md):

- AsyncStorage: small non-sensitive key/value state with version/migration;
- SecureStore: small secrets, with biometric invalidation/reauth and real-device tests;
- expo-sqlite: structured/queryable durable data and migrations;
- filesystem: large files with explicit metadata/lifecycle;
- durable outbox/sync: operation identity, idempotency, ordering, conflicts, reconciliation, account isolation.

BackgroundTask is deferrable and OS-scheduled; it is not an exact timer or guaranteed immediate sync. Design foreground recovery and server-side completion/notifications as needed.

### 8. Native modules and device APIs

- Prefer Expo SDK modules that match the selected SDK.
- For third-party native libraries, check React Native Directory/current docs, New Architecture, config plugin, platform versions, maintenance, license, and release-build proof.
- Use Expo Modules API/inline modules for owned native functionality when appropriate; define JS/native types, threading, cancellation, lifecycle, errors, and tests.
- Review permissions, usage strings, entitlements/capabilities, manifests, Gradle/Xcode/CocoaPods, ProGuard/R8, and store privacy.
- Test unavailable hardware, denied/restricted permissions, interruptions, background/foreground, process death, and platform-specific behavior.

### 9. Animation and gestures

- Use RN built-ins/CSS-like transitions where sufficient.
- Use Gesture Handler/Reanimated for complex gestures, shared values, layout/interruptible native-thread motion that justify native dependencies.
- SDK 57's official changelog documents a known Reanimated/Hermes memory regression; read the dated reference, measure the app, and use the documented mitigation where applicable.
- Keep gesture competition, scroll/nested handlers, cancellation, reduced motion, screen-reader interaction, and low-end device memory/frame behavior explicit.
- Do not add a motion engine for decorative mount fades alone.

### 10. Accessibility, adaptive UI, and localization

- Use RN accessibility roles/states/labels/hints/actions and native controls appropriately.
- Verify screen-reader order/focus, live announcements, modal focus, touch targets, contrast, font scaling, reduce motion, keyboard/switch, and disabled/error state.
- Test safe areas, edge-to-edge, system bars, keyboard avoidance, orientation, tablets/foldables where supported, RTL, long strings, and locale formats.
- Preserve iOS and Android navigation/input conventions instead of forcing identical behavior where it harms usability.

### 11. Testing

Use:

- unit tests for domain/state/parsing/sync;
- React Native Testing Library for user-observable component behavior and accessibility;
- integration tests around storage/network/native adapters;
- Jest with `jest-expo` aligned to the SDK where the repository uses Jest;
- E2E on development/release builds and real/emulated devices for critical flows; Expo documents Maestro integration with EAS Workflows;
- targeted manual/physical-device checks for biometrics, notifications, links, background, permissions, updates, performance, and accessibility.

Do not mock every native/network boundary; cover the real integration somewhere. Treat snapshot-only coverage as insufficient for behavior.

### 12. Performance and observability

- Profile release/development builds with RN DevTools/platform tools and representative devices.
- Inspect startup, JS/UI thread work, frames, memory, list virtualization, image decode, bridge/native module behavior, serialization, network/storage, and bundle/dependency duplication.
- Use lazy routes/components/assets only when it improves measured behavior without breaking navigation/focus.
- Add crash/error/performance/network traces with release/update/runtime/channel identity and privacy/cardinality controls.
- Distinguish JS errors, native crashes/ANRs, handled domain failures, and update failures.

### 13. EAS Build, Update, and store release

Use [`references/release-checklist.md`](references/release-checklist.md).

- Build signed binaries with explicit profiles and environment inputs.
- EAS Update can deliver compatible non-native JS/assets only; native dependency/config/permission changes require a new binary.
- Define `runtimeVersion`, channels/branches, rollout, compatibility, update checks, failure/reload behavior, and rollback/republish procedure.
- Test a published update against every compatible binary/runtime; do not rely only on development mode.
- Validate Android/iOS store identifiers, versions, signing, permissions/privacy, app links, notifications, symbols/source maps, metadata/assets, and policy.
- Use staged tracks/phased release, monitoring, kill/rollback controls, and support ownership.

Return exact files, dependency/native/config decisions, commands/results, build/device/update/store evidence, known gaps, and release handoff.

## Interaction boundaries

- `mobile-architecture-director` owns platform selection.
- `product-design-director`/`screenshot-to-interface` own design/reference evidence.
- `codebase-evolution-controller` owns SDK/RN/package/native migration plans.
- This skill owns feature-level Expo/RN verification; `verification-and-release` owns final gate.
- `documentation-synchronizer` owns setup, configuration, migration, update, store, and user documentation.

## Failure handling

- If a native library is incompatible with the selected SDK/New Architecture, choose a supported alternative, own a native module, or route a platform/migration decision; do not disable the architecture on SDK 55+.
- If prebuild changes are unexpected, stop and inspect config-plugin/input versions before manual native edits.
- If an update causes failure, use the defined runtime/channel rollback or republish path and preserve candidate/update evidence.
- If memory/performance changes after adding Reanimated or another native dependency, measure import/use paths and official known issues before blaming UI code.
- If Expo Go succeeds but development/release build fails, treat the latter as authoritative.

## Stop conditions

Stop when required flows work across supported lifecycle/platform states, SDK/native/package/update choices are evidenced, data/security/accessibility/performance/observability are verified on production-like builds/devices, and store/update risks are explicit. Hand final release judgment to `verification-and-release`.
