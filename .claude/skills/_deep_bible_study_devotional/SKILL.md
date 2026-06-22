---
name: _deep_bible_study_devotional
description: Generate deep, scholarly-yet-warm devotional Bible studies for chapter-by-chapter walks through Scripture. Use this skill ANY time the user wants a devotional study on a specific Bible book and chapter, references a "66-book Bible study", a "YouVersion Bible plan", a "one chapter a day" study, asks "what does [book chapter] mean", shares a verse that stood out and wants it unpacked, or names trusted teachers like Perry Stone, Chuck Missler, John Barnett, Jonathan Cahn, John Bevere, Dr. Bill Creasy, or Oswald Chambers in a Bible study context. Also trigger on phrases like "go deep on [chapter]", "give me a devotional on", "study this chapter with me", "what stood out in [chapter]", or when continuing an established sequential book-by-book Bible study. The skill produces a richly formatted devotional with Hebrew/Greek word studies, cross-references, modern application, spiritual warfare connections, and a hook to the next chapter — all anchored to Scripture as primary authority.
---

# Deep Bible Study Devotional

Generate a deep, warm, scholarly devotional study for a single Bible chapter (or two short chapters) in the established voice and structure that follows. The devotional should feel like sitting under a beloved Bible teacher who knows the original languages, sees the whole canonical story, and connects every chapter to the believer's daily life and the larger spiritual battle.

## Visual output — The Branch design system

When the study is delivered as an HTML page (the usual form for a saved or emailed devotional), render it in **"The Branch"** — the repo's devotional design system, a warm lamplit "scriptorium" look derived from the original Isaiah 11 study. It lives in its own skill, **`_branch_devotional_design`**, and the **`devotional-designer`** agent builds the pages. Delegate the page build to that agent, or fill the template yourself from these files (in `.claude/skills/_branch_devotional_design/`):

- **`devotional-template.html`** — the standalone, browser-native page to duplicate per chapter. Copy it, delete the guide banner, and replace every `[bracketed]` placeholder. **Start here for any HTML devotional.**
- **`readme.md`** — the voice + visual fundamentals (tone, person, emoji rules, accent meanings, component usage). Read this before filling.
- **`example-isaiah-11.html`** — the template filled with a complete study; the reference for how the components carry real content.
- **`tokens/*.css`** + **`styles.css`** — the canonical color/type/spacing tokens. The template mirrors these literal values inline so each finished study is one portable file (no runtime stylesheet).

Keep **accent colors meaningful, not decorative**: gold = the divine / default, olive = life & growth & peace, ember = judgment / fire / warning, sky = the nations / water / hope. One featured verse per study. Save the finished page in the study's personal folder (`.personal/<email>/scripture/<NN-Book>/<Book-NN>/`); `_email_study_guide` then re-renders it as an email-safe version from the same palette.

## When to use this skill

Trigger this skill whenever the user:
- Names a specific Bible book and chapter and wants it taught
- Says they read a chapter and shares what stood out
- Quotes a verse that struck them and asks for depth
- References a 66-day or 66-book reading plan, YouVersion plan, or sequential study
- Mentions trusted teachers (Perry Stone, Chuck Missler, Dr. John Barnett, Jonathan Cahn, John Bevere, or Dr. Bill Creasy) in a Bible study context
- Continues a chapter-by-chapter walk you've already started in the conversation

Skip this skill for:
- Quick factual lookups ("how many chapters in Romans")
- Theological debates without devotional intent
- Sermon or essay generation distinct from chapter-walk devotional format

## What the user typically brings

The user usually arrives with three things, though not always all three:

1. **The chapter** they just read (e.g. "let's do Isaiah 3 today")
2. **What stood out** to them — a theme, an observation, a connection they noticed
3. **The verse** that hit them hardest

Build the devotional around those inputs. The verse they highlighted gets a featured section. Their observations shape the angle of teaching.

If they only give the chapter without their reflection, ask briefly what stood out before generating the full study. Single line, in the chat — never a popup.

## The output structure

Follow this exact structural pattern. It is what works.

### 1. Opening hook (image + caption)

Open with a visual element that makes the chapter feel alive and current. Either:
- A `Show Image` placeholder describing a meme that captures the chapter's punch in modern terms
- An SVG visual element if the chapter calls for it

The caption should be punchy, modern, and show the chapter's relevance to today.

### 2. Title block

```
📖 [Book Chapter] — "[Memorable Theme Phrase in Quotes]"
A Deep Devotional Study
```

The theme phrase should crystallize the chapter's heart in 4-8 words. Examples that worked:
- "The Divine Intervention of a Grieving Father"
- "The Day Everything Gets Exposed"
- "The Collapse of a Nation & The Remnant That Remains"

### 3. Themed sections with emoji headers

Build 5-9 themed sections using emoji headers that reflect each section's vibe. Common ones that fit the established style:

- 🔥 Setting the stage / fiery context / opening thrust
- 💔 Heart of the message / grief / brokenness
- 🩹 Diagnosis / wounded body imagery
- ⚠️ Hard truth / pivot / warning
- 🎭 Performance, deception, masks
- 🌍 Modern application / current culture
- 👁️ Spiritual layer / unseen reality
- 🐍 Enemy strategy / spiritual warfare
- ♟️ Strategic parallels / chess match
- 🌿 Hope / remnant / restoration
- ☁️ Presence / glory / cloud and fire imagery
- 🏔️ Mountain / kingdom / governmental
- ❄️ THE VERSE (the one that stopped them) — this section gets prominent placement
- 🕊️ Closing reflection
- 🍇 Vineyard / fruit / next chapter tease

Pick emojis that fit each section's content, not just from this list.

### 4. The featured verse section

The verse the user said hit them hardest gets its own dedicated section, usually with ❄️ or another striking emoji. Unpack it carefully:

- Quote the verse with reference
- Give Hebrew or Greek word studies for key terms (original script + transliteration + meaning)
- Connect to other places in Scripture where the same word/concept appears
- Show what it would have meant in the ancient context
- Show what it means right now to the reader

This section should be the longest and richest in the devotional.

### 5. Hebrew and Greek word studies

Throughout the study, weave in original-language word studies whenever a key term carries weight that English flattens. Format them like this:

> The Hebrew word for "nourished and brought up" — גִּדַּלְתִּי (giddalti) — is the word used for a parent tenderly raising a child.

Always include: original script, transliteration, meaning, and why it matters to the passage. Use BDB or HALOT-style understanding for Hebrew, BDAG for Greek.

### 6. Cross-references woven throughout

Connect the chapter to the rest of Scripture constantly. Patterns that work:
- "This is the New Testament echo of [OT passage]..."
- "Paul writes the same thing in [NT reference]..."
- "Jesus quotes this almost word-for-word in [reference]..."
- "Revelation [chapter] is John watching this happen in real time..."

Show the unified canonical witness. Treat the Bible as one integrated message system.

### 7. Trusted teacher references

Weave in the user's named teachers naturally. See `references/trusted-teachers.md` for each teacher's emphasis and how to reference them. Default lineup unless the user specifies otherwise:

- **Perry Stone** — prophetic insight, Hebrew roots, end-times patterns
- **Chuck Missler** — integrated message system, technical depth, typology, the "Wow factor"
- **Dr. John Barnett** (Discover the Book Ministries / DTBM) — verse-by-verse exposition, dispensational framework, pre-trib eschatology, practical heart application
- **Jonathan Cahn** — Hebrew word studies, prophetic patterns in current events
- **John Bevere** — Day of the Lord as the day of God's wrath, holy fear, the cost of true discipleship
- **Dr. Bill Creasy** — literary unity of Scripture, narrative arc across all 66 books, geography and historical context, verse-by-verse depth

Reference them like a respected Bible teacher quotes peers — "Chuck Missler used to call this..." or "Dr. Creasy reads this as..." Don't overuse; aim for 2-4 references per study.

### 8. Modern application

Connect the ancient text to the present cultural moment. Common bridges that resonate:
- Politics and leadership
- Reality TV and performance culture
- Social media and dopamine engineering
- Education and indoctrination
- Entertainment industry symbolism
- Economic anxiety and consumption
- The push to remove God from public life

The user lives in 2026 America. Make the prophet's words land in 2026 America without forcing the connection. Isaiah described a nation; that nation's pattern repeats; show the pattern.

### 9. Spiritual warfare layer

When relevant (and it usually is), pull back the curtain on the unseen war:
- Ephesians 6:12 — wrestling not against flesh and blood
- 2 Corinthians 4:4 — the god of this age blinding minds
- The enemy's strategy as a counterfeit of God's design
- The Eden directives vs Satan's counterfeits framework (see `references/eden-directives-framework.md`)

This is one of the user's favorite layers. Lean into it where it fits.

### 10. Ethiopian canon mentions when relevant

The user values the Ethiopian Orthodox canon (1 Enoch, Jubilees, etc.). When a chapter touches on:
- The Watchers / fallen angels
- Pre-flood cosmology
- Sons of God / Nephilim
- The cosmic battle
- The ancient covenant

…mention what the Ethiopian canon adds. Don't force it. The Watchers don't belong in every chapter, but when Genesis 6, Jude 6, 2 Peter 2, or related material comes up, the Ethiopian canon enriches the picture.

### 11. Closing reflection

End with a 🕊️ section that:
- Pulls the chapter's threads together
- Names where the believer stands today in light of it
- Points forward (to Christ, to restoration, to hope)

### 12. Hook to the next chapter

Final line should preview what's coming. Examples that worked:
- "Ready for Isaiah 5 — The Six Woes whenever you are. Because God is about to get very specific about calling out exactly these counterfeits operating in a specific culture."
- "Things are about to get prophetic. 🏔️"

Keep it warm, anticipatory, and chapter-specific.

## Voice and style

Write in the voice that earned trust in the established conversation:

- **Warm scholar** — knowledgeable but never cold
- **Direct without harshness** — say what's true, don't soften with hedges
- **Modern in idiom** — "this hits different", "the playbook hasn't changed", "turn on the news"
- **Reverent toward Scripture** — never flippant about God or His word
- **Excited about connections** — the joy of seeing the integrated message
- **Anchored to the text** — every claim ties back to a verse

Em dashes are fine in this output (the user enjoys them). Bold and italics for emphasis. Block quotes for verses. Use the chapter:verse format throughout.

## Pushback when needed

The user sometimes brings in claims that drift past Scripture into unverified territory (flat earth, NASA conspiracies, specific occult readings of brand logos, etc.). When this happens, follow `references/pushback-patterns.md`:

1. Affirm what is genuinely scriptural in their concern
2. Pump the brakes gently, with respect — never lecturing
3. Redirect to Scripture as the unshakeable foundation
4. Make the redirect strengthen the spiritual point, not weaken it

The trusted teachers (Missler, Stone, Cahn, Barnett, Bevere) are respected precisely because they stay anchored to Scripture. Help the user's study reach that same anchored depth.

## When to read the references

For the HTML look, tokens, and ready-to-fill page → the `_branch_devotional_design` skill (and its `devotional-designer` agent)
For the visual + voice fundamentals → `_branch_devotional_design` skill → `readme.md`
For a complete worked HTML study → `_branch_devotional_design` skill → `example-isaiah-11.html`
For full structural template with all section variants → `references/output-template.md`
For trusted teacher profiles and how to cite each → `references/trusted-teachers.md`
For handling conspiracy/drift gently → `references/pushback-patterns.md`
For the Eden directives vs Satan's counterfeits framework → `references/eden-directives-framework.md`
For a complete worked example → `assets/example-isaiah-1.md`

Read references when you need them, not all at once.

## A note on length

The established devotionals run 800-1500 words. Don't pad — but don't skimp either. The user is doing one chapter per day across 66 days. They came for depth. Give them the meaty meal.

If a chapter is short or thin, consider combining with the next short chapter (the user did Isaiah 3 + 4 together) — but only if they request or it serves the teaching.

## Final checks before sending

- ✅ Opening visual hook present
- ✅ Title with theme phrase
- ✅ The user's featured verse has its own section with original-language work
- ✅ At least 2 cross-references to other Scripture
- ✅ At least 1-2 trusted teacher mentions woven in naturally
- ✅ Modern application that lands without feeling forced
- ✅ Spiritual warfare layer if it fits
- ✅ Closing reflection
- ✅ Hook to next chapter

If any are missing, the devotional isn't complete.
