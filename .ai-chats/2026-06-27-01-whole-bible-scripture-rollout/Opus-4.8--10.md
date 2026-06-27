# Exchange 10: Digging into Greek/Hebrew; cost model; Tier 3 drawbacks; go with recommendation
- **Timestamp:** 2026-06-27
- **Context:** Planning the word-study capability and its cost.

## User Input
1. "how can we dig into the greek and hebrew for word studies?"
2. "what is the cheapest, yet effective model for doing this? or should we use /_new_ai_app? I dont want to blow through all of our ai credits... or is this based on scripts running?"
3. "what are the drawbacks to doing the 3rd level?" (full per-verse interlinear)
4. "let's go with your recommendation"

## AI Response
Explained **Strong's numbers as the bridge**; verified getbible gives original **text** (Hebrew codex/aleppo, Greek lxx/TR/WH/Tischendorf) but **NOT Strong's tags** (`kjva` returns plain KJV) — tags come from OpenScriptures/STEPBible. Laid out tiers 0–3 and recommended **Tier 2 (`words/` engine)**. On cost: the bulk work is **scripts + free data ≈ $0 AI**; tokens only for written prose (Sonnet workhorse, Haiku trivial, Opus featured); `/_new_ai_app` is the wrong tool. Detailed **Tier 3 drawbacks** (markdown can't stack; RTL Hebrew; clutters BBE pages; repo bloat across 31,102 verses; ~14k dead-link stubs; invites over-reading; high cost/low value) → recommended **on-demand interlinear** instead. User approved. Then built the **BBE-primary README front page** generator and rolled it to all 150 Psalms (commit `068136b`).

## Tool Calls
- Bash/curl: verify Hebrew/Greek + kjva tag absence (UTF-8 file to dodge cp1252)
- Write/Edit: rewrite build_readme_index.py (front page); Bash build + commit 068136b

## Files Read/Modified
- Rewrote scripts/build_readme_index.py; rebuilt 150 Psalms READMEs; commit 068136b
