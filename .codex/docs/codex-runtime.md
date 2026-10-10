# Codex studio runtime

User instructions and the host's permissions take precedence over workflow defaults.

- Find the project root containing `AGENTS.md` and `project.yaml`; run relative
  commands there. `.agents/skills/<name>/SKILL.md` is the skill entrypoint.
  Invoke workflows with `$name` and obtain arguments from the user's request.
- Use the available file, shell, search, browser and question tools. Operation
  names in workflow prose describe capabilities, not required API names.
  Read referenced files explicitly; execute fenced setup commands when reached.
  Resolve settings with `bash .codex/scripts/yaml-helper.sh resolve_config`,
  retaining a workflow's `--keys` and system argument. Use actual command output.
- Preserve existing authorization. An implementation, setup or fix request
  authorizes necessary local edits. Per-file approval examples in workflow
  templates do not require repeated approval for that work. Ask when a material
  choice or new scope lacks user intent. Silence never answers a pending choice.
  `modes.automation` controls undecided design choices; it does not revoke prior
  authorization. Commit, push, publish and message people only when requested.
- Studio roles are `.codex/roles/<role>.md`; native custom agents are
  `.codex/agents/<role>.toml`. Inherit the session model and reasoning settings.
  If delegation is available and authorized, pass scoped inputs, role instructions,
  owned files and expected artifacts to the host's subagent tool. Give independent
  writers distinct files and verify their returned artifacts. Otherwise perform
  role steps sequentially and report that approach honestly. Keep task state with
  host planning tools or a Markdown ledger under `production/`.
- Run validation explicitly. Instruction files do not install automatic event
  handlers, grant permissions or enforce execution security. Read relevant
  `.codex/rules/*.md` by path before editing. Record substantial work in
  `production/session-state/active.md` and read it on resume. Optional role memory
  is `.codex/agent-memory/<role>/` and must be read explicitly.
- Game implementation requires runnable code and observed verification. Check
  tool availability, execute configured engine/build/test commands and observe
  UI when tooling is available. Missing engines, skipped tests and human playtests
  are NOT passes. Record commands, outcomes and limitations; keep blocked work open.
