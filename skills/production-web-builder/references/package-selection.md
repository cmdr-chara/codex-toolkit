# Conditional Package Selection

A dependency is a design decision with ongoing update, security, bundle/runtime, and migration cost.

## Decision record

```markdown
Package/capability:
Problem owned:
Existing/native/framework alternative:
Repository compatibility and peer constraints:
Maintenance/release evidence:
License:
Security/deprecation evidence:
 Runtime/build/bundle effect:
Choose when:
Avoid when:
Removal/migration cost:
Sources and information checked date:
```

## Common decisions

| Concern | Prefer built-in/existing when | Consider a package when | Avoid package when |
| --- | --- | --- | --- |
| Server data | framework server fetch/cache/mutations cover ownership and rendering | rich client cache, background refresh, optimistic mutations, offline/retry coordination are required | duplicating server cache or a handful of static requests |
| Client state | local state, URL, form, or server cache owns it | independent cross-tree client state with real lifecycle/persistence exists | storing server data or every component value globally |
| Forms | native form/action and simple controlled/uncontrolled fields are sufficient | dynamic arrays, complex validation/state, large forms, performance/ergonomics justify it | simple contact/search/login form with no complexity |
| Validation | narrow handwritten boundary checks or generated schema suffice | shared runtime schema parsing and typed inference reduce contract drift | validating trusted internal objects repeatedly on hot paths |
| Accessible primitives | native element or existing system implements the pattern | complex dialog/menu/combobox/popover behavior needs maintained primitives | wrapping native buttons/inputs in a second incompatible system |
| Motion | CSS/Web Animations handle state transition | coordinated layout/gesture/scroll/spring orchestration is central | decorative reveal-only animation or tight performance budget |
| Testing | framework runner and current harness suffice | missing browser, unit, component, or network boundary requires a focused tool | adding two overlapping runners or testing internals |
| Observability | deployment platform provides adequate traces/logs/errors | vendor-neutral context propagation or custom instrumentation is required | blanket browser auto-instrumentation without privacy/performance review |

Do not choose two packages for the same state, form, component, or animation layer without a written migration boundary.
