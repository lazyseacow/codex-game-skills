"""Runtime regressions; no API login or engine required."""
import shutil
import contextlib
import io
import tomllib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from validate_codex import validate
from sync_roles import synchronize


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="codex-studio-test-")
        self.root = Path(self.temp.name)
        (self.root / "project.yaml").write_text("schema_version: 1\n")
        for folder in ["scripts"]:
            shutil.copytree(ROOT / ".codex" / folder, self.root / ".codex" / folder)
        (self.root / ".codex/docs").mkdir()
        shutil.copy(ROOT / ".codex/docs/workflow-catalog.yaml", self.root / ".codex/docs")

    def tearDown(self):
        self.temp.cleanup()

    def run_script(self, path, *args, cwd=None):
        result = subprocess.run(["bash", str(self.root / path), *args], cwd=cwd or self.root,
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def resolve(self, cwd=None):
        return self.run_script(".codex/scripts/yaml-helper.sh", "resolve_config", cwd=cwd)

    def test_inventory_and_executable_integrity(self):
        errors, skills, roles = validate(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual((skills, roles), (74, 49))

    def test_config_subdirectory_anchor(self):
        (self.root / "project.yaml").write_text("modes:\n  rigor: full\n")
        child = self.root / "src/gameplay"
        child.mkdir(parents=True)
        output = self.resolve(child)
        self.assertIn("workflow: full (rigor:full)", output)
        self.assertIn("qa.level: full (rigor:full)", output)

    def test_nested_project_uses_own_config(self):
        (self.root / "project.yaml").write_text("modes:\n  rigor: full\n")
        child = self.root / "nested"
        child.mkdir()
        (child / "project.yaml").write_text("modes:\n  rigor: minimal\n")
        self.assertIn("workflow: minimal (rigor:minimal)", self.resolve(child))

    def test_personal_override_and_rigor_precedence(self):
        (self.root / "project.yaml").write_text("modes:\n  rigor: full\n  workflow: standard\n  automation: collaborative\n")
        (self.root / "project.local.yaml").write_text("modes:\n  automation: guided\n  workflow: minimal\n")
        output = self.resolve()
        self.assertIn("automation: guided (project.local.yaml)", output)
        self.assertIn("workflow: standard (project.yaml)", output)
        self.assertIn("qa.level: full (rigor:full)", output)
        self.assertIn("not locally overridable", output)

    def test_bad_enum_reports_and_falls_back(self):
        (self.root / "project.yaml").write_text("modes:\n  rigor: invalid-tier\n")
        output = self.resolve()
        self.assertIn("workflow: minimal (rigor:minimal)", output)
        self.assertIn("invalid-tier", output)

    def test_orphan_local_config_does_not_inherit_parent(self):
        child = self.root / "orphan"
        child.mkdir()
        (child / "project.local.yaml").write_text("modes:\n  automation: guided\n")
        self.assertIn("project.yaml is missing", self.resolve(child))

    def test_story_order_and_done_word_boundary(self):
        directory = self.root / "production/epics/epic-001"
        directory.mkdir(parents=True)
        for name, status in [("01", "Ready"), ("02", "In Progress"), ("03", "In Review"),
                             ("04", "Done."), ("05", "Not Done"), ("06", "Completed")]:
            (directory / f"story-{name}.md").write_text(f"# Story\n> **Status**: {status}\n")
        child = self.root / "src"
        child.mkdir()
        output = self.run_script(".codex/scripts/story-status.sh", cwd=child)
        rows = output.splitlines()
        for row, expected in zip(rows, ["IN_REVIEW", "IN_PROGRESS", "TODO"]):
            self.assertTrue(row.startswith(expected), row)
        self.assertIn("COMPLETE     1 of 6", output)

    def test_artifact_checker_observes_real_game_brief(self):
        missing = self.run_script(".codex/scripts/artifact-check.sh", "--path", "minimal")
        self.assertRegex(missing, r"STEP: game-brief .*status=ABSENT")
        (self.root / "design").mkdir()
        (self.root / "design/game-brief.md").write_text("# Game brief\nMove, dodge, survive.\n")
        present = self.run_script(".codex/scripts/artifact-check.sh", "--path", "minimal")
        self.assertRegex(present, r"STEP: game-brief .*status=PRESENT")

    def copy_collection(self):
        shutil.copytree(ROOT / ".agents", self.root / ".agents")
        for folder in ["roles", "agents"]:
            shutil.copytree(ROOT / ".codex" / folder, self.root / ".codex" / folder)
        shutil.copy(ROOT / ".codex/docs/codex-runtime.md", self.root / ".codex/docs")
        shutil.copytree(ROOT / "tests/skills", self.root / "tests/skills")

    def test_missing_phase_reference_is_reported(self):
        self.copy_collection()
        reference = self.root / ".agents/skills/setup-engine/references/4-project-stack.md"
        reference.unlink()
        errors, _, _ = validate(self.root)
        self.assertTrue(any("missing skill reference" in error for error in errors), errors)

    def test_native_role_drift_is_reported(self):
        self.copy_collection()
        role = self.root / ".codex/roles/prototyper.md"
        role.write_text(role.read_text() + "\nProject-specific role update\n")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("role instructions differ" in error for error in errors), errors)

    def test_role_update_sync_preserves_description_and_detects_drift(self):
        self.copy_collection()
        config = self.root / ".codex/agents/prototyper.toml"
        before = tomllib.loads(config.read_text())
        brief = self.root / ".codex/roles/prototyper.md"
        brief.write_text(brief.read_text() + "\nFocus on the selected game mechanic.\n")
        with self.assertRaisesRegex(SystemExit, "need synchronization"):
            synchronize(self.root, check=True)
        with contextlib.redirect_stdout(io.StringIO()):
            synchronize(self.root)
            synchronize(self.root, check=True)
        after = tomllib.loads(config.read_text())
        self.assertEqual(after["description"], before["description"])
        self.assertIn("Focus on the selected game mechanic.", after["developer_instructions"])
        self.assertEqual(validate(self.root)[0], [])


if __name__ == "__main__":
    unittest.main()
