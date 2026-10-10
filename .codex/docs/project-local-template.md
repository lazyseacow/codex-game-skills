# Local project instructions

Put personal workflow preferences in the ignored `project.local.yaml`:

```yaml
modes:
  automation: guided
```

For machine-specific instructions, Codex supports `AGENTS.override.md`.
It takes precedence over `AGENTS.md` at that directory level rather than appending
its contents. Include any shared instructions that must still apply. Keep this
file ignored and leave execution permissions in the host's configuration.
