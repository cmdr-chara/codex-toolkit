# Codex Toolkit

> Reusable playbooks that help Codex understand, change, and verify real software projects.

[![License: MIT](https://img.shields.io/badge/license-MIT-0ea5e9.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Codex_skills-15-7c3aed.svg)](skills)
[![Custom agents](https://img.shields.io/badge/custom_agents-6-f97316.svg)](agents/mission-control)
[![Validation](https://img.shields.io/badge/validation-structural_%2B_smoke-10b981.svg)](evaluations/README.md)

Codex can already write code. These skills help it handle the harder parts: understanding an unfamiliar repository, choosing a safe approach, making focused changes, and proving the result works.

Install only the skill you need. When a task grows, the skills can hand work to one another.

## Start in three steps

1. List the available skills:

       npx skills add https://github.com/cmdr-chara/codex-toolkit --list

2. Install one skill globally:

       npx skills add https://github.com/cmdr-chara/codex-toolkit --skill "debugging-investigator" -g

3. Start a new Codex task and ask normally, or name the skill:

       Use $debugging-investigator to find why checkout sometimes shows stale totals.

Replace debugging-investigator with any skill listed below.

## Pick a skill

### Understand and change code

| You want to... | Use |
| --- | --- |
| Understand an unfamiliar repository or see what a change could affect | [repository-intelligence](skills/repository-intelligence) |
| Review a change or plan a safe refactor | [review-and-refactor-code](skills/review-and-refactor-code) |
| Find the cause of a bug or regression | [debugging-investigator](skills/debugging-investigator) |
| Measure a slow path and plan an optimization | [optimize-codebase-performance](skills/optimize-codebase-performance) |
| Upgrade a dependency, framework, schema, API, or runtime | [codebase-evolution-controller](skills/codebase-evolution-controller) |
| Update guides, examples, API docs, configuration, or runbooks | [documentation-synchronizer](skills/documentation-synchronizer) |
| Decide what must be tested or whether a release is ready | [verification-and-release](skills/verification-and-release) |

Review/refactor and performance requests start with inspection and a proposal. They do not edit files until you approve the proposed batch.

### Build products and interfaces

| You want to... | Use |
| --- | --- |
| Decide how a product should look and behave | [product-design-director](skills/product-design-director) |
| Rebuild an interface from screenshots | [screenshot-to-interface](skills/screenshot-to-interface) |
| Build or audit a production web app | [production-web-builder](skills/production-web-builder) |
| Choose between Flutter, Expo/React Native, native, or another mobile approach | [mobile-architecture-director](skills/mobile-architecture-director) |
| Build an app after Flutter is chosen | [flutter-production-builder](skills/flutter-production-builder) |
| Build an app after Expo or React Native is chosen | [expo-react-native-builder](skills/expo-react-native-builder) |

### Work with multiple agents

| You want to... | Use |
| --- | --- |
| Split understood work into safe, non-overlapping tasks | [multi-agent-work-coordinator](skills/multi-agent-work-coordinator) |
| Send approved tasks to the toolkit's reader and writer agents | [delegate-with-mission-cards](skills/delegate-with-mission-cards) |

Use the smallest skill that owns the decision in front of you. A skill can hand off to another one when the task changes.

## How skills work together

A task does not need every skill. Common paths are:

- Unknown repository -> repository-intelligence -> the relevant implementation skill.
- Bug with an unknown cause -> debugging-investigator -> a focused fix -> verification-and-release.
- Requested cleanup -> review-and-refactor-code -> your approval -> incremental refactor.
- Slow critical path -> optimize-codebase-performance -> your approval -> measured optimization.
- Framework or schema upgrade -> codebase-evolution-controller -> documentation-synchronizer -> verification-and-release.
- New product direction -> product-design-director -> a web or mobile builder.

The builder verifies its own change. Verification-and-release makes the final decision about the integrated release.

## Mission Control

Mission Control is optional. It installs six custom agents plus delegate-with-mission-cards.

Install it directly from GitHub:

    npx --yes github:cmdr-chara/codex-toolkit

On Windows, a cloned checkout can use:

    .\scripts\install-mission-control.ps1

Existing Mission Control files are backed up under ~/.codex/backups before replacement.

| Agent | Best for |
| --- | --- |
| pathfinder-reader | Fast file, symbol, and fact lookup |
| patcher-writer | Small isolated edits |
| investigator-reader | Debugging, tracing, and focused reviews |
| builder-writer | Features, tests, fixes, docs, and configuration |
| sentinel-reader | Security, privacy, migrations, and other high-risk analysis |
| architect-writer | Difficult architecture and failure-sensitive changes |

The coordinator decides how work is divided. Mission Control chooses an agent for each approved task. The parent Codex task still owns integration and final verification.

## What is inside

Each skill is an installable folder with:

- SKILL.md for its trigger, workflow, safety rules, and stopping points;
- agents/openai.yaml for the name and prompt shown in Codex;
- optional references for detail that should load only when needed;
- optional read-only scripts for deterministic inspection.

Skills are designed to work independently. No skill depends on a hidden shared runtime folder.

## Check the toolkit

Run the structural validator:

    python scripts/validate_skill_pack.py . --as-of 2026-07-31

Run the network-free helper smoke tests:

    python scripts/run_smoke_tests.py . --as-of 2026-07-31

The structural check covers skill metadata, links, routing cases, references, licensing, and Python safety rules. The smoke suite runs every helper against temporary sample projects and confirms that fixture inputs do not change.

See [the evaluation guide](evaluations/README.md) for routing and workflow tests.

## Repository layout

| Folder | Contents |
| --- | --- |
| agents | Six optional Mission Control agents |
| docs | Design decisions, boundaries, and research sources |
| evaluations | Routing, overlap, workflow, and smoke-test cases |
| scripts | Installers and validation tools |
| skills | Fifteen installable skills |

## Research and credit

Web research was refreshed on 2026-07-31; mobile research was checked on 2026-07-17. Always compare it with the versions and lockfiles in the project you are changing.

Product design and screenshot reconstruction include adaptations from Leonxlnx's MIT-licensed Taste Skill project. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) contains the license and source mapping.

The code-review, refactoring, and performance skills were independently authored after inspecting an unlicensed public skill collection. No source prose or code was copied. The research record is in [docs/research-ledger.md](docs/research-ledger.md).

## License

[MIT](LICENSE) Copyright 2026 cmdr-chara
