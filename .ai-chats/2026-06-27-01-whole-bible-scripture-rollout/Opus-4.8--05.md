# Exchange 05: Add BBE; README verse-index with per-version links
- **Timestamp:** 2026-06-24
- **Context:** Adding a plainer version, then making READMEs navigable.

## User Input
1. "add basicenglish to our fetches. then get the book of psalms from that version in the repo"
2. "the readme file in each chapter folder should provide a markdown listing of all verses. each verse number should have a link reference for all the versions that are in that folder. make sense?"

## AI Response
Added **`basicenglish` to the default fetch set** with a clean filename **`BBE.md`** (via `FILE_STEMS`); fetched BBE for all 150 Psalms (now 4 versions each). Then built the verse-index feature in two parts: (1) added **per-verse `<a id="vN">` anchors** to every version file (re-ran fetch render; injected anchors into the existing 596 files locally to avoid re-downloading); (2) wrote `scripts/build_readme_index.py` to generate a **Verses table** in each README linking every verse to all present versions, wrapped in regenerate-safe markers. Piloted on Psalm 1, then rolled to all 150. (This first layout was a link-only grid — later replaced by the BBE-primary readable table.)

## Tool Calls
- Edit: fetch_scripture.py (basicenglish default, FILE_STEMS, anchors in render)
- Write: scripts/build_readme_index.py
- Bash: BBE fetch ×150; anchor injection; build READMEs ×150; spot-checks

## Files Read/Modified
- Created 150 `BBE.md`; anchored 596 version files; rebuilt 150 READMEs
- Created scripts/build_readme_index.py
