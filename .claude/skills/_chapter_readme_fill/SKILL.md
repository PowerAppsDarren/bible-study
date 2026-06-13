---
name: _chapter_readme_fill
description: Fill in a stub chapter README in `scripture/<NN-Book>/<Book>-<NN>/README.md` with shared-quality reference content following the README-TEMPLATE.md structure (Key Verses, Summary, Notes, Cross References, Questions). Use when the user says "fill in the chapter README for Genesis 1", "complete the stub for Romans 8", "populate the Genesis-03 README", "build out the chapter notes for [book chapter]", or wants the existing `# Read Me` placeholder turned into real reference content. Output is shared, factual, reference-quality — no denominational positioning, no extended copyrighted-translation quotes, no personal reflection. This is the repo-maintenance counterpart to _deep_bible_study_devotional (which produces personal devotional content).
---

# Chapter README Fill

Convert a stub `# Read Me` chapter README into shared, reference-quality content following `README-TEMPLATE.md`.

This is the **shared-layer** counterpart to `_personal_reflection` (which writes to `.personal/<email>/`) and to `_deep_bible_study_devotional` (which produces a personal devotional). The output here is the kind of note that belongs in the margins of a study Bible everyone in the group consults.

## Triggers

- "Fill in the chapter README for Genesis 1"
- "Complete the stub for Romans 8"
- "Populate Genesis-03/README.md"
- "Build out the chapter notes for [book chapter]"
- "Turn the Genesis-01 stub into real content"

## Repo context

Read `CLAUDE.md` first. Output destination:

- **Always:** `scripture/<NN-Book>/<Book>-<NN>/README.md` (e.g., `scripture/01-Genesis/Genesis-01/README.md`).
- This is **shared** — committed via PR. Do not write personal reflection here. Personal goes in `.personal/<user-email>/`.

The template structure is in `/README-TEMPLATE.md` at the repo root: heading `# [Book] [Chapter]`, then sections **Key Verses**, **Summary**, **Notes**, **Cross References**, **Questions**.

## Workflow

1. **Verify the target.** Confirm the passage exists and the existing file is a stub (`# Read Me` placeholder) and not someone's in-progress work.
2. **Delegate the close reading to the `exegete` agent** — single-passage exposition, literary structure, key verses, summary, notes.
3. **Delegate the cross-reference selection to the `cross-references` agent** — choose 4–10 of the most theologically significant cross-refs (not exhaustive; that's the **_cross_reference_map** skill's job).
4. **Pull `historian` or `geographer`** if the chapter's interpretation hinges on background.
5. **Run every candidate line through the Shared-Layer Integration Gate** (see `CLAUDE.md` → "Shared-layer integration gate"). Each line must pass all six tests — factual / margin-worthy / durable / sourceable / non-sectarian / license-clean. Drop anything that only restates the verse or carries personal-layer voice. **Apply the chapter-promotion rule:** if the study didn't yield enough gate-passing substance for a genuine five-section set, don't manufacture thin sections to fill the template — leave the stub or deposit the one good item elsewhere, and say so.
6. **Assemble** the gate-passing material in the template structure.
7. **Save** to the chapter README path.

## Output structure (matches `README-TEMPLATE.md`)

```
# [Book] [Chapter]

## Key Verses
- **v.X** — [verse in KJV / ASV / WEB or paraphrase] — [one-line note on why this verse carries weight]
- [3–5 verses total]

## Summary
[3–5 sentences of what happens (narrative) or what's argued (didactic). Stays close to the text.]

## Notes
- [Bulleted observations: structural — chiasm, parallelism, inclusio]
- [Lexical — Hebrew/Greek terms that matter for this chapter]
- [Genre — narrative, law, poetry, prophecy, gospel, epistle, apocalyptic]
- [Background — historical, cultural, geographical when load-bearing]
- [Theological — what this chapter contributes, without sliding into denominational positioning]

## Cross References
- [Book Chapter](../../NN-Book/Book-CC/README.md) — short note on the connection
- [4–10 entries]

## Questions
- [Honest study questions — tensions in the text, things to revisit, application angles. Not rhetorical, not leading.]
- [2–4 entries]
```

## Discipline

- **The Shared-Layer Integration Gate is the bar.** Every line must clear all six tests in `CLAUDE.md` → "Shared-layer integration gate." When in doubt, leave it out — the personal layer is lossless, the shared layer is curated.
- **Factual, reference-quality.** This is the shared note that everyone in the group sees. Devotional flourishes go in `.personal/<email>/`.
- **No denominational corner-painting.** Where the chapter is read differently in different traditions (Romans 9 election, Hebrews 6 perseverance, baptism passages, eucharist passages), name the traditions and move on.
- **No extended copyrighted-translation quotes.** Use KJV / ASV / WEB or paraphrase, ≤25 words at a time.
- **Cite when it matters.** "Beale & Carson note X" is better than asserting a contested allusion as obvious.
- **Don't overwrite an in-progress file.** If the file isn't a `# Read Me` stub, ask before replacing.

## Composition

- Orchestrates **exegete** (primary), **cross-references**, and (when needed) **historian / geographer / linguist**.
- Counterpart to **_personal_reflection** (same chapter, opposite layer).
- Counterpart to **_deep_bible_study_devotional** (same chapter, devotional rather than reference).
- Feeds **_group_discussion_prep**'s leader notes.

## Avoid

- Writing devotional or first-person content into the shared README.
- Filling all chapters of a book in one pass without verifying each — chapter-by-chapter, with attention.
- Padding Notes with restatement of Summary or list-form duplication of Cross References.
- Asserting authorship, dating, or background as settled when scholarship genuinely disagrees (Job's date, Daniel's date, the Pastorals' authorship, etc.).
