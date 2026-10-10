# Updating Codex Game Skills

For a new game, clone the latest `main` branch. For an existing game, fetch a
separate copy of https://github.com/lazyseacow/codex-game-skills and review changes
before merging its `.agents/skills/`, `.codex/`, `tools/` and `tests/` directories.

Preserve engine settings, project-specific role guidance and rules, and local
changes to `AGENTS.md` and `project.yaml`. Merge instructions and config fields;
do not replace the game's source, assets, design or production records.
`project.local.yaml` and `AGENTS.override.md` remain personal files.

After merging, synchronize roles and validate:

```sh
python3 tools/sync_roles.py
python3 tools/validate_codex.py
python3 -m unittest discover -s tests/codex -v
git diff --check
```

Run the game's configured build/test commands before continuing development.
Reopen Codex when new skill discovery requires a new session.
