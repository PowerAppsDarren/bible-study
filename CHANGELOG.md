# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Changed

- **Top-level folders renamed** to match the working repo: `books-of-bible/` → `scripture/`, `topics-of-study/` → `topics/`. Docs (README, STRUCTURE, CONTRIBUTING) updated to the on-disk names.
- **`.personal/` is now a multi-user, git-tracked layer**, superseding the original single-user gitignored model. Each contributor owns a folder named by their email address (`.personal/<email>/`); notes are shared by pushing, privacy is by convention.
- **Personal book studies nest under `.personal/<email>/scripture/`**, mirroring the repo root, with raw inputs (transcripts, chat exports) in a per-book `sources/` folder.

### Added

- **Shared-layer devotional pages ("The Branch")** — illustrated, self-contained `devotional.html` study pages now live beside chapter READMEs in the shared layer (`scripture/<NN-Book>/<Book-NN>/`) when they clear the integration gate. First set: **Psalms 1–10** and **Ezekiel 1**. Each carries a table of contents and links every Bible-chapter mention to that chapter's repo README.
- **Devotional finalize post-processors** in the `_branch_devotional_design` skill: `link_chapters.py` (turns every chapter reference into a link to `scripture/<NN-Book>/<Book>-<CC>/README.md`; existence-checked, idempotent, never self-links) and `add_toc.py` (injects an "In This Study" table of contents and stable section ids).
- **`_bible_dual_home_guard` skill + `.githooks/pre-commit`** — keeps the repo's `.claude/` bible skills and agents byte-identical with the global `~/.claude/` copies on every commit (enforces the long-standing dual-home rule; pure-Python, cross-platform, non-blocking).
- **Shared-Layer Integration Gate** — a six-test quality standard (factual / margin-worthy / durable / sourceable / non-sectarian / license-clean) governing what earns a place in the shared layer, plus the "study once, deposit twice" routing and a chapter-promotion rule. Authoritative version in `CLAUDE.md`; summary in `CONTRIBUTING.md`; enforced by the `_chapter_readme_fill` skill.
- **Full public-domain scripture text in `scripture/`** — every chapter (all 66 books, 1,189 chapters) now carries four public-domain translations as sibling files (`BBE.md`, `WEB.md`, `KJV.md`, `ASV.md`) with per-verse anchors. **BBE (Bible in Basic English) is the default/primary version.** Source: getbible.net v2.
- **Chapter README front pages** — each chapter `README.md` is now a generated front page: a YAML metadata header (book / chapter / genre / verses / primary / versions / themes), prev/next/up navigation, full-text links, a BBE-primary verse-index table linking each verse to all available versions, and factual study-notes sections (personal reflection routed to `.personal/`). The auto-generated region is regenerate-safe and never clobbers hand-written notes.
- **`scripts/` tooling** (content-population utilities, Python stdlib only, cross-platform): `fetch_scripture.py` (getbible fetch, per-verse anchors, `--bulk` whole-translation mode, full 117-translation catalog), `build_readme_index.py` (README front-page generator), and `word_study.py` (Strong's-based Greek/Hebrew word-study engine using public-domain OpenScriptures lexicons → `words/<lang>/`).
- **`people/biblical-figures/David.md`** — shared-layer character study.

## [1.2.0] - 2026-01-31

### Added

- Shared vs. Personal two-layer model: `.personal/` folder (gitignored) for private study notes
- `.personal/` added to `.gitignore`
- Prominent documentation of the two-layer model in README.md, CONTRIBUTING.md, and STRUCTURE.md

## [1.1.0] - 2026-01-31

### Added

- `STRUCTURE.md` — Full reference map of all 66 books with chapter counts
- `CONTRIBUTING.md` — Guide for using, forking, and contributing to the template
- `CODE_OF_CONDUCT.md` — Faith-friendly community guidelines
- `CHANGELOG.md` — This file

### Updated

- `README-TEMPLATE.md` — Fleshed out with Key Verses, Summary, Notes, Cross References, and Questions sections
- All 66 book-level `README.md` files — Added Overview, Author, Date Written, Chapters, and Key Themes
- Top-level `README.md` — Improved title, added stats and links to supporting documents

## [1.0.0] - 2026-01-25

### Added

- Initial scaffold of all 66 books of the Protestant Bible
- 1,189 chapter folders, each with a placeholder `README.md`
- `topics-of-study/` directory for cross-cutting themes
- `.gitignore` for common OS, editor, and build artifacts
- MIT License
