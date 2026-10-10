# Studio coordination in Codex

Read `codex-runtime.md` before delegation. Keep design, implementation and QA
responsibilities distinct. Consult the appropriate role for cross-domain
decisions, and preserve the user's game vision.

Native roles are `.codex/agents/*.toml`. Each has a name, description and
developer instructions; no model, permissions or sandbox policy is overridden.
For hosts without native custom roles, load `.codex/roles/<role>.md` into a
generic subagent brief. When subagents are unavailable or unauthorized, execute
the role steps sequentially. Role Markdown files are not auto-discovered agents.

For authorized parallel work, assign non-overlapping file ownership and clear
return contracts. Wait for dependencies before integrating results. Verify
artifacts exist and tests actually ran. Surface blocked results and preserve
completed independent work. A role's recommendation does not authorize
publishing, contacting people or changing the project scope.
