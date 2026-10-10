# Codex Game Skills workflow guide

Start at `$start` for a new game or `$adopt` for existing work. Use `$help` to
inspect the current project state. Choose workflow depth with `$settings`:
`minimal` for small projects, `standard` for design and test traceability, and
`full` for complete production gates.

## Explore and validate

Use `$brainstorm` to establish the game idea and `$setup-engine` to pin the
installed engine and language. `$prototype` tests a focused mechanic or technical
question with HTML, engine or paper artifacts. Record runnable verification
separately from human fun assessment.

## Design and architect

At standard/full rigor, `$map-systems` identifies dependencies, `$design-system`
authors system designs, `$art-bible` establishes the visual identity, and
`$ux-design` defines player-facing flows. `$create-architecture` and
`$architecture-decision` document implementation boundaries. Review designs,
architecture and traceability before depending on them.

## Plan and implement

`$create-epics` and `$create-stories` produce implementable work. `$story-readiness`
checks inputs, `$dev-story` implements the chosen story, and `$story-done` verifies
acceptance criteria and evidence. `$sprint-plan` and `$sprint-status` track progress.
Use `$team-*` workflows for scoped collaboration when authorized.

## Verify and release

`$test-setup` establishes the engine's test runner. `$qa-plan`, `$smoke-check`,
`$regression-suite` and `$test-evidence-review` execute and assess actual checks.
`$gate-check` assesses readiness for the requested phase using required inputs;
missing evidence stays NOT ASSESSED. Use `$release-checklist` and
`$launch-checklist` to prepare a release, with publication authorized separately.

## Reference files

- `.codex/docs/workflow-catalog.yaml`: ordered steps by workflow depth.
- `.codex/docs/director-gates.md`: review inputs and verdicts.
- `.codex/docs/effects-map.md`: configuration fields and behavior.
- `.codex/docs/codex-runtime.md`: tool, authorization and verification contract.
- `.codex/docs/skills-reference.md`: full skill directory.
