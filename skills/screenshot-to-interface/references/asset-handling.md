# Asset Handling

## Decision order

1. Use an original asset supplied by the user or already licensed in the repository.
2. Use an approved design-system or brand-kit asset.
3. Recreate simple non-copyrightable geometry with CSS/SVG when appropriate.
4. Use a licensed substitute with recorded source/license.
5. Use a neutral placeholder that preserves layout and disclose the fidelity gap.

## Record

| Asset | Source | Rights/license | Repository location | Transformation | Alt/decorative semantics | Fidelity note |
| --- | --- | --- | --- | --- | --- | --- |

## Rules

- Do not extract a low-resolution logo, photo, illustration, icon set, or font from a screenshot for redistribution.
- Preserve aspect ratio and meaningful focal point; define responsive crop behavior.
- Optimize derivatives through project tooling and retain authoritative originals where policy requires.
- Avoid embedding large data URLs or bypassing image/CDN/security policy for convenience.
- Treat text rendered inside imagery as content only when the product intentionally requires an image of text and an accessible equivalent exists.
- Verify dark/light/high-contrast variants and transparent-edge behavior.
