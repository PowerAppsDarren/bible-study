# Exchange 08: Remember BBE is the default; "that's the one to show"
- **Timestamp:** 2026-06-25
- **Context:** Locking the default version and the README layout.

## User Input
1. "put that html page in my personal folder pls"
2. "remember this: make BBE our default version we use for everything, unless otherwise stated"
3. "so, in the readme files, that's the one to show"

## AI Response
Copied the demo to `.personal/darren@neese.us/readme-options-demo.html`. Saved a **memory file** (`bible-default-version-bbe.md`) + MEMORY.md index line: **BBE is primary for everything unless Darren names another version** (WEB/KJV/ASV stay as comparisons; Hebrew/Greek still from originals). Confirmed BBE is the text shown in READMEs → that rules out the link-only grid (Option C). Refreshed the HTML demo with **BBE as the lead text** (compare-links to WEB/KJV/ASV) and re-sent it; narrowed the choice to readable table (A) vs prose (B).

## Tool Calls
- Bash: cp demo to personal folder
- Write: memory bible-default-version-bbe.md; Edit MEMORY.md
- Write + SendUserFile: refreshed demo

## Files Read/Modified
- Created .personal/darren@neese.us/readme-options-demo.html
- Created memory bible-default-version-bbe.md; updated MEMORY.md
