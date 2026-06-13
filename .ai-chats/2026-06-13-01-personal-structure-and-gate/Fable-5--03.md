# Exchange 03 — Docs-to-disk reconciliation

## User

> proceed with your recommended plan

*(The recommended plan, offered at the end of Exchange 02, was: standardize the published-doc path references to match disk — `scripture/`, `topics/` — as a separate tidy-up pass. This authorized disk as canonical.)*

## Assistant

Found all stale references via grep, then categorized:

- **Fix** (published docs describing current layout): `README.md`, `STRUCTURE.md`, `CONTRIBUTING.md`.
- **Special-case** `CHANGELOG.md`: historical entries are accurate for their dates → don't falsify; add an `[Unreleased]` section instead.
- **Leave** (intentional): `repo-planning.md` / `docs/top-level-folders.md` (aspirational 12-folder vision), `.ai-chats/` (verbatim history), `graphify-out/` (generated). `cross-references.md` already defers to disk.

### Executed

- **README/STRUCTURE/CONTRIBUTING:** `books-of-bible/`→`scripture/`, `topics-of-study/`→`topics/` in every tree, list, and prose mention. Updated the `.personal/<email>/` trees to show book studies under `scripture/` with `sources/`. Finished migrating the stale "gitignored, never pushed" `.personal/` language to the multi-user tracked-in-git model (two-layer tables, backup section). Preserved heading anchors (`#shared-vs-personal--how-this-repo-works`, `#the-two-layer-model`).
- **CHANGELOG:** added `[Unreleased]` documenting the rename, the multi-user `.personal/` shift, and the integration gate; left 1.2.0/1.0.0 intact.
- **CLAUDE.md:** rewrote `## Layout on disk vs. layout in the docs` → `## Layout on disk — canonical`; dropped the "ask which side is canonical" instruction (the inconsistency is resolved); replaced the "two stale claims" block with a "historical-record exception" note; removed the now-false "STRUCTURE.md uses old books-of-bible/ paths" parenthetical.

### Verified

- Grep confirmed no `books-of-bible/` / `topics-of-study/` remain in live docs — only planning/vision docs, `.ai-chats/`, and `graphify-out/` (all intentional).
- No live doc links to the renamed heading.
- All remaining "gitignored" mentions are either correct framing, the historical CHANGELOG entry, or the real per-user `private/` subfolder convention.

**Commit `e091bc2`** — docs: reconcile published docs to on-disk layout (scripture/, topics/).

---

*Session then moved to `/_wrap_up_session`: no feature branches to clean (only `main`), nothing to merge, 3 commits ahead of `origin` → push at wrap-up.*
