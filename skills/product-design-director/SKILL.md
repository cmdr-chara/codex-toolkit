---
name: product-design-director
description: Define or elevate product UX and visual direction through brief inference, brand evidence, user-flow and state reasoning, explicit design calibration, responsive systems, accessibility, and redesign critique. Use when the core decision is what the experience should communicate and how it should feel or behave. Do not use for literal screenshot reconstruction, routine frontend implementation, or production architecture without a design-direction question.
---

# Product Design Director

Turn product intent into an implementable experience system. Direction comes from evidence and constraints, not a default aesthetic.

## Trigger boundary

Use this skill for:

- establishing product, UX, brand, and visual direction for a new experience;
- redesigning an existing interface without losing functional truth;
- extracting a coherent design system from product/brand evidence;
- critiquing hierarchy, flows, states, responsive behavior, accessibility, and visual consistency;
- preparing an implementation-ready design brief for web or mobile builders.

Do not trigger for:

- reproducing a supplied screenshot or visual reference—use `screenshot-to-interface`;
- building an already-specified web/mobile interface—use the platform builder;
- choosing Flutter versus Expo—use `mobile-architecture-director`;
- applying a fashionable style without product, audience, and content evidence.

## Required inputs

Gather or infer with labeled assumptions:

1. product, user, job-to-be-done, and primary success action;
2. content/information hierarchy and required flows;
3. brand assets, existing product, competitors/references, and prohibited directions;
4. target devices, input modes, languages, content variability, and accessibility obligations;
5. technical/organizational constraints and delivery stage;
6. for redesigns, screenshots and current implementation/state inventory.

Do not block on subjective adjectives alone. Translate “premium,” “simple,” or “bold” into observable hierarchy, density, typography, material, motion, and interaction choices.

## Provenance

This skill is an original restructuring that selectively adapts concepts from Leonxlnx/taste-skill. Read [`references/provenance.md`](references/provenance.md) and preserve the root `THIRD_PARTY_NOTICES.md` when redistributing.

## Safety baseline

- Inspect the current product, repository, and approved assets before proposing replacement.
- Preserve validated behavior, content obligations, platform conventions, and user work; do not disguise functional regression as visual simplification.
- Distinguish observed product/brand evidence from inference and subjective preference.
- Do not copy a competitor's protected assets, trade dress, or distinctive composition; record provenance and rights for supplied material.
- Do not use accessibility as a late polish step or trade it away for an aesthetic without an explicit product/legal decision.
- Do not prescribe a framework, package, or broad rewrite merely to express the direction.

## Workflow

### 1. Infer the design problem

Write a compact brief:

```text
Audience and context:
Core job and success action:
Trust/emotion to establish:
Information users must understand first:
Required flows and states:
Brand evidence:
Constraints and non-goals:
Assumptions to validate:
```

Resolve tension explicitly. Examples: expressive brand versus high-density operations; cinematic storytelling versus fast task completion; novelty versus platform convention.

### 2. Audit the current experience when redesigning

Use [`references/redesign-audit.md`](references/redesign-audit.md). Inventory current behavior before proposing visual change:

- navigation, flows, permissions, form/data states, and responsive variants;
- components/tokens, typography, spacing, color, imagery, iconography, and motion;
- accessibility behavior and content constraints;
- recognizable brand assets and high-performing interaction patterns;
- generic repetition, weak hierarchy, inconsistency, missing states, and implementation debt.

Preserve functional truth. Do not rewrite a working product solely to express a new visual idea.

### 3. Define experience principles

Create three to five principles tied to the brief. Each must include a consequence and anti-consequence:

```text
Principle: Operational calm
Therefore: one dominant action, stable geometry, restrained motion, visible system status.
Not: low contrast, hidden controls, or decorative emptiness.
```

Reject principles that could describe every product.

### 4. Generate distinct direction hypotheses

Produce two or three meaningfully different directions, not color variants. For each state:

- product/brand rationale;
- composition and hierarchy model;
- typography and content voice;
- color/material/image/icon approach;
- motion and interaction character;
- responsive behavior;
- accessibility and implementation risks;
- where it should and should not be used.

Use the axes in [`references/direction-calibration.md`](references/direction-calibration.md) to make differences explicit. Select one direction or a deliberate synthesis. Do not combine incompatible signatures into visual noise.

### 5. Model journeys and states

For every critical flow define:

- entry and exit;
- primary and secondary actions;
- decision points and progressive disclosure;
- loading, empty, partial, success, validation, error, offline/retry, permission, and destructive-confirmation states;
- recovery and back navigation;
- responsive and input-mode changes;
- analytics/feedback moment when product learning matters.

A polished happy path with undefined failure states is not a complete direction.

### 6. Establish the visual system

Define implementable rules, not only adjectives:

- type roles, scale/rhythm, line length, emphasis, and content hierarchy;
- spacing cadence, grid, alignment, container behavior, and density modes;
- semantic color roles and contrast constraints;
- shape, border, elevation, and surface logic;
- imagery/illustration/data-visualization treatment and asset provenance;
- icon semantics and label policy;
- component families, variants, states, and composition limits;
- motion purpose, duration classes, interruption, reduced-motion behavior;
- token candidates and where values remain contextual.

Avoid repetitive template signals: identical rounded containers around every section, ornamental pills, arbitrary gradients/glow, fake system labels, redundant card nesting, and motion without state or hierarchy purpose. These are diagnostic prompts, not universal prohibitions.

### 7. Design responsive behavior

Do not shrink the desktop composition mechanically. Specify:

- content priority and reordering;
- breakpoint conditions based on layout failure, not named devices alone;
- navigation transformation;
- grid collapse, media crops, data/table alternatives, and touch target changes;
- fixed/sticky behavior and viewport/safe-area constraints;
- long text, localization expansion, zoom, orientation, and dynamic type;
- what is removed, deferred, or moved behind disclosure—and why.

### 8. Integrate accessibility

Use [`references/accessibility-and-responsive-review.md`](references/accessibility-and-responsive-review.md). Accessibility is a design input:

- semantic structure and reading/focus order;
- keyboard, switch, touch, pointer, and assistive-technology paths;
- visible focus, target size, labels, instructions, validation, status, and recovery;
- contrast, color independence, text resizing/reflow, reduced motion, media alternatives;
- native/platform conventions before custom interactions;
- cognitive load, plain language, and time/interrupt handling.

When aesthetic intent conflicts with comprehension or operation, revise the direction rather than delegating the conflict to implementation.

### 9. Critique against the brief

Review in this order:

1. task clarity and content hierarchy;
2. flow completeness and state recovery;
3. brand/product fit and distinctiveness;
4. system consistency and responsive logic;
5. accessibility and input modes;
6. feasibility, performance, and maintainability;
7. surface polish.

Do not use “looks modern” as evidence. Point to concrete choices and likely user effects.

### 10. Prepare the handoff

Return:

- brief, assumptions, and non-goals;
- selected direction and rejected alternatives with reasons;
- experience principles;
- journey/state map;
- visual system and responsive rules;
- component inventory and content requirements;
- accessibility acceptance criteria;
- asset/provenance notes;
- open decisions and risks;
- verification plan for implementation.

Use real content or content constraints. Placeholder copy must not hide hierarchy or localization risk.

## Interaction boundaries

- `screenshot-to-interface` owns structural reconstruction and fidelity to a visual reference.
- `production-web-builder`, `flutter-production-builder`, and `expo-react-native-builder` own code architecture and feature-level verification.
- `documentation-synchronizer` owns factual documentation updates; this skill may define voice and experience terminology.
- `verification-and-release` owns the release gate, not aesthetic approval.

## Failure handling

- If brand evidence conflicts, show the conflict and propose a hierarchy of authority.
- If essential content or workflow is unknown, define content/state constraints and mark the decision provisional instead of filling with generic UI.
- If references are copied too literally, return to product principles and asset/provenance constraints.
- If the direction requires fragile performance, inaccessible behavior, or unsupported platform patterns, redesign the mechanism.
- If stakeholders disagree subjectively, compare directions against agreed user, brand, accessibility, and feasibility criteria.

## Stop conditions

Stop when the selected direction is distinguishable, traceable to product evidence, complete across critical states and responsive modes, accessible in intent, and specific enough for implementation and verification. Do not begin production coding unless explicitly handed to the relevant builder.
