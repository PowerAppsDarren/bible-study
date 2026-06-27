---
name: _bible_dual_home_guard
description: Keep this repo's bible skills AND agents byte-identical between the repo `.claude/` and the global `~/.claude/`, enforcing the dual-home rule in CLAUDE.md. Use when the user says "sync the bible skills", "check the dual-home", "are the bible skills in sync", "mirror skills to global", "install the bible sync hook", "the bible skills drifted", or after adding/editing any bible skill or agent. Runs automatically on every `git commit` via the repo pre-commit hook (`.githooks/pre-commit`), mirroring the repo copy (canonical) out to `~/.claude/`. Project-only — do not surface outside this repo.
---

# _bible_dual_home_guard

Enforces the repo rule (see `CLAUDE.md` → "Bible study is global"): every bible
skill and agent must live **identically** in BOTH the repo's `.claude/` and the
user's global `~/.claude/`, so the whole bible battery fires in every Claude Code
session — not only inside this repo.

## What it mirrors

Source of truth = **this repo** (the version you are committing is canonical):

| Source (repo)                       | Destination (global)              |
|-------------------------------------|-----------------------------------|
| `.claude/skills/<skill dir>/`       | `~/.claude/skills/<skill dir>/`   |
| `.claude/agents/<agent>.md`         | `~/.claude/agents/<agent>.md`     |

Deliberately **excluded**: the `_bible_dual_home_guard` skill itself (project-only),
and `.claude/agents/README.md` (a generic index that could collide with an
unrelated global file). Edit those exclusions at the top of `guard.py`.

## How it runs

- **Automatically on `git commit`** — the repo configures `core.hooksPath` to
  `.githooks/`, and `.githooks/pre-commit` runs `guard.py`. It mirrors repo →
  `~/.claude/`, prints a one-line-per-item summary, and **never blocks the commit**
  (a sync hiccup must not stop you committing).
- **On demand** — run the script directly:
  - Sync now:   `python .claude/skills/_bible_dual_home_guard/guard.py`
  - Audit only: `python .claude/skills/_bible_dual_home_guard/guard.py --check`
    (writes nothing; exits non-zero and lists drift if the two homes differ).

## First-time install on a new machine

The hook travels with the repo, but `core.hooksPath` is local git config, so on a
fresh clone run once:

```sh
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit   # no-op on Windows; needed on WSL/macOS/Linux
```

After that, every commit keeps `~/.claude/` in sync automatically.

## Direction & safety notes

- The mirror is **one-way on commit: repo → global.** Committing a bible skill
  means that repo version becomes canonical and overwrites the global copy.
- For skill **directories** the destination is removed and recopied, so the global
  copy is an exact mirror (no stale leftover files). Agent files are copied in place.
- To catch the reverse case (someone edited the *global* copy and forgot the repo),
  run `guard.py --check` — it reports any difference in either direction before you
  decide which way to sync.
- Pure-Python + `Path.home()`; works on Windows, WSL, macOS, and Linux.
