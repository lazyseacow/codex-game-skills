# Behavioral evaluation instructions

Read `catalog.yaml` to locate the requested skill or role spec and its category.
Skill entrypoints are `.agents/skills/<name>/SKILL.md`; role briefs are
`.codex/roles/<name>.md`, with native config in `.codex/agents/<name>.toml`.
Read relevant skill references and `.codex/docs/codex-runtime.md` explicitly.

Evaluate the spec's static assertions, cases and protocol checks against the
actual workflow and runtime contract. Skill frontmatter requires `name` and
`description`. Native roles contain `name`, `description` and
`developer_instructions`, inheriting session model and permissions.
Existing authorization covers necessary local implementation edits; undecided
choices and external publication still follow user intent. Delegation depends
on available tools and authorization; sequential role execution is supported.

Use the matching section in `quality-rubric.md` for category checks. Missing
inputs are NOT ASSESSED, not passes. Separate written-spec review from executed
behavioral evidence. Save results only within the user's requested scope.
