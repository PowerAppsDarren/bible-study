# Exchange 17: Where do my personal-folder edits get checked into?
- **Timestamp:** 2026-06-27
- **Context:** After discovering commit 4615c17 un-tracked `.personal/`; user wants to know where personal edits now go. (Awaiting the D/E/F policy decision.)

## User Input
ok, when i make edits to my personal folders, where does that get checked into?

## AI Response
Answered plainly: **right now, nowhere.** With the new `.personal/.gitignore` (`/*/` + `!_template/`), `.personal/darren@neese.us/` is **ignored by git** — edits are not staged/committed/pushed; they live only on local disk (no version history, no backup). Checked `.personal/darren@neese.us/` for a nested `.git` → **none**, so it isn't its own repo yet either. Explained the **intended design** (documented in `.personal/setup.sh` + `.personal/README.md`): each person's folder is meant to be **its own separate, private git repo** pushed to **their own** git (Forgejo / private GitHub / NAS); the public repo ships only the `_template/` starter, never anyone's folder or email. Flagged the gap: the final setup step was never run for the existing folder, and the root `.gitignore`/CLAUDE.md "intentionally tracked" wording is now stale and contradicts this model. Offered to (1) init the personal folder as its own private repo (with/without a remote) and (2) reconcile the stale docs.

## Tool Calls
- Bash: check for nested `.git`; read `.personal/setup.sh` + `.personal/README.md`

## Files Read/Modified
- Read `.personal/setup.sh`, `.personal/README.md`, root `.gitignore`, `.personal/.gitignore` (no writes)
