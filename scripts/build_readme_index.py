#!/usr/bin/env python3
"""Build each chapter's README.md front page: metadata header, nav, and a
BBE-primary verse index.

Layout produced (per the approved design):

    ---
    book: Psalms          # metadata header — search & graph can filter on these
    chapter: 1
    genre: Poetry / Worship
    verses: 6
    primary: BBE
    versions: [BBE, WEB, KJV, ASV]
    themes: []            # filled later by a real study, never by this sweep
    ---

    # Psalms 1

    <!-- BEGIN AUTO-INDEX ... -->
    ↑ Psalms  ·  Psalm 2 ›                       <- prev / next / up nav
    📖 Full text: BBE · WEB · KJV · ASV          <- whole-chapter links

    ## Verses (6)
    | # | Bible in Basic English | Compare |     <- BBE text + compare links
    | 1 | Happy is the man...     | WEB · KJV · ASV |
    <!-- END AUTO-INDEX -->

    ## At a glance
    _Poetry / Worship — to be filled: theme · structure._

    ## Study notes
    _Factual, shared-layer ... Personal reflection → .personal/<you>/..._
    ### Key verses / Summary / Notes / Cross references / Questions

What's AUTO vs HAND-WRITTEN
---------------------------
Everything between the AUTO-INDEX markers (nav + full-text links + verse table)
is regenerated every run — safe to re-run forever. The metadata header is
*merged*: derivable keys (book/chapter/genre/verses/primary/versions) are
refreshed, but `themes` and any hand-added keys are preserved. Everything after
the END marker (At a glance + Study notes) is hand/agent territory and is never
clobbered once it holds real content. Empty placeholder templates are replaced
with the clean current structure.

BBE (Bible in Basic English) is the primary/default version (Darren's standing
instruction); the others appear as compare-links. Verse deep-links rely on the
<a id="vN"> anchors that fetch_scripture.py writes into each translation file.

Usage:
    python scripts/build_readme_index.py scripture/19-Psalms
    python scripts/build_readme_index.py scripture/19-Psalms --chapters 1-3
    python scripts/build_readme_index.py --all

Standard library only. Runs the same on Windows (python) and WSL/Linux (python3).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTURE = REPO_ROOT / "scripture"

AUTO_BEGIN = "<!-- BEGIN AUTO-INDEX (verse table + nav; auto-generated — safe to regenerate) -->"
AUTO_END = "<!-- END AUTO-INDEX -->"
OLD_END = "<!-- END VERSE-INDEX -->"  # recognize & migrate the first-pass format

# Column order: BBE first (primary), then the rest; anything unknown trails alpha.
VERSION_ORDER = ["BBE", "WEB", "KJV", "ASV", "YLT", "KJVA", "AKJV", "WB", "DRA",
                 "TYNDALE", "WEYMOUTH", "WYCLIFFE"]
PRIMARY_PREF = "BBE"
NON_VERSION = {"README.md", "notes.md", "NOTES.md", "study.md"}

FM_ORDER = ["book", "chapter", "genre", "verses", "primary", "versions", "themes"]

# Book-number → genre (durable, book-level; per-chapter nuance goes in "At a glance").
GENRE = {}
for _n in range(1, 6):   GENRE[_n] = "Law (Torah)"
for _n in range(6, 18):  GENRE[_n] = "History"
GENRE[18] = "Wisdom"; GENRE[19] = "Poetry / Worship"; GENRE[20] = "Wisdom"
GENRE[21] = "Wisdom"; GENRE[22] = "Poetry / Wisdom"
for _n in range(23, 28): GENRE[_n] = "Prophets (Major)"
for _n in range(28, 40): GENRE[_n] = "Prophets (Minor)"
for _n in range(40, 44): GENRE[_n] = "Gospel"
GENRE[44] = "History (NT)"
for _n in range(45, 58): GENRE[_n] = "Epistle (Pauline)"
GENRE[58] = "Epistle"
for _n in range(59, 66): GENRE[_n] = "Epistle (General)"
GENRE[66] = "Apocalyptic / Prophecy"


# ---------- discovery helpers ----------

def book_number(book_dir: Path):
    m = re.match(r"^(\d+)-", book_dir.name)
    return int(m.group(1)) if m else None


def book_label(book_dir: Path) -> str:
    return re.sub(r"^\d+-", "", book_dir.name).replace("-", " ")


def chapter_folders(book_dir: Path):
    found = []
    for child in book_dir.iterdir():
        m = re.search(r"-(\d+)$", child.name) if child.is_dir() else None
        if m:
            found.append((int(m.group(1)), child))
    found.sort(key=lambda t: t[0])
    return found


def version_files(folder: Path):
    files = {p.stem: p for p in folder.glob("*.md") if p.name not in NON_VERSION}
    ordered = [s for s in VERSION_ORDER if s in files]
    ordered += sorted(s for s in files if s not in VERSION_ORDER)
    return [(s, files[s]) for s in ordered]


# ---------- version-file parsing ----------

def verses_present(path: Path):
    txt = path.read_text(encoding="utf-8")
    nums = {int(n) for n in re.findall(r'id="v(\d+)"', txt)}
    if not nums:
        nums = {int(n) for n in re.findall(r"(?m)^\*\*(\d+)\*\*", txt)}
    return nums


def parse_verse_text(path: Path):
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^(?:<a id="v(\d+)"></a>)?\*\*(\d+)\*\*\s*(.*)$', line)
        if m:
            out[int(m.group(1) or m.group(2))] = m.group(3).strip()
    return out


def full_name(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    m = re.match(r"#\s*.+?\s+—\s+(.+?)\s*\(", first)
    return m.group(1).strip() if m else path.stem


# ---------- front matter ----------

def fm_parse(content: str):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.S)
    if not m:
        return {}, content
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


def fm_build(existing, book, chapter, genre, verses, primary, labels):
    fm = dict(existing)
    fm.update(book=book, chapter=chapter, genre=genre, verses=verses, primary=primary,
              versions="[" + ", ".join(labels) + "]")
    fm.setdefault("themes", "[]")
    return fm


def fm_serialize(fm) -> str:
    lines = ["---"]
    for k in FM_ORDER:
        if k in fm:
            lines.append(f"{k}: {fm[k]}")
    for k, v in fm.items():
        if k not in FM_ORDER:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


# ---------- body sections ----------

def glance_section(genre: str) -> str:
    hint = f"_{genre} — to be filled: theme · structure._" if genre else "_To be filled: genre · theme · structure._"
    return f"## At a glance\n\n{hint}"


def notes_section(book_dirname: str, foldername: str) -> str:
    personal = f".personal/<you>/scripture/{book_dirname}/{foldername}/"
    return (
        "## Study notes\n\n"
        f"_Factual, shared-layer notes that clear the integration gate. "
        f"Personal reflection → `{personal}`._\n\n"
        "### Key verses\n\n### Summary\n\n### Notes\n\n### Cross references\n\n### Questions"
    )


def default_tail(genre, book_dirname, foldername):
    return glance_section(genre) + "\n\n" + notes_section(book_dirname, foldername)


def has_real_notes(tail: str) -> bool:
    t = re.sub(r"(?s)<!--.*?-->", "", tail)        # drop HTML comments
    t = re.sub(r"(?m)^\s{0,3}#{1,6}\s.*$", "", t)  # drop headers
    return bool(t.strip())


def extract_tail(body: str) -> str:
    if AUTO_END in body:
        return body.split(AUTO_END, 1)[1]
    if OLD_END in body:
        return body.split(OLD_END, 1)[1]
    lines = body.splitlines()
    for i, l in enumerate(lines):
        if l.startswith("# "):
            return "\n".join(lines[i + 1:])
    return body


def ensure_sections(tail, genre, book_dirname, foldername):
    t = tail.strip()
    if "at a glance" not in t.lower():
        t = glance_section(genre) + "\n\n" + t
    if "study notes" not in t.lower() and "## key verses" not in t.lower():
        t = t + "\n\n" + notes_section(book_dirname, foldername)
    return t


# ---------- the AUTO block ----------

def build_auto(book, chapter, chapters_index, labels, primary, primary_full, present, ptext, all_verses):
    nav = [f"↑ [{book}](../README.md)"]
    if chapter - 1 in chapters_index:
        nav.append(f"[‹ {book} {chapter-1}](../{chapters_index[chapter-1]}/README.md)")
    if chapter + 1 in chapters_index:
        nav.append(f"[{book} {chapter+1} ›](../{chapters_index[chapter+1]}/README.md)")
    full = "📖 **Full text:** " + " · ".join(f"[{l}]({l}.md)" for l in labels)
    compare = [l for l in labels if l != primary]
    rows = []
    for v in all_verses:
        txt = (ptext.get(v, "—").replace("|", "\\|").strip()) or "—"
        cmp = " · ".join(f"[{l}]({l}.md#v{v})" for l in compare if v in present[l]) or "—"
        rows.append(f"| [{v}]({primary}.md#v{v}) | {txt} | {cmp} |")
    return "\n".join([
        AUTO_BEGIN, "",
        "  ·  ".join(nav), "",
        full, "",
        f"## Verses ({len(all_verses)})", "",
        f"| # | {primary_full} | Compare |", "|---|---|---|",
        *rows, "",
        AUTO_END,
    ])


# ---------- per-chapter update ----------

def update_readme(folder, book_dir, genre, chapters_index, book):
    versions = version_files(folder)
    if not versions:
        return "skip (no translation files)"
    labels = [l for l, _ in versions]
    paths = {l: p for l, p in versions}
    primary = PRIMARY_PREF if PRIMARY_PREF in labels else labels[0]
    present = {l: verses_present(paths[l]) for l in labels}
    all_verses = sorted(set().union(*present.values())) if present else []
    ptext = parse_verse_text(paths[primary])
    chapter = int(re.search(r"-(\d+)$", folder.name).group(1))

    auto = build_auto(book, chapter, chapters_index, labels, primary,
                      full_name(paths[primary]), present, ptext, all_verses)

    readme = folder / "README.md"
    content = readme.read_text(encoding="utf-8") if readme.exists() else ""
    fm, body = fm_parse(content)
    tail = extract_tail(body)
    if has_real_notes(tail):
        tail = ensure_sections(tail, genre, book_dir.name, folder.name)
        kept = "notes preserved"
    else:
        tail = default_tail(genre, book_dir.name, folder.name)
        kept = "fresh scaffold"

    fm = fm_build(fm, book, chapter, genre, len(all_verses), primary, labels)
    new = f"{fm_serialize(fm)}\n\n# {book} {chapter}\n\n{auto}\n\n{tail.strip()}\n"
    readme.write_text(new, encoding="utf-8", newline="\n")
    return f"{kept} ({len(labels)} versions, {len(all_verses)} verses)"


# ---------- driver ----------

def parse_range(spec):
    if not spec:
        return None
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return range(int(lo), int(hi) + 1)
    n = int(spec)
    return range(n, n + 1)


def main(argv=None):
    p = argparse.ArgumentParser(description="Build BBE-primary verse-index READMEs.")
    p.add_argument("book", nargs="?", help="path to a book folder, e.g. scripture/19-Psalms")
    p.add_argument("--all", action="store_true", help="process every book under scripture/")
    p.add_argument("--chapters", help="chapter or range, e.g. 1 or 1-3 (single book)")
    args = p.parse_args(argv)

    if not args.all and not args.book:
        p.error("give a book folder or --all")
    chap_range = parse_range(args.chapters)

    if args.all:
        books = sorted(d for d in SCRIPTURE.iterdir() if d.is_dir() and book_number(d) is not None)
    else:
        bdir = Path(args.book)
        if not bdir.is_absolute():
            bdir = Path.cwd() / bdir
        if not bdir.exists():
            bdir = REPO_ROOT / args.book
        books = [bdir.resolve()]

    total = 0
    for bdir in books:
        bnum = book_number(bdir)
        genre = GENRE.get(bnum, "")
        book = book_label(bdir)
        chapters = chapter_folders(bdir)
        index = {ch: f.name for ch, f in chapters}
        print(f"-> {bdir.name}  (genre: {genre or '—'})")
        for chapter, folder in chapters:
            if chap_range is not None and chapter not in chap_range:
                continue
            result = update_readme(folder, bdir, genre, index, book)
            total += 1
            if not args.all:
                print(f"   {folder.name}: {result}")
        if args.all:
            print(f"   processed {len(chapters)} chapters")
    print(f"\nDONE. READMEs built: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
