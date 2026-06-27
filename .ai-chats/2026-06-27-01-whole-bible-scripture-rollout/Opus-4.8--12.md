# Exchange 12: Do A then B then C (GitDoc / word-study engine / whole Bible)
- **Timestamp:** 2026-06-27
- **Context:** Three pending items, executed in order.

## User Input
1. "." (re-orient)
2. "do A, then B, then C" — A: track down the auto-committer; B: word-study engine; C: whole-Bible rollout

## AI Response
**A — auto-committer:** ruled out hooks/scheduled-tasks/live-processes; found the **GitDoc** extension (`vsls-contrib.gitdoc`) — confirmed via its global `state.vscdb` entry + exthost activation log in the rogue-commit window + AI-style messages with no Claude trailer. Disabled via `gitdoc.enabled:false` (+autoPush/autoPull off) in user settings; flagged that the live instance needs a reload/Disable to fully stop.
**B — word-study engine:** built `scripts/word_study.py` (Strong's lookup / `--find`; OpenScriptures PD lexicons auto-cached outside repo; writes `words/<lang>/<slug>.md`; won't clobber existing; UTF-8 stdout). Seeded esher/towrah/hagah. Commit `a767f2e`.
**C — whole Bible:** added `--bulk` mode to `fetch_scripture.py`; tested on Jude; fetched **all 1,189 chapters × BBE/WEB/KJV/ASV (4,756 files)**; built **1,189 front-page READMEs**. GitDoc left a stale lock twice — cleared safely. Commit `645a679`, pushed.

*(Long diagnostic outputs + 5,900-file commit warnings elided.)*

## Tool Calls
- Bash/PowerShell: git+VS Code forensics; Edit user settings (gitdoc)
- Write: scripts/word_study.py; Bash: lexicon fetch, seeds, commit a767f2e
- Edit: fetch_scripture.py (--bulk); Bash: bulk fetch --all, build --all, commit 645a679

## Files Read/Modified
- Edited VS Code user settings (gitdoc disable)
- Created scripts/word_study.py + words/hebrew/{esher,towrah,hagah}.md (a767f2e)
- Edited scripts/fetch_scripture.py (--bulk); created 4,756 version files + 1,189 READMEs (645a679)
