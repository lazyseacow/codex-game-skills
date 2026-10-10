# Codex Game Skills

This repository provides project-local Codex workflows for game development.
Maintain skills directly in `.agents/skills/`, role briefs in `.codex/roles/`,
and shared guidance and helpers in `.codex/`. Preserve game-specific changes
when updating the skill collection. Preserve `LICENSE` and `NOTICE` when
redistributing or embedding the collection.

## Technology Stack

- **Engine**: [CHOOSE: Godot 4 / Unity / Unreal Engine 5 / browser prototype]
- **Language**: [CHOOSE to match the engine]
- **Version Control**: Git with trunk-based development
- **Build System**: [SPECIFY after choosing engine]
- **Asset Pipeline**: [SPECIFY after choosing engine]

## Working contract

Read `.codex/docs/codex-runtime.md` before using a studio skill or role.
Necessary local edits are authorized by an implementation request; preserve
undecided user choices and the host's permission rules.

Read `project.yaml` for engine and workflow settings, and
`production/session-state/active.md` if it exists when resuming work. Resolve
settings through `bash .codex/scripts/yaml-helper.sh resolve_config`.

## Engine Version Reference

<!-- ENGINE-REFERENCE-IMPORT: setup-engine updates the explicit read instruction. -->
Read `docs/engine-reference/godot/VERSION.md` when Godot is selected.

## Development workflows

Skills are discoverable under `.agents/skills/`. Use `$start` for onboarding,
`$setup-engine` for engine setup, `$prototype` to test a mechanic, `$dev-story`
for implementation, `$smoke-check` for runnable validation, and `$story-done`
to verify completion. Read references as their phases require. Use `$help`
to find the next useful step for the current project state.

Before editing game code, read `.codex/docs/coding-standards.md` and the relevant
`.codex/rules/*.md` selected by their `paths` frontmatter. These are instructions,
not automatically enforced execpolicy. Prototype rules apply under `prototypes/`.
Use the code root for the selected engine (`src/`, `Assets/`, or `Source/`).

Studio custom roles live in `.codex/agents/*.toml`, with portable role briefs
in `.codex/roles/*.md`. Use subagents only when available and authorized by the
user or invoked workflow; otherwise perform the role steps sequentially. Keep
the session model and reasoning defaults. Verify returned artifacts on disk.

## Verification

For collection changes run:

```sh
python3 tools/sync_roles.py --check
python3 tools/validate_codex.py
python3 -m unittest discover -s tests/codex -v
git diff --check
```

For game changes, execute the configured build/test commands and observe the
game when tooling is available. Record actual outputs and limitations. Missing
tools, skipped checks and manual playtests are not passes. Store a checkpoint
after substantial work. Helpers emit observations, not quality verdicts.
Do not commit, push or publish without user instruction.
