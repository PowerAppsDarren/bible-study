# Exchange 02 — Shared-Layer Integration Gate

## User (a)

> Hey, whenever we do a bible study as an individual, I feel like we should be filling things out in the main portion of the repo. can you provide any advice and guidance on how we can plan and structure that moving forward?

## Assistant (a)

Diagnosed the gap: chapter studies produce personal output (`.personal/.../scripture/23-Isaiah/Isaiah-10/devotional.html`), but the shared `scripture/23-Isaiah/Isaiah-10/README.md` stays a `# Read Me` stub. The factual substance is reference-quality material that belongs in the shared layer, and `_chapter_readme_fill` already exists to extract it — it's just never invoked as part of the study flow.

Recommended **"study once, deposit twice"**: each study deposits a shared README (factual residue) and a personal devotional (reflection). Offered three options (a) chain the skills, (b) chain + backfill Isaiah 1–10, (c) keep manual.

## User (b)

> I don't want to clutter up the non-personal stuff though either. we need good helpful and valuable material in the non-personal area, but there should be a gate or a standard by which it is determined on what to integrate and what not to.
>
> *(then, via /model switch to Opus 4.8, and:)* pls proceed

## User (c)

> everything should be nice, clean, tidy, and orderly!

## Assistant (b/c)

Recognized the new constraint as the important one: a **value gate**, not just the category rule the repo already had. A fact can be perfectly true and still be clutter if it just restates the verse.

Anchored the design in existing standards (`CONTRIBUTING.md`, `_chapter_readme_fill` discipline, `README-TEMPLATE.md`), then wrote the gate.

### The Shared-Layer Integration Gate

Principle: the shared layer is curated, not a dumping ground — **an honest stub beats a padded margin.** Default state of a chapter README is empty; content earns its way in.

A candidate line is admitted only if it passes all six:
1. **Factual, not personal**
2. **Margin-worthy** (tells the reader something the verse alone doesn't)
3. **Durable**
4. **Sourceable**
5. **Non-sectarian**
6. **License-clean** (KJV/ASV/WEB or paraphrase, ≤25 words)

Plus **study once, deposit twice** routing and a **chapter-promotion rule** (don't manufacture thin sections around one good cross-ref).

### Codified (single source of truth, no drift)

- **`CLAUDE.md`** — authoritative `## Shared-layer integration gate` section.
- **`_chapter_readme_fill/SKILL.md`** — gate-check as an explicit workflow step + a Discipline pointer.
- **`CONTRIBUTING.md`** — human-facing summary that defers to CLAUDE.md; also corrected the stale "`.personal/` is gitignored" claims in the two-layer table, the personal-notes paragraph, and the backup section so the doc is coherent with the deposit-twice model.

**Commit `33b9472`** — docs(shared-layer): add the Shared-Layer Integration Gate.
