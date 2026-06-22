---
name: _branch_devotional_design
description: The repo's devotional design system — "The Branch", a warm, lamplit "scriptorium" look for HTML Bible-study pages (one per chapter), word studies, and topical reflections. Use this skill whenever a devotional or study is being rendered, saved, or emailed as an HTML page, when the user says "make it a page", "render the study", "build the devotional page", "use The Branch", "apply the devotional design", "design this study", or when `_deep_bible_study_devotional` (or a teacher-voice agent) produces content that needs a visual home. Holds the color/type/spacing tokens, the voice + visual guide, a ready-to-fill template, and a complete worked example. Pairs with the `devotional-designer` agent (which builds and iterates the pages) and `_deep_bible_study_devotional` (which writes the content); `_email_study_guide` re-renders the finished page for email.
user-invocable: true
---

# The Branch — Devotional Study Design System

"The Branch" is the repo's design system for devotional Bible-study pages: a warm,
low-light "scriptorium" aesthetic (deep ember-black grounds, parchment inks, four
meaningful scripture accents, Hebrew set as a recurring star). It was designed on
claude.ai/design from the original *Isaiah 11 — "The Branch the Axe Couldn't Touch"*
study and imported here as the canonical, browser-native system.

**Read `readme.md` first.** It holds the two things that matter most:
- **CONTENT FUNDAMENTALS** — voice, person, tense, emoji usage, the structure of a study.
- **VISUAL FOUNDATIONS** — color meanings, type, spacing, cards, motion, iconography.

Everything else hangs off those two sections.

## Files (all in this skill folder)
- **`readme.md`** — the content + visual fundamentals. The source of truth for tone and look.
- **`devotional-template.html`** — a **ready-to-fill chapter page**, standalone and
  browser-native. Duplicate it, delete the guide banner, and replace every `[bracketed]`
  placeholder. **Start here for a new study page.**
- **`example-isaiah-11.html`** — the template **filled** with a complete study; the worked
  reference for how the components carry real content (hero, verse blocks, Hebrew word
  cards, the sevenfold-Spirit menorah list, teacher callouts, peaceable-kingdom pairs,
  closing pillars, next-chapter teaser).
- **`styles.css`** + **`tokens/colors.css` · `tokens/typography.css` · `tokens/spacing.css`**
  — the canonical color / type / spacing tokens (source of truth). The template mirrors
  these literal values **inline** so every finished study is one self-contained, portable
  file with no runtime stylesheet.

## How it fits the rest of the battery
- **`_deep_bible_study_devotional`** writes the *content*; this skill is the *look*. The
  **`devotional-designer`** agent is the hand that fills the template — delegate the page
  build to it, or fill the template directly using `readme.md`.
- The **teacher-voice agents** (Perry Stone, Chuck Missler, John Barnett, Jonathan Cahn,
  John Bevere, Bill Creasy, Oswald Chambers, Jamie Winship) supply the voice that goes into
  the callouts and the commentary.
- **`_email_study_guide`** re-renders the finished page into email-safe HTML from the same
  palette — keep the literal accent hex values aligned with the tokens so browser and email
  match.

## To make a new study page
1. Duplicate `devotional-template.html`, rename it for the chapter (e.g. `devotional.html`),
   and save it in the study's **personal** folder:
   `.personal/<email>/scripture/<NN-Book>/<Book-NN>/`. Finished study pages are personal /
   teacher-voice output — never write them into the shared layer, and never into another
   user's email folder.
2. Delete the `✍️` guide banner; replace every `[bracketed]` placeholder.
3. Follow the voice in `readme.md`: second person, present tense, one bolded punch per
   paragraph, scripture in italic serif with a tracked uppercase reference, Hebrew given room.
4. Keep **accent meanings** consistent so the whole canon reads as one work:
   - **gold** — the divine / default
   - **olive** — life, growth, peace
   - **ember** — judgment, fire, warning
   - **sky** — the nations, water, hope
5. One **featured verse** per study. Use the **menorah list** only for enumerated ideas,
   **pairs** for contrasts, **teacher callouts** for named voices.

## Output discipline
- Every page is a **single self-contained HTML file**: inline styles, fonts via the one
  Google Fonts `<link>`, the `.wordcard:hover` rule in `<head>`. No external stylesheet,
  no build step, no claude.ai/design scaffolding (`<x-dc>`, `support.js`, `data-screen-label`,
  `style-hover`) — those belong only to the design-canvas source, not the implemented page.
- Parchment inks, never pure white. Warm grounds + low-alpha lamplight glows for depth, not
  drop-shadows. Emoji are iconography (one per section header), never decoration spam.
- When a token changes, update it in `tokens/` **and** in the inline values of
  `devotional-template.html` so the two stay in lockstep.
