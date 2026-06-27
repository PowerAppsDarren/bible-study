# Exchange 09: Terminal font 18 → 24
- **Timestamp:** 2026-06-26
- **Context:** User finds the VS Code terminal hard to read.

## User Input
1. "make our terminal font bigger please here in vs code"
2. "having a hard time reading all this" / "what is it set at now?" / "maybe bump it up 3pts"
3. "go with 24"

## AI Response
Located the VS Code **user** settings (`%APPDATA%/Code/User/settings.json`) — the right place for a personal preference (not the protected workspace `.vscode/settings.json`). Current `terminal.integrated.fontSize` was **18**; bumped to **21** (+3), then to **24** on request. Applies live.

## Tool Calls
- Bash/Read: locate + read user settings.json
- Edit: terminal.integrated.fontSize 18→21→24

## Files Read/Modified
- Edited C:\Users\DarrenNeese\AppData\Roaming\Code\User\settings.json
