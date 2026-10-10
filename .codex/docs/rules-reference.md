# Path rules in Codex

Before editing, select `.codex/rules/*.md` by their `paths` YAML frontmatter and
read the relevant rules. `AGENTS.md` requests this explicitly. These Markdown
rules are instruction references; they are not Codex execpolicy rules or a
security boundary, and no instruction-loading audit hook runs automatically.

Prototype code uses `prototype-code.md`. Production gameplay, AI, network, UI,
engine, shaders, data and narrative each have their own rule file. Test code uses
`test-standards.md`; design documents use `design-docs.md`. See the runtime contract
for the user's authorization and role ownership rules.
