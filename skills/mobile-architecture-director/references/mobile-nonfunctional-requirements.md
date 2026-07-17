# Mobile Nonfunctional Requirements

## Product and UX

- first usable frame and cold/warm start expectations;
- 60/120 Hz interactions, large lists, media, camera, maps, charts, or graphics;
- platform-specific navigation, back behavior, keyboard, share, intents, links, widgets/extensions;
- screen readers, dynamic type/font scale, switch/keyboard, contrast, reduce motion, orientation;
- localization, RTL, long text, calendar/number/address formats;
- offline duration and degraded connectivity behavior.

## Data and reliability

- source of truth, local schema, cache, durable queue, attachments, encryption;
- conflict strategy, idempotency, retries, ordering, reconciliation, and clock assumptions;
- background scheduling limits, push/silent notification role, battery/data usage;
- data migrations across app versions and rollback/forward recovery;
- account switching, logout, device transfer, backup/restore, and deletion.

## Security and privacy

- authentication/reauth, authorization, token lifecycle, device binding/attestation;
- secret versus sensitive data storage, screenshots/app switcher, logs/crash reports;
- certificate/network policy, compromised/rooted device posture, biometrics and fallback;
- permissions, consent, data minimization/retention/export/deletion;
- supply chain, native plugins, signing keys, build provenance, and update trust.

## Operations

- supported OS/device matrix and deprecation cadence;
- CI/build minutes, macOS availability, signing/provisioning, store accounts;
- development builds/internal distribution/beta tracks;
- phased rollout, over-the-air scope, runtime compatibility, rollback;
- crash/ANR/hang/startup/performance/network telemetry and privacy;
- support diagnostics and release identity;
- store review, privacy labels/manifests, export compliance, policy ownership.
