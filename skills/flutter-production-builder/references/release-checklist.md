# Flutter Release Checklist

## Candidate

- Flutter/Dart version, lockfile, generated outputs, commit/artifact, flavor/environment are fixed.
- Known baseline failures and package advisories are recorded.
- `dart format`/repository formatter, `flutter analyze`, tests, generation consistency, and build checks are recorded where applicable.

## Android

- application ID, versionCode/versionName, min/target/compile SDK and Gradle/AGP/Kotlin/JDK compatibility;
- signing/app bundle, Play tracks, symbols/mapping/native symbols;
- permissions, data safety/privacy, deep/app links, notifications, backup, network security;
- R8/resource shrinking and release-only plugin behavior;
- install/upgrade and representative physical devices/API levels.

## Apple

- bundle ID, marketing/build version, deployment target/Xcode/CocoaPods/SPM compatibility;
- signing, entitlements/capabilities, privacy usage descriptions/manifests, export compliance;
- universal links, notifications/background modes, keychain/backup behavior;
- archives, symbols, TestFlight/store metadata, install/upgrade on real devices.

## Cross-platform

- local-data migrations from every supported released schema;
- auth/account switching/logout/deletion and secure-storage failure;
- offline/retry/conflict, links/notifications, permissions, process death/background;
- semantics/screen readers, text scale/dynamic type, RTL, reduce motion;
- profile/release startup, frame, memory, battery/network on representative devices;
- crash/error/performance telemetry with release identity;
- phased rollout, feature flag/kill switch, support notes, rollback or forward-fix.

Use current official store/platform submission requirements at release time; this checklist is not a substitute for policy review.
