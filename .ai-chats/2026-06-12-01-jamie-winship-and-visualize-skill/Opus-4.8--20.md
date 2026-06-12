# Exchange 20: Store workspace.json in personal folder?

- **Timestamp:** 2026-06-12
- **Context:** User proposes storing workspace.json in their personal folder to get sync without collisions.

## User Input

what about storing it in my personal folder?

## AI Response

Called it the right design (fits the two-layer model), with one catch: Obsidian only reads `workspace.json` from `.obsidian/`, so the real file goes in `.personal/<email>/` and `.obsidian/workspace.json` is **linked** to it. Payoff: syncs across the user's machines, no collisions (it's in their email folder), churn-without-conflict. Costs: one-time symlink per workstation (Windows needs Developer Mode/admin), and it can break if Obsidian rewrites the file by delete-and-recreate. Offered to set it up: move the file, create the link on this machine, and add a `link-workspace.ps1` for per-machine setup.

## Tool Calls

None.

## Files Read/Modified

None.
