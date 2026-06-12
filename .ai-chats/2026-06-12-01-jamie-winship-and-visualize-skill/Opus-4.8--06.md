# Exchange 06: Create the `_visualize_this` skill (ultrathink)

- **Timestamp:** 2026-06-12
- **Context:** User wants a new skill for assimilating information visually. "ultrathink" requested.

## User Input

i need a very convenient way to assimilate information. Let's create a skill called `/_visualize_this`. ultrathink

## AI Response

Designed and built the skill. Studied house style (`skills/README.md`, `_word_study`, the heavyweight skill's `references/` pattern). Core design (the ultrathink):

- **Medium = Mermaid-in-markdown** — renders inline on GitHub / VS Code / Obsidian; a diagram is just more markdown (no export, diffs cleanly, lives next to its text).
- **Intelligence = shape-matching.** A rubric maps the *shape of the information* → the right diagram: chronology→timeline, concept-breakdown→mindmap, argument/cause→flowchart, relationships→network graph, dialogue→sequence, two-axis→quadrant, emotional arc→journey, feature grid→table, chiasm/inclusio→indented text.
- **Assimilation guardrails:** ≤7±2 nodes/cluster, split don't crowd, every node traces to a verse, color/direction must encode meaning.
- **Two-layer + copyright honored;** inline by default, save on request.
- **Distinct from `graphify`** (persistent whole-corpus graph vs. one focused inline diagram).

Built `SKILL.md` (triggers, repo context, workflow, selection rubric, composition, avoid) + `references/diagram-catalog.md` (9 worked templates with valid Mermaid + syntax gotchas). Updated `skills/README.md` (new "Assimilation skills" section) and `CLAUDE.md`. Proved it end-to-end by rendering Winship's abiding loop as a flowchart inline.

## Tool Calls

- `Read` ×2 (skills README, _word_study); `Glob` skills tree
- `Read` CLAUDE.md skills section (×2 offsets)
- `Write` SKILL.md, references/diagram-catalog.md
- `Edit` skills/README.md, CLAUDE.md

## Files Read/Modified

- **+** `.claude/skills/_visualize_this/SKILL.md`
- **+** `.claude/skills/_visualize_this/references/diagram-catalog.md`
- **~** `.claude/skills/README.md`, `CLAUDE.md`
