# Web Production Readiness

## Browser and accessibility

- Critical routes support direct load, refresh, back/forward, deep links, and error recovery.
- Semantic landmarks/headings/forms/tables/lists are correct; custom widgets follow WAI patterns.
- Keyboard path, visible focus, modal focus restoration, status/error announcements, and skip navigation are verified.
- Zoom/reflow, long text/localization, reduced motion, contrast, touch targets, and multiple input modes are checked.
- Supported browser/OS differences are recorded from production build.

## Performance

- Core Web Vitals are measured or estimated with representative field/test evidence: LCP, INP, CLS.
- Route/client JavaScript and third-party scripts are justified; accidental hydration/client boundaries removed.
- Images/fonts have intrinsic sizing, appropriate formats/loading/priority, stable layout, and licensed sources.
- Network waterfalls, duplicate requests, cache keys, personalized caching, and invalidation are inspected.
- Slow CPU/network, large content/data, and cold/warm cache behavior are tested.

Current web.dev guidance uses “good” thresholds at the 75th percentile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Treat these as user-experience targets, not proof that every route or business flow is fast.

## Reliability and observability

- Expected error classes have user recovery and operational signal.
- Error boundaries do not hide server failures or sensitive details.
- Logs/traces/metrics carry safe correlation and release/environment identity.
- Alerts map to actionable symptoms and rollout/rollback decisions.
- Background/retry/idempotency behavior is tested where applicable.

## Security and privacy

- Authentication and authorization are enforced server-side.
- Inputs, redirects, files, external fetches, and rendered HTML are validated at trust boundaries.
- Cookie/session/token and CSRF strategy match architecture; secrets remain server-side.
- CSP/headers/third-party scripts/source maps/dependencies are reviewed.
- Analytics, consent, retention, and personal-data collection are minimized and documented.

## SEO/discovery when applicable

- semantic content and links are server-visible/crawlable as required;
- title/description/canonical/robots/sitemap/social metadata are correct;
- structured data matches visible content and official schema;
- redirects/status codes and duplicate URLs are controlled;
- dynamic/private/app routes are intentionally excluded or indexed.

## Deployment

- production build and start/preview run using the actual adapter/runtime;
- environment validation, migrations, health/readiness, static assets, and cache behavior are checked;
- feature flag/kill switch and rollback or forward-fix path are documented;
- candidate identity is visible in telemetry and evidence.
