# Exchange 21: Set it up under .personal (5f71763)

- **Timestamp:** 2026-06-12
- **Context:** User confirms the personal-folder path for storing workspace.json.

## User Input

.personal\darren@neese.us

## AI Response

Set it up. Wrote `link-workspace.ps1` (tries symlink, falls back to hardlink). Moved `.obsidian/workspace.json` → `.personal/darren@neese.us/obsidian/workspace.json`. Symlink creation **failed** ("Administrator privilege required" — Developer Mode off), so used a **file hardlink** instead (no elevation needed): `.obsidian/workspace.json` and the personal copy are now one file (verified: both 5669 chars). Hardened the script to prefer symlink then fall back to hardlink. Committed `5f71763` (personal workspace.json + the link script) and pushed.

Result: layout syncs across the user's machines (tracked personal copy), no collisions (own email folder). New-machine flow: pull → run `link-workspace.ps1`. Caveats noted: link can break if Obsidian replaces-instead-of-edits (rerun script); shows as a normal modified file in the user's own commits.

## Tool Calls

- `Write` `link-workspace.ps1`
- `PowerShell` Move-Item; New-Item SymbolicLink (failed: admin); New-Item HardLink (ok) + verify
- `Edit` `link-workspace.ps1` (symlink→hardlink fallback)
- `Bash` git add personal/obsidian + commit `5f71763` + push

## Files Read/Modified

- **+** `.personal/darren@neese.us/obsidian/workspace.json`, `link-workspace.ps1`
- Hardlink: `.obsidian/workspace.json` ⇔ personal copy
- Commit `5f71763` pushed.
