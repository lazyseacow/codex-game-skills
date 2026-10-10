# Personal settings

Use `project.local.yaml` for personal workflow preferences accepted by the
resolver. Team policy belongs in `project.yaml`; see `config-resolution.md` for
precedence and the list of locally overridable keys.

```yaml
modes:
  automation: guided
```

Use the Codex host's settings for model selection, execution permissions,
sandboxing and external integrations. This project does not install a separate
permissions file or change global settings.
