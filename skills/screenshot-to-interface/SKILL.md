---
name: screenshot-to-interface
description: Reconstruct a maintainable interface from screenshots or visual references through evidence capture, structural decomposition, asset handling, responsive inference, component boundaries, accessibility, and iterative visual comparison. Use when fidelity to supplied visual evidence is the primary requirement. Do not use for greenfield art direction, generic frontend production hardening, or copying assets without rights.
---

# Screenshot to Interface

Treat references as evidence, not as a bitmap to trace blindly. Reconstruct the underlying layout and behavior while preserving maintainability and rights.

## Trigger boundary

Use this skill for:

- implementing a page, screen, component, or flow from screenshots;
- translating a design comp into responsive components;
- auditing why an implementation differs from its reference;
- inferring a coherent component/system model from multiple visual states.

Do not trigger for:

- deciding an original visual direction without a reference—use `product-design-director`;
- a production web/mobile audit unrelated to reference fidelity—use the platform builder;
- extracting or redistributing protected assets without permission;
- image OCR or screenshot transcription where no interface reconstruction is requested.

## Required inputs

Obtain or record as unknown:

1. all reference images and their source/provenance;
2. pixel dimensions, device scale factor, viewport, orientation, theme, locale, and state if known;
3. target repository, stack, routes, and existing design system;
4. required interactions, responsive range, browsers/devices, and accessibility target;
5. asset rights and available original logos/icons/fonts/images;
6. acceptable fidelity tolerance and whether content may be adapted.

Do not infer one desktop screenshot as the complete responsive specification.

## Provenance

This skill is an original restructuring that selectively adapts visual-reference and fidelity concepts from Leonxlnx/taste-skill. Read [`references/provenance.md`](references/provenance.md) and preserve the root notice.

## Safety baseline

- Inspect repository and working-tree state before editing.
- Reuse existing tokens/components when they can express the reference without distortion.
- Do not replace project architecture, framework, or styling system solely for visual convenience.
- Do not embed screenshots as the interface, hard-code coordinates for one viewport, or use inaccessible canvas/text images for ordinary UI.
- Do not download fonts/assets from a reference without rights and license evidence.
- Preserve user code and keep generated or broad formatting changes out of the diff.

## Workflow

### 1. Build the reference register

For every image record:

```text
ID/path:
Source and rights:
Pixel dimensions/device scale:
Inferred viewport/device:
Theme/locale/state:
Known relationships to other images:
Quality issues/crops/occlusion:
```

Mark what is visible, implied, or unknown. Do not present guessed font names, exact pixel values, or interaction behavior as observed facts.

### 2. Inspect the target implementation context

Identify:

- framework, rendering model, routes, component and styling conventions;
- existing tokens, fonts, icons, assets, layout primitives, and accessibility helpers;
- content/data boundaries and state management;
- test, story, screenshot, and browser/device verification tooling;
- constraints such as CSP, image optimization, localization, theming, or native safe areas.

If production architecture is missing or unsafe, reconstruct the bounded interface first and hand hardening to the relevant builder.

### 3. Decompose the visual structure

Use [`references/visual-decomposition.md`](references/visual-decomposition.md). Infer:

- page/screen regions and stacking contexts;
- layout model: flow, grid, flex, overlay, sticky/fixed, scroll container;
- containers, gutters, alignment lines, column spans, aspect ratios, and whitespace rhythm;
- typography roles, wrapping, line height, emphasis, and truncation;
- semantic color/surface/elevation/border/radius rules;
- components, variants, repeated motifs, and one-off art-directed exceptions;
- interactive, loading, empty, selected, disabled, error, and navigation states visible across images.

Choose relative constraints before literal pixels. Derive a model that explains all references with minimal exceptions.

### 4. Handle content and assets

Follow [`references/asset-handling.md`](references/asset-handling.md):

- prefer provided originals and repository assets;
- match crop/focal treatment through responsive media containers;
- recreate simple geometric decoration in CSS/SVG only when legally and technically appropriate;
- replace unavailable protected assets with approved placeholders that preserve layout, and disclose fidelity impact;
- load fonts through the project's licensed mechanism or select an approved metric-compatible alternative;
- preserve alt text and decorative semantics.

Do not stretch a raster crop to hide missing source material.

### 5. Infer responsive behavior

Across references, distinguish invariant rules from viewport-specific outcomes. Infer:

- fluid versus capped dimensions;
- wrap/reflow/reorder/collapse behavior;
- breakpoint conditions where composition fails;
- media crop and focal-point changes;
- navigation and control transformations;
- touch target, safe-area, keyboard, orientation, and dynamic-type behavior;
- content overflow for long text and localization.

For missing breakpoints, formulate hypotheses and test intermediate widths. Prefer continuity over a collection of unrelated snapshots.

### 6. Design component boundaries

Create components where there is semantic behavior, state, repeated structure, or a stable visual primitive. Avoid:

- one component per visual rectangle;
- a giant page component with repeated magic values;
- abstractions used once that obscure geometry;
- premature universal tokens from one screenshot;
- duplicating an existing project primitive with slightly different styling.

Separate content/data from layout when it enables state and responsive testing. Keep art-directed exceptions explicit.

### 7. Establish the first implementation

Implement in this order:

1. semantic document/screen structure and interaction model;
2. major geometry, scroll behavior, and responsive containers;
3. typography metrics and content wrapping;
4. assets/media crops;
5. color, borders, radii, elevation, and effects;
6. states and transitions;
7. fine optical alignment.

Use real or shape-representative content early. A layout tuned to short placeholders is not faithful.

### 8. Compare iteratively

Use [`references/fidelity-loop.md`](references/fidelity-loop.md). At each target viewport/state:

- capture the implementation in the same dimensions, theme, content, and scroll position;
- compare side by side and, where tooling permits, overlay/difference images;
- classify mismatches by structure, geometry, typography, asset, color/material, state, or rendering;
- fix the highest-level mismatch first;
- repeat at intermediate responsive widths to avoid overfitting.

Never declare fidelity from memory or from inspecting source code alone.

### 9. Verify accessibility and interaction

Even when the reference omits them, implement:

- correct landmarks/headings/roles or native semantics;
- keyboard/touch/pointer operation and visible focus;
- accessible names, error/status communication, and logical order;
- sufficient contrast or document a reference conflict requiring design decision;
- reduced motion and no information conveyed only through animation/color;
- zoom, dynamic type, localization, and content overflow behavior.

When accessibility requires a visible deviation, preserve hierarchy and document the reason rather than silently copying an inaccessible reference.

### 10. Finish and hand off

Return:

- reference register and uncertainty log;
- structural/component/responsive model;
- asset/provenance decisions;
- exact files changed;
- target and intermediate viewport comparison results;
- interaction/accessibility checks;
- known fidelity differences with reason and severity;
- production concerns for the platform builder.

## Interaction boundaries

- `product-design-director` resolves ambiguous or conflicting visual direction.
- `production-web-builder` owns data, auth, rendering architecture, performance, SEO, observability, and production browser verification beyond the reference-bound slice.
- Flutter/Expo builders own native platform conventions, performance, release, and device integration.
- `documentation-synchronizer` updates user/developer documentation and screenshots after the final behavior stabilizes.

## Failure handling

- If reference dimensions or state are unknown, test multiple plausible viewports and label confidence.
- If images conflict, establish whether they represent breakpoints, themes, states, or different revisions; do not merge them arbitrarily.
- If an asset is unavailable or unlicensed, preserve layout with an approved substitute and report the gap.
- If exact fidelity requires brittle fixed positioning, revise the underlying model and document any deliberate tolerance.
- If browser/font rendering creates small differences, verify font files, weight availability, device scale, antialiasing, and screenshot environment before tuning offsets.

## Stop conditions

Stop when the component model explains all supplied references, comparisons pass the agreed tolerance at target and intermediate viewports, accessibility/interaction requirements are met or conflicts are explicitly decided, and remaining differences are documented. Do not claim production readiness outside the reconstructed scope.
