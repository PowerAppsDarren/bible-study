# AI Chat Session: Whole-Bible Scripture Rollout, README Front-Pages, Word-Study Engine

- **Date:** 2026-06-27 (session began 2026-06-24, ran across 06-24/25/27)
- **Model:** Opus 4.8 (1M context)
- **Topic:** Populate the repo with public-domain scripture text + build the tooling, README front-page design, and a Greek/Hebrew word-study engine
- **Tool:** Claude Code
- **Project:** bible-study
- **Exchange Count:** 18 (logged)

## 💡 Conversation Summary

A long, multi-day build session that took the repo from "stub READMEs" to a **fully populated, navigable scripture library**:

- **Studied Psalm 1** (devotional: the two ways, tree vs. chaff, Hebrew word work).
- Established that **public-domain Bible text can be hosted in-repo** (KJV/ASV/WEB/BBE; never NIV/ESV/etc.). Source: **getbible.net v2 API** (117 translations).
- Built **three reusable Python scripts** under `scripts/` (stdlib-only, cross-platform, content-population utilities — not a build system):
  - `fetch_scripture.py` — pulls text, writes per-verse `<a id="vN">` anchors, carries the full 117-translation catalog in comments, and (added later) a **`--bulk` mode** that downloads a whole translation in one request and splits locally.
  - `build_readme_index.py` — rebuilds each chapter `README.md` as a front page.
  - `word_study.py` — Strong's-based word-study engine.
- **Set BBE (Bible in Basic English) as the project's default/primary version** for everything (saved to memory).
- **Designed and rolled out the chapter README front page** (after an HTML mockup comparison): YAML metadata header (book/chapter/genre/verses/primary/versions/themes), prev/next/up nav, full-text links, a **BBE-primary verse-index table** (BBE text + compare-links to WEB/KJV/ASV), an "At a glance" placeholder, and factual study-notes sections (personal reflection routed to `.personal/`).
- Decided word-study approach: **Tier 2 (`words/` engine)** yes; **Tier 3 (full interlinear in every README)** rejected with reasons; interlinear becomes on-demand.
- **Found and disabled the mystery auto-committer: the GitDoc VS Code extension.**
- Whole-Bible rollout: **all 1,189 chapters × BBE/WEB/KJV/ASV (4,756 files) + 1,189 README front pages.**
- Also: David character study (`people/biblical-figures/David.md`), VS Code terminal font 18→24.

## 🔧 Technical Details

**Scripts created (`scripts/`):**
- `fetch_scripture.py` — getbible v2; default versions `basicenglish, web, kjv, asv` (BBE first = primary); `FILE_STEMS` maps long names (basicenglish→BBE, douayrheims→DRA); browser User-Agent (getbible CDN 403s default urllib); per-verse anchors; `--bulk`/`--refresh` (whole-translation cache at `~/.cache/bible-study/translations`); 117-translation catalog in header comments.
- `build_readme_index.py` — front-page generator; merges YAML front-matter (preserves `themes`/hand keys), regenerates only between `<!-- BEGIN/END AUTO-INDEX -->`, preserves real study notes (`has_real_notes`), 66-book genre map.
- `word_study.py` — Strong's H/G lookup or `--find <gloss>`; writes `words/<lang>/<slug>.md`; lexicons (OpenScriptures PD Strong's, CC-BY-SA JSON) auto-cache to `~/.cache/bible-study/lexicons`; won't clobber existing studies (skip unless `--force`); utf-8 stdout for Hebrew/Greek on Windows.
- `scripts/README.md` — documents all three.

**Content generated:**
- `scripture/**/{BBE,WEB,KJV,ASV}.md` — 4,756 files (all 66 books, 1,189 chapters).
- `scripture/**/README.md` — 1,189 front pages rebuilt.
- `people/biblical-figures/David.md` — shared-layer character study (via `biographer` agent).
- `words/hebrew/{esher,towrah,hagah}.md` — seed word studies.
- `.personal/darren@neese.us/readme-options-demo.html` — README layout comparison demo.

**Commits (this session, all on `main`, pushed to `origin`):**
- `8e560fe`, `2da2879`, `3c76865` — **GitDoc auto-commits** (not me; how the culprit was found).
- `eb558e9` — Psalms 2–150 BBE/WEB/KJV/ASV + anchors + verse index.
- `068136b` — Psalms READMEs rebuilt as BBE-primary front pages.
- `a767f2e` — word-study engine (Tier 2) + 3 seed words.
- `645a679` — whole-Bible rollout (66 books) + `--bulk` mode.

**Config:**
- VS Code user settings: `terminal.integrated.fontSize` 18→21→24; `gitdoc.enabled:false` + `autoPush/autoPull:off` + `commitOnClose:false`.

## 📚 Lessons Learned

- **getbible CDN 403s the default Python urllib User-Agent** — must send a browser-like UA.
- **Windows console is cp1252** — Hebrew/Greek crash on print; write UTF-8 files or `sys.stdout.reconfigure(encoding="utf-8")`.
- **Bulk endpoints are the kind way to fetch** — whole translation in ~1 request (~8.8 MB) vs ~4,756 per-chapter calls; eliminates rate-limit risk.
- **The auto-committer was GitDoc** (extension): commits the working tree + pushes with Copilot-written messages; its on/off flag lives in VS Code's `state.vscdb`, not settings.json. Setting `gitdoc.enabled:false` does **not** stop the already-running instance — needs a VS Code reload or "GitDoc: Disable". It caused two `.git/index.lock` collisions; each was a stale 0-byte lock cleared safely after confirming no live git process.
- **getbible `kjva` does NOT carry Strong's tags** (returns plain KJV) — Strong's data must come from a separate dataset (OpenScriptures / STEPBible).
- **README was doing two jobs**; the new front page separates the shared/factual layer from personal reflection per the integration gate.

## ⏭️ Next Steps

1. **GitDoc uninstalled** (`vsls-contrib.gitdoc`, exchange 15) — reload VS Code once ("Developer: Reload Window") to evict the still-running copy from memory.
2. **Word-study concordance** — add a Strong's-tagged Bible so `word_study.py` can list every occurrence (the noted next increment).
3. **Fill scholarship** — "At a glance" + study-notes are placeholders across all 1,189 chapters; fill via `_chapter_readme_fill` / `linguist` as studies happen.
4. Optional: on-demand interlinear artifact generator; book-level README index pages.

## 📁 Exchange Index

(Large session; user inputs are verbatim, long AI outputs are referenced/elided per protocol.)

- [01 — Study Psalm 1](./Opus-4.8--01.md)
- [02 — Fill scripture / is the Bible public domain? + pilot Psalm 1](./Opus-4.8--02.md)
- [03 — Whole book of Psalms + "where are the scripts / what API / scripts folder?"](./Opus-4.8--03.md)
- [04 — Add the 117-translation catalog; "what other versions?"](./Opus-4.8--04.md)
- [05 — Add BBE; README verse-index with per-version links](./Opus-4.8--05.md)
- [06 — Track, commit, push (GitDoc auto-commits surface)](./Opus-4.8--06.md)
- [07 — Rate-limit risk? → bulk mode; brainstorm README structure + HTML demo](./Opus-4.8--07.md)
- [08 — Remember: BBE is the default; "that's the one to show"](./Opus-4.8--08.md)
- [09 — Terminal font 18→24](./Opus-4.8--09.md)
- [10 — Digging into Greek/Hebrew; cost model; Tier 3 drawbacks; go with recommendation](./Opus-4.8--10.md)
- [11 — Remember all decisions and why](./Opus-4.8--11.md)
- [12 — Do A then B then C (GitDoc / word-study engine / whole Bible)](./Opus-4.8--12.md)
- [13 — Wrap up per AI-Chats Protocol v3.2](./Opus-4.8--13.md)
- [14 — What is GitDoc and why is it interfering?](./Opus-4.8--14.md)
- [15 — Uninstall GitDoc](./Opus-4.8--15.md)
- [16 — Wrap up (continuation)](./Opus-4.8--16.md)
- [17 — Where do my personal-folder edits get checked into?](./Opus-4.8--17.md)
- [18 — Wrap up (continuation)](./Opus-4.8--18.md)
