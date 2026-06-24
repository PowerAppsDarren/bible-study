# scripts/

Small **content-population utilities** for this repo. This is *not* a build
system, test runner, or toolchain — the repo stays markdown-only. These scripts
just help fill the folders with text that already exists in the public domain.

## `fetch_scripture.py`

Downloads public-domain scripture text into the chapter folders, writing one
markdown file per translation (`WEB.md`, `KJV.md`, `ASV.md`, …) **next to** each
chapter's `README.md`. It never touches `README.md` — that's your study-notes /
commentary layer. The raw text and your notes stay cleanly separated.

- **Source:** [getbible.net](https://getbible.net) v2 API — free, no key,
  public-domain texts only.
- **Default translations:** `web` (World English Bible), `kjv` (King James),
  `asv` (American Standard 1901), `basicenglish` (Bible in Basic English).
  117 translations are available in total (incl. `ylt`, `kjva` with Strong's
  numbers, and Hebrew/Greek originals) — pass any with `--translations`.
- **Filenames:** most versions write as their uppercase abbreviation
  (`web` → `WEB.md`). A few long names get a short standard stem instead —
  `basicenglish` → `BBE.md`, `douayrheims` → `DRA.md` (see `FILE_STEMS`).
- **No dependencies:** Python 3 standard library only. No `jq`, no `pip install`.
- **Cross-platform:** runs the same on Windows (`python`) and WSL/Linux
  (`python3`). Paths are resolved relative to the repo, never hardcoded.

### Usage

```bash
# one book — every chapter folder it contains, default translations (web kjv asv)
python scripts/fetch_scripture.py scripture/19-Psalms

# choose translations
python scripts/fetch_scripture.py scripture/19-Psalms --translations web kjv

# limit to a chapter range (single book)
python scripts/fetch_scripture.py scripture/01-Genesis --chapters 1-3

# the whole Bible — every book under scripture/
python scripts/fetch_scripture.py --all

# don't overwrite files that already exist
python scripts/fetch_scripture.py scripture/19-Psalms --skip-existing
```

### How it maps folders → references

It reads the folder names already on disk, so there's no hardcoded book table:

- Book number = leading digits of the book folder (`19-Psalms` → book 19)
- Chapter number = trailing digits of the chapter folder (`Psalms-001` → ch 1)

Zero-padding differences (`Psalms-001` vs `Genesis-01`) are handled
automatically because the script mirrors whatever folders exist.

### A translation quirk worth knowing

The **WEB** renders the divine name as **"Yahweh"** where **KJV/ASV** use
**"the LORD"**. That's the WEB's editorial style, not an error.
