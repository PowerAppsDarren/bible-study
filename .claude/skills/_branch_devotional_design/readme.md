# The Branch — Devotional Study Design System

A warm, low-light "scriptorium" system for deep, verse-by-verse devotional studies.
Built to scale to **one study per Bible chapter** plus standalone pieces (word
studies, topical reflections). Derived and elevated from the original
*Isaiah 11 — "The Branch the Axe Couldn't Touch"* study.

The name comes from Isaiah 11:1 — *netzer*, the Branch from the cut stump. The
whole look is built on that image: deep, burned-down grounds (the stump) lit by a
single warm lamp, with one green shoot of life (olive) and gold of the Spirit.

> **Origin:** this system was designed on claude.ai/design (project
> *"Design system creation"*) and imported into this repo. The repo copy below is
> the canonical, browser-native version the `_deep_bible_study_devotional` skill
> builds against. The `.dc.html` files in the design project are claude.ai-design
> source; `devotional-template.html` here is the implemented, standalone artifact.

---

## Sources
- Seed artifact: the Isaiah 11 study at
  `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/devotional.html`.
- This system refines its palette, type, spacing, and components into a reusable kit.

## Files / manifest
- **`styles.css`** — global entry (import this). Pulls in the three token files.
- **`tokens/colors.css`** — grounds, inks, the four scripture accents, washes, semantic aliases.
- **`tokens/typography.css`** — three font families, fluid type scale, line-heights, tracking.
- **`tokens/spacing.css`** — spacing scale, measures, radii, borders, glows, motion.
- **`devotional-template.html`** — a **ready-to-fill chapter page**, standalone and
  browser-native. Duplicate it per chapter and replace the `[bracketed]` content.
  **Start here for a new study.**
- **`example-isaiah-11.html`** — the template **filled** with the seed Isaiah 11 study;
  the worked reference for voice, depth, and how the components carry real content.

> The template styles **inline** (no shared stylesheet at runtime) so a single
> `.html` file is fully self-contained and portable — it can be emailed, archived,
> or opened offline with no dependencies. The token files are the **canonical
> source of truth**; the template mirrors those exact literal values inline. When a
> token changes, update it here AND in `devotional-template.html`.

---

## CONTENT FUNDAMENTALS — how the writing works

This is the soul of the system. The visuals serve the voice.

- **Voice:** a warm, awed teacher sitting next to you, not a lecturer above you.
  Confident and reverent, never stiff or academic-cold. It marvels out loud
  ("Here's the secret.", "Watch the upgrade.", "Isaiah saw the rod of His mouth;
  John filmed it.").
- **Person:** mostly **second person** — talks *to* the reader ("You have to read
  the last line of chapter 10…", "that's you"). First-person plural ("we live as
  people who already know the ending") for the closing turn. Avoid detached third
  person.
- **Tense / immediacy:** present-tense and physical. Abstractions get grounded in
  images you can see and touch (a twig you could snap, a hand in a snake's den,
  footage and rumors). Modern parallels are welcome and pointed (optics, deepfakes,
  trial-by-timeline) — they make an ancient text land *now*.
- **Casing:** sentence case for headings and body. **Small-caps-style tracked
  uppercase** is reserved for kickers, scripture references, and labels only
  (`letter-spacing: .28em`).
- **Scripture quotes:** italic serif, set apart in verse blocks. Always cited with
  a tracked, uppercase, accent-colored reference (`ISAIAH 11:1`).
- **Hebrew:** the original word is a recurring star. Give it room: large, gold,
  RTL, followed by an italic transliteration and a plain-language gloss. Treat the
  word as a discovery, not a footnote.
- **Emphasis:** **bold** lands the single most important phrase in a paragraph
  (the "punch"); *italic* carries quoted scripture and gentle stress. Don't bold
  more than one idea per paragraph.
- **Structure of a study:** a hook (chapter-to-chapter cliffhanger) → verse-by-verse
  sections, each opening on a scripture block → word studies → a "layer under the
  layer" insight → teacher callouts (named voices) → a three-pillar closing → a
  next-chapter teaser. Not every study needs every part; keep the rhythm.
- **Teacher callouts:** quote named teachers respectfully and specifically (what
  they'd "light up at" or "point straight at"). They add chorus, not authority over
  the text.
- **Emoji:** **yes — kept on purpose.** Used as section glyphs and small accents
  (🌱 stump/shoot, 🕎 Spirit/menorah, ⚖️ judgment, 🐺🐑 the pairs, 🚩 banner,
  🕊️ peace, 💧 water). One per section header, plus the occasional inline accent.
  Never decorative spam; each emoji *is* the section's image. See ICONOGRAPHY.

---

## VISUAL FOUNDATIONS

**Overall mood:** an illuminated manuscript read by lamplight. Dark, warm, hushed,
reverent — but modern and legible, not gothic-kitsch. Long-form reading first.

**Color**
- Grounds are warm near-blacks layered in four steps (`--bg` → `--panel-2`) so depth
  reads as lamplight on parchment, not flat black.
- Inks are parchment, never pure white (`--ink #ece4d5`, headings `--ink-strong`).
- Four scripture accents, one tonal family (shared OKLCH lightness/chroma band):
  **gold** = the Branch / the Spirit / the divine (primary); **olive** = life,
  growth, peace, the living stump; **ember** = judgment, fire, warning; **sky** =
  the nations, water, hope. Use accent color to *mean* something, not to decorate.
- Saturated color is rationed. Most of any page is ground + ink; accents are the
  punctuation.

**Type** — see `tokens/typography.css`. Cormorant Garamond (display + scripture,
often italic), Inter (body + labels), Noto Serif Hebrew (the source word). Body at
17.5px / 1.78 line-height for comfortable long reading.

**Backgrounds:** flat warm grounds plus **low-alpha radial glows** behind hero,
featured, and closing slabs (olive from the top, gold from the bottom) — lamplight
pooling, ~10–20% alpha. No photographic backgrounds, no busy textures, no noise.
For imagery slots, use a subtly-striped placeholder with a monospace caption (never
hand-drawn SVG art).

**Cards:** calm rectangles. `--panel` surface, 1px `--line` hairline border,
`--r-md` (16px) radius, generous padding (26–30px). Some cards carry a 3px **top
accent bar** (gradient fading to transparent) or a 3px **left accent bar** (verses)
to signal type/meaning. Featured + closing use `--r-lg` (20px) and an inner glow.

**Borders:** hairline (1px `--line`) is the default separator everywhere. Accent
borders (verse left-bar, card top-bar) are 3px and gradient-washed. Dashed accent
border is reserved for the "next chapter" teaser (a not-yet, looking-ahead feel).

**Shadows / depth:** almost none. Depth = layered grounds + glows. A soft lift
(`--shadow-card`) is allowed on hover only.

**Radii:** 12 / 16 / 20 / pill. Consistent and soft, never sharp, never fully round
except labels and avatars.

**Motion:** restrained. Fades and gentle lifts (`--dur-base` 240ms, `--ease`).
Cards may lift 2–3px and brighten their border on hover. No bounces, no parallax,
no attention-seeking animation — the text is the event.

**Layout:** single centered reading column, `--measure` 860px. Sections separated
by `--space-9` (80px). Narrow callouts/teasers use `--measure-narrow` 640px. Word
cards and pairs use responsive `auto-fit` grids with `gap`.

**Hover / press:** hover = border brightens toward the relevant accent + 2–3px lift;
press = settle back (no shrink gimmicks). Links/refs brighten in their accent color.

---

## ICONOGRAPHY

This system **embraces emoji** as its iconography — it's part of the charm and the
teaching. Rules:
- **One emoji per section header**, living in a rounded `--panel-2` tile (54px,
  `--r-sm`, hairline border). The emoji *is* the section's central image.
- Recurring vocabulary: 🌱 stump/shoot/growth · ❄️ stillness/turning point ·
  🕎🔥 Spirit/menorah · ⚖️ judgment/justice · 🐺🐑🐆🐐🦁🐄👶🐍 the peaceable-kingdom
  pairs · 🚩 banner/ensign · 🛣️ highway/journey · 🕊️ peace · 💧 water/salvation.
- Small inline emoji are allowed inside hooks and dividers as a single accent.
- **No hand-drawn SVG illustrations.** Geometric primitives (circles, the flame
  radial-gradient dot) are fine; pictorial art is always emoji or a labelled image
  placeholder.
- Avatars in teacher callouts are **initials** in a gold→olive gradient circle, not
  photos.

---

## Reuse — to make a new study
1. Duplicate `devotional-template.html`, rename it for the chapter (e.g.
   `isaiah-12.html`), and save it in the study's personal folder
   (`.personal/<email>/scripture/<NN-Book>/<Book-NN>/`).
2. Replace every `[bracketed]` placeholder; delete the guide banner at the top.
3. Follow the voice in CONTENT FUNDAMENTALS above: second person, present tense, one
   bolded punch per paragraph, scripture in italic serif with a tracked uppercase
   reference.
4. Keep **accent meanings** consistent so the whole canon reads as one work:
   - **gold** — the divine / default
   - **olive** — life, growth, peace
   - **ember** — judgment, fire, warning
   - **sky** — the nations, water, hope
5. One **featured verse** per study. Use the **menorah list** only for enumerated
   ideas, **pairs** for contrasts, **teacher callouts** for named voices.

Keep accent meanings consistent across studies so the whole canon reads as one work.
The `_email_study_guide` skill re-renders the finished study as an email-safe parchment
email from the same palette — keep the literal accent hex values aligned with the tokens
so the browser and email versions match.
