#!/usr/bin/env python3
"""Synchronize native Codex agent instructions from maintained role briefs."""
import argparse
import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def role_instructions(root, name):
    runtime = (root / '.codex/docs/codex-runtime.md').read_text().strip()
    brief = (root / f'.codex/roles/{name}.md').read_text().strip()
    return runtime + '\n\n' + brief + '\n'


def synchronize(root=ROOT, check=False):
    changed = []
    for brief in sorted((root / '.codex/roles').glob('*.md')):
        target = root / f'.codex/agents/{brief.stem}.toml'
        current = tomllib.loads(target.read_text()) if target.exists() else {}
        description = current.get('description', f'{brief.stem} game-development role')
        values = {'name': brief.stem, 'description': description,
                  'developer_instructions': role_instructions(root, brief.stem)}
        content = ''.join(f'{key} = {json.dumps(value, ensure_ascii=False)}\n'
                          for key, value in values.items())
        if not target.exists() or target.read_text() != content:
            changed.append(str(target.relative_to(root)))
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
    if check and changed:
        raise SystemExit('Role configs need synchronization: ' + ', '.join(changed))
    print(f'Native roles current: {len(list((root / ".codex/roles").glob("*.md")))}; '
          f'{len(changed)} updated' if not check else 'Native role configs match their briefs')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    synchronize(check=args.check)
