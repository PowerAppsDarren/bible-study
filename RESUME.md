# RESUME

Rolling 7-day session log. Add `<!-- pin -->` to any entry to keep it permanently.

---

## 2026-06-27 — Whole-Bible scripture rollout + tooling + word-study engine (Opus-4.8) <!-- pin -->

**Accomplished:**
- **Whole Bible populated:** all 66 books / 1,189 chapters now have **BBE · WEB · KJV · ASV** text (4,756 files) with per-verse `<a id="vN">` anchors. BBE is the **default/primary version** (saved to memory).
- **Chapter READMEs rebuilt as front pages** (all 1,189): YAML metadata header (book/chapter/genre via 66-book map/verses/primary/versions/themes), prev/next/up nav, full-text links, BBE-primary verse table (compare-links to WEB/KJV/ASV), "At a glance" + factual study-notes scaffold (reflection → `.personal/`).
- **Three reusable scripts** (`scripts/`, stdlib-only, cross-platform): `fetch_scripture.py` (getbible v2, anchors, `--bulk` whole-translation mode, 117-translation catalog), `build_readme_index.py` (front-page generator, regenerate-safe, preserves notes), `word_study.py` (Strong's/OpenScriptures word-study engine → `words/<lang>/`).
- **Word-study engine (Tier 2)** seeded esher/towrah/hagah from Psalm 1.
- **David character study** → `people/biblical-figures/David.md` (biographer agent).
- **Found + disabled the GitDoc auto-committer** (caused two index.lock collisions).
- VS Code terminal font 18→24.

**Key commits:** `eb558e9` (Psalms text/anchors/index), `068136b` (Psalms front pages), `a767f2e` (word-study engine), `645a679` (whole-Bible rollout) — all pushed to origin/main.

**Files changed:** `scripts/{fetch_scripture,build_readme_index,word_study}.py` + `scripts/README.md`; `scripture/**/{BBE,WEB,KJV,ASV}.md` (4,756) + `scripture/**/README.md` (1,189); `people/biblical-figures/David.md`; `words/hebrew/{esher,towrah,hagah}.md`; `.personal/darren@neese.us/readme-options-demo.html`; 3 memory files; VS Code user settings (gitdoc + font).

**Not done / next:**
- **Fully stop GitDoc** — "GitDoc: Disable" / reload VS Code, or uninstall `vsls-contrib.gitdoc` (config disable doesn't stop the live instance).
- **Word-study concordance** — add a Strong's-tagged Bible so `word_study.py` lists every occurrence.
- Fill "At a glance" + study notes across chapters via `_chapter_readme_fill` / `linguist` as studies happen.
- (Carried) Isaiah 12; Isaiah 1–10 README backfill; dedup overlapping planning docs.

---

## 2026-06-22 — Isaiah 11 devotional + `_email_study_guide` skill + email delivery (Opus-4.8)

**Accomplished:**
- Generated the **Isaiah 11** devotional `devotional.html` — *"The Branch the Axe Couldn't Touch"* — in the established dark-gold style (featured 11:1–2: the *choter/geza/netzer* Branch + sevenfold-Spirit menorah; peaceable kingdom; Eden-reversal serpent; *nes* banner; second-Exodus highway; Missler/Cahn/Creasy/Perry Stone; hook to Isaiah 12). At `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/devotional.html`.
- Created new project skill **`_email_study_guide`** — re-renders a `devotional.html` into email-safe HTML (table layout, inline styles, parchment theme, web-safe fonts), sends via the **Mailgun HTTP API** (not SMTP — secret is API-key-based), attaches the full browser version, CCs darren@spl.tech, archives the send. Registered in `CLAUDE.md` + `.claude/skills/README.md`.
- Built `Isaiah-11/email.html` and **sent the study** to nicole@specialmom.app + darren@specialmom.app (CC darren@spl.tech), full dark version attached. Two sends (build + skill execution): Mailgun ids `…130717…` and `…131540…`, both HTTP 200.

**Files changed:** `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/{devotional.html,email.html}` (personal layer), `.claude/skills/_email_study_guide/SKILL.md`, `CLAUDE.md`, `.claude/skills/README.md`, `.ai-chats/2026-06-22-01-*`, this file.

**Branches:** only `main` — nothing to clean.

**Not done / next:**
- Isaiah 12 next chapter (the song of the redeemed — "wells of salvation," *Yeshua*).
- Optional: promote Isaiah 11 gate-passing facts (netzer/Nazareth, sevenfold-Spirit→Revelation, Romans 15:12) to shared `scripture/23-Isaiah/Isaiah-11/README.md`.
- Duplicate-send today was benign (two copies); consider a re-send guard in `_email_study_guide` if it becomes routine.
- (Carried) Backfill `scripture/` chapter READMEs for Isaiah 1–10 through the Integration Gate; dedup overlapping planning docs (`repo-planning.md`, `docs/top-level-folders.md`, `____bible-study-top-level-folders.md`).
