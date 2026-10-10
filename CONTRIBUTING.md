# Contributing

Maintain skills directly in `.agents/skills/`, role briefs in `.codex/roles/`,
and shared guidance, rules and helpers in `.codex/`. Behavioral evaluation specs
and their catalog live in `tests/skills/`.

Skills use `name` and `description` frontmatter and explicit references.
Use the host's available tools and current permissions; inherit session model
settings. Preserve user authorization and report sequential role execution
honestly when subagents are unavailable. Validation helpers report observations,
not creative verdicts or evidence that a missing engine ran.

After editing role briefs or the runtime contract, synchronize native agents:

```sh
python3 tools/sync_roles.py
python3 tools/validate_codex.py
python3 -m unittest discover -s tests/codex -v
git diff --check
```

For workflow changes, verify the observable artifacts and behavior relevant to
the change. Use `$skill-test` for behavioral specs and category reviews.
Engine claims require the actual configured engine/build/test tools.
Keep temporary experiments, local settings, credentials and logs out of commits.

Use concise commits describing the resulting behavior. PR descriptions should
explain the problem, final change, validation and any remaining limits.
Preserve the original MIT copyright and permission notice in `LICENSE`, and
the source attribution in `NOTICE`. Keep both with redistributed copies or
substantial portions; retain these notices when embedding the collection.
