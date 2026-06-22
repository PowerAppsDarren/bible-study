# Skills

This directory holds the project's skills. Claude Code loads them automatically and the model invokes them based on description-matching when the user's message fits.

For the user-invoked counterpart (typeable shortcuts), see `.claude/commands/` (when present).

## The battery

A coherent system for chapter-by-chapter, group-anchored Bible study. Skills compose with each other and with the agents in `.claude/agents/`.

### Heavyweight chapter walk

| Skill | Use when |
|---|---|
| `_deep_bible_study_devotional` | The user wants a full, scholarly-yet-warm devotional walk through a chapter. All-in-one: word work, cross-refs, application, hook to next chapter. |

### Research skills (single-axis, narrower than the devotional)

| Skill | Use when | Orchestrates |
|---|---|---|
| `_word_study` | A single Hebrew / Greek / Aramaic lemma deserves depth | `linguist` |
| `_cross_reference_map` | A passage needs a deeper cross-ref web than what fits in a chapter README | `cross-references` |
| `_character_study` | A biblical figure, church-history figure, or modern scholar | `biographer` (+ `historian`) |
| `_place_study` | A city, region, landmark, or route | `geographer` (+ `historian`) |
| `_topic_trace` | A theme traced redemptive-historically through the canon | `theologian` (+ `cross-references`, `linguist`) |

### Group skills

| Skill | Use when | Notes |
|---|---|---|
| `_group_discussion_prep` | Preparing to lead a small group, Sunday school, or Bible study | Leader's prep packet — questions, opening, wrap-up |
| `_compare_notes` | Surfacing what the group has been studying across `.personal/*/` folders | Multi-user, attribution-preserving |

### Personal skills (always write to `.personal/<user-email>/`)

| Skill | Use when |
|---|---|
| `_personal_reflection` | Scaffolding a journal entry or chapter-anchored reflection |
| `_prayer_from_passage` | Turning a passage into structured prayer (ACTS or passage-suggested form) |

### Maintenance skills (write to the shared layer)

| Skill | Use when |
|---|---|
| `_chapter_readme_fill` | Converting a stub `# Read Me` chapter README into reference-quality shared content |
| `_new_teacher_agent` | Scaffolding a new `teacher-<name>.md` subagent and updating `TEACHERS.md` + `CLAUDE.md` so the agent registry stays coherent |

### Assimilation skills (visual — either layer)

| Skill | Use when | Output |
|---|---|---|
| `_visualize_this` | Any information needs to become a diagram for fast assimilation — chapter structure, a teacher's framework, cross-refs, a chronology, an argument, a chiasm | Mermaid-in-markdown (renders on GitHub / VS Code / Obsidian) or an indented text diagram; inline by default, saveable to a shared `*/` folder or `.personal/<email>/` |

### Delivery skills (send a study out)

| Skill | Use when | Output |
|---|---|---|
| `_email_study_guide` | A generated study guide needs to go to people by email | An email-safe HTML rendition (`email.html`, table layout + inline styles + parchment theme — survives Gmail/Outlook) sent via Mailgun with the full browser `devotional.html` attached; CCs `darren@spl.tech`; archived under `~/.skills/_send_email/` |

## How skills compose

A typical group-week workflow:

1. **Leader prep** — `_deep_bible_study_devotional` for the chapter (overnight if it's a heavy passage), then `_group_discussion_prep` for the meeting. Send the finished study to the group with `_email_study_guide`.
2. **Member personal study** — `_personal_reflection` and `_prayer_from_passage` for individual journals; ad-hoc `_word_study`, `_character_study`, or `_place_study` when the chapter raises a specific question.
3. **Mid-week deepening** — `_topic_trace` or `_cross_reference_map` when the group's discussion surfaces a thread worth chasing.
4. **End of week** — `_compare_notes` to see what the group has written across `.personal/*/`; insights from this often seed the next week's `_chapter_readme_fill` work to make the shared layer richer.

## Two-layer discipline (mandatory across all skills)

- **Shared output** (`scripture/`, `topics/`, `words/`, `people/`, `places/`, etc.): factual, reference-quality, no denominational positioning, no copyrighted-translation extended quotes.
- **Personal output** (`.personal/<user-email>/`): first-person, devotional, application-focused — yours to keep, share, or delete.

Skills that produce shared output never write to `.personal/`. Skills that produce personal output never write outside the user's email folder. The skill descriptions above name the destination explicitly.

## Multi-user paradigm

`.personal/` is **intentionally tracked in git**, not gitignored. Each user has a folder named by their email address (e.g., `.personal/darren@neese.us/`, `.personal/sarah@church.org/`). Members share notes by pushing; privacy is by convention — if you don't want others to see something, don't commit it.

The `_compare_notes` skill is the multi-user feature that surfaces what the group has been writing across all email folders.

## Adding a new skill

Each skill is a folder under `.claude/skills/_<snake_case_name>/` with a `SKILL.md` file containing YAML frontmatter (`name`, `description`) plus the skill's instructions.

**Convention: `_snake_case` for every custom skill.** Underscore prefix (distinguishes our work from third-party bundles like GSD) + snake_case body (no hyphens). Examples: `_word_study`, `_chapter_readme_fill`, `_new_teacher_agent`. The folder name and the `name:` frontmatter field must match exactly. Agents use a different convention — `kebab-case` with no prefix (see `.claude/agents/README.md`); don't mix the two.

The `description` field is what Claude uses to decide when to invoke the skill, so write it with strong, specific triggers — concrete user phrases the skill should match. Vague descriptions don't fire reliably.

After adding or editing a skill, the next Claude Code session picks it up automatically.

## Skills vs commands

Skills are **model-invoked** — Claude decides when to use them based on description-matching. Commands (`.claude/commands/`) are **user-invoked** — the user types `/<name>` to trigger them deterministically. Both kinds of triggering matter, and the two coexist:

- Use a skill when "Claude should figure out the right time."
- Use a command when "I know exactly what I want, give me a typeable shortcut."

Many skills could have a corresponding command as a deterministic shortcut into the same workflow.
