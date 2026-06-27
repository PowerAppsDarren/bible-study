# AI Chat Session: Psalms 1–10 + Ezekiel 1 devotional pages, dual-home guard, chapter cross-linking & TOC

- **Date:** 2026-06-27
- **Model:** Claude Opus 4.8 (1M context)
- **Topic:** Build shared-layer "Branch" devotional HTML pages for Psalms 1–10 and Ezekiel 1; add a Bible-skills dual-home git hook; auto-link chapter references to repo READMEs; add a table of contents.
- **Tool:** Claude Code
- **Project:** bible-study
- **Exchange Count:** 5 (+ wrap-up)

## 💡 Conversation Summary

Started by identifying which skill builds the devotional HTML pages (`_branch_devotional_design`,
wielded by the `devotional-designer` agent, content from `_deep_bible_study_devotional` + teacher
agents). Darren then asked for **Psalms 1–10** as pages, placed in the **shared** scripture folders
(not `.personal/`). Resolved the shared-vs-personal tension by **adapting the voice to clear the
six-point integration gate** (factual, non-sectarian, license-clean, footer → `bible-study` not
`.personal`) while keeping the full Branch design depth. Built Psalm 1 as a template, verified, then
fanned out 2–10 and later Ezekiel 1 via parallel `devotional-designer` agents.

Mid-session Darren asked whether all skills are global+local and whether a sync/auto-improve skill is
needed. Corrected the premise (only the **bible battery** is dual-homed by design; sync/update skills
already exist), and per his answers (**scope: bible dual-home guard; trigger: git commit**) built a
new project-only skill **`_bible_dual_home_guard`** + `.githooks/pre-commit` that mirrors the repo's
`.claude/` bible skills+agents to `~/.claude/`. It immediately caught and fixed real drift in
`TEACHERS.md`.

Then Darren asked that **every mention of another chapter link to that chapter's repo README**. Built
`link_chapters.py` (existence-checked, idempotent, never broken/self links) → 424 links across 11
pages, zero skipped. Finally he asked to **stop self-links** and **add a table of contents**; built
`add_toc.py` and hardened `link_chapters.py` to strip+suppress self-links. Both baked into the skill
as a mandatory "Finalize" step, documented in the agent, and saved to memory.

**Outcome:** 11 polished shared devotional pages + a dual-home guard hook + two idempotent
post-processors (TOC + chapter cross-linking), all verified, with the conventions captured in the
skill, agent, and project memory, and the bible battery synced to `~/.claude/`.

## 🔧 Technical Details

**Devotional pages (new, shared layer):**
- `scripture/19-Psalms/Psalms-001..010/devotional.html` (10)
- `scripture/26-Ezekiel/Ezekiel-01/devotional.html`
- Built by parallel `devotional-designer` agents; BBE-primary, six-point-gate-clean, footer
  `<Book Chapter> · A Deep Devotional Study · bible-study`, kicker `… of 150` / `… of 48`.

**New skill — `_bible_dual_home_guard`:**
- `.claude/skills/_bible_dual_home_guard/SKILL.md` + `guard.py` (pure-Python, `Path.home()`).
- `.githooks/pre-commit` (POSIX sh → python); `git config core.hooksPath .githooks`.
- Mirrors repo `.claude/skills/*` + `.claude/agents/*.md` → `~/.claude/` (excludes the guard skill
  itself + `agents/README.md`). `--check` audits; default mirrors. Non-blocking on commit.

**Post-processors in `_branch_devotional_design`:**
- `link_chapters.py` — links `Book Chapter[:verse]` → `../../<NN-Book>/<Book>-<CC>/README.md`
  (Psalms 3-digit pad, else 2). Existence-checked, idempotent, skips `<a>/<nav>/<header>/<title>/
  <footer>/<style>/<script>/<head>`, strips + suppresses self-links.
- `add_toc.py` — gives each `<section>` a slug `id`, injects `<nav class="toc">` ("In This Study")
  at top of `.wrap`, themed from page CSS vars; idempotent via markers.

**Docs/memory updated:**
- `.claude/skills/_branch_devotional_design/SKILL.md` (file list + Finalize step + shared/personal
  placement), `.claude/agents/devotional-designer.md` (placement + Finalize note).
- Memory: `bible-devotional-chapter-crosslinks.md` (+ MEMORY.md index) in the project memory dir;
  self-improvement journal lines.

**Verification:** 424 links / 0 broken / 0 self after fix; TOC entries ↔ section ids 1:1; re-runs
idempotent (+0 links, single TOC/CSS block).

## 📚 Lessons Learned

- When a "personal" design system is asked to output to the **shared** layer, adapt the **voice** to
  the gate rather than refusing or copying the personal template verbatim.
- For repeatable text transforms across many generated files, prefer a small **idempotent,
  existence-checked post-processor** baked into the skill over per-file agent edits — uniform,
  re-runnable, never emits broken links, enforces the convention mechanically.
- When a generator pass is too aggressive (self-links), fix at the **source script** with a
  strip+suppress pass so one re-run cleans old output and prevents recurrence.
- `devotional-designer` has no shell — the **main session** must run the finalize scripts.

## ⏭️ Next Steps

- Visual sign-off of a page in a browser.
- Separately resolve the staged `CLAUDE.md`/`CONTRIBUTING.md` `.personal` private-repo edits
  (prior-session open decision; CHANGELOG `[Unreleased]` still describes the old multi-user model).
- Continue Psalms 11+ / more chapters as desired (now born with TOC + cross-links via the scripts).

## 📁 Exchange Index
- [01 — Which skill builds the devotional HTML](./Opus-4.8--01.md)
- [02 — Psalms 1–10 (shared) + skills-sync question + dual-home guard](./Opus-4.8--02.md)
- [03 — Ezekiel 1](./Opus-4.8--03.md)
- [04 — Cross-link chapter mentions to READMEs](./Opus-4.8--04.md)
- [05 — No self-links + table of contents](./Opus-4.8--05.md)
