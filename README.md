# Codex Toolkit

A growing collection of reusable Codex skills, custom agents, and installation helpers.

## Included packages

### Mission Control

`delegate-with-mission-cards` delegates independent repository work to six model-routed reader and writer roles. It uses delegation gates, mission ledgers, exclusive writer ownership, staged parallel waves, and parent-side verification.

| Role | Model | Effort | Access |
| --- | --- | --- | --- |
| `pathfinder-reader` | GPT-5.6 Luna | Medium | Read-only |
| `patcher-writer` | GPT-5.6 Luna | High | Workspace write |
| `investigator-reader` | GPT-5.6 Terra | High | Read-only |
| `builder-writer` | GPT-5.6 Terra | High | Workspace write |
| `sentinel-reader` | GPT-5.6 Sol | XHigh | Read-only |
| `architect-writer` | GPT-5.6 Sol | XHigh | Workspace write |

## Installing

### Full Mission Control bundle

Install the skill and all six model-routed custom agents:

```shell
npx --yes github:cmdr-chara/codex-toolkit
```

### Skill only

Install the portable Agent Skill without the custom model-routing agents:

```shell
npx skills add https://github.com/cmdr-chara/codex-toolkit --skill "delegate-with-mission-cards" -g
```

List the skills available in this repository:

```shell
npx skills add https://github.com/cmdr-chara/codex-toolkit --list
```

### Cloned checkout

Run the PowerShell installer:

```powershell
.\scripts\install-mission-control.ps1
```

The installer backs up conflicting files before installing into `~/.codex`. Start a fresh Codex task after installation, then invoke:

```text
Use $delegate-with-mission-cards to handle this task.
```

## Skills

Each skill has one stable install name. More skills can be added without changing existing install commands.

| Skill folder | Install name | Description |
| --- | --- | --- |
| `delegate-with-mission-cards` | `delegate-with-mission-cards` | Mission-gated delegation with specialized readers and writers, safe parallel waves, and parent-side verification |

See [`skills/llms.txt`](skills/llms.txt) for the compact machine-readable catalog and [`CHANGELOG.md`](CHANGELOG.md) for release notes.

## Safety

This repository does not contain credentials, sessions, memories, logs, or a complete machine-specific `config.toml`. Review skills and agent definitions before installing them; instruction files are executable policy for an agent.

## License

MIT
