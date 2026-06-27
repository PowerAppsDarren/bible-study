# Exchange 05: no emails on GitHub either

- **Timestamp:** 2026-06-27
- **Context:** Darren added the no-PII constraint, sharpening the design to a "kit, not a container."

## User Input
also, i dont really want anyone's email addresses out on github, so, .personal should have good files in there that explain how it all works and will generate their own personal space, but not create and thereby exposing their personal stuff out there to the world

## AI Response
Adopted "kit, not container": the public repo ships instructions + a generator that creates the person's space locally; no email folder is ever committed. Read the existing `.personal/README.md`, then BUILT the kit in the working tree (no commit/push):
- `.personal/.gitignore` (`/*/` + `!_template/`)
- `.personal/setup.sh` (cross-platform generator)
- `.personal/_template/` skeleton files
- rewrote `.personal/README.md`
- `git rm -r --cached .personal/darren@neese.us` (after clearing a stale index.lock)
- added root `.gitattributes` (`*.sh` → LF)
Verified: ignore rule matches real email folders, `_template/` visible, staged `.personal/` paths grep-clean of `@`, 16 files safe on disk.

## Tool Calls
- Read `.personal/README.md`
- Write: `.gitignore`, `setup.sh`, `_template/*`, rewrite `README.md`, root `.gitattributes`
- Bash: `git rm --cached`, `git check-ignore`, verification greps

## Files Read/Modified
- Created kit files; untracked `darren@neese.us/`; all verified
