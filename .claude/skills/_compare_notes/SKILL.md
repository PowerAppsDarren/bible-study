---
name: _compare_notes
description: Compare personal Bible-study notes across multiple users in a small-group or church repo. Use when the user asks "what did [name] think about [chapter]", "compare my notes with [other user]'s on [passage]", "what did the group take away from [chapter]", "weekly review of what we've been studying", "summarize everyone's notes on Genesis 1", or wants to surface what other members of the group have written in their `.personal/<email>/` folders. The skill enumerates `.personal/*/` (each user's email-named folder), reads notes by passage/topic, and produces a synthesis — points of agreement, divergence, unique insights, and unanswered questions across the group.
---

# Compare Notes

Surface what the group has been studying by reading across `.personal/*/` (the multi-user shared-personal layer) and synthesizing.

This skill is the multi-user feature of the repo. It exists because the repo's `.personal/` is intentionally tracked in git (not gitignored), and members share their study notes by pushing — but each member has their own email-named subfolder, so privacy is by convention. **This skill respects that convention:** it only reads files that have been committed and intentionally shared.

## Triggers

- "What did [name] think about [chapter]?"
- "Compare my notes with [other user]'s on [passage]"
- "What did the group take away from [chapter]?"
- "Weekly review" / "summarize this week's studies"
- "Where do we agree / disagree on [passage]?"

## Repo context

Read `CLAUDE.md` first. The repo's multi-user paradigm:

- `.personal/<user-email>/` — each user's space (e.g., `.personal/darren@neese.us/`, `.personal/sarah@church.org/`).
- Folders are committed and shared via git pull.
- Each user organizes their own folder freely; common conventions: `.personal/<email>/scripture/<book>/<book-chapter>/notes.md` (older notes may sit at `.personal/<email>/<book>/...` without the `scripture/` level — scan both), `.personal/<email>/topics/<theme>.md`, `.personal/<email>/journal/YYYY-MM-DD.md`.

## Workflow

1. **Confirm scope.** Which passage, theme, or time range? Which users (all of them, or specific names/emails)?
2. **Enumerate `.personal/*/` directories.** Map each subfolder to a user (the folder name *is* the email).
3. **Find relevant notes.** Use Grep / Glob to find files matching the passage or theme across all user folders.
4. **Read each user's note.** Preserve attribution — every observation is anchored to whose folder it came from.
5. **Synthesize** in the output structure below.
6. **Output is ephemeral by default** — render in the chat, don't auto-save. If the user wants it saved, default destination: `.personal/<requester-email>/group-syntheses/<topic>-YYYY-MM-DD.md`.

## Output structure

```
# Group synthesis — [passage or topic]

**Compared:** [list of users included]
**Date range:** [if applicable]
**Files read:** [count + paths]

## Common ground
- [observation cited to multiple users with attribution]

## Divergences
- [where users read the passage differently, with attribution]

## Unique insights
- [observation found in exactly one user's notes, attributed]

## Unanswered questions
- [questions raised in any user's notes that no one in the group has answered]

## Suggested follow-up
- [topics, cross-references, or word studies the group would benefit from next]
```

## Discipline

- **Always attribute.** "Darren noted X; Sarah pushed back with Y." Never strip names — that erases the very thing this skill exists to surface.
- **Read only what's committed.** A user's local-uncommitted file is private until they push. Don't try to access their working tree.
- **Don't editorialize between users.** Report each position fairly; don't pick a winner.
- **Quote sparingly.** A short snippet plus attribution is enough; don't reproduce someone's whole note in the synthesis.
- **Honor privacy by convention.** Some users may have a `.personal/<email>/private/` subfolder they consider off-limits even though it's committed; respect a `# private` or `do-not-share` marker if present in a file's frontmatter or first line.

## Composition

- No agent dependency — this is a repo-reading skill, not a research skill.
- Pairs with **_group_discussion_prep** when a leader wants to surface group take-aways before the next meeting.
- Pairs with **_topic_trace** when group divergence on a theme suggests the theme deserves a shared topic page.

## Avoid

- Reading and summarizing without attribution.
- Leaking content from someone's folder that they marked private.
- Pretending agreement where there is honest disagreement.
- Doing this for users who haven't pushed — there's nothing to read.
