---
name: _personal_reflection
description: Scaffold a personal reflection / journal entry on a Bible passage, chapter, or theme in the user's `.personal/<email>/` folder. Use when the user says "journal about [chapter]", "I want to reflect on [passage]", "help me write what this means to me", "personal reflection on [verse]", "what's stirring in me from [chapter]", or wants devotional / reflective output that is explicitly *theirs* and explicitly *personal* (not shared reference material). Output goes to `.personal/<user-email>/journal/` or `.personal/<user-email>/scripture/<book>/<chapter>/notes.md` — never the shared layer.
---

# Personal Reflection

Scaffold a personal reflection or journal entry. Output is the user's own — first-person, devotional, application-focused — and lives in their email-named folder under `.personal/`.

This is the *opposite* of `_chapter_readme_fill`, which produces factual reference content for the shared layer. Personal reflection is yours to keep, share, or delete — by convention, not gitignore.

## Triggers

- "Journal about [chapter or verse]"
- "I want to reflect on [passage]"
- "Help me write what this means to me"
- "Personal reflection on [chapter]"
- "What's stirring in me from [reading]"
- "Write a journal entry on today's reading"

## Repo context

Read `CLAUDE.md` first. Output destinations (always under the user's email folder):

- `.personal/<user-email>/journal/YYYY-MM-DD.md` — dated journal entry.
- `.personal/<user-email>/scripture/<book-folder>/<book>-<chapter>/notes.md` — chapter-anchored reflection (book folders nest under `scripture/`, mirroring the repo root layout).
- `.personal/<user-email>/topics/<theme>.md` — reflection on a cross-cutting theme.

Filename and folder convention is up to the user; default to one of the above.

## Workflow

1. **Confirm the anchor.** A passage, a verse, a theme, or just "today's reading"? What date?
2. **Confirm the destination.** Journal-by-date or chapter-anchored or topic-anchored?
3. **Generate a reflective scaffold** — prompts for the user to fill in, NOT a finished essay. The user is the author; the skill is a scaffold.
4. **Save** to the chosen path under their email folder.

## Output structure

```
# [Title — passage or theme + optional date]

**Date:** YYYY-MM-DD
**Passage:** [Book Chapter:Verses]
**Translation read:** [optional]

## What stood out
[2–4 sentences from the user — what hit them? what unsettled them? what comforted them?]

## Honest first reaction
[The user's gut reading before research — preserved on purpose. Don't sand it off.]

## What I want to understand better
[Questions to revisit — could feed a future _word_study, _cross_reference_map, or conversation with the group]

## Where my life intersects this
[Application that's specific, not generic. "I will be more loving" is generic. "I will not interrupt my wife when she tells me about her day" is specific.]

## Prayer
[3–5 sentences responding to the passage in prayer]

## Verse to carry today
[Optional — a single verse to memorize or hold onto]
```

## Discipline

- **Scaffold, don't ghostwrite.** The structure is a prompt set; the user fills the content. If the user asks for a draft, mark it "DRAFT — replace with your own words" and keep it short.
- **First-person voice.** Reference content is third-person and reference-quality; reflection is first-person and honest.
- **No denominational pre-painting.** This is the user's reflection, not a tradition's lecture.
- **Honor honest reaction.** If the user's gut reading is wrong, they'll find out later — don't pre-correct it in the scaffold.
- **No copyrighted-translation extended quotes** — even in personal output, follow the repo's translation discipline (KJV, ASV, WEB, or paraphrase).

## Composition

- No primary agent dependency — this is a personal-output skill, not a research skill.
- Pairs with **_prayer_from_passage** when the user wants prayer to be the primary output.
- Pairs with **_deep_bible_study_devotional** when the user wants both: research-grounded study *and* a personal reflection saved separately.
- The **_compare_notes** skill can later surface this reflection alongside others' if it's committed.

## Avoid

- Writing the reflection *for* the user. The whole point is that this is theirs.
- Saving to the shared layer. Reflection always goes to `.personal/<user-email>/`.
- Application that's too generic to act on tomorrow.
- Performing piety in the writing — the journal is honest or it's nothing.
