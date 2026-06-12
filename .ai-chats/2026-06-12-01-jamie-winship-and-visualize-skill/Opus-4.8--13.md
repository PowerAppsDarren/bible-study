# Exchange 13: Actually I pointed Obsidian at this repo

- **Timestamp:** 2026-06-12
- **Context:** User clarifies they've opened the bible-study repo itself as an Obsidian vault.

## User Input

no, i just pointed obsidian at this repo. :)

## AI Response

Acknowledged the better setup — the whole repo is now the vault. Noted the implications: all the repo's Mermaid renders natively (Winship resources, future `_visualize_this` output, chapter-structure diagrams); Canvas works here too; the external `Visuals.canvas` is now orphaned from this vault. **Practical heads-up:** opening the repo as a vault makes Obsidian create a `.obsidian/` config folder at the repo root — which will show in `git status` — so a decision is needed: gitignore it (keep personal settings out) or commit it (share vault settings with the group). Offered to add `.obsidian/` to `.gitignore` or set it up shared, and to drop a `Visuals.canvas` into the repo.

## Tool Calls

None.

## Files Read/Modified

None.
