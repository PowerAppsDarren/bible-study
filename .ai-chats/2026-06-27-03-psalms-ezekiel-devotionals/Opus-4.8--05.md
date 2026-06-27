# Exchange 05: No self-links + table of contents

- **Timestamp:** 2026-06-27
- **Context:** After cross-linking, Darren notices pages link to their own chapter and asks for a table of contents.

## User Input

yeah, dont link to the same file within the file. that would be weird. we do need a table of contents in these amazing html files.

## AI Response

Did both as idempotent scripts. Hardened `link_chapters.py` to **strip existing self-links and never
create them** (computes the page's own README href from its path; pre-pass unwraps, repl skips). Wrote
**`add_toc.py`**: gives each titled `<section>` a stable slug `id` and injects a styled
`<nav class="toc">` ("In This Study" — number · emoji · title → in-page anchor) at the top of `.wrap`,
themed from the page's CSS variables, idempotent via fence markers. Ran TOC then linker on all 11:
TOC with 8–11 entries each; **15–30 self-links removed per page, 0 remaining**; external links intact
(9–20/page); section ids ↔ TOC anchors 1:1; fully idempotent on re-run. Documented both as the skill's
mandatory "Finalize" step, updated the agent + memory, and synced to `~/.claude/`.

## Tool Calls
- Write (`link_chapters.py` v2, `add_toc.py`), Bash (run both passes + verify TOC/ids/self=0/
  idempotency), Edit (`SKILL.md`, `devotional-designer.md`, memory), Bash (guard sync).

## Function Results
- add_toc: 8–11 entries/page; link_chapters: +0 links, −15..−30 self per page; re-run stable
  (1 TOC, 1 CSS block, +0 links).

## Files Read/Modified
- Created `.claude/skills/_branch_devotional_design/add_toc.py`; rewrote `link_chapters.py`; edited the
  skill `SKILL.md`, `devotional-designer.md`, and the crosslinks memory; modified all 11
  `devotional.html` (TOC added, self-links removed).
