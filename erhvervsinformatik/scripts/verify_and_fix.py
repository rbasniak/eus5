"""Loop audit + fix until all bilingual spans are translated."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
MAX_ROUNDS = 8


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=SCRIPTS,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**dict(**__import__("os").environ), "PYTHONIOENCODING": "utf-8"},
    )


def audit_issue_count() -> int:
    result = run([sys.executable, "audit_translations.py"])
    print(result.stdout, end="")
    if result.returncode != 0 and result.stderr:
        print(result.stderr, file=sys.stderr)
    for line in result.stdout.splitlines():
        if line.startswith("Issues found:"):
            return int(line.split(":", 1)[1].strip())
    return -1


def main() -> int:
    for round_index in range(1, MAX_ROUNDS + 1):
        issues = audit_issue_count()
        if issues == 0:
            print("All chapters fully translated.")
            return 0
        if issues < 0:
            print("Could not parse audit output.", file=sys.stderr)
            return 1
        print(f"Round {round_index}: fixing {issues} untranslated strings...", flush=True)
        fix = run([sys.executable, "fix_untranslated.py"])
        print(fix.stdout, end="")
        if fix.stderr:
            print(fix.stderr, file=sys.stderr)
        if fix.returncode != 0:
            return fix.returncode

    remaining = audit_issue_count()
    if remaining == 0:
        print("All chapters fully translated.")
        return 0
    print(f"Stopped after {MAX_ROUNDS} rounds; {remaining} issues remain.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
