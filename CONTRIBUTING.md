# Contributing

Thank you for your interest in this Bible study template. Whether you're using it for personal study or contributing improvements back to the project, this guide will help you get started.

---

## The Two-Layer Model

This repo separates **shared reference material** from **personal study notes**. Understanding this distinction is the most important thing before you start.

| What | Where | Shared? | Examples |
|------|-------|---------|----------|
| Reference material | `scripture/`, `topics/`, root docs | **Yes** — curated, must clear the integration gate | Book overviews, people, places, timelines, cross-references |
| Personal notes | `.personal/<your-email>/` | **Yes** — tracked in git, shared by convention | Your reflections, prayers, questions, sermon notes |

**Rule of thumb:** if it's a fact that's the same for everyone *and it clears the [integration gate](#the-shared-layer-integration-gate)*, it belongs in the shared repo. If it's *your* thought, reflection, or personal study note, it belongs in `.personal/<your-email>/`. Both layers are committed to git — the difference is that the shared layer is curated and the personal layer is lossless.

See the [README](README.md#shared-vs-personal--how-this-repo-works) for a fuller explanation.

---

## Getting Started

1. Clone the repo (or your group's fork of it).
2. Create a `.personal/` folder in the root of your local clone.
3. Start studying. Use the shared content as reference. Write your personal notes in `.personal/`.

That's it. The structure is already in place — just use it.

## Your Personal Notes (`.personal/<your-email>/`)

Each contributor has a folder named by their email address (e.g., `.personal/darren@neese.us/`). This folder **is tracked in git** — when you commit and push, the rest of the group can pull and read your notes. Privacy is by convention: if you don't want something shared, don't commit it (or keep it in a `private/` subfolder). Never write inside another contributor's email folder — that space is read-only by convention.

### Recommended structure

Mirror the repo layout so your notes are easy to find — book studies nest under `scripture/`, with raw inputs (transcripts, chat exports, scans) in a `sources/` folder:

```
.personal/<your-email>/
├── journal/
│   └── YYYY-MM-DD.md
├── scripture/
│   └── 01-Genesis/
│       ├── Genesis-01/
│       │   └── notes.md
│       └── sources/
└── topics/
    └── prayer.md
```

This is a recommendation, not a requirement. Organize your own folder however works best for you — flat files, nested folders, or any other structure. See [`.personal/README.md`](.personal/README.md) for the full convention.

### Backing up your personal notes

Because your folder is committed and pushed, **git is your backup** — every push to the group remote preserves your notes off-machine. For extra redundancy you can still add cloud sync (OneDrive, Dropbox, etc.) or a second remote, but it isn't required the way it was under the old gitignored single-user model.

---

## Shared Content — What Goes in the Repo

Everything outside `.personal/` is shared. This includes:

- **Book-level READMEs** (`books-of-bible/NN-BookName/README.md`) — overview, author, date, themes
- **Chapter-level READMEs** (`books-of-bible/NN-BookName/BookName-NN/README.md`) — shared summaries, key verses, cross-references
- **Topics of study** (`topics-of-study/`) — cross-cutting themes
- **Root documentation** — README, STRUCTURE, CONTRIBUTING, etc.

Shared content should be **factual, reference-quality, and beneficial to everyone**. Think of it as building a shared study Bible — the notes in the margins that any reader would find useful.

### What belongs in the shared repo

- Book and chapter summaries
- Key verses and cross-references
- People, places, and events (factual reference data)
- Timelines and historical context
- Topical studies grounded in Scripture

### What does NOT belong in the shared repo

- Personal reflections, prayers, or journal entries (put these in `.personal/<your-email>/`)
- Denominational or doctrinal commentary
- Content from copyrighted Bible translations
- Anything that is opinion rather than widely-accepted biblical scholarship

---

## The Shared-Layer Integration Gate

The shared layer is **curated, not a dumping ground.** Factual content alone isn't enough — a line can be perfectly true and still be clutter if it just restates the verse. Before a line goes into a shared README, it must clear all six tests:

1. **Factual, not personal** — a verifiable claim about the text, language, history, or structure; not your reflection or application.
2. **Margin-worthy** — it tells the reader something the verse alone doesn't (a word meaning, a structure, a background fact, a connection). If it only restates the verse, cut it.
3. **Durable** — true regardless of who reads it or when; not tied to a moment, a sermon, or your circumstances.
4. **Sourceable** — grounded in the text or mainstream scholarship you could cite. Where scholarship genuinely disagrees, name the views; don't pick a side.
5. **Non-sectarian** — no denominational corner-painting on contested passages. Name the traditions and move on.
6. **License-clean** — no extended copyrighted-translation text; KJV / ASV / WEB or paraphrase, ≤25 words at a stretch.

**Fail any one → it stays in your `.personal/<your-email>/` folder.** When in doubt, leave it out: the personal layer is lossless, the shared layer is curated.

**Study once, deposit twice.** A single study naturally produces both kinds of material — route each half to its home. The factual residue (word studies, structure, cross-refs, background) goes to the shared README; the reflection, application, and teacher-voice stay personal.

**Don't pad to look complete.** Fill a stub chapter README only when the study yielded enough gate-passing substance for a genuine Key Verses / Summary / Notes / Cross References / Questions set. One good cross-reference doesn't justify manufacturing four thin sections around it — leave the stub. An honest empty margin beats a padded one. The default state of a chapter README is empty; content earns its way in.

> The authoritative, always-current version of this gate lives in [`CLAUDE.md`](CLAUDE.md#shared-layer-integration-gate). This summary defers to it.

---

## Naming Conventions

### Book Folders

Each book folder is numbered and hyphenated:

```
NN-BookName
```

Examples: `01-Genesis`, `46-1-Corinthians`, `66-Revelation`

See [STRUCTURE.md](STRUCTURE.md) for the full list.

### Chapter Folders

Chapter folders use the book name followed by a zero-padded chapter number:

```
BookName-NN
```

Examples: `Genesis-01`, `Psalms-119`, `Revelation-22`

### File Names

Every folder contains a `README.md`. This is the only file required by the template. You are free to add additional files (images, PDFs, audio notes) alongside the README as needed.

## Chapter README Format

Each chapter `README.md` should follow the structure in [README-TEMPLATE.md](README-TEMPLATE.md):

- **Key Verses** — Notable verses from the chapter
- **Summary** — Brief overview of what happens
- **Notes** — Shared observations useful to everyone
- **Cross References** — Links to related passages
- **Questions** — Discussion questions for group study

Remember: personal reflections go in `.personal/`, not in the shared chapter READMEs.

## Book-Level README Format

Each book's `README.md` (e.g., `01-Genesis/README.md`) includes:

- Book name as heading
- Overview (brief description)
- Author, date written, chapter count
- Key themes

These are pre-filled in the template. Expand them with factual reference material via pull requests.

## Topics of Study

The `topics-of-study/` directory is for cross-cutting themes — topics that span multiple books and chapters. To add a topic:

1. Create a subfolder: `topics-of-study/prayer/`
2. Add a `README.md` with shared reference content.
3. Link back to relevant chapter folders in `books-of-bible/`.

For personal topical notes, use `.personal/topics-of-study/` instead.

---

## Contributing to the Shared Repo

If you'd like to improve the shared content, here's how:

1. Create a branch for your change.
2. Make your edits.
3. Open a pull request with a clear description of what you changed and why.

### What Makes a Good Contribution

- Adding factual reference content (people, places, historical context)
- Curating key verses and cross-references
- Fixing typos or factual errors in book metadata
- Improving the README-TEMPLATE.md structure
- Improving documentation (STRUCTURE.md, this file, etc.)

### What Doesn't Belong in a Pull Request

- Personal study notes (keep those in `.personal/`)
- Denominational or doctrinal commentary
- Content from copyrighted Bible translations

## Code of Conduct

Please read and follow the [Code of Conduct](CODE_OF_CONDUCT.md). The short version: be respectful, assume good faith, and keep things constructive.
