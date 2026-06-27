# Exchange 04: Cross-link chapter mentions to READMEs

- **Timestamp:** 2026-06-27
- **Context:** Pages built; Darren wants every Bible-chapter mention inside the HTML to link to that chapter's repo README, and the convention remembered.

## User Input

love it, but inside the html file, whenever other chapters of the bible are mentioned, it should link over to the readme file in this repo for that chapter! please remembrer this and update your skills and memories. make it so

## AI Response

Chose a **mechanical post-processor** over per-file edits. Confirmed the 66 on-disk book folders and
that sample targets exist, then wrote `link_chapters.py` in the `_branch_devotional_design` skill:
maps book aliases (incl. singular "Psalm", numbered books, Song-of-Solomon variants) → folder, links
`Book Chapter` to `../../<NN-Book>/<Book>-<CC>/README.md` (Psalms 3-digit pad else 2), leaves trailing
`:verse` plain, **only links when the target README exists** (never broken), and skips chrome/CSS/
already-linked text. Ran it on all 11 pages → **424 links, 0 skipped**. Spot-checked links, hero/footer
untouched, idempotent (+0 on re-run). Documented the rule in the skill + agent, saved a project memory
(`bible-devotional-chapter-crosslinks`) and indexed it, and synced the updated skill+agent to
`~/.claude/` via the guard.

## Tool Calls
- Bash (list 66 folders, verify targets), Write (`link_chapters.py`), Bash (run linker + spot-check +
  idempotency), Read/Edit (`SKILL.md`, `devotional-designer.md`), Write/Edit (memory + MEMORY.md),
  Bash (guard sync).

## Function Results
- Linker: `+40/+36/+33/+34/+43/+30/+39/+39/+48/+48/+34` links (total 424), 0 skipped; re-run +0.

## Files Read/Modified
- Created `.claude/skills/_branch_devotional_design/link_chapters.py`; edited that skill's `SKILL.md`
  and `.claude/agents/devotional-designer.md`; created memory `bible-devotional-chapter-crosslinks.md`
  + updated `MEMORY.md`; modified all 11 `devotional.html` (links inserted).
