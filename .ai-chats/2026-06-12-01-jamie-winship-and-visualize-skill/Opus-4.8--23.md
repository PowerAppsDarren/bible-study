# Exchange 23: Modify global VS Code settings

- **Timestamp:** 2026-06-12
- **Context:** User asks to apply the lineHeight change to global VS Code settings.

## User Input

go ahead and modify the global vs code settingsto do this

## AI Response

Read the global settings (`%APPDATA%\Code\User\settings.json`) and found `terminal.integrated.lineHeight` was **already set to 1.2** (line 57) — so this was a bump, not an add. Raised it to **1.4** for a clearly taller line without touching width. (First Edit attempt failed because the truncated read didn't register; re-read the region around line 57, then edited.) Noted `fontSize` is 18 (the both-directions knob) and `letterSpacing` is 0 (the horizontal one), offering to tweak either.

## Tool Calls

- `Read` settings.json (partial, 1126 lines) → found line 57
- `Read` settings.json offset 52 limit 12 (to satisfy Edit)
- `Edit` `terminal.integrated.lineHeight` 1.2 → 1.4

## Files Read/Modified

- **~** `C:\Users\DarrenNeese\AppData\Roaming\Code\User\settings.json` (lineHeight 1.2→1.4)
