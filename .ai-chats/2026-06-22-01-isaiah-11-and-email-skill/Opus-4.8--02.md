# Exchange 02: Create `_email_study_guide` skill + first send

- **Timestamp:** 2026-06-22
- **Context:** Right after the Isaiah 11 devotional. User asked for a reusable skill to email generated study guides; mid-build, supplied the recipients as a second message.

## User Input

```
can you create a skill to create html email to send out great study guide that you generate
```

Then, while work was in progress:

```
email it to nicole and me: nicole@specialmom.app and darren@specialmom.app
```

## AI Response

Identified the core problem: the browser devotionals rely on CSS variables, grid, gradients, and Google Fonts — all stripped by Gmail/Outlook — so the skill must produce a separate email-safe rendition and attach the full browser version.

Inspected the project skills layout, the `_deep_bible_study_devotional` frontmatter, and the global `_send_email` skill. Confirmed `~/.claude/secrets/mailgun.json` exists.

First send attempt used Python `smtplib` per the `_send_email` doc → failed with `KeyError: 'MAILGUN_SMTP_USERNAME'`. Inspected the secret's keys: `MAILGUN_API_KEY`, `MAILGUN_DOMAIN`, `MAILGUN_REGION`, `MAILGUN_FROM` — HTTP-API-only, no SMTP. Switched to the Mailgun HTTP API via curl.

Built `email.html` (email-safe parchment rendition of Isaiah 11) and sent it: to nicole@specialmom.app + darren@specialmom.app, CC darren@spl.tech, full `devotional.html` attached as `Isaiah-11-full-study.html`. Result: `{"id":"<20260622130717.0dd9255299208c3b@mail.spl.tech>","message":"Queued. Thank you."}`, HTTP 200.

Wrote the skill `.claude/skills/_email_study_guide/SKILL.md` (conversion hard-rules + HTTP-API send + archive convention + two-layer note + checklist). Registered it in `CLAUDE.md` (Skills → Delivery) and `.claude/skills/README.md` (new Delivery table + compose-workflow mention). Archived the send under `~/.skills/_send_email/nicole@specialmom.app/`.

Reported the send + the new skill, and noted the one judgment call (light parchment email theme vs. dark, dark attached for fidelity).

## Tool Calls
- `Bash` — inspect skills, devotional frontmatter, mailgun secret presence, `_send_email` location
- `Read` — `~/.claude/skills/_send_email/SKILL.md`
- `Write` — `Isaiah-11/email.html`
- `Bash` — Python `smtplib` send attempt (**failed**, KeyError)
- `Bash` — `python -c` to list secret keys
- `Bash` — curl Mailgun HTTP API send (**HTTP 200**)
- `Write` — `.claude/skills/_email_study_guide/SKILL.md`
- `Bash` — archive send + meta
- `Grep`/`Read`/`Edit` — register skill in `CLAUDE.md` and `.claude/skills/README.md`

## Function Results
- smtplib attempt: `KeyError: 'MAILGUN_SMTP_USERNAME'` (secret is API-key-based).
- Secret keys: `['MAILGUN_API_KEY', 'MAILGUN_DOMAIN', 'MAILGUN_REGION', 'MAILGUN_FROM', 'stored_at']`.
- Send: region base `https://api.mailgun.net`, domain `mail.spl.tech`, from `support@mail.spl.tech`; queued, HTTP 200.

## Files Read/Modified
- Read: `~/.claude/skills/_send_email/SKILL.md`
- Created: `Isaiah-11/email.html`, `.claude/skills/_email_study_guide/SKILL.md`
- Modified: `CLAUDE.md`, `.claude/skills/README.md`
- Archive: `~/.skills/_send_email/nicole@specialmom.app/20260622-130717-isaiah-11-the-branch.{html,meta.json}`
