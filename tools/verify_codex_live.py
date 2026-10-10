#!/usr/bin/env python3
"""Opt-in live Codex workflow check, using the user's current login/model.

Creates an isolated skill collection and asks Codex to build a browser game prototype.
This invokes a real model and may consume account usage. It never publishes.
The generated game still needs independent browser validation.
"""
import argparse
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT = """Use $prototype --spike to implement a minimal self-contained HTML
dodging game that answers this question: can a player move horizontally, avoid
falling obstacles, survive a collision and restart the same loop? Choose the HTML
route. No engine, external assets, network resources, libraries or build system.
Use arrows and A/D for movement, R for restart, responsive canvas, survival timer,
and a clear collision state. Keep it an unpolished mechanic experiment.

All local implementation and validation edits in this isolated workspace are
authorized. No unresolved design choices require user input. Run the real config
resolver and follow the Codex runtime contract and prototype references. Perform
role steps sequentially; do not spawn other agents or invoke other chats. No human
fun/playtest feedback exists: report it as NOT ASSESSED, not a creative PASS.

Write prototypes/dodge-concept/prototype.html. Also expose a small deterministic
test API as window.__studioProbe with snapshot(), reset(), step(seconds),
setInput(left, right), and addObstacle(x, y); snapshot returns player {x, y,
width, height}, obstacles, alive and elapsed. Use the SAME simulation for the
test API and the canvas game. Keep test-only methods off the player-facing UI.
Use delta time and avoid leaps/tunneling on long frames. Add tests/game.mjs that
executes the actual HTML script with a lightweight DOM/canvas stub in Node and
asserts movement, bounds, obstacle falling, collision, restart and time-step
consistency. Run it and fix failures. Write a factual short prototype report
and production/session-state/active.md checkpoint. Do not commit or publish.
Finish with artifact paths, real test outcomes and manual-playtest limitations.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True, help="new or empty directory")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    target = args.workspace.resolve()
    if target.exists() and any(target.iterdir()):
        parser.error("workspace must be new or empty; existing files will not be overwritten")
    target.mkdir(parents=True, exist_ok=True)
    for name in [".agents", ".codex", "docs", "design"]:
        shutil.copytree(ROOT / name, target / name)
    for name in ["AGENTS.md", "project.yaml"]:
        shutil.copy(ROOT / name, target / name)
    (target / "project.local.yaml").write_text("modes:\n  automation: guided\n")
    command = ["codex", "exec", "--ephemeral", "--strict-config", "--json",
               "--skip-git-repo-check", "-s", "workspace-write", "-C", str(target),
               "-o", str(target / "final.md"), PROMPT]
    print(f"Live Codex check workspace: {target}", flush=True)
    with (target / "events.jsonl").open("w") as out, (target / "stderr.txt").open("w") as err:
        try:
            result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                    timeout=args.timeout)
        except subprocess.TimeoutExpired:
            raise SystemExit("Codex timed out; preserved all evidence in the workspace")
    if result.returncode:
        raise SystemExit(f"Codex failed ({result.returncode}); inspect stderr.txt and events.jsonl")
    artifacts = ["prototypes/dodge-concept/prototype.html", "tests/game.mjs",
                 "production/session-state/active.md"]
    missing = [name for name in artifacts if not (target / name).is_file()]
    if missing:
        raise SystemExit("Codex returned without required artifacts: " + ", ".join(missing))
    events = [json.loads(line) for line in (target / "events.jsonl").read_text().splitlines() if line]
    commands = [event.get("item", {}).get("command", "") for event in events]
    if not any("yaml-helper.sh" in cmd and "resolve_config" in cmd for cmd in commands):
        raise SystemExit("No evidence Codex actually executed the config resolver")
    result = subprocess.run(["node", "tests/game.mjs"], cwd=target, capture_output=True, text=True, timeout=30)
    (target / "independent-node-check.txt").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise SystemExit("Independent rerun of the generated game tests failed")
    print("PASS: skill workflow produced a game, executed config, wrote a checkpoint; Node checks rerun")
    print("Browser interaction and manual fun assessment remain separate checks")


if __name__ == "__main__":
    main()
