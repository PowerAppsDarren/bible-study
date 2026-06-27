# Exchange 07: Rate-limit risk? → bulk mode; brainstorm README structure + HTML demo
- **Timestamp:** 2026-06-25
- **Context:** Before scaling to the whole Bible, user checks risk and wants to improve the README design.

## User Input
1. "do we run a risk of being rate limited or throttled for so much use?"
2. "ok. sure! /_recommended --- but let's brainstorm here on how to better structure our readme's? it seems now would be the best time to improve them before we do all this work, right?" (+ /effort ultracode, + /_ultra)
3. "I can't see your examples... create an html table demo'ing those 3 examples so i can see them"

## AI Response
On throttling: per-chapter whole Bible ≈ 4,756 requests (impolite to a free API), but getbible serves a **whole translation in ONE ~8.8 MB request** → whole Bible = ~4 requests. Recommended **bulk mode**. On the README: identified it was doing two jobs (one conflicting with the shared/personal rule) and proposed a front-page redesign; right-sized to **do it directly, not via an agent team** despite ultracode. Built an **HTML demo** comparing 3 verse-list layouts (readable table / readable prose / link grid) + study-note split + scaffolding extras, with real Psalm 1 text; sent it via SendUserFile.

*(Full HTML demo elided — see `.personal/darren@neese.us/readme-options-demo.html`.)*

## Tool Calls
- Bash/curl: verify getbible whole-book/whole-translation endpoints + sizes
- Write + SendUserFile: readme-options-demo.html

## Files Read/Modified
- Created scratchpad readme-options-demo.html (later copied to personal layer)
