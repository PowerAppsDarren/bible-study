# Agents

This directory holds the project's specialized subagents. Claude Code loads them automatically — invoke via the Agent tool with `subagent_type: <agent-name>`, or just describe a task that fits an agent's description and the main Claude can delegate.

## The team

| Agent | Use when |
|-------|----------|
| `exegete` | Filling in or improving a chapter README; close reading of a single passage |
| `theologian` | Doctrinal questions; topical / thematic studies in `topics/` or `theology/` |
| `linguist` | Building word-study notes in `words/`; questions hinging on a Hebrew or Greek word |
| `historian` | Historical, cultural, archaeological context |
| `geographer` | Notes for `places/`; geography or routes (Exodus, Paul's journeys) |
| `biographer` | Notes for `people/` — biblical figures, church history, modern scholars |
| `cross-references` | Cross-References sections; tracing citation / allusion threads |

### Teacher-voice agents

A second tier of agents teaches a chapter through the methodology and emphases of a specific Bible teacher. They do **not** impersonate or fabricate quotes — they apply the teacher's hermeneutical lens. See `TEACHERS.md` for the full overview and pairing suggestions.

| Agent | Lens |
|-------|------|
| `teacher-perry-stone` | Hebrew roots, festival typology, prophetic patterns, spiritual warfare |
| `teacher-chuck-missler` | Integrated message system, typology, Christ-types, design of Scripture |
| `teacher-john-barnett` | Verse-by-verse, dispensational, pre-trib, practical discipleship |
| `teacher-jonathan-cahn` | Hebrew word studies, ancient-to-modern prophetic parallels, Shemitah/Jubilee |
| `teacher-john-bevere` | Fear of the Lord, Day of the Lord, tribulation vs wrath, cost of discipleship |
| `teacher-bill-creasy` | Bible as unified literary work, genre awareness, geography, narrative arc |

These pair with the `_deep_bible_study_devotional` skill (in `.claude/skills/`), which provides the devotional output structure. The agents are the voices; the skill is the format. Output from teacher-voice agents is devotional in tone and generally belongs in `.personal/`, not the shared repo.

### Design / production agent

A third tier turns a finished study into its visual form. Output is devotional and lands in `.personal/`, not the shared repo.

| Agent | Use when |
|-------|----------|
| `devotional-designer` | A chapter study needs to become a polished, standalone HTML page in "The Branch" look — filling the devotional template, or restyling an existing page. Pairs with the `_branch_devotional_design` skill (the design system) and the teacher-voice agents (the voice). |

Each agent reads `CLAUDE.md` at the repo root for project conventions before producing output.

## Shared discipline

All research agents follow the same shared-repo rules (the teacher-voice agents follow them too, but their devotional output usually lands in `.personal/`):

- **Two-layer model.** Output is for the *shared* repo — factual and reference-quality. Personal reflection belongs in `.personal/`.
- **No copyrighted translations.** Use KJV / ASV / WEB or paraphrase. Cite chapter / verse, not extended text.
- **No denominational positioning.** Where traditions disagree, name them and present each fairly without endorsing.
- **Naming conventions.** Books `NN-BookName/`, chapters `BookName-NN/`, words lowercase transliteration, places / people human-readable names.

## How agents divide labor

- The **exegete** does single-passage close reading. The **theologian** does cross-passage synthesis. Use the exegete for "what does Genesis 3 say"; the theologian for "what does Scripture say about original sin."
- The **cross-references** agent handles mechanical cross-ref work — citation, allusion, parallel, typology. The exegete cites a few important refs; the cross-references agent goes deeper.
- The **linguist** does single-lemma word studies. The theologian uses lemmas to anchor doctrines but doesn't write the word study itself.
- The **historian** handles temporal / cultural background; the **geographer** handles spatial / locational background. They overlap on archaeology — historian for "what did this find prove"; geographer for "where is this site."
- The **biographer** owns persons (biblical, historical, modern). The historian owns events and cultures.

When more than one agent could fit, the main Claude should pick the *narrowest* one — depth over breadth.

## Editing or adding agents

Each agent is a markdown file with YAML frontmatter (`name`, `description`, optionally `tools`, `model`). The filename must match `name`. After editing, the next Claude Code session picks up the changes automatically.

To add an eighth agent, copy any existing file as a template and update `name`, `description`, and the system prompt. Keep the specialization distinct from the existing seven so the main Claude can pick the right one.

Candidates the planning doc (`____bible-study-top-level-folders.md`) suggests but the team currently lacks:

- A **timeline / chronology** specialist (overlaps with `historian`).
- A **commentary curator** that knows the landscape of major commentary series (NICOT / NICNT, BECNT, Word, Pillar, Hermeneia, Tyndale, ICC).
- A **homiletics / teaching** specialist for `teaching/` — but this is the kind of content that belongs more in `.personal/` than in the shared repo.
