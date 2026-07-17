# Visual Decomposition Worksheet

## Evidence levels

- **Observed:** directly visible in the reference.
- **Derived:** geometric or system relationship supported by multiple observations.
- **Hypothesized:** likely behavior/style requiring implementation test or another reference.

## Layers

1. **Frame:** viewport, safe area, page background, scroll direction, global chrome.
2. **Regions:** header/navigation, main sections, rails, overlays, footer/tab bar.
3. **Geometry:** container width, gutters, grid tracks, alignment lines, gaps, aspect ratios, overlap.
4. **Typography:** role, relative size, weight, line height, wrapping, max measure, tracking, truncation.
5. **Surfaces:** semantic color, border, radius, shadow/elevation, texture, blur, opacity.
6. **Assets:** source, crop, focal point, fit mode, mask, icon family, illustration behavior.
7. **State:** selected, hover/focus implied, disabled, validation, loading, error, empty, modal/popover.
8. **Behavior:** sticky/fixed, scrolling, disclosure, carousel, drag, keyboard/touch expectations.

## Constraint table

```markdown
| Element | Observed geometry | Relationship/constraint | Responsive hypothesis | Confidence |
```

## Component test

A candidate component deserves a boundary when at least one is true:

- semantic behavior/state is independent;
- structure repeats with meaningful variants;
- it is an existing design-system primitive;
- it needs isolated accessibility or responsive testing;
- its content/data source is independently reusable.

Visual rectangles alone are not component boundaries.
