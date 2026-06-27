# Exchange 02: Fill scripture / is the Bible public domain? + pilot Psalm 1
- **Timestamp:** 2026-06-24
- **Context:** User wants to start putting actual scripture text into the scripture folders.

## User Input
I want to start filling in scripture in the folders... for  example, here: c:\Users\DarrenNeese\src\bible-study\scripture\19-Psalms\Psalms-001
is the bible not in public domain? can we not have the scripture here?
scripture goes in the scripture folders. personal notes go into the personal folders.
c:\Users\DarrenNeese\src\bible-study\.personal\darren@neese.us\profile.md

*(Follow-up, mid-work):* "let's just do chapter 1 of psalms for now" / "to make sure things settle in right"

## AI Response
Confirmed **yes — the Bible is in the public domain**: WEB, KJV (US), ASV, YLT, etc. are free to host; NIV/ESV/NASB/NLT/NKJV/CSB are copyrighted. Noted CLAUDE.md already bakes this in for margin quotes, but full-text hosting is a new layer. Inspected the repo: Psalms uses **3-digit padding** (`Psalms-001`); each chapter has one stub `README.md`. Asked two decisions via AskUserQuestion → user chose **WEB + KJV + ASV** and **separate text file per version** (alongside README). Piloted Psalm 1: fetched WEB/KJV/ASV from getbible v2 (via PowerShell, since `jq` absent) → `WEB.md`/`KJV.md`/`ASV.md`. Honored "just chapter 1 to settle."

## Tool Calls
- AskUserQuestion (translation set; file layout)
- Bash/PowerShell: getbible v2 fetch for Psalm 1
- Read: README-TEMPLATE.md, .personal/darren@neese.us/profile.md

## Files Read/Modified
- Created `scripture/19-Psalms/Psalms-001/{WEB,KJV,ASV}.md`
