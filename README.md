# Bible Structure — Study Template

A repo template with all books and chapters of the Protestant Holy Bible scaffolded out. It could be used for many reasons, but the simplest of reasons may be to serve as the beginning of a personal Bible study.

---

## Shared vs. Personal — How This Repo Works

This repo is designed for **group use**. It has two layers:

| Layer | Location | Pushed to Git? | Who edits it? |
|-------|----------|----------------|---------------|
| **Shared** | Everything *outside* `.personal/` | Yes — curated, must clear the integration gate | The group, via pull requests |
| **Personal** | `.personal/<your-email>/` | **Yes — by convention** | You (your own email folder only) |

### Shared content (the repo itself)

The shared layer contains **reference material that is the same for everyone**: book overviews, people, places, timelines, cross-references, and curated chapter summaries. Once established, this content rarely changes (aside from the occasional correction). Everyone pulls from the same source of truth.

**Do not put personal study notes in the shared folders.** If you want to contribute a factual correction or add reference material that benefits everyone, open a pull request.

### Personal content (`.personal/`)

Your study notes live in `.personal/<your-email>/` — a folder named by your email address (e.g., `.personal/darren@neese.us/`). Unlike the old single-user model, this folder **is tracked in git**: when you commit and push, the group can pull and read your notes. Privacy is by convention — if you don't want something shared, don't commit it. Never write inside another contributor's email folder; that space is read-only by convention.

The recommended structure mirrors the repo — book studies nest under `scripture/`, with raw inputs (transcripts, chat exports, scans) in a `sources/` folder:

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

This makes it easy to find your notes — they sit in the same path as the shared content, just under `.personal/<your-email>/`. But this is a recommendation, not a requirement. Organize your own folder however works best for you.

**To get started:** create your `.personal/<your-email>/` folder in your local clone and start writing.

---

## What's Inside

- **66 books** organized in canonical order (`scripture/`)
- **1,189 chapter folders**, each with its own `README.md` for shared reference notes
- **Book-level overviews** with author, date, and key themes for every book
- **Topics directory** (`topics/`) for cross-cutting themes and topical studies
- **Chapter template** ([README-TEMPLATE.md](README-TEMPLATE.md)) with sections for key verses, summary, notes, cross references, and questions

## Quick Start

1. Clone the repo (or your group's fork of it).
2. Create a `.personal/` folder in the root for your private notes.
3. Study. Use the shared content as reference. Write your personal notes in `.personal/`.
4. To improve the shared content, open a pull request.

## Memory & Retrieval (MemPalace)

This repo is wired up to [MemPalace](https://github.com/mempalace/mempalace) — a local, semantic search index over the repo's content **and** every Claude Code conversation that has ever touched it. Nothing leaves your machine. No API key, no LLM required.

### One-time install (per machine)

```powershell
winget install astral-sh.uv
uv tool install mempalace
```

After install, restart your shell so `mempalace` and `mempalace-mcp` are on `PATH` (they live in `%USERPROFILE%\.local\bin`).

### Initialize this repo's palace

Run once after cloning:

```powershell
mempalace init . --yes --auto-mine --no-llm
```

This creates `mempalace.yaml` + `entities.json` (already in `.gitignore`), maps your top-level folders to "rooms" (`scripture/`, `topics/`, `words/`, `people/`, `places/`, `theology/`, `commentary/`, `resources/`, etc.), and indexes every file. The palace itself lives outside the repo at `~/.mempalace/palace`.

### Pull in past Claude Code conversations

```powershell
mempalace mine "$env:USERPROFILE\.claude\projects\C--Users-DarrenNeese-src-bible-structure" --mode convos --wing bible_structure
```

Re-run any time after long Claude Code sessions to absorb new transcripts. (Auto-save hooks below handle this on the fly going forward.)

### Daily use

```powershell
mempalace search "what did we decide about the chapter README format"
mempalace search "Isaiah 1 notes" --wing bible_structure --room scripture
mempalace status                  # what's been filed
mempalace wake-up --wing bible_structure   # ~600-900 token context blob to paste into a fresh chat
```

### Auto-save hooks (already configured)

`.claude/settings.json` registers three Claude Code hooks that run automatically:

| Hook | When | What |
|---|---|---|
| `SessionStart` | new Claude Code session | loads palace context |
| `Stop` | end of an assistant turn | persists the exchange |
| `PreCompact` | before context compaction | snapshots the conversation so nothing is lost |

If you're running Claude Code in this repo, these fire on their own — no action needed.

### MCP server (already configured)

`.mcp.json` exposes the palace to Claude Code as an MCP server (`mempalace-mcp`), so the agent can query memory natively without shelling out to the CLI. Approve it the first time Claude Code prompts you on this repo.

### Useful commands

```powershell
mempalace --help                  # all commands
mempalace status                  # palace contents
mempalace mine .                  # re-mine repo files (incremental, skips unchanged)
mempalace compress                # ~30x reduction on cold drawers
mempalace mcp                     # show MCP setup string
```

---

## Documentation

| Document                                 | Description                                  |
|------------------------------------------|----------------------------------------------|
| [STRUCTURE.md](STRUCTURE.md)             | Full map of all 66 books and chapter counts  |
| [README-TEMPLATE.md](README-TEMPLATE.md) | Template for chapter-level study notes        |
| [CONTRIBUTING.md](CONTRIBUTING.md)       | How to use, fork, and contribute             |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community guidelines                         |
| [CHANGELOG.md](CHANGELOG.md)            | Version history                              |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
