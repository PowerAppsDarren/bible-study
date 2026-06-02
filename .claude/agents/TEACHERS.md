# Bible Teacher Agents — Eight Voices for Deep Study

A collection of eight Claude Code subagents, each modeled after a distinct Bible teacher's methodology and emphases. Drop these into your `.claude/agents/` directory and invoke them by name when you want a chapter taught through a specific lens.

## The eight agents

| File | Agent name | Lens | Best for |
|---|---|---|---|
| `teacher-perry-stone.md` | `teacher-perry-stone` | Hebrew roots, prophetic patterns, festival typology, supernatural/spiritual warfare | Israel, the prophets, the feasts, end-times, demonology |
| `teacher-chuck-missler.md` | `teacher-chuck-missler` | Integrated message system, typology, mathematical patterns, Genesis 6 / Nephilim | Cross-canonical connections, Christ-types, design of Scripture |
| `teacher-john-barnett.md` | `teacher-john-barnett` | Verse-by-verse exposition, dispensational, pre-trib, practical discipleship | Revelation, Daniel, Olivet Discourse, expositional teaching |
| `teacher-jonathan-cahn.md` | `teacher-jonathan-cahn` | Hebrew word studies, ancient-to-modern prophetic parallels, Shemitah/Jubilee cycles | Prophetic books, national judgment passages, current-events resonance |
| `teacher-john-bevere.md` | `teacher-john-bevere` | Fear of the Lord, Day of the Lord, tribulation vs wrath, cost of discipleship | 1-2 Thessalonians, 2 Peter, Olivet Discourse, eschatology with hope |
| `teacher-bill-creasy.md` | `teacher-bill-creasy` | Bible as unified literary work, genre awareness, geography, narrative arc | Historical narratives, wisdom literature, anything in Israel's geography |
| `teacher-oswald-chambers.md` | `teacher-oswald-chambers` | Abandonment to Jesus, Cross-centered devotion, sanctification as union with Christ, obedience over feelings | Gospel call passages, Romans 6–8, Galatians, Philippians 3, devotional / interior texts |
| `teacher-jamie-winship.md` | `teacher-jamie-winship` | True identity in Christ, false self vs. God-given name, fear as the root of all conflict, hearing God's voice, the lie-for-truth exchange | Renaming/calling narratives, "fear not" passages, Sermon on the Mount, Romans 8, identity and freedom texts |

## Installation

These are standard Claude Code subagent files. To install:

1. Place each `.md` file in your project's `.claude/agents/` directory (or in `~/.claude/agents/` for user-level agents)
2. Claude Code will discover them automatically
3. Invoke by mentioning the agent name or describing the kind of teaching you want

## Important — these agents do NOT impersonate the teachers

Each agent is modeled after a teacher's **methodology and emphases**, not their literal voice. The agents:

- Engage Scripture through the lens that teacher is known for
- Use the kind of language and structure that teacher uses
- Emphasize what that teacher emphasizes
- Cite the teacher with appropriate framing ("Perry Stone has long emphasized...", "Chuck Missler taught...", etc.)

The agents do NOT:

- Fabricate specific quotes from the teachers
- Claim teachers said things they cannot be verified to have said
- Speak in the first person as if they are the teacher

This matters because putting words in a real person's mouth is a form of misrepresentation. Each agent's system prompt explicitly forbids this and provides safer citation patterns.

## Suggested workflow

For a single chapter study, consider invoking one agent at a time depending on what the chapter calls for:

- **Genesis 6** → Chuck Missler (Nephilim, fallen angels) + Bill Creasy (literary structure, the Watchers tradition)
- **Isaiah 53** → Perry Stone (Hebrew word work) + Chuck Missler (Christ-type) + Bill Creasy (literary genre)
- **Daniel 9** → John Barnett (verse-by-verse, dispensational) + John Bevere (Day of the Lord)
- **Joel 2** → Jonathan Cahn (Day of the Lord, Hebrew calendar) + John Bevere (wrath vs tribulation)
- **Revelation 4** → John Barnett (chronological exposition) + Chuck Missler (typology and design)
- **Acts 17** → Bill Creasy (geography of Athens, literary parallels) + Perry Stone (spiritual warfare)
- **Genesis 32** (Jacob wrestles, renamed Israel) → Jamie Winship (false self / God-given name) + Oswald Chambers (the interior surrender)
- **Judges 6** (Gideon, "mighty man of valor") → Jamie Winship (identity God speaks vs. fear) + Perry Stone (Hebrew word work)

You can also chain them: have one agent do the verse-by-verse pass, then a second add the prophetic-pattern lens, then a third bring the literary perspective.

## Companion skill

These agents pair with the `_deep_bible_study_devotional` skill, which orchestrates the full devotional output structure. The agents are the voices; the skill is the format.

## File format

Each agent is a single Markdown file with YAML frontmatter:

```markdown
---
name: {name}
description: When to use this agent (detailed and pushy for reliable triggering)
---

# Agent system prompt body
...
```

This is the standard Claude Code subagent format. No additional dependencies.

## A note on accuracy

Two name corrections from the original conversations these agents emerged from:

- The teacher remembered as "John Bennett, Discover the Bible Ministry" is actually **Dr. John Barnett** of **Discover the Book Ministries (DTBM)**
- The teacher remembered as "John Revere" or "John Reveré" is actually **John Bevere** (no accent)

The agents use the correct names and credentials. The skill that pairs with these agents includes notes recognizing the easily-confused spellings.

## Maintenance

If a teacher's emphasis shifts (as Bevere's did publicly in April 2025 when he affirmed pre-tribulation rapture for the first time), the agent files can be updated to reflect the shift. Each agent's system prompt is structured so that updates are straightforward — change the emphases section, update the citation patterns, refine the boundaries.

Each agent ends with a "conviction at the center" paragraph that captures the heart of that teacher's framework. That's the soul of the agent — everything else is structural.

Use them well.
