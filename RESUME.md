# RESUME

Rolling 7-day session log. Add `<!-- pin -->` to any entry to keep it permanently.

---

## 2026-06-13 — Personal-layer restructure + Integration Gate + docs reconciliation (Fable-5)

**Accomplished:**
- Restructured `.personal/darren@neese.us/` — book studies now nest under `scripture/` (mirroring repo root); loose `Isaiah/` raw material folded into `scripture/23-Isaiah/sources/`; audio transcript re-encoded UTF-16→UTF-8. Convention codified in `.personal/README.md`, `_personal_reflection`, `_compare_notes`, `CLAUDE.md`. *(`7eadf4c`)*
- Created the **Shared-Layer Integration Gate** — six-test value standard (factual / margin-worthy / durable / sourceable / non-sectarian / license-clean) + "study once, deposit twice" + chapter-promotion rule. Authoritative in `CLAUDE.md`, enforced by `_chapter_readme_fill`, summarized in `CONTRIBUTING.md`. *(`33b9472`)*
- Reconciled published docs to on-disk layout — `books-of-bible/`→`scripture/`, `topics-of-study/`→`topics/`; finished migrating stale gitignored `.personal/` language to multi-user model; CHANGELOG `[Unreleased]`; CLAUDE.md declares disk canonical. *(`e091bc2`)*

**Files changed:** `.personal/` tree (moves + README + sources), `_personal_reflection`, `_compare_notes`, `_chapter_readme_fill`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, `STRUCTURE.md`, `CHANGELOG.md`, plus `.ai-chats/2026-06-13-01-*` and this file.

**Branches:** only `main` — no feature branches to clean, nothing to merge.

**Not done / next:**
- Backfill `scripture/` chapter READMEs for Isaiah 1–10 via `_chapter_readme_fill` through the new gate (deferred by design).
- Dedup the overlapping planning docs (`repo-planning.md`, `docs/top-level-folders.md`, `____bible-study-top-level-folders.md`).
