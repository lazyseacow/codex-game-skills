# Skill Test Spec: $skill-test

## Skill summary

Validate skill structure, evaluate behavioral specs and category rubrics, or
report catalog coverage. Distinguish written review from executed behavior.

## Static assertions

- Frontmatter contains `name` and `description`.
- Static mode uses seven host-neutral checks defined in the skill.
- Specs and categories are resolved through `tests/skills/catalog.yaml`.
- User authorization and available tools determine writes and delegation.

## Cases

1. Valid short skill: acceptable metadata and a clear one-step workflow are not
   failed for lacking an arbitrary phase count.
2. Missing description: report NON-COMPLIANT and the exact metadata defect.
3. Missing phase reference: report the unresolved path; do not treat the phase
   as complete merely because the entrypoint mentions it.
4. Review skill with no required input available: report NOT ASSESSED with the
   missing evidence, rather than PASS.
5. Native role spec: inspect its TOML and role brief, inherit session model and
   permissions, and evaluate domain ownership against the relevant gates.
6. Static all: report the examined and available counts with per-skill results;
   missing or unreadable files do not silently disappear from the denominator.
7. Category review without subagent authorization: perform the role steps
   sequentially and label the evidence honestly rather than inventing agents.
8. Spec review: cite the files supporting each assertion; written instructions
   alone are not evidence that a runtime or human playtest occurred.

## Protocol

Static mode writes no files. Save assessments only within requested scope.
Missing specs stay visible in audit output. Correct invalid specs toward the
runtime contract rather than weakening substantive behavioral requirements.
