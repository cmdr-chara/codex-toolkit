# Expo Offline, Updates, and Security

## Data classes

| Data | Default candidate | Constraints |
| --- | --- | --- |
| Ephemeral server cache | memory/server-state cache | staleness, account/query isolation, eviction |
| Small non-sensitive preferences | AsyncStorage | version/migration, no secrets, bounded size/serialization |
| Credentials/key material | `expo-secure-store` | small values, platform keychain/keystore, biometric/key invalidation, device tests, reauth fallback |
| Relational/offline records | `expo-sqlite` | schema migrations, transactions/indexes, account isolation, backup/encryption decision |
| Files/attachments | Expo FileSystem or platform file API | quota, integrity, upload state, encryption/backup/deletion |
| Durable mutations | database outbox | stable operation ID, idempotency, order/dependency, retry, conflict/reconciliation |

## Offline/sync contract

```text
Local source of truth:
Schema/version migration:
Operation identity and idempotency:
Server version/revision:
Conflict detection/resolution UX:
Retryable/terminal errors:
Attachment lifecycle:
Foreground/background triggers:
Account switch/logout/deletion:
Metrics/support diagnostics:
```

Expo's local-first guide is explicitly evolving; do not adopt a sync product as a default without repository-specific evaluation.

## EAS Update contract

- Native binary identity and `runtimeVersion` define compatibility.
- Update only JS and assets compatible with the installed native runtime.
- New native module, config plugin output, permission, entitlement, manifest, or native dependency requires a new binary.
- Define channel/branch/environment mapping and who can publish/promote/rollback.
- Sign and protect update credentials according to organizational policy.
- Test update download, apply/reload, failure recovery, rollback/republish, and offline launch.
- Include binary version, runtime, update ID, channel, and release in observability.
- Respect App Store/Play policies; an update mechanism is not permission to change forbidden native/product behavior.

## Security boundary

- Mobile clients are untrusted; backend authenticates and authorizes every protected operation.
- `EXPO_PUBLIC_*` and bundled config are public.
- Avoid sensitive payloads in logs, analytics, crash breadcrumbs, AsyncStorage, screenshots/app switcher, and source maps.
- Define token expiry/refresh/revocation, account isolation, logout cleanup, biometric fallback, compromised-device posture, transport/certificate policy, and consent/retention.
- Review native-module/config-plugin supply chain and build/update signing permissions.
