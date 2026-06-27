# Exchange 07: GitDoc race discovered, scrub halted

- **Timestamp:** 2026-06-27
- **Context:** Mid-commit, staged work vanished and HEAD had moved on its own.

## User Input
(no user message — autonomous diagnosis after `git status` showed my staged `.personal/` work gone, the session-start `M .ai-chats/INDEX.md` gone, and new untracked files appearing)

## AI Response
Halted all destructive plans. Diagnosed via `git reflog`/`git log`: a new commit `4615c17` "Session 2026-06-27 (cont.) - log GitDoc explanation + uninstall" had appeared on top of `dfe4c96`. Identified **GitDoc** (VS Code auto-commit+push) as the cause — it captured my kit + the 16-file folder removal and pushed them; `origin/main` moved to `4615c17`. My `CLAUDE.md`/`CONTRIBUTING.md` edits were NOT in it (still staged). Established the core risk: force-pushing a scrubbed history while GitDoc holds the old history would resurrect the emails. Confirmed GitDoc looks stopped (HEAD stable, stale 0-byte `index.lock`) but could not prove it off (no `code` CLI). Paused and asked Darren to confirm GitDoc fully off before the scrub. Backup bundle safe throughout.

## Tool Calls
- Bash: `git status`, `git log`, `git reflog`, inspect `4615c17` diff, `git rev-parse origin/main`, check `index.lock`, grep `.vscode/settings.json` for gitdoc
- Appended a durable journal lesson about auto-committers

## Files Read/Modified
- (read-only diagnosis) + `~/.claude/docs/self-improvement-journal.md`
