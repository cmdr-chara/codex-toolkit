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

## Install

Run from PowerShell:

```powershell
.\scripts\install-mission-control.ps1
```

The installer backs up conflicting files before installing into `~/.codex`. Start a fresh Codex task after installation, then invoke:

```text
Use $delegate-with-mission-cards to handle this task.
```

## Safety

This repository does not contain credentials, sessions, memories, logs, or a complete machine-specific `config.toml`. Review skills and agent definitions before installing them; instruction files are executable policy for an agent.

## License

MIT
