#!/usr/bin/env python3
"""Auto-link Bible chapter references inside a devotional.html to the matching
chapter README in this repo.

Convention (Darren, 2026-06-27): whenever a devotional/study HTML page mentions
another chapter of the Bible, that mention should link to that chapter's
`README.md` in `scripture/<NN-Book>/<Book>-<CC>/README.md`.

This is the canonical post-processor for "The Branch" pages. Run it after a
devotional.html is written or edited:

    python .claude/skills/_branch_devotional_design/link_chapters.py PATH [PATH ...]

It is SAFE and IDEMPOTENT:
  - only ever links a reference whose target README actually exists on disk
    (never emits a broken link),
  - NEVER links a page to its OWN chapter (a page linking to itself is removed and
    not re-created),
  - never links inside an existing <a>, the hero <header>, <title>, <footer>,
    <nav> (the table of contents), <style>, <script>, or <head> (so chrome and CSS
    are untouched and re-runs don't double-link),
  - links the CHAPTER ("Jeremiah 17"); any trailing ":5-8" verse text is left
    as-is after the link.

Prints a per-file report of links added / self-links removed / refs skipped.
Pure stdlib; cross-platform.
"""
import os
import re
import sys

FOLDERS = [
    "01-Genesis", "02-Exodus", "03-Leviticus", "04-Numbers", "05-Deuteronomy",
    "06-Joshua", "07-Judges", "08-Ruth", "09-1-Samuel", "10-2-Samuel",
    "11-1-Kings", "12-2-Kings", "13-1-Chronicles", "14-2-Chronicles", "15-Ezra",
    "16-Nehemiah", "17-Esther", "18-Job", "19-Psalms", "20-Proverbs",
    "21-Ecclesiastes", "22-Song-of-Solomon", "23-Isaiah", "24-Jeremiah",
    "25-Lamentations", "26-Ezekiel", "27-Daniel", "28-Hosea", "29-Joel",
    "30-Amos", "31-Obadiah", "32-Jonah", "33-Micah", "34-Nahum", "35-Habakkuk",
    "36-Zephaniah", "37-Haggai", "38-Zechariah", "39-Malachi", "40-Matthew",
    "41-Mark", "42-Luke", "43-John", "44-Acts", "45-Romans", "46-1-Corinthians",
    "47-2-Corinthians", "48-Galatians", "49-Ephesians", "50-Philippians",
    "51-Colossians", "52-1-Thessalonians", "53-2-Thessalonians", "54-1-Timothy",
    "55-2-Timothy", "56-Titus", "57-Philemon", "58-Hebrews", "59-James",
    "60-1-Peter", "61-2-Peter", "62-1-John", "63-2-John", "64-3-John", "65-Jude",
    "66-Revelation",
]
WORDNUM = {"1": "First", "2": "Second", "3": "Third"}


def bookname(folder):
    return folder.split("-", 1)[1]


def pad_width(folder):
    return 3 if folder == "19-Psalms" else 2


def build_alias_map():
    alias_to_folder = {}

    def add(alias, folder):
        alias_to_folder.setdefault(alias.lower(), folder)

    for folder in FOLDERS:
        spaced = bookname(folder).replace("-", " ")
        add(spaced, folder)
        m = re.match(r"^([123]) (.+)$", spaced)
        if m:
            add(f"{WORDNUM[m.group(1)]} {m.group(2)}", folder)

    add("Psalm", "19-Psalms")
    add("Song of Songs", "22-Song-of-Solomon")
    add("Canticles", "22-Song-of-Solomon")
    add("Revelations", "66-Revelation")
    add("Qoheleth", "21-Ecclesiastes")

    aliases = sorted(alias_to_folder.keys(), key=len, reverse=True)
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(a) for a in aliases) + r")\s+(\d{1,3})\b",
        re.IGNORECASE,
    )
    return alias_to_folder, pattern


ALIAS_TO_FOLDER, REF_RE = build_alias_map()
REPO = None


def linkify_text(text, stats, own_href):
    def repl(m):
        alias, chap = m.group(1), int(m.group(2))
        folder = ALIAS_TO_FOLDER.get(alias.lower())
        if not folder:
            return m.group(0)
        chap_folder = f"{bookname(folder)}-{chap:0{pad_width(folder)}d}"
        href = f"../../{folder}/{chap_folder}/README.md"
        if href == own_href:                       # never link a page to itself
            return m.group(0)
        target_fs = os.path.join(REPO, "scripture", folder, chap_folder, "README.md")
        if not os.path.isfile(target_fs):
            stats["skipped"].append(f"{m.group(0)} -> {folder}/{chap_folder} (no README)")
            return m.group(0)
        stats["linked"] += 1
        return f'<a href="{href}">{m.group(0)}</a>'
    return REF_RE.sub(repl, text)


TAG = re.compile(r"(<[^>]+>)")
SKIP_OPEN = re.compile(r"<\s*(a|nav|header|title|footer|style|script|head)\b", re.I)
SKIP_CLOSE = re.compile(r"<\s*/\s*(a|nav|header|title|footer|style|script|head)\s*>", re.I)


def process(html, stats, own_href):
    out, depth = [], 0
    for tok in TAG.split(html):
        if not tok:
            continue
        if tok.startswith("<"):
            if SKIP_OPEN.match(tok) and not tok.rstrip().endswith("/>"):
                depth += 1
            elif SKIP_CLOSE.match(tok) and depth > 0:
                depth -= 1
            out.append(tok)
        else:
            out.append(tok if depth > 0 else linkify_text(tok, stats, own_href))
    return "".join(out)


def own_target_href(path):
    """The README href that points at the page's OWN chapter, or None."""
    parts = os.path.normpath(path).replace("\\", "/").split("/")
    if "scripture" in parts:
        i = parts.index("scripture")
        if i + 2 < len(parts):
            return f"../../{parts[i + 1]}/{parts[i + 2]}/README.md"
    return None


def main(argv):
    global REPO
    REPO = os.popen("git rev-parse --show-toplevel").read().strip() or os.getcwd()
    paths = argv[1:]
    if not paths:
        print("usage: link_chapters.py PATH [PATH ...]")
        return 1
    grand = 0
    for p in paths:
        with open(p, encoding="utf-8") as f:
            html = f.read()
        own_href = own_target_href(p)
        removed = 0
        if own_href:                               # strip any pre-existing self-links
            html, removed = re.subn(
                r'<a href="' + re.escape(own_href) + r'">(.*?)</a>',
                r"\1", html, flags=re.S)
        stats = {"linked": 0, "skipped": []}
        new = process(html, stats, own_href)
        if new != html or removed:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(new)
        grand += stats["linked"]
        rel = os.path.relpath(p, REPO)
        extra = []
        if removed:
            extra.append(f"-{removed} self")
        if stats["skipped"]:
            extra.append(f"{len(stats['skipped'])} skipped")
        print(f"{rel}: +{stats['linked']} links" + (", " + ", ".join(extra) if extra else ""))
        for s in stats["skipped"]:
            print(f"    skip: {s}")
    print(f"--- total links added: {grand} ---")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
