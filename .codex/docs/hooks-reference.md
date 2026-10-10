# Explicit validation

Run `python3 tools/validate_codex.py` for collection integrity and
`python3 -m unittest discover -s tests/codex -v` for runtime regressions.
For games, execute configured build/test commands and follow `$smoke-check`.

The `.codex/scripts/` helpers report observations for workflows to interpret.
`yaml-helper.sh` is an explicit config library and CLI. The collection does not
register automatic event handlers or change host execution permissions.
