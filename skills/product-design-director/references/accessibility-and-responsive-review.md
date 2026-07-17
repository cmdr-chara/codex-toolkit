# Accessibility and Responsive Review

Primary standards and patterns:

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI-ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Web Content Accessibility Guidelines overview: https://www.w3.org/WAI/standards-guidelines/wcag/
- Apple accessibility: https://developer.apple.com/accessibility/
- Android accessibility: https://developer.android.com/guide/topics/ui/accessibility

## Design acceptance prompts

- Reading order, visual order, DOM/semantics, and focus order agree.
- Every action has a visible label or an accessible name that matches its purpose.
- Focus is visible and restored predictably after dialogs, navigation, errors, and dynamic updates.
- Hover, color, motion, and spatial position are not the only carriers of meaning.
- Text reflows under zoom/dynamic type; controls and content do not overlap or clip.
- Touch/pointer targets and spacing support the target platform and motor needs.
- Errors identify the field/problem, explain recovery, and preserve user input.
- Loading/status changes are exposed without causing disruptive announcements.
- Timeouts, auto-advance, animation, and parallax have pause/reduce/disable behavior where needed.
- Custom widgets follow an established platform/WAI pattern; otherwise use native controls.
- Responsive transformation preserves access to actions and context rather than hiding them.

Validate exact conformance requirements for the project's jurisdiction and policy; this reference does not declare legal compliance.
