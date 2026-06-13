# Exchange 01 — Personal-layer restructure

## User

> we need to have more structure in the .personal subfolders. please review and create a plan - c:\Users\DarrenNeese\src\bible-study\.personal\darren@neese.us\23-Isaiah c:\Users\DarrenNeese\src\bible-study\.personal\darren@neese.us\Isaiah <- these two folders should not be in the root of a personal area, right?

*(Session began in plan mode.)*

## Assistant (plan + execution)

Explored `.personal/` and confirmed the issue. The personal root held two loose Isaiah folders:

- `23-Isaiah/` — chapter notes (`Isaiah-06/notes.md`, `Isaiah-10/devotional.html`). Matched the *documented* convention (book folders directly under the email folder), but with 66 books that convention litters the root.
- `Isaiah/` — non-conforming raw material: `nicoles-claude-chat.md` (chat export), `26-05-09--isaiah-part-01.txt` (UTF-16 audio transcript with per-character spacing artifacts), and a stub `README.md`.

Asked the user three clarifying questions. Answers:
- **Book folders** → nest under `scripture/` (mirror the repo root).
- **Loose `Isaiah/` raw material** → move into the book folder as `sources/`.
- **Codify + fix encoding** → update README + skills; re-encode the transcript to UTF-8.

### Executed

Target layout:
```
.personal/darren@neese.us/
├── scripture/
│   └── 23-Isaiah/
│       ├── Isaiah-06/notes.md
│       ├── Isaiah-10/devotional.html
│       └── sources/
│           ├── nicoles-claude-chat.md
│           └── 2026-05-09-isaiah-conversation-transcript.txt   (re-encoded UTF-8)
├── journal/ · prayer/ · visuals/ · obsidian/ · private/
├── insights.md · profile.md · reading-plan.md
```

- `git mv` for the three as-is files (history preserved as renames).
- Re-encoded the transcript UTF-16→UTF-8 in PowerShell, renamed it, verified no NUL bytes.
- Dropped the stub `Isaiah/README.md`; added a `sources/README.md`.
- Fixed relative links in `reading-plan.md` and `insights.md` (`23-Isaiah/...` → `scripture/23-Isaiah/...`). Left `.ai-chats/` references untouched (verbatim history).
- Codified the `scripture/`-nesting convention in `.personal/README.md`, `_personal_reflection`, `_compare_notes`, and project `CLAUDE.md`.

**Commit `7eadf4c`** — refactor(personal): nest book studies under scripture/, fold raw Isaiah sources into 23-Isaiah/sources.
