# Redesign Audit

Audit before proposing change. Capture screenshots and behavior at representative widths when possible.

## Functional truth

- routes/navigation and back/deep-link behavior;
- roles/permissions and destructive actions;
- forms, validation, async, offline, retry, and recovery states;
- data density, sorting/filtering/search, tables/charts, and export;
- platform/browser/device constraints;
- high-value behavior that must remain unchanged.

## Experience diagnosis

| Area | Inspect | Evidence of weakness |
| --- | --- | --- |
| Hierarchy | first action, reading order, grouping, contrast | competing focal points, hidden primary action, uniform emphasis |
| Layout | grid, alignment, rhythm, whitespace, responsive transformation | accidental gaps, repetitive blocks, unstable geometry, overflow |
| Type/content | roles, scale, line length, terminology, real-content stress | weak differentiation, truncation, generic/filler copy |
| Components | variants, states, composition, semantics | one-off drift, nested containers, missing states, inconsistent controls |
| Color/material | semantic roles, contrast, depth, imagery | decoration replacing hierarchy, inconsistent status, inaccessible contrast |
| Motion | purpose, sequencing, interruption, reduced motion | delayed task completion, layout shift, non-dismissible effects |
| Accessibility | semantics, focus, targets, reflow, status/error | visual-only affordance, trapped flow, unreadable zoom/dynamic type |
| Brand | recognizable assets and voice | erased identity or disconnected campaign aesthetic |

## Change strategy

Classify each finding:

- preserve;
- clarify without structural change;
- consolidate into system;
- redesign interaction;
- remove;
- prototype before deciding.

Prioritize user outcome and risk, not visual novelty. Keep a regression list for behavior the redesign must not break.
