# Mobile Platform Decision Matrix — 2026-07-17

**Information checked:** 2026-07-17  
**Next review:** 2026-10-15 or earlier after a platform/framework/store change.  
**Purpose:** Current evidence prompts for architecture selection; not a universal ranking.

## Current framework observations

- Flutter stable documentation and release notes identify Flutter 3.44 as current.
- Expo SDK 57 was released on 2026-06-30 and maps to React Native 0.86, React 19.2.3, and minimum Node.js 22.13.x in Expo's SDK table.
- React Native 0.86 is active; 0.85 is also active; 0.84 is end-of-cycle; 0.87 is scheduled as a future release for 2026-08-10.
- Expo SDK 55+ always uses React Native's New Architecture; it cannot be disabled.

Recheck exact patch versions, OS/toolchain minimums, and store requirements during implementation.

## Option comparison

| Option | Strong fit | Material risks/costs | Prototype before choosing when |
| --- | --- | --- | --- |
| Flutter | One team needs highly consistent/custom UI across iOS/Android; Dart ownership is acceptable; shared widget/rendering system has high value; additional desktop/web targets may share product UI | platform conventions need deliberate adaptation; plugin/native integration and binary/startup/memory must be measured; native teams still needed for complex APIs/release issues | critical native SDK/plugin, extension/widget, advanced media/graphics, background, accessibility, startup/binary, or platform-specific UX is central |
| Expo/React Native | React/TypeScript team; iOS/Android with native components/APIs; Expo build/update/module ecosystem reduces native operations; product benefits from web/domain reuse | native-module/New Architecture compatibility; JS/native performance and lifecycle; dependency duplication; update runtime policy; native code still required for unsupported integrations | custom native module, high-rate animation/media, background work, monorepo dependency shape, memory/startup, or store/update constraints are critical |
| Separate native iOS + Android | Maximal platform API access, conventions, performance control, extensions/widgets/background, and independent platform delivery | two UI implementations, duplicated testing/product work, staffing and release coordination; shared behavior can drift | business assumes native is prohibitively slow or cross-platform is automatically cheaper—prototype comparable slices and operating cost |
| Kotlin Multiplatform + native UI | Kotlin expertise; shared domain/data/network logic is valuable while preserving SwiftUI/Compose UX and native APIs | shared boundary design, interop, two UIs, iOS tooling/ownership; not a one-codebase UI solution by default | complex concurrency, persistence, networking, Swift interop, binary size/build, or shared-domain test workflow is central |
| Capacitor/web container or PWA | Existing web product dominates; content/forms/enterprise workflows; native API set is modest; one web delivery path has high value | platform feel, offline/background, performance, keyboard/webview quirks, app-store policy, native plugins and accessibility need proof | camera/media/maps/files/background/push, offline durability, high-motion UI, or store expectations are important |

## Weighted criteria template

| Criterion | Weight | Flutter | Expo/RN | Native | KMP + native UI | Web container/PWA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hard native/API fit | | | | | | |
| UX/platform convention | | | | | | |
| Performance/resource | | | | | | |
| Offline/data | | | | | | |
| Accessibility | | | | | | |
| Security/compliance | | | | | | |
| Team/ownership | | | | | | |
| Build/store/update operations | | | | | | |
| Shared-code value | | | | | | |
| Migration/reversibility | | | | | | |

Every score needs evidence and confidence. Apply disqualifiers before totals and perform sensitivity analysis.

## Source URLs

- https://docs.flutter.dev/release/release-notes/release-notes-3.44.0
- https://docs.flutter.dev/app-architecture
- https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility
- https://docs.flutter.dev/perf
- https://expo.dev/changelog/sdk-57
- https://docs.expo.dev/versions/latest/
- https://docs.expo.dev/guides/new-architecture/
- https://reactnative.dev/docs/releases
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.android.com/design/ui/mobile
- https://kotlinlang.org/docs/multiplatform.html
- https://capacitorjs.com/docs
- https://web.dev/learn/pwa/
