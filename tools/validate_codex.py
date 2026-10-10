#!/usr/bin/env python3
"""Validate the standalone Codex skill collection without a login or engine."""
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

from sync_roles import ROOT, role_instructions


def split_frontmatter(text):
    match = re.match(r'\A---\n(.*?)\n---\n(.*)', text, re.S)
    if not match:
        raise ValueError('missing frontmatter block')
    fields = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(':')
        if not separator or not key.strip() or key.strip() in fields:
            raise ValueError('invalid or duplicate frontmatter field')
        fields[key.strip()] = value.strip()
    return fields, match[2]


def validate(root=ROOT):
    errors = []
    skills = sorted((root / '.agents/skills').glob('*/SKILL.md'))
    for file in skills:
        try:
            fields, body = split_frontmatter(file.read_text())
            name, description = (json.loads(fields[k]) for k in ('name', 'description'))
            if name != file.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
                errors.append(f'invalid skill name: {file}')
            if not isinstance(description, str) or not description or len(description) > 1024 or any(c in description for c in '<>'):
                errors.append(f'invalid skill description: {file}')
            if set(fields) != {'name', 'description'}:
                errors.append(f'unsupported skill metadata: {file}')
        except (KeyError, ValueError, TypeError):
            errors.append(f'invalid skill frontmatter: {file}')
        for source in file.parent.rglob('*.md'):
            text = source.read_text()
            references = re.findall(r'`(references/[^`\n]+\.md)`', text)
            references += re.findall(r'\]\((references/[^)\n]+\.md)\)', text)
            for ref in references:
                if not any(c in ref for c in '[<*') and not (file.parent / ref).is_file():
                    errors.append(f'missing skill reference: {source}: {ref}')

    roles = sorted((root / '.codex/agents').glob('*.toml'))
    briefs = {file.stem for file in (root / '.codex/roles').glob('*.md')}
    if {file.stem for file in roles} != briefs:
        errors.append('native role and brief inventories differ')
    for file in roles:
        try:
            role = tomllib.loads(file.read_text())
            if set(role) != {'name', 'description', 'developer_instructions'}:
                errors.append(f'unexpected role settings: {file}')
            if role['name'] != file.stem or not role['description'] or not role['developer_instructions']:
                errors.append(f'invalid custom role: {file}')
            if role['developer_instructions'] != role_instructions(root, file.stem):
                errors.append(f'role instructions differ from maintained brief: {file}')
        except (tomllib.TOMLDecodeError, KeyError, OSError) as exc:
            errors.append(f'invalid role TOML: {file}: {exc}')

    for file in sorted((root / '.codex/scripts').glob('*.sh')):
        result = subprocess.run(['bash', '-n', str(file)], capture_output=True, text=True)
        if result.returncode:
            errors.append(f'shell parse error: {file}: {result.stderr.strip()}')

    catalog = root / 'tests/skills/catalog.yaml'
    if not catalog.is_file():
        errors.append('missing behavioral evaluation catalog')
    else:
        entries = re.findall(r'^\s+- name: (\S+)\n\s+spec: ([^\n]+)', catalog.read_text(), re.M)
        expected_names = {file.parent.name for file in skills} | briefs
        if {name for name, _ in entries} != expected_names or len(entries) != len(skills) + len(roles):
            errors.append('behavioral catalog inventory does not match skills and roles')
        for name, path in entries:
            if not (root / path.strip()).is_file():
                errors.append(f'missing behavioral spec: {name}: {path}')
    if (len(skills), len(roles)) != (74, 49):
        errors.append(f'inventory mismatch: skills={len(skills)}/74, roles={len(roles)}/49')
    return errors, len(skills), len(roles)


if __name__ == '__main__':
    errors, skills, roles = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        raise SystemExit(1)
    print(f'PASS: {skills} skills, {roles} native roles, references, behavioral catalog and Bash syntax')
