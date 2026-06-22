---
name: _email_study_guide
description: Turn a generated Bible study guide (a devotional.html or chapter study) into an email-safe HTML email and send it to a group via Mailgun. Use when the user says "email this study", "send this devotional to...", "email the study guide to the group", "mail Isaiah 11 to...", or otherwise wants a study guide delivered by email. Converts the rich browser devotional (CSS variables, grid, gradients, web fonts — all of which Gmail/Outlook strip) into a bulletproof table-based, inline-styled parchment email, attaches the full illustrated browser version for fidelity, CCs darren@spl.tech, and archives the send.
---

# Email Study Guide

Take a study guide this repo generates (normally a `devotional.html` from `_deep_bible_study_devotional`, but any chapter/topic study works) and **email it to people** in a form that actually renders in their inbox.

## The core problem this skill solves

The browser devotionals are gorgeous because they use modern CSS — `var(--gold)` custom properties, CSS grid, flexbox, `clamp()`, radial-gradients, and Google web fonts. **Email clients destroy all of that.** Gmail strips `<head><style>` rules it doesn't like and ignores CSS variables entirely; Outlook (Word rendering engine) ignores background images, grid, and flex; web fonts don't load. Send the raw `devotional.html` and most people see a broken, unstyled wall of text.

So this skill does **not** forward the browser HTML as the body. It produces a **parallel email-safe rendition** of the same study, and attaches the full browser version as an `.html` file so anyone can open the beautiful one too.

## When to use

- User asks to email / send / mail a study guide or devotional to one or more people
- Right after generating a study with `_deep_bible_study_devotional`, when the user wants it delivered
- User says "send the group this week's study"

## Inputs

- **Source study** — path to the `devotional.html` (default: the one just generated this session). If only markdown/chapter content exists, render the email directly from that.
- **Recipients (`to`)** — one or more email addresses. Ask if not given.
- **Subject** — default to the study's title, e.g. `Isaiah 11 — "The Branch the Axe Couldn't Touch" (Bible Study)`.

## Workflow

### Step 1 — Locate the source study
Find the `devotional.html` (usually `.personal/<email>/scripture/<NN-Book>/<Book-NN>/devotional.html`). Read it so you have the title, theme phrase, sections, verses, Hebrew word cards, teacher callouts, and the next-chapter hook.

### Step 2 — Build the email-safe HTML (`email.html` beside the source)

Re-render the study following these **hard rules** (this is what survives Gmail + Outlook + Apple Mail + mobile):

1. **Table layout only.** One outer `<table>` for the background, one centered inner `<table width="600">` for the card. No CSS grid, no flexbox for layout.
2. **Inline styles on every element.** Put colors, borders, padding, font-size directly in `style="..."`. The `<head><style>` block is allowed ONLY for: `body` reset, `a` color, and one `@media (max-width:620px)` block that sets `.container{width:100%}` and `.pad{padding:20px}`. Assume nothing in `<head>` survives except those.
3. **No CSS variables.** Every color is a literal hex. (Resolve the browser theme: gold `#b8923a`/`#d4a843`, olive `#6f8f4f`/`#7c9a5c`, ember `#b4503a`, sky `#6da3c4`, ink `#2c2417`.)
4. **Web-safe fonts only.** `font-family:Georgia,'Times New Roman',serif` for the body/headings (evokes the Cormorant serif); `Arial,Helvetica,sans-serif` for kickers/labels. No Google Fonts links.
5. **Theme = light parchment, not dark.** Outer bg `#efe7d6`, card `#fffdf8`. Dark backgrounds in email get force-inverted or look broken on some clients — use a warm parchment/illuminated-manuscript light theme for the body, and reserve a dark panel ONLY for the single featured-verse block (where `bgcolor` on a table cell is reliable). Add `<meta name="color-scheme" content="light only">` and `supported-color-schemes` so clients don't dark-mode-invert it.
6. **Hebrew** renders as Unicode entities or raw Unicode in a `<span>` with a gold color and larger size — default client fonts display Hebrew fine; do NOT rely on Noto Serif Hebrew loading. Include the transliteration right under it.
7. **Verses** = a one-cell table with `border-left:4px solid <accent>` and a tinted bg, rounded right corners. **Word studies** = stacked one-cell tables with a `border-top:3px solid` accent. **Teacher callouts** = a tinted panel with the teacher name in an uppercase Arial label.
8. **Emoji** in headers are fine (Unicode entities, e.g. `&#x1F331;` 🌱). Keep one per section like the browser version.
9. Include a hidden **preheader** div (the one-line hook) right after `<body>`.
10. Footer line notes: "The full illustrated version is attached as an HTML file — open it in any browser."

Keep all the substance — every section, the featured verse with its three Hebrew word cards, the sevenfold-Spirit list, the cross-references, the teacher voices, the closing three pillars, and the next-chapter hook. An email can be long; it's a study guide.

Use the most recent committed `email.html` in the repo as the reference implementation (e.g. `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/email.html`).

### Step 3 — Send via Mailgun HTTP API

The repo's Mailgun secret (`~/.claude/secrets/mailgun.json`) holds the **HTTP API key** (`MAILGUN_API_KEY`, `MAILGUN_DOMAIN`, `MAILGUN_REGION`, `MAILGUN_FROM`) — **not** SMTP creds. So send via the HTTP API, not `smtplib`. Standing rule: **always CC `darren@spl.tech`.**

```bash
cd "<folder with email.html and devotional.html>"
eval $(python -c "
import json,os
d=json.load(open(os.path.expanduser('~/.claude/secrets/mailgun.json')))
region=(d.get('MAILGUN_REGION') or '').lower()
base='https://api.eu.mailgun.net' if region.startswith('eu') else 'https://api.mailgun.net'
print(f'export MG_KEY={d[\"MAILGUN_API_KEY\"]!r}')
print(f'export MG_DOMAIN={d[\"MAILGUN_DOMAIN\"]!r}')
print(f'export MG_FROM={d[\"MAILGUN_FROM\"]!r}')
print(f'export MG_BASE={base!r}')
")
curl -s --user "api:$MG_KEY" "$MG_BASE/v3/$MG_DOMAIN/messages" \
  -F from="Bible Study <$MG_FROM>" \
  -F to="<recipient1>" -F to="<recipient2>" \
  -F cc="darren@spl.tech" \
  -F subject="<subject>" \
  -F text="<plain-text fallback summary>" \
  --form-string "html=$(cat email.html)" \
  -F attachment=@devotional.html \
  -w $'\nHTTP %{http_code}\n'
```

A `{"id":"...","message":"Queued. Thank you."}` with `HTTP 200` means it sent. Each `-F to=` adds a recipient; repeat for the group. Use `--form-string` for the html field so `$` and other shell metacharacters in the HTML aren't mangled.

### Step 4 — Archive
Mirror `_send_email`'s archive convention so there's a permanent record:
`~/.skills/_send_email/<first-recipient>/<YYYYMMDD-HHMMSS>-<pid>-<slug>.html` plus a `.meta.json` ({to, cc, subject, from, method:"mailgun-http-api", mailgun id, status}). Never use `/tmp`.

### Step 5 — Report
Tell the user who it went to, the subject, the Mailgun id, and where `email.html` + the archive live.

## Two-layer note

`email.html` is a derived artifact of a personal-layer study — write it into the **same personal folder** as its `devotional.html` (`.personal/<email>/scripture/...`). Don't put email renditions in the shared `scripture/` tree.

## Composition

- Upstream: `_deep_bible_study_devotional` generates the `devotional.html` this skill emails.
- Reuses the Mailgun credentials and archive convention from the global `_send_email` skill (but uses the HTTP API path, since this machine's secret is API-key-based).

## Checklist before sending

- ✅ `email.html` is table-based, fully inline-styled, light parchment theme, web-safe fonts
- ✅ No CSS variables / grid / flex / web-font links in the body
- ✅ Featured verse + all sections + teacher voices + next-chapter hook carried over
- ✅ Full browser `devotional.html` attached
- ✅ `darren@spl.tech` CC'd
- ✅ Plain-text fallback set
- ✅ Send returned HTTP 200 + a Mailgun queue id
- ✅ Archived under `~/.skills/_send_email/<recipient>/`
