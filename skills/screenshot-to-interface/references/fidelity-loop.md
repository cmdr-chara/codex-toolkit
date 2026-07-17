# Fidelity Loop

## Capture controls

Match reference where known:

- viewport CSS pixels and device scale factor;
- browser/OS or device/emulator;
- theme, locale, font loading, reduced-motion setting;
- content, state, scroll position, keyboard/safe-area visibility;
- animation settled point and network/data fixtures.

## Mismatch order

Fix from highest leverage to lowest:

1. wrong content/state or missing region;
2. wrong layout model, container, stacking, scroll, or breakpoint;
3. typography metrics and wrapping;
4. media source/crop/aspect;
5. spacing and component dimensions;
6. color, border, radius, elevation, effects;
7. icons and optical alignment;
8. browser rasterization differences.

Fine offsets cannot repair a wrong constraint model.

## Difference record

```markdown
| Viewport/state | Region | Category | Observed difference | Cause hypothesis | Fix | Result/tolerance |
```

## Tolerance

Define tolerance by consequence, not a universal pixel threshold:

- structural/interaction/overflow/accessibility mismatch: zero tolerance unless explicitly approved;
- typography wrap, media crop, and responsive breakpoint: close semantic/visual equivalence required;
- minor antialiasing or subpixel rendering: document when environment-dependent;
- unavailable asset/font: approved substitute and explicit deviation.

Always inspect intermediate widths and extreme content after matching supplied screenshots.
