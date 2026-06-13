# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A markdown-only Bible study scaffold. **There is no build system, no tests, no lint, no package manifest.** Every "file" is a `README.md` in a folder. Don't look for `npm`/`pip`/`make` commands — they don't exist. Tasks here are content edits, folder reorganization, and documentation.

## Layout on disk — canonical

A refactor (commits `55df16f` and `02835da`) established this top-level layout, and the published docs (`README.md`, `STRUCTURE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`) were reconciled to match it. **Disk is canonical.**

```
scripture/        # the 66 books (formerly "books-of-bible/" in older docs)
topics/           # cross-cutting themes (formerly "topics-of-study/")
commentary/       # stub
people/           # stub
places/           # stub
resources/        # stub
theology/         # stub
words/            # stub (Hebrew/Greek word studies)
.personal/        # per-user notes, tracked in git (see two-layer model below)
.ai-chats/        # AI session logs (see protocol below)
```

The stub content folders each contain a one-line `# Read Me` placeholder. The 12-folder *vision* behind this layout is in `____bible-study-top-level-folders.md` (and its byte-identical duplicate `repo-planning.md`, plus `docs/top-level-folders.md`) — those are aspirational planning docs and deliberately retain the original long names (`word-studies/`, `topics-of-study/`) and folders not on disk (`_home/`, `timeline/`, `context/`, `teaching/`, `templates/`). Don't treat them as describing the current layout, and don't rewrite them to match disk — they're a record of the original plan.

**The earlier docs-vs-disk inconsistency has been resolved** (the published docs now use `scripture/` and `topics/`). The only files that still reference the old `books-of-bible/` / `topics-of-study/` names are: the planning/vision docs above (intentional), `.ai-chats/` session logs (verbatim history — never rewrite), and `graphify-out/` (generated; regenerate, don't hand-edit).

## Two-layer model: shared vs. shared-personal (multi-user)

The repo is designed for small-group / church use. Two layers:

- **Shared layer** — everything outside `.personal/` (`scripture/`, `topics/`, `words/`, `people/`, `places/`, `theology/`, etc.). Factual reference material that benefits everyone, changed via PR.
- **Shared-personal layer** — `.personal/<user-email>/`: each user has a folder named by their email address (e.g., `.personal/darren@neese.us/`). Personal reflections, journals, prayer notes, teaching prep. The folder is **intentionally tracked in git** (not gitignored). Members share by pushing; privacy is by convention. See `.personal/README.md`. Inside a user's folder, book studies nest under `scripture/` (e.g., `.personal/<email>/scripture/23-Isaiah/Isaiah-06/notes.md`, raw inputs in `scripture/<book>/sources/`), mirroring the repo root layout.

`CONTRIBUTING.md` rule: fact = shared; *your thought* = `.personal/<your-email>/`. Never write inside another user's email folder — that space is read-only by convention.

**Historical-record exception:** the `CHANGELOG.md` 1.2.0 entry still describes `.personal/` as gitignored and the layout as `books-of-bible/`. That's an accurate record of what those releases shipped — left intact on purpose. The current state (multi-user `.personal/`, `scripture/`/`topics/`) is captured in the CHANGELOG `[Unreleased]` section. The `.gitignore` correctly does NOT exclude `.personal/`.

## Naming conventions

- **Book folders:** `NN-BookName`, zero-padded — `01-Genesis`, `46-1-Corinthians`, `66-Revelation`. Full list in `STRUCTURE.md`.
- **Chapter folders:** `BookName-NN`, zero-padded — `Genesis-01`, `Psalms-119`, `Revelation-22`.
- **Every folder has exactly one `README.md`.** Additional files (images, attachments) may sit alongside.
- **Counts to preserve:** 66 books, 1,189 chapter folders.

## Chapter README format

Defined in `README-TEMPLATE.md`: `# [Book] [Chapter]` heading, then sections **Key Verses**, **Summary**, **Notes**, **Cross References**, **Questions**. Most chapter READMEs in `scripture/` are still stub `# Read Me` placeholders waiting to be filled in. Book-level READMEs (e.g., `scripture/01-Genesis/README.md`) follow a different format with Overview / Author / Date Written / Chapters / Key Themes.

When filling chapter content: factual, reference-quality, study-Bible-margin tone. `CONTRIBUTING.md` explicitly excludes denominational/doctrinal commentary and content from copyrighted translations from the shared layer.

## Shared-layer integration gate

**This is the standard for what earns a place in the shared layer. It exists to keep `scripture/`, `topics/`, `words/`, etc. valuable and uncluttered — an honest stub beats a padded margin.** When a study (devotional, reflection, word study) produces material, route it *study once, deposit twice*:

- **Personal half** — reflection, application, teacher-voice, what stirred *you*, speculative connections → `.personal/<email>/scripture/...`. The personal layer is lossless; everything is welcome there.
- **Factual half** — what the text *says, means, and connects to* → the shared chapter/topic README, **but only the lines that clear the gate below.** The shared layer is curated, not a dumping ground.

A candidate line is admitted to the shared layer only if it passes **all six**:

1. **Factual, not personal** — a verifiable claim about the text, language, history, or structure; not your reflection or application. (*"`chaqaq` means to inscribe/decree"* passes; *"this convicted me about my own decrees"* does not.)
2. **Margin-worthy** — it tells the reader something the verse alone doesn't (a word meaning, a structure, a background fact, a connection). If it only restates the verse in other words, it's clutter — cut it.
3. **Durable** — true regardless of who reads it or when. Not tied to a moment, a sermon, or your circumstances.
4. **Sourceable** — grounded in the text or in mainstream scholarship you could cite. Where scholarship genuinely disagrees (Job's date, Daniel's date, the Pastorals' authorship), name the views; don't pick a side or assert it as settled.
5. **Non-sectarian** — no denominational corner-painting on contested passages (election, perseverance, baptism, eucharist, end-times schemes). Name the traditions, move on.
6. **License-clean** — no extended copyrighted-translation text. KJV / ASV / WEB or paraphrase, ≤25 words at a stretch.

**Fail any one → it stays in the personal layer, or gets reworked until it passes. When in doubt, leave it out.**

**Chapter-promotion rule:** fill a stub chapter README only when the study yielded enough gate-passing substance for a genuine Key Verses / Summary / Notes / Cross References / Questions set. Don't manufacture four thin sections around one good cross-reference to make a chapter "look complete" — leave the stub, or add the single good item to a chapter that's already rich. The default state of a chapter README is empty; content earns its way in.

`_chapter_readme_fill` is the skill that applies this gate; `CONTRIBUTING.md` carries the human-facing summary. Both defer to this section as the source of truth.

## Specialized agents

Two tiers of subagents are committed under `.claude/agents/` and load automatically. Use them via the Agent tool when work matches their specialization.

**Research / theology agents** (output for the shared repo):

- `exegete` — single-passage close reading; chapter-README content
- `theologian` — systematic / biblical theology; topical studies
- `linguist` — Hebrew / Greek word studies
- `historian` — ANE / Second Temple / Greco-Roman background
- `geographer` — places, regions, routes
- `biographer` — biblical figures, church history, modern scholars
- `cross-references` — citations, allusions, parallels, typology

**Teacher-voice agents** (devotional output, usually for `.personal/`) — apply a specific teacher's hermeneutical lens without impersonating them:

- `teacher-perry-stone` — Hebrew roots, festival typology, prophetic patterns
- `teacher-chuck-missler` — integrated message system, typology, Christ-types
- `teacher-john-barnett` — verse-by-verse, dispensational, pre-trib
- `teacher-jonathan-cahn` — Hebrew word studies, prophetic parallels, Shemitah
- `teacher-john-bevere` — fear of the Lord, Day of the Lord, wrath vs tribulation
- `teacher-bill-creasy` — Bible as unified literary work, genre, geography
- `teacher-oswald-chambers` — abandonment to Jesus, Cross-centered devotion, sanctification as union with Christ
- `teacher-jamie-winship` — true identity in Christ, false self vs. God-given name, fear as the root of conflict, hearing God's voice

The teacher-voice agents pair with the `_deep_bible_study_devotional` skill in `.claude/skills/`, which provides the devotional output structure.

See `.claude/agents/README.md` for how the agents divide labor and `.claude/agents/TEACHERS.md` for teacher-pairing suggestions. Each agent is told to read this CLAUDE.md before producing output, so updates here propagate.

## Skills

A coordinated battery of skills under `.claude/skills/` covers the four phases of small-group Bible study. Skills are **model-invoked** (Claude decides when to fire based on the user's message); user-typed shortcuts go in `.claude/commands/` (not yet present).

- **Heavyweight chapter walk:** `_deep_bible_study_devotional`
- **Research:** `_word_study`, `_cross_reference_map`, `_character_study`, `_place_study`, `_topic_trace`
- **Group:** `_group_discussion_prep`, `_compare_notes` (multi-user — reads across `.personal/*/`)
- **Personal:** `_personal_reflection`, `_prayer_from_passage` (write to `.personal/<email>/` only)
- **Maintenance:** `_chapter_readme_fill` (writes to shared `scripture/`), `_new_teacher_agent` (scaffolds a teacher agent + updates the registries)
- **Assimilation (visual):** `_visualize_this` (turns any content into a Mermaid/text diagram; inline by default, saveable to either layer)

See `.claude/skills/README.md` for how skills compose with each other and with the agents. Skills enforce the two-layer discipline: shared output goes to top-level folders; personal output stays inside the user's email folder.

### Naming convention — `_snake_case` for custom skills and commands, `kebab-case` for agents

Two conventions, applied strictly:

- **Custom skills and slash commands:** `_snake_case` — underscore prefix, then snake_case (e.g., `_word_study`, `_chapter_readme_fill`, `_new_teacher_agent`). The underscore distinguishes our work from third-party skill bundles (GSD and similar); the snake_case differentiates skill identifiers from agent identifiers at a glance.
- **Agents:** `kebab-case`, no prefix (e.g., `exegete`, `theologian`, `teacher-perry-stone`, `teacher-oswald-chambers`).

When adding a new skill or command:
- Folder/file name: `.claude/skills/_<snake_case_name>/SKILL.md` or `.claude/commands/_<snake_case_name>.md`.
- `name:` frontmatter field must match exactly (`name: _<snake_case_name>`).
- No hyphens anywhere in custom skill names — convert each hyphen to an underscore.
- Update references in this `CLAUDE.md`, `.claude/skills/README.md`, and any cross-references between skills.

When adding a new agent:
- Folder/file name: `.claude/agents/<kebab-case-name>.md`.
- `name:` frontmatter field must match (`name: <kebab-case-name>`).
- No underscore prefix on agents — the prefix is reserved for skills/commands.

## AI-Chats protocol

`.ai-chats/README.md` documents a self-imposed session-logging protocol (v3.2) the user actively maintains. Key rules:

- Each session is a folder `YYYY-MM-DD-NN-kebab-description/` (e.g., `2026-01-31-04-template-completion/`).
- Files inside follow `[Model-Version]--NN.md` — **no spaces, double-dash before sequence**. Example for this Claude Code session: `Opus-4.7--00.md`.
- `--00.md` is the main doc (summary, tech, lessons). `--01`, `--02`, ... are verbatim exchanges.
- `.ai-chats/INDEX.md` is the master index and must be updated when sessions are added.
- Only create/update these files when explicitly asked, or when the user is clearly continuing an existing session — don't auto-spawn them on every interaction.

## Things to avoid

- **Never write inside another user's `.personal/<email>/` folder.** Each user owns their own. Other users' folders are read-only by convention.
- Don't `git add -A` paths outside the user's own email folder unless intentionally PR-ing shared content. The intentional-tracking of `.personal/` makes wildcard adds safer than they were under the old paradigm, but staying scoped is still good hygiene.
- Don't invent build/test/lint commands. There is no toolchain here.
- Don't fill chapter content with sermon-style or denominational commentary — that belongs in `.personal/<your-email>/`, not the shared repo.
- Don't reconcile the docs-vs-disk inconsistency without asking which side is canonical.
