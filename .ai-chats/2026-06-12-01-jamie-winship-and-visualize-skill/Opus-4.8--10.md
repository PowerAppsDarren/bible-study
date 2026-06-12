# Exchange 10: HTML doesn't render; fix it (def402a)

- **Timestamp:** 2026-06-12
- **Context:** User reports the HTML sheet shows no rendered Mermaid — defeats the purpose. Asks to fix it all.

## User Input

wtf! your html doesn't render the mermaid and the visuals... that completly defeates the purpose of doing this visual skill. pls fix it all

## AI Response

Found **two** real bugs (apologized; the first version was broken):

1. **Fragile loader.** The template loaded Mermaid as an **ESM module** (`<script type="module"> import from CDN`). ES-module scripts get blocked over `file://` (double-click) on locked-down machines → nothing loads, diagrams stay as raw text.
2. **Parse error in the demo.** Labels like `[Awareness: hear what is true]` had **unquoted colons** — a Mermaid parse error (violating the skill's own catalog rule).

**Fix:** switched to the classic **UMD** build via a normal `<script src>`, **vendored `mermaid.min.js` (v10.9.3, 3.18 MB) next to the HTML** so it renders fully offline, with a CDN fallback and explicit `mermaid.run()`. Quoted every punctuation label. Verified both diagrams through the Mermaid Chart MCP (`valid:true`, type flowchart) before rebuilding. Hardened both templates (repo + global) and the SKILL docs with the rules (classic UMD, vendor-first, flush-left source, quoted labels). Committed `def402a` and pushed; re-sent the fixed demo.

## Tool Calls

- `PowerShell` `Invoke-WebRequest` (download mermaid v11 then v10.9.3 UMD); inspect global exposure
- `ToolSearch` + `mcp__claude_ai_Mermaid_Chart__validate_and_render_mermaid_diagram` ×2 (both valid)
- `Bash` extract `valid` flag from saved results (json)
- `Write` demo HTML (fixed); `Write`/`Bash cp` templates (repo + global); `Edit` ×2 SKILL.md
- `Bash` git add/commit `def402a`; `git push`; `SendUserFile`

## Files Read/Modified

- **~** demo HTML; **+** vendored `mermaid.min.js`; **~** both `html-template.html`; **~** both `SKILL.md`
- Commit `def402a` pushed (4 files, +2092/−47).
