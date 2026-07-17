---
name: production-web-builder
description: Build or audit production web interfaces across architecture, rendering, components, data, forms, authentication boundaries, motion, accessibility, performance, responsive behavior, testing, observability, SEO, deployment, and final browser verification. Use when implementation quality and production behavior are the main decisions. Do not use for visual direction alone, literal screenshot reconstruction alone, mobile-platform selection, or unconditional package installation.
---

# Production Web Builder

Build the smallest coherent web system that satisfies product behavior and production constraints. Prefer platform/framework capabilities until a demonstrated requirement justifies a dependency.

## Trigger boundary

Use this skill for:

- implementing a production web feature, route, application, or redesign handoff;
- auditing an existing web interface for architecture and production readiness;
- choosing rendering/data/form/state/motion/testing approaches from repository evidence;
- completing browser, accessibility, performance, SEO, observability, and deployment verification.

Do not trigger for:

- defining the product's visual direction—use `product-design-director`;
- reference reconstruction where fidelity is the primary problem—start with `screenshot-to-interface`;
- choosing or implementing Flutter/Expo/mobile-native applications;
- adding a package because it appears on a preferred stack list.

## Required inputs

Capture:

1. repository state, framework/runtime/package manager, deployment target, and supported browsers;
2. product/design requirements, flows, content, responsive and accessibility acceptance criteria;
3. data, API, authentication/authorization, cache, mutation, and error contracts;
4. SEO/discovery needs, localization, privacy/security, analytics, and observability policy;
5. performance budget or critical user journeys;
6. test/CI/deploy tooling and environments.

Run the read-only inventory to locate current choices before recommending new ones:

```sh
python skills/production-web-builder/scripts/web_project_inventory.py . --format markdown
```

## Safety baseline

- Inspect and preserve uncommitted work; avoid broad formatting or generated churn.
- Read manifests, lockfile, framework configuration, and existing patterns before package changes.
- Do not expose secrets in client bundles, logs, source maps, browser storage, or test fixtures.
- Treat server/client and trusted/untrusted boundaries explicitly; client validation is not authorization.
- Do not disable type, lint, accessibility, CSP, certificate, auth, or browser safeguards to make a check pass.
- Confirm package commands and compatibility from current official sources and the active repository; never invent CLI flags.

## Workflow

### 1. Establish the web execution model

Map:

- route and layout structure;
- server, edge, client, worker, and build-time execution;
- rendering mode and cache/revalidation behavior per route/data source;
- authentication/session and authorization enforcement point;
- deployment adapter/runtime limitations;
- static assets, image/font pipeline, and CSP/security headers;
- existing component, style, state, data, form, and test layers.

In React Server Component frameworks, keep interactive client boundaries deliberate. Do not mark large trees client-side to solve one local interaction.

### 2. Define behavior and state before components

For each journey specify:

- initial, loading/streaming/skeleton, empty, partial, success, error, retry, offline, stale, and unauthorized states;
- mutation pending, optimistic or pessimistic behavior, validation, idempotency, and reconciliation;
- URL/navigation/back/refresh/deep-link semantics;
- focus and announcement behavior after navigation, validation, dialogs, and async updates;
- telemetry and user recovery.

Implement the contract, not a collection of screenshots.

### 3. Choose architecture and dependencies conditionally

Do not start with a package list.

Use [`references/package-selection.md`](references/package-selection.md) and the dated [`references/web-ecosystem-2026-07-17.md`](references/web-ecosystem-2026-07-17.md).

Decision order:

1. native HTML/CSS/Web APIs and current framework capabilities;
2. existing repository package/pattern when suitable;
3. a maintained dependency with a clearly owned problem;
4. custom abstraction only when native/framework/dependency choices cannot satisfy the constraint.

For every new dependency record compatibility, maintenance, license, security/deprecation, runtime/bundle effect, built-in alternative, choose/avoid conditions, and removal cost. Avoid parallel libraries that solve the same concern without migration intent.

### 4. Build semantic component boundaries

- Start with native semantics and established accessible interaction patterns.
- Separate server/data boundaries from presentational and interactive client components.
- Co-locate behavior, styles, tests, and stories where repository conventions support it.
- Represent variants and state explicitly; avoid boolean-prop combinations that create invalid states.
- Keep one-off page composition visible instead of forcing it through an over-general component API.
- Use tokens for semantic roles and repeated decisions, not every literal value.
- Preserve stable keys, focus, form state, and scroll during updates.

### 5. Implement data and mutations

- Fetch at the layer that owns trust, credentials, caching, and latency.
- Avoid request waterfalls by composing server work, preloading, parallel independent requests, or route-level data as the framework permits.
- Define cache ownership, freshness, invalidation, and personalized-data isolation.
- Validate untrusted input at the server boundary; authorize every protected operation.
- Model errors by class and recovery, not one generic catch-all.
- For optimistic updates, define rollback and server reconciliation; do not assume success.
- Prevent duplicate effects with appropriate idempotency and pending-state controls.
- Avoid copying server state into global client state without a demonstrated need.

### 6. Build forms and interaction

- Prefer native controls and form semantics; add a form library only for complexity it materially reduces.
- Keep labels, descriptions, constraints, error association, and summary/focus behavior accessible.
- Preserve user input after recoverable server errors.
- Separate client convenience validation from authoritative server validation.
- Handle double submission, cancellation/navigation, file limits, autofill, password managers, and localization.
- Use dialogs, popovers, comboboxes, tabs, menus, and grids through native or established accessible primitives rather than ad hoc keyboard behavior.

### 7. Apply visual direction and responsive behavior

Consume design/reconstruction handoffs. Verify:

- hierarchy and component states with real content;
- fluid constraints and intermediate widths, not only named breakpoints;
- long text, zoom, localization, reduced motion, high contrast, and input modes;
- image crop, intrinsic size, aspect, loading priority, and layout stability;
- mobile navigation, safe viewport units, virtual keyboard, touch targets, and sticky/fixed elements;
- print or embedded contexts when required.

Avoid style systems that require runtime JavaScript for static layout unless the existing stack justifies it.

### 8. Use motion with a purpose

Classify motion as feedback, continuity, hierarchy, spatial explanation, or brand expression. Prefer CSS/Web Animations for simple state transitions. Add a motion library for coordinated, interruptible, gesture/scroll, layout, or spring behavior that cannot be maintained clearly otherwise.

Ensure:

- animations can be interrupted and do not block input;
- transform/opacity are favored where appropriate without hiding layout or focus bugs;
- reduced-motion behavior preserves meaning;
- initial load does not animate every element indiscriminately;
- scroll-linked work does not create main-thread jank or inaccessible hijacking.

### 9. Secure and protect privacy

Review:

- server-side authn/authz and tenant boundaries;
- output encoding and dangerous HTML;
- CSRF/session/cookie attributes and token storage;
- redirect/URL validation, file upload, SSRF-like server fetches, and webhook boundaries;
- secrets/environment exposure and source maps;
- CSP and third-party scripts;
- dependency advisories and framework security releases;
- analytics/consent/data minimization.

Use current framework and platform security guidance. The dated reference flags an imminent Next.js security release requiring refresh.

### 10. Verify feature behavior

Use the appropriate mix:

- unit/component tests for logic and states;
- integration tests at server/data/form/auth boundaries;
- browser E2E for critical journeys and navigation;
- accessibility automation plus keyboard/screen-reader-informed manual review;
- responsive visual checks and screenshot comparison for design-critical surfaces;
- failure/timeout/offline/retry and unauthorized paths;
- supported browser/device matrix.

Tests must run against the final integrated state and stable test data. Mock only at a boundary whose real integration is covered elsewhere.

### 11. Verify performance and production behavior

Follow [`references/production-readiness.md`](references/production-readiness.md):

- measure route-level bundle/client JS and eliminate accidental client boundaries;
- inspect request waterfalls, cache behavior, images/fonts, hydration/render work, and third-party scripts;
- use field-relevant Core Web Vitals targets and repository budgets;
- test slow network/CPU, large data/content, and error paths;
- add structured logs, traces, metrics, error boundaries, and correlation without sensitive data;
- validate build/start/deploy adapter, environment, health, and rollback/flag controls;
- verify metadata, canonical/robots/sitemap/structured data and crawlability when SEO applies.

### 12. Final browser pass and handoff

In a real browser at supported viewports:

1. execute critical journeys and refresh/deep-link/back behavior;
2. use keyboard and inspect focus/order/status/errors;
3. inspect console, failed requests, hydration/runtime errors, and layout shift;
4. test responsive extremes, zoom, long content, reduced motion, and theme;
5. capture performance and accessibility evidence appropriate to risk;
6. verify production build/preview behavior, not development mode only.

Return files changed, architecture/dependency decisions, commands/results, browser evidence, known gaps, operational notes, and focused risks. Hand integrated release judgment to `verification-and-release`.

## Interaction boundaries

- Consume experience direction from `product-design-director`; do not reopen it unless repository evidence makes it infeasible.
- Consume reference decomposition from `screenshot-to-interface`; own responsive, data, accessibility, performance, security, and production-browser completion.
- Ask `repository-intelligence` for unclear cross-package impact and `codebase-evolution-controller` for framework/dependency/schema transitions.
- Hand code-caused documentation drift to `documentation-synchronizer`.
- Own feature-level verification only; give the integrated evidence package to `verification-and-release` for the release gate.

## Failure handling

- If repository conventions conflict, preserve the established architecture unless evidence shows it cannot meet the requirement; document migration separately.
- If package compatibility or security is unclear, do not install it. Prototype with built-ins or pin the decision pending primary-source evidence.
- If a browser issue cannot be reproduced, capture browser/OS/build/content and reduce to a controlled fixture.
- If performance targets are absent, establish journey-specific budgets from product and deployment context; do not invent universal bundle limits.
- If backend/auth contracts are unavailable, implement typed boundary adapters and explicit blocked states rather than fake production behavior.

## Stop conditions

Stop when required journeys and states work in production-like builds, semantics/accessibility and responsive behavior are verified, critical performance/security/observability/deployment risks have evidence, and remaining gaps are explicit. Do not claim release readiness; provide the evidence package to `verification-and-release`.
