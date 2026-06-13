# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Changed

- **Top-level folders renamed** to match the working repo: `books-of-bible/` → `scripture/`, `topics-of-study/` → `topics/`. Docs (README, STRUCTURE, CONTRIBUTING) updated to the on-disk names.
- **`.personal/` is now a multi-user, git-tracked layer**, superseding the original single-user gitignored model. Each contributor owns a folder named by their email address (`.personal/<email>/`); notes are shared by pushing, privacy is by convention.
- **Personal book studies nest under `.personal/<email>/scripture/`**, mirroring the repo root, with raw inputs (transcripts, chat exports) in a per-book `sources/` folder.

### Added

- **Shared-Layer Integration Gate** — a six-test quality standard (factual / margin-worthy / durable / sourceable / non-sectarian / license-clean) governing what earns a place in the shared layer, plus the "study once, deposit twice" routing and a chapter-promotion rule. Authoritative version in `CLAUDE.md`; summary in `CONTRIBUTING.md`; enforced by the `_chapter_readme_fill` skill.

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
