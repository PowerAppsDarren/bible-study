# AI Chat Session: `.personal/` → per-user private repos

- **Date:** 2026-06-27
- **Model:** Claude Opus 4.8 (1M context)
- **Topic:** Convert `.personal/<email>/` from in-repo tracked folders into per-user private repos; keep personal notes + email addresses off the public GitHub repo
- **Tool:** Claude Code
- **Project:** bible-study
- **Exchange Count:** 8

## 💡 Conversation Summary

Darren wanted each email-named folder under `.personal/` to be its **own separate repo** — one per person. Through the conversation the requirements sharpened:

1. Each person's `.personal/<email>/` = their own repo.
2. Private content must live in a repo, **but not on github.com** — Darren keeps his on his own private Forgejo.
3. The public repo must still **encourage adoption** (newcomers integrating it into daily Bible study).
4. **No email addresses** should appear on GitHub either.

**Design chosen — "one public scaffold, many private journals":** the public GitHub repo ships a *kit* (instructions + a generator), never a real person's folder. Each person's space is generated locally as its own private repo (Darren's → Forgejo), and the public repo is told to ignore every email-named subfolder.

**Built (the kit):**
- `.personal/.gitignore` — `/*/` ignores every email folder, `!_template/` keeps the starter visible.
- `.personal/setup.sh` — one-command, cross-platform generator (asks email → copies `_template/` → `git init` → optional remote).
- `.personal/_template/` — skeleton (README, profile.md, reading-plan.md, prayer/, scripture/, journal/) with no email/PII.
- `.personal/README.md` — rewritten to teach the new model.
- root `.gitattributes` — `*.sh text eol=lf` so the script runs on Linux/Mac/WSL.
- `darren@neese.us/` untracked from the public repo (16 files preserved on disk).
- `CLAUDE.md` + `CONTRIBUTING.md` — rewritten to the new two-layer model (staged this session).

**Key event / hazard:** A VS Code **GitDoc** extension was auto-committing AND auto-pushing in the background. It swept up the staged kit + folder-removal and pushed them as commit `4615c17`, moving HEAD/`origin/main` out from under the operation. The work landed on GitHub — but not deliberately. The planned **history scrub + force-push was halted**: force-pushing a scrubbed history while a live GitDoc holds the old history would let GitDoc re-push the old commits and **resurrect the very emails being scrubbed**. Scrub deferred pending an explicit "GitDoc is fully off" confirmation.

**Outcome:** Going-forward privacy is achieved (public repo now tracks only the kit; no new emails/notes). The past-history scrub and the Forgejo private-repo creation remain queued.

## 🔧 Technical Details

Files created:
- `.personal/.gitignore`, `.personal/setup.sh`, `.gitattributes`
- `.personal/_template/{README.md, profile.md, reading-plan.md, prayer/prayer-list.md, scripture/README.md, journal/.gitkeep}`

Files modified:
- `.personal/README.md` (rewritten)
- `CLAUDE.md` (two-layer model section, layout comment, "things to avoid")
- `CONTRIBUTING.md` (two-layer table, Getting Started, Personal Notes, backups)

Git facts:
- Backup point / pre-op `origin/main`: `dfe4c96`
- GitDoc auto-commit that captured the kit + folder removal: `4615c17` (now HEAD and `origin/main`)
- Email folder appeared in ~10 historical commits (still present in history → scrub target)
- Full verified backup bundle: `…/scratchpad/bible-study-FULL-backup.bundle` (26 MB, complete history)

Ignore-rule verification: `/*/` matched a test path; `_template/` confirmed visible; staged `.personal/` paths grep-clean of `@`.

Tooling: `git filter-repo` NOT installed (Python 3.12.10 present → install when scrub runs). `core.hooksPath=.githooks` (bible dual-home guard pre-commit — mirror-only, never blocks).

## 📚 Lessons Learned

- **Auto-committers are a live hazard for deliberate git work.** GitDoc auto-commit+push raced the operation and moved HEAD. Before any history rewrite/force-push, detect background writers (`git reflog`, watch `origin/main`), and NEVER force-push a scrubbed history while an auto-pusher holds the old history — it will resurrect the scrubbed data.
- **Stale `index.lock`** (0 bytes, unchanged for 30+ min with no HEAD movement) = safe to clear; an active git op holds it for seconds and writes content.
- **Removing a folder from tracking ≠ removing it from history.** `git rm --cached` + `.gitignore` stops future tracking; past commits (and the email in their paths) persist until a history rewrite.
- A repo can serve **public-adoption** and **private-journaling** at once by shipping a *kit*, not a *container*.

## ⏭️ Next Steps

1. **Confirm GitDoc fully off** (whole VS Code), then: clear stale lock → install `git filter-repo` → scrub `.personal/<email>/` from all history → force-push `main`.
2. **Create the private Forgejo repo** `git.spl.tech/darren/bible-study-personal`, `git init` the on-disk `darren@neese.us/`, add remote, push.
3. Note GitHub retains orphaned old commits (reachable by SHA) until GC — may need a fresh repo or GitHub support for a hard purge.

## 📁 Exchange Index
- [01 — make email folders separate repos](./Opus-4.8--01.md)
- [02 — clarify the questions first](./Opus-4.8--02.md)
- [03 — private Forgejo, not GitHub](./Opus-4.8--03.md)
- [04 — also encourage adoption; design it](./Opus-4.8--04.md)
- [05 — no emails on GitHub either](./Opus-4.8--05.md)
- [06 — approvals A/B/C/D yes](./Opus-4.8--06.md)
- [07 — GitDoc race discovered, scrub halted](./Opus-4.8--07.md)
- [08 — wrap-up](./Opus-4.8--08.md)
