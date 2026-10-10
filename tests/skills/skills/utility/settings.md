# Skill Test Spec: $settings

## Skill summary

Read or change project configuration with the actual config resolver. Preserve
team-owned keys and only permit documented personal overrides.

## Static assertions

- Skill metadata contains `name` and `description`.
- Resolver execution uses `.codex/scripts/yaml-helper.sh` explicitly.
- Writes stay within requested config changes and preserve unrelated fields.

## Behavioral cases

1. Read shared settings from a subdirectory: resolve the project root and report
   actual effective values with their sources; create no config files.
2. Shared rigor is full with no explicit workflow: report workflow full derived
   from rigor, rather than a default minimal value.
3. Set local automation guided: update `project.local.yaml`, preserving the
   shared config and unrelated local keys.
4. Attempt a local rigor override: explain that this team-owned key belongs in
   `project.yaml`; do not silently accept an ineffective personal value.
5. Invalid enum value: report the rejected value and the actual fallback without
   claiming that the invalid value is effective.

## Evidence

Static review does not prove execution. The executable resolver regressions in
`tests/codex/test_runtime.py` cover root anchoring, precedence and invalid enums.
