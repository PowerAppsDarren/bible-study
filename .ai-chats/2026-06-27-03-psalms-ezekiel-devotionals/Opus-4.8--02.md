# Exchange 02: Psalms 1–10 (shared) + skills-sync question + dual-home guard

- **Timestamp:** 2026-06-27
- **Context:** Darren asks for Psalms 1–10 as pages in the shared scripture folders; mid-build he interjects a question about keeping skills updated and in sync.

## User Input

> Yes, the first 10 chapters of psalms. but put those files in the appropriate place, not in my personal stuff. if it has to deal with me or is specific to me, then yes, put it in my personal folder. here: c:\Users\DarrenNeese\src\bible-study\scripture\19-Psalms\Psalms-001, c:\Users\DarrenNeese\src\bible-study\scripture\19-Psalms\Psalms-002, etc

Interrupt (while working):

> all of our skills are global and local to this repo, right? i feel like we need a skill to keep them updated (auto-improving) and in sync

## AI Response

Decided placement: `devotional.html` in each **shared** chapter folder, voice adapted to clear the
six-point gate (footer → `bible-study`, no first-person confession), BBE primary. Read the Isaiah 11
reference for the quality bar; confirmed each Psalms folder already had `BBE/WEB/KJV/ASV.md` + README.
Built Psalm 1 via a `devotional-designer` agent, spot-checked the footer/shared-voice, then fanned out
Psalms 2–10 with parallel agents (briefed with per-psalm hooks: 1+2 twin gateway, 3/4/5 day-cycle, 6
penitential, 9+10 one acrostic).

For the skills question: corrected the premise — only the **bible battery** is dual-homed by design;
sync/update skills (`_skills_sync`, `_skills_update_all`, `_claude_config_propagate`) already exist.
Identified the real gap as **automation + a bible-specific two-way mirror guard**, and asked two
scoping questions.

## Tool Calls
- Read (Isaiah 11 reference), Glob (Psalms folders), AskUserQuestion (scope + trigger), Agent ×10
  (`devotional-designer` for Psalms 1–10), Grep/Bash (verify footers, no `.personal`).

## Function Results
- AskUserQuestion → **Scope: "Just the Bible dual-home guard"; Trigger: "On git commit (hook)"**.
- All 10 agents returned on-spec pages (BBE-primary, gate-clean, correct footers). [tool transcripts elided]

## Files Read/Modified
- Created `scripture/19-Psalms/Psalms-001..010/devotional.html`.
- Created `.claude/skills/_bible_dual_home_guard/{SKILL.md,guard.py}` + `.githooks/pre-commit`;
  set `core.hooksPath=.githooks`; guard run mirrored `TEACHERS.md` → `~/.claude/`.
