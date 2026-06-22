# AI Chat Session: Isaiah 11 Devotional + `_email_study_guide` Skill + Email Delivery

- **Date:** 2026-06-22
- **Model:** Claude Opus 4.8 (1M context)
- **Topic:** Isaiah 11 deep devotional (HTML) → new `_email_study_guide` skill → emailed the study to the Special Mom addresses via Mailgun
- **Tool:** Claude Code
- **Project:** bible-study
- **Exchange Count:** 3 (+ wrap-up)

## 💡 Conversation Summary

Continued the sequential Isaiah walk. Generated the **Isaiah 11** devotional — *"The Branch the Axe Couldn't Touch"* — in the established dark-gold HTML style (matching the Isaiah 10 `devotional.html`), featuring 11:1–2 as the heart: the three Hebrew words for the Branch (*choter* / *geza* / *netzer*, with the *netzer*→Nazareth/Matthew 2:23 payoff) and the sevenfold Spirit rendered as a menorah tied to Revelation's seven Spirits. Sections covered the King who won't judge by optics (11:3–5), the peaceable kingdom (11:6–9), the Eden-reversal serpent layer (11:8, *nachash*/Gen 3:15/Rom 16:20), the *nes* banner (11:10–12, bronze serpent → John 3:14, Romans 15:12), and the second-Exodus highway (11:13–16) — with Missler, Cahn, Creasy, and Perry Stone voices and a hook to Isaiah 12.

The user then asked for a **skill to turn study guides into HTML email and send them**, and mid-build added the recipients (nicole@specialmom.app, darren@specialmom.app). Built `_email_study_guide`: it re-renders a browser `devotional.html` into an **email-safe** parallel `email.html` (table layout, fully inline styles, web-safe fonts, light parchment theme, Hebrew as Unicode) and sends via the **Mailgun HTTP API** with the full dark browser version attached. Sent Isaiah 11 to both recipients, CC darren@spl.tech. The user then said "execute it and send the email," so the skill was invoked formally and the email sent a second time. Registered the skill in `CLAUDE.md` and `.claude/skills/README.md`.

**Key decisions:**
- Email body = **light parchment theme**, not the signature dark-gold — dark HTML emails get force-inverted/mangled across clients. Full dark version rides along as an attachment.
- Send via **Mailgun HTTP API**, not SMTP — the secret on this machine (`~/.claude/secrets/mailgun.json`) holds `MAILGUN_API_KEY`/`MAILGUN_DOMAIN`/`MAILGUN_REGION`/`MAILGUN_FROM`, no SMTP creds. The global `_send_email` skill's SMTP assumption fails here; the new skill documents the API path.
- Standing rule honored: CC darren@spl.tech on every send.

## 🔧 Technical Details

**Created:**
- `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/devotional.html` — full dark-gold browser devotional (~480 lines, mirrors Isaiah-10 CSS).
- `.personal/darren@neese.us/scripture/23-Isaiah/Isaiah-11/email.html` — email-safe parchment rendition (table layout, inline styles).
- `.claude/skills/_email_study_guide/SKILL.md` — new project skill (email-safe conversion rules + Mailgun HTTP API send + archive convention).

**Modified:**
- `CLAUDE.md` — added `_email_study_guide` under Skills → Delivery.
- `.claude/skills/README.md` — new "Delivery skills" table + folded delivery into the compose workflow.

**Email sends (Mailgun HTTP API, domain mail.spl.tech, from support@mail.spl.tech):**
- Send 1 (during build): message id `20260622130717.0dd9255299208c3b@mail.spl.tech` — HTTP 200.
- Send 2 (skill execution): message id `20260622131540.05d21155f8824939@mail.spl.tech` — HTTP 200.
- Recipients: nicole@specialmom.app, darren@specialmom.app; CC darren@spl.tech; attachment `Isaiah-11-full-study.html`.
- Archived under `~/.skills/_send_email/nicole@specialmom.app/` (both sends, `.html` + `.meta.json`).

**Send command shape:** `curl --user "api:$KEY" $BASE/v3/$DOMAIN/messages -F from -F to -F to -F cc -F subject -F text --form-string "html=$(cat email.html)" -F attachment=@devotional.html`. `--form-string` for the html field so shell metacharacters in the markup aren't mangled.

## 📚 Lessons Learned
- **Browser HTML ≠ email HTML.** CSS variables, grid/flex, gradients, and Google Fonts all die in Gmail/Outlook. The reliable path is a separate table-based, inline-styled, light-theme rendition + the pretty version as an attachment.
- **Verify the secret's actual keys before scripting a send.** The first attempt used `smtplib` per the global skill doc and hit `KeyError: MAILGUN_SMTP_USERNAME` — the secret was API-key-based. Inspect `list(d.keys())` first.
- **Region matters** for Mailgun base URL (`api.eu.mailgun.net` vs `api.mailgun.net`); derive it from `MAILGUN_REGION`.

## ⏭️ Next Steps
- Isaiah 12 next chapter (the song of the redeemed — "wells of salvation," *Yeshua*).
- Optional: promote Isaiah 11 gate-passing facts to shared `scripture/23-Isaiah/Isaiah-11/README.md`.
- Duplicate-send is benign; if re-sending becomes routine, consider a guard in the skill.

## 📁 Exchange Index
- [01 — Isaiah 11 devotional](./Opus-4.8--01.md)
- [02 — Create `_email_study_guide` skill + first send](./Opus-4.8--02.md)
- [03 — Execute the skill + second send](./Opus-4.8--03.md)
