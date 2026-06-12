# Exchange 11: Find my Obsidian vault

- **Timestamp:** 2026-06-12
- **Context:** User asks whether their Obsidian vault can be located under ~/Documents.

## User Input

can you find my obsidian vault in ~/Documents ??

## AI Response

Found one vault: **`C:\Users\DarrenNeese\Documents\Darren\`** (the `.obsidian` config folder lives inside it). Summarized it: 3,188 markdown notes (3,563 files), organized in a PARA + Johnny-Decimal system (`00-META`, `10-INBOX`, `20-MAPS`, `30-CALENDAR`, `40-PROJECTS`, `50-AREAs`, `60-RESOURCES`, `70-JOURNAL`, `80-ARCHIVE`, `90-UTILITY`, `95-CARDS`, `Tags`). Most-recent activity late May 2026 (`20-MAPS/Vault-Health.md`, journal entries, a Qdrant alert project, a Claude resources area). Noted it's the only vault under `~/Documents` (searched 4 levels for `.obsidian`), and that since Obsidian renders Mermaid natively, `_visualize_this` output would display inline there.

## Tool Calls

- `Bash` `find ~/Documents -maxdepth 4 -type d -name .obsidian`
- `Bash` summarize vault (top folders, counts, recent notes)

## Files Read/Modified

None (read-only).
