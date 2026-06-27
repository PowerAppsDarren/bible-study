#!/usr/bin/env python3
"""Bible dual-home guard.

Repo rule (see CLAUDE.md): every bible skill and agent must exist *identically*
in BOTH this repo's `.claude/` AND the user's global `~/.claude/`, so the bible
battery fires in every Claude Code session, not just inside this repo.

This script enforces that rule. On commit the repo copy is treated as canonical
and is mirrored out to `~/.claude/`, so the two homes never drift.

Source of truth (this repo):
    .claude/skills/<each skill dir>      ->  ~/.claude/skills/<same>
    .claude/agents/<each *.md agent>     ->  ~/.claude/agents/<same>

Modes:
    (default)   mirror repo -> ~/.claude, print a summary, ALWAYS exit 0
                (a sync must never block a commit)
    --check     report drift only, write nothing; exit 1 if anything differs
                (use for CI / manual audits)

Excluded on purpose:
    - the `_bible_dual_home_guard` skill itself  (project-only; never pushed global)
    - agents/README.md                            (generic index that could collide
                                                    with an unrelated global file)
Cross-platform: pure Python + Path.home(); runs on Windows, WSL, macOS, Linux.
"""
import sys
import shutil
import filecmp
import subprocess
from pathlib import Path

EXCLUDE_SKILL_DIRS = {"_bible_dual_home_guard"}
EXCLUDE_AGENT_FILES = {"README.md"}


def repo_root() -> Path:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        if out:
            return Path(out)
    except Exception:
        pass
    # Fallback: .../.claude/skills/_bible_dual_home_guard/guard.py -> repo root
    return Path(__file__).resolve().parents[3]


def dirs_identical(a: Path, b: Path) -> bool:
    """True only if every file under a exists byte-identical under b (and vice-versa)."""
    if not b.exists():
        return False
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    for sub in cmp.common_dirs:
        if not dirs_identical(a / sub, b / sub):
            return False
    return True


def main() -> int:
    check = "--check" in sys.argv
    repo = repo_root()
    src_skills = repo / ".claude" / "skills"
    src_agents = repo / ".claude" / "agents"
    home = Path.home() / ".claude"
    dst_skills = home / "skills"
    dst_agents = home / "agents"

    drift, synced = [], []

    # --- skills (each is a directory) ---
    if src_skills.is_dir():
        for d in sorted(p for p in src_skills.iterdir() if p.is_dir()):
            if d.name in EXCLUDE_SKILL_DIRS:
                continue
            dst = dst_skills / d.name
            if dirs_identical(d, dst):
                continue
            drift.append(f"skill  {d.name}")
            if not check:
                dst_skills.mkdir(parents=True, exist_ok=True)
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(d, dst)
                synced.append(f"skill  {d.name}")

    # --- agents (each is a *.md file) ---
    if src_agents.is_dir():
        for f in sorted(p for p in src_agents.iterdir()
                        if p.is_file() and p.suffix == ".md"):
            if f.name in EXCLUDE_AGENT_FILES:
                continue
            dst = dst_agents / f.name
            if dst.exists() and filecmp.cmp(f, dst, shallow=False):
                continue
            drift.append(f"agent  {f.name}")
            if not check:
                dst_agents.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dst)
                synced.append(f"agent  {f.name}")

    tag = "bible-dual-home-guard"
    if check:
        if drift:
            print(f"[{tag}] DRIFT - {len(drift)} item(s) differ between repo and ~/.claude:")
            for x in drift:
                print(f"  - {x}")
            print(f"[{tag}] run without --check (or commit) to mirror repo -> ~/.claude")
            return 1
        print(f"[{tag}] OK - repo .claude bible skills/agents already match ~/.claude")
        return 0

    if synced:
        print(f"[{tag}] mirrored {len(synced)} item(s) repo -> ~/.claude:")
        for x in synced:
            print(f"  - {x}")
    else:
        print(f"[{tag}] OK - ~/.claude already in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
