# Codex Game Studios quick start

Open the repository root in Codex. Use `$start` to choose a workflow. For an
engine game, the minimal route is `$setup-engine` → `$brainstorm` →
`$create-stories` → `$dev-story` and `$story-done` for each story.
Use `$smoke-check` to execute the build/test checks and record evidence.

For a small mechanic experiment, use `$prototype` with the HTML, engine or paper
route. A browser prototype can be self-contained and need no game engine.
For an existing game, use `$adopt` to inspect its state and `$help` to find the
next useful workflow. More detailed planning can use standard/full rigor.

Skills are `.agents/skills/`, native roles are `.codex/agents/*.toml`, portable
role briefs are `.codex/roles/`. All roles inherit the session model.
See `directory-structure.md` and `codex-runtime.md` for the integration contract.

Set the chosen engine/version and build/test commands in `project.yaml`; local
preferences are `project.local.yaml`. Resolve config explicitly:

```bash
bash .codex/scripts/yaml-helper.sh resolve_config
```

Native agent discovery depends on host support. Workflows perform roles
sequentially when delegation is unavailable or unauthorized.
