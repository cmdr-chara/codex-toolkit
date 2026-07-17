# Expo/React Native Release Checklist

## Candidate and dependency health

- Expo SDK/RN/React/Node/package manager/lockfile and native project state are fixed.
- `npx expo-doctor` or repository equivalent, type/lint/tests, config validation, and duplicate dependency checks are recorded where applicable.
- New Architecture and native-module compatibility are verified in development/release builds.
- Known Expo/RN/package regressions and advisories are reviewed.

## Builds and native configuration

- app identifiers, versions/build numbers/version codes, schemes/links, icons/splash, orientation/system UI;
- EAS profiles, environment variables/secrets references, credentials/signing, artifact provenance;
- permissions, usage descriptions, entitlements/capabilities, Android manifests/Gradle, iOS Xcode/Pods;
- config-plugin/prebuild native diff reviewed and reproducible;
- symbols/source maps uploaded and release/update identity connected to telemetry.

## Data, lifecycle, and devices

- install and upgrade from supported released binaries and local database versions;
- auth/account switch/logout/deletion, SecureStore invalidation/reauth;
- offline launch/read/write/sync/conflict, BackgroundTask deferral, push/links, permissions;
- foreground/background/inactive, process death, low memory, interruption, keyboard/safe area;
- screen readers, font scale, reduce motion, contrast, RTL/long text;
- startup, frames, memory, list/image/network/storage on representative low/high devices.

## Updates

- runtimeVersion compatibility and channel/branch/environment mapping;
- published update tested against each compatible binary on real devices;
- native changes excluded from OTA; update failure/offline/rollback/republish rehearsed;
- access, signing, promotion, staged rollout, metrics, and support owner defined.

## Stores

- signed `.aab`/`.ipa` or required artifact, store tracks/TestFlight, metadata/assets/privacy answers;
- Android target/min SDK and Play policy; iOS deployment/Xcode/privacy/export policy;
- notifications, links, subscriptions/purchases/identity review where applicable;
- staged/phased release, crash/ANR/performance/update monitoring, kill switch/rollback or forward-fix.

Review current Apple, Google, Expo, and EAS policy/tooling immediately before submission.
