# Engine stack in AGENTS.md

Read `.codex/docs/codex-runtime.md` for authorization. Preserve all existing
project instructions in `AGENTS.md` while updating its Technology Stack section.
Use the engine/version and language already selected by the user. If Godot's
language is unresolved, offer GDScript, C# or both. For Unreal, determine C++ or
Blueprint-primary. Use `references/godot-language-config.md` for the Godot stack
and naming templates; engine-specific fields belong in `project.yaml` too.

Godot uses its editor/import pipeline; Unity uses C# and Unity Build Pipeline;
Unreal uses Unreal Build Tool with the chosen C++/Blueprint split. Verify the
installed engine's version instead of guessing one.

Under the `ENGINE-REFERENCE-IMPORT` marker, write an explicit instruction:

```markdown
Read `docs/engine-reference/<engine>/VERSION.md` before engine-specific work.
```

Replace `<engine>` with `godot`, `unity` or `unreal`. Do not use `@` imports;
Codex does not expand them. Complete the existing skill's config, reference and
scaffolding phases. Updating the stack alone is not engine setup.
