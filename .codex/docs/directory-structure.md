# Codex project layout

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Project instructions, engine stack and workflow entrypoints |
| `.agents/skills/<name>/` | 74 Codex-discoverable workflow skills and references |
| `.codex/agents/<role>.toml` | 49 native Codex custom agents |
| `.codex/roles/<role>.md` | Portable role briefs for sequential or generic-agent use |
| `.codex/docs/` | Coordination, workflow policy, engine guidance and templates |
| `.codex/rules/` | Path-specific instruction references, loaded explicitly |
| `.codex/scripts/` | Portable observation helpers |
| `.codex/scripts/yaml-helper.sh` | Config resolver; no automatic hook registration |
| `project.yaml`, `project.local.yaml` | Shared settings and ignored personal overrides |
| `design/`, `docs/`, `production/` | Game design, architecture and production artifacts |
| `prototypes/` | Experiments; not production code |
| `tools/`, `tests/codex/` | Native role synchronization and validation |

## Engine code roots

Godot: `src/`, tests in `tests/`, assets in `assets/`.
Unity: `Assets/`, tests in `Assets/Tests/`.
Unreal: `Source/<Module>/`, tests in `Source/<Module>/Private/Tests/`.
Resolve the selected root through `.codex/docs/code-root-resolution.md`.

Checkpoints are in `production/session-state/active.md` and are ignored by Git.
Role memory is in `.codex/agent-memory/<role>/` and is read explicitly.
