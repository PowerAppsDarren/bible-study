# Exchange 22: Make terminal text taller, not wider

- **Timestamp:** 2026-06-12
- **Context:** New thread — VS Code terminal typography.

## User Input

how can we make the text in this terminal (vs code terminal window) taller without making it wider?

## AI Response

That's `terminal.integrated.lineHeight` — adds vertical space per line without touching character width, so column count stays the same. (`fontSize` scales both directions; `lineHeight` is the height-only knob.) Default `1.0`; suggested `1.2`–`1.4`. Quick route: `Ctrl+,` → search "terminal line height". Or `settings.json`: `"terminal.integrated.lineHeight": 1.3`. Caveat: it spaces the *lines* apart (airier), it doesn't stretch the glyphs taller (that needs a tall/condensed font, impractical). Offered to set it in the global `settings.json` (`%APPDATA%\Code\User\settings.json`), suggesting `1.3`.

## Tool Calls

None.

## Files Read/Modified

None.
