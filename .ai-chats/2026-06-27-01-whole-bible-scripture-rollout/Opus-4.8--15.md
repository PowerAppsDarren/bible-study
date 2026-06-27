# Exchange 15: Uninstall GitDoc
- **Timestamp:** 2026-06-27
- **Context:** User chose option A (uninstall).

## User Input
D:A;

## AI Response
Uninstalled GitDoc via the VS Code CLI: `code --uninstall-extension vsls-contrib.gitdoc` → "successfully uninstalled"; confirmed it's gone from `--list-extensions`. Noted that since VS Code is still running, the already-loaded copy stays in memory until a one-time **"Developer: Reload Window"** (or close/reopen); after that it's fully gone. Left the now-orphan `gitdoc.enabled:false` setting as a harmless no-op.

## Tool Calls
- PowerShell: `code --uninstall-extension vsls-contrib.gitdoc`; `code --list-extensions | Select-String gitdoc` (verify absent)

## Files Read/Modified
- VS Code extension removed (no repo files changed)
