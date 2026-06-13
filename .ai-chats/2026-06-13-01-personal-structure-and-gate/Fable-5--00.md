# AI Chat Session: Personal-layer restructure + Shared-Layer Integration Gate + docs reconciliation

- **Date:** 2026-06-13 (work spanned 2026-06-12 → 2026-06-13)
- **Model:** Fable-5 (Claude Fable 5, claude-fable-5)
- **Tool:** Claude Code
- **Project:** bible-study

## Summary

Three connected pieces of repo-structure work, each committed separately:

1. **Restructured `.personal/darren@neese.us/`** so book studies nest under a `scripture/` subfolder mirroring the repo root, instead of littering the personal root with up to 66 book folders. Two loose folders were resolved:
   - `23-Isaiah/` (chapter notes: `Isaiah-06/notes.md`, `Isaiah-10/devotional.html`) → moved to `scripture/23-Isaiah/`.
   - `Isaiah/` (non-conforming raw material) → folded into `scripture/23-Isaiah/sources/`. The audio transcript was re-encoded from broken UTF-16 (per-character spacing artifacts) to clean UTF-8 and renamed `2026-05-09-isaiah-conversation-transcript.txt`. The stub `Isaiah/README.md` was dropped; a new `sources/README.md` describes the folder.
   - Convention codified in `.personal/README.md`, `_personal_reflection`, `_compare_notes`, and project `CLAUDE.md`.

2. **Created the Shared-Layer Integration Gate** — a quality standard governing what earns a place in the shared layer, prompted by the user's concern about cluttering the non-personal area. The existing repo rule was only *category* (fact vs. thought); the gate adds a *value* test (a fact can still be clutter if it just restates the verse). Six tests: **factual / margin-worthy / durable / sourceable / non-sectarian / license-clean.** Plus the "study once, deposit twice" routing and a chapter-promotion rule ("an honest stub beats a padded margin"). Authoritative version in `CLAUDE.md`; enforced as a workflow step in `_chapter_readme_fill`; human-facing summary in `CONTRIBUTING.md`.

3. **Reconciled the published docs to the on-disk layout** (user chose disk as canonical). Standardized `books-of-bible/`→`scripture/` and `topics-of-study/`→`topics/` across README/STRUCTURE/CONTRIBUTING; finished migrating the stale single-user "`.personal/` is gitignored" language to the multi-user tracked-in-git paradigm; added a CHANGELOG `[Unreleased]` section (historical 1.2.0/1.0.0 entries left intact); rewrote CLAUDE.md's "Layout on disk vs. docs" section to "Layout on disk — canonical," removing the now-moot "ask which side is canonical" instruction.

## Technical Details

- **Commits (all on `main`, pushed at wrap-up):**
  - `7eadf4c` — refactor(personal): nest book studies under scripture/, fold raw Isaiah sources into 23-Isaiah/sources
  - `33b9472` — docs(shared-layer): add the Shared-Layer Integration Gate
  - `e091bc2` — docs: reconcile published docs to on-disk layout (scripture/, topics/)
- **UTF-16 → UTF-8 re-encode** done in PowerShell: `[System.IO.File]::ReadAllText(path, Unicode)` → `WriteAllText(path, UTF8Encoding($false))`. Verified no NUL bytes remained.
- **`git mv`** used for the as-is moves so history is preserved (renames detected as `R`). The transcript changed content (re-encode), so it was `git rm` + add.
- **Single source of truth discipline:** the gate's authoritative text lives only in `CLAUDE.md`; the skill and CONTRIBUTING.md point to it to avoid drift. Anchor links verified (`#shared-layer-integration-gate`, `#the-shared-layer-integration-gate`).

## Lessons Learned

- **Fixing a doc can make a meta-doc stale.** Reconciling README/STRUCTURE/CONTRIBUTING to disk made CLAUDE.md's "the docs say books-of-bible/, ask which is canonical" warning false — that had to be rewritten in the same pass, or future sessions would have re-litigated a resolved question.
- **Two kinds of staleness, two treatments.** Path-name and gitignored claims in *published* docs → fix. The same names in *historical* CHANGELOG entries and `.ai-chats/` logs → leave (accurate record of their moment); document current state in an `[Unreleased]` section instead.
- **Category ≠ quality.** The repo already routed fact→shared, thought→personal, but had no bar for whether a fact was worth keeping. The gate's "margin-worthy" + "don't pad to look complete" rules are what actually protect the shared layer from clutter.

## Next Steps

- **Push 3 commits to origin** (done at wrap-up).
- **Backfill `scripture/` chapter READMEs** for Isaiah 1–10 by running `_chapter_readme_fill` through the new gate, using existing notes/devotionals as source. Not started — deferred by design.
- **Dedup planning docs** — `repo-planning.md`, `docs/top-level-folders.md`, and `____bible-study-top-level-folders.md` overlap; a future consolidation is a separate question.

## Exchange Index

- [01 — Personal-layer restructure (.personal/scripture/ nesting + sources/)](./Fable-5--01.md)
- [02 — Shared-Layer Integration Gate](./Fable-5--02.md)
- [03 — Docs-to-disk reconciliation](./Fable-5--03.md)
