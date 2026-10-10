# Codex setup requirements

Open the project root in Codex desktop, CLI or IDE. Repository skills are in
`.agents/skills/`; instructions are in `AGENTS.md`; native custom roles are in
`.codex/agents/`. Older hosts can load `.codex/roles/` as role briefs and run
workflows sequentially.

The collection checks require Python 3.11+ and Bash. Engine development additionally
requires the chosen Godot, Unity or Unreal installation and its build/test tools.
Verify the installed engine version before choosing commands. A browser prototype
can use the `$prototype` HTML route without an engine.

No provider credentials, model, permissions, MCP integrations, global config or
automatic hooks are installed by this template. Use your existing Codex login
and host settings. New skills may require reopening the chat on some hosts.
