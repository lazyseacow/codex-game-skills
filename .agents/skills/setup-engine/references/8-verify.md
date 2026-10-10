# Verify engine setup and read back

Read `AGENTS.md` and confirm the explicit read instruction under
`ENGINE-REFERENCE-IMPORT` points to the engine just configured. Confirm the
engine reference file actually exists. No `@` import should be written.

Run from the project root:

```bash
bash .codex/scripts/project-coherence.sh
```

This compares `project.yaml`, the engine reference, Godot project settings where
applicable, installed engine version and configured command targets. Report and
resolve each `[DIFFERS]` observation. `[NOT CHECKED]` is not a pass: name the
missing binary or artifact. Run the chosen engine's build/test commands when
available and record actual results. Do not infer success from a template.
