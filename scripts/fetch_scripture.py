#!/usr/bin/env python3
"""Fetch public-domain scripture text into the chapter folders.

This is a one-off CONTENT-POPULATION utility, not a build tool. The repo is
markdown-only; this script just fills each chapter folder with the actual
verses from public-domain translations so the text lives alongside the
study-notes README.md.

Source
------
getbible.net v2 API (free, no key, public-domain texts):
    https://api.getbible.net/v2/{translation}/{book_nr}/{chapter}.json

Layout it writes
----------------
For every chapter folder it finds on disk, it writes one file per translation
(WEB.md, KJV.md, ASV.md, ...) NEXT TO the existing README.md. It never touches
README.md (that is your commentary / study-notes layer).

    scripture/19-Psalms/Psalms-001/
        README.md   <- left untouched (your study notes)
        WEB.md      <- written by this script
        KJV.md      <- written by this script
        ASV.md      <- written by this script

How it figures out book + chapter numbers
------------------------------------------
It reads the folder names already on disk -- no hardcoded book table:
  * Book number  = leading digits of the top-level book folder ("19-Psalms" -> 19)
  * Chapter number = trailing digits of each chapter folder ("Psalms-001" -> 1)
So zero-padding (Psalms-001 vs Genesis-01) is handled automatically because it
mirrors whatever folders exist.

Usage
-----
    # one book (every chapter folder it contains)
    python scripts/fetch_scripture.py scripture/19-Psalms

    # pick translations (default: web kjv asv basicenglish)
    python scripts/fetch_scripture.py scripture/19-Psalms --translations web kjv

    # limit to a chapter range
    python scripts/fetch_scripture.py scripture/01-Genesis --chapters 1-3

    # every book under scripture/
    python scripts/fetch_scripture.py --all

    # don't overwrite files that already exist
    python scripts/fetch_scripture.py scripture/19-Psalms --skip-existing

Runs on Windows (python) and WSL/Linux (python3) identically -- standard
library only, no jq, no pip install.
"""
# ===========================================================================
# AVAILABLE TRANSLATIONS on getbible.net v2 (117 total) -- all public domain.
# Pass any abbreviation (left column) via --translations. Generated from the API.
# Default set used by this script: web, kjv, asv, basicenglish.
# Notable extras: ylt (hyper-literal), kjva (KJV w/ Strong's numbers + Apocrypha),
#   plus Hebrew/Greek originals (see the Hebrew/Greek groups below) for word study.
#
# English (12):
#   akjv             American King James Version
#   asv              American Standard Version
#   basicenglish     Basic English Bible
#   douayrheims      Douay Rheims
#   kjv              King James Version
#   kjva             King James Version (1769) with Strongs Numbers and Morpholo...
#   tyndale          William Tyndale Bible (1525/1530)
#   wb               Webster's Bible
#   web              World English Bible
#   weymouth         Weymouth NT
#   wycliffe         John Wycliffe Bible (c.1395)
#   ylt              Young's Literal Translation
# Afrikaans (1):
#   aov              Ou Vertaling
# Albanian (1):
#   alb              Albanian Bible
# Arabic (1):
#   arabicsv         Smith and Van Dyke
# Armenian (2):
#   easternarmenian  Eastern (Genesis Exodus Gospels)
#   westernarmenian  Western NT
# Basque (1):
#   basque           (Navarro Labourdin) NT
# Breton (1):
#   breton           Gospels
# Calo (1):
#   calo             El Evangelio segun S. Lucas, traducido al Romaní, ó dialect...
# Chamorro (1):
#   chamorro         (Psalms Gospels Acts)
# Cherokee (1):
#   che1860          Cherokee New Testament (1860) with Sequoyah transliterated ...
# Chinese (5):
#   chiunl           聖經 (文理和合)
#   cns              NCV Simplified
#   cnt              NCV Traditional
#   cus              Union Simplified
#   cut              Union Traditional
# Coptic (2):
#   coptic           New Testament
#   sahidic          Sahidic NT
# Croatian (1):
#   croatia          Croatian
# Czech (2):
#   bkr              Czech BKR
#   cep              Czech CEP
# Danish (3):
#   danish           Danish
#   danish1819       Danish New Testament from 1819 with original orthography
#   danish1871       Danish OT1871 + NT1907 with original orthography
# Dari (1):
#   dari             Dari Translation
# Dutch (3):
#   canisius         Petrus Canisius Translation
#   statenvertaling  Dutch Staten Vertaling
#   statenvertalinga De ganse Heilige Schrift bevattende al de kanonieke boeken ...
# Esperanto (1):
#   esperanto        Esperanto
# Estonian (1):
#   estonian         Estonian
# Finnish (3):
#   finnish1776      Finnish Bible (1776)
#   pyharaamattu1933 Pyha Raamattu (1933 1938)
#   pyharaamattu1992 Pyha Raamattu (1992)
# French (3):
#   darby            Darby
#   ls1910           Louis Segond (1910)
#   martin           Martin (1744)
# German (4):
#   elberfelder      Elberfelder (1871)
#   elberfelder1905  Elberfelder (1905)
#   luther1545       Luther (1545)
#   schlachter       Schlachter (1951)
# Gothic (1):
#   gothic           Gothic (Nehemiah NT Portions)
# Greek (4):
#   lxx              OT LXX Accented
#   textusreceptus   NT Textus Receptus (1550 1894) Parsed
#   tischendorf      NT Tischendorf 8th Ed
#   westcotthort     NT Westcott Hort UBS4 variants Parsed
# Greek Modern (1):
#   moderngreek      Greek Modern
# Hebrew (3):
#   aleppo           Aleppo Codex
#   codex            OT Westminster Leningrad Codex
#   modernhebrew     Hebrew Modern
# Hungarian (1):
#   karoli           Hungarian Karoli
# Italian (2):
#   giovanni         Giovanni Diodati Bible (1649)
#   riveduta         Riveduta Bible (1927)
# Japanese (4):
#   japbungo         明治元訳「舊約聖書」(1953年版) 大正改訳「新約聖書
#   japdenmo         Japanese Denmo 電網聖書
#   japkougo         Japanese Kougo-yaku 口語訳「聖書」(1954/1955年版)
#   japraguet        Japanese Raguet-yaku ラゲ訳「我主イエズスキリストの新約聖書」(1910年版)
# Korean (2):
#   korean           Korean
#   koreankjv        Hangul King James Version
# Latin (1):
#   vulgate          Vulgata Clementina
# Latvian (1):
#   latvian          New Testament
# Lithuanian (1):
#   lithuanian       Lithuanian
# Malagasy (1):
#   mg1865           Baiboly Malagasy (1865)
# Manx Gaelic (1):
#   manxgaelic       Manx Gaelic (Esther Jonah 4 Gospels)
# Maori (1):
#   maori            Maori
# Mongolian (1):
#   monkjv           Mongolian King James Version
# Myanmar Burmse (2):
#   burcbcm          ဤဘာသာပြန်ကျမ်းကိုကက်သလစ်ဆရာတော်များရုံးချုပ်ရှိ  သမမ္မာ ကျမ...
#   judson           Judson (1835)
# Ndebele (1):
#   ndebele          Ndebele Bible
# Norwegian bokmal (1):
#   bibelselskap     Det Norsk Bibelselskap (1930)
# Norwegian nynorsk (1):
#   norsmb           Studentmållagsbibelen frå 1921
# Other (3):
#   klv              Klingon Language Version of the World English Bible
#   mal1910          Sathyavedapusthakam (Malayalam Bible) published in 1910
#   tpikjpb          King Jems Pisin Baibel
# Pohnpeian (2):
#   pohnold          Old Public Domain Pohnpeian Bible
#   pohnpeian        Bible in Pohnpeian language
# Polish (2):
#   polgdanska       Polish Biblia Gdanska (1881)
#   polugdanska      Updated Gdańsk Bible
# Portuguese (3):
#   almeida          Almeida Atualizada
#   livre            Bíblia Livre
#   livretr          Bíblia Livre - Textus Receptus
# Potawatomi (1):
#   potawatomi       Potawatomi (Matthew Acts) (Lykins 1844)
# Romanian (1):
#   cornilescu       Cornilescu
# Russian (2):
#   synodal          Synodal Translation (1876)
#   zhuromsky        Victor Zhuromsky NT
# Scottish Gaelic (1):
#   gaelic           Scots Gaelic (Gospel of Mark)
# Serbian (2):
#   srkdekavski      Serbian Bible Daničić-Karadžić Ekavski
#   srkdijekav       Serbian Bible Daničić-Karadžić Ijekavski
# Shona (1):
#   shona            Shona Bible
# Slavonic Elizabeth (1):
#   csielizabeth     1757 Church Slavonic Elizabeth Bible
# Spanish (3):
#   rv1858           Reina Valera NT (1858)
#   sse              Sagradas Escrituras (1569)
#   valera           Reina Valera (1909)
# Swahili (1):
#   swahili          Swahili
# Swedish (3):
#   swedish          Swedish (1917)
#   swekarlxii       Svenska Karl XII:s Bibel (1703)
#   swekarlxii1873   Svenska Karl XII:s Bibel (1873)
# Syriac (1):
#   peshitta         Peshitta NT
# Tagalog (1):
#   tagalog          Ang Dating Biblia (1905)
# Tausug (1):
#   tausug           Tausug Kitab Injil
# Thai (1):
#   thai             Thai from kjv
# Turkish (2):
#   turhadi          Turkish Easy-to-Read Translation (HADI)
#   turkish          Turkish
# Ukrainian (2):
#   ukranian         NT (P Kulish 1871)
#   ukrogienko       Українська Біблія. Переклад Івана Огієнка.
# Uma (1):
#   uma              Uma NT
# Vietnamese (1):
#   vietnamese       Vietnamese (1934)
# ===========================================================================

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

API = "https://api.getbible.net/v2/{translation}/{book}/{chapter}.json"

# getbible.net's CDN rejects the default urllib user-agent (HTTP 403), so send a
# browser-like one. This is a plain GET of public-domain JSON, nothing sneaky.
USER_AGENT = "Mozilla/5.0 (compatible; bible-study-fetch/1.0; +https://getbible.net)"

# translation abbreviations (lowercase, as the API wants)
# BBE (basicenglish) is FIRST because it is the project's primary/default version
# (Darren's standing instruction) — the others are kept as comparison texts.
DEFAULT_TRANSLATIONS = ["basicenglish", "web", "kjv", "asv"]

# Nicer, short output filenames for versions whose API abbreviation is long.
# Anything not listed here just uppercases its API abbreviation (web -> WEB.md).
FILE_STEMS = {
    "basicenglish": "BBE",   # Bible in Basic English
    "douayrheims": "DRA",    # Douay-Rheims
}


def file_stem(translation: str) -> str:
    return FILE_STEMS.get(translation, translation.upper())

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTURE = REPO_ROOT / "scripture"

PAUSE_SECONDS = 0.12  # be polite to the free API


def book_number(book_dir: Path) -> int | None:
    m = re.match(r"^(\d+)-", book_dir.name)
    return int(m.group(1)) if m else None


def chapter_folders(book_dir: Path):
    """Yield (chapter_int, folder_path) for chapter subfolders, sorted."""
    found = []
    for child in book_dir.iterdir():
        if not child.is_dir():
            continue
        m = re.search(r"-(\d+)$", child.name)
        if m:
            found.append((int(m.group(1)), child))
    found.sort(key=lambda t: t[0])
    return found


def fetch(translation: str, book: int, chapter: int, retries: int = 2):
    url = API.format(translation=translation, book=book, chapter=chapter)
    last_err = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 - report and retry
            last_err = e
            time.sleep(0.5)
    raise RuntimeError(f"failed {url}: {last_err}")


def render(data: dict, abbr_upper: str) -> str:
    lines = [
        f"# {data['book_name']} {data['chapter']} — {data['translation']} ({abbr_upper})",
        "",
        "*Public domain. Source: getbible.net.*",
        "",
        "---",
        "",
    ]
    for v in data["verses"]:
        text = re.sub(r"\s+$", "", v["text"]).strip()
        # Per-verse anchor so README links like WEB.md#v3 jump to the verse.
        lines.append(f'<a id="v{v["verse"]}"></a>**{v["verse"]}** {text}')
        lines.append("")
    return "\n".join(lines)


def parse_chapter_range(spec: str | None):
    if not spec:
        return None
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return range(int(lo), int(hi) + 1)
    n = int(spec)
    return range(n, n + 1)


def process_book(book_dir: Path, translations, chap_range, skip_existing: bool):
    bnum = book_number(book_dir)
    if bnum is None:
        print(f"  ! skipping {book_dir.name} (no leading book number)")
        return 0, []
    written, failures = 0, []
    for chapter, folder in chapter_folders(book_dir):
        if chap_range is not None and chapter not in chap_range:
            continue
        for t in translations:
            abbr = file_stem(t)
            out = folder / f"{abbr}.md"
            if skip_existing and out.exists():
                continue
            try:
                data = fetch(t, bnum, chapter)
                out.write_text(render(data, abbr), encoding="utf-8", newline="\n")
                written += 1
            except Exception as e:  # noqa: BLE001
                failures.append(f"{abbr} {book_dir.name} ch{chapter}: {e}")
            time.sleep(PAUSE_SECONDS)
    return written, failures


def main(argv=None):
    p = argparse.ArgumentParser(description="Fetch public-domain scripture into chapter folders.")
    p.add_argument("book", nargs="?", help="path to a book folder, e.g. scripture/19-Psalms")
    p.add_argument("--all", action="store_true", help="process every book under scripture/")
    p.add_argument("--translations", nargs="+", default=DEFAULT_TRANSLATIONS,
                   help=f"translation abbreviations (default: {' '.join(DEFAULT_TRANSLATIONS)})")
    p.add_argument("--chapters", help="chapter or range, e.g. 1 or 1-3 (single-book only)")
    p.add_argument("--skip-existing", action="store_true", help="don't overwrite existing files")
    args = p.parse_args(argv)

    if not args.all and not args.book:
        p.error("give a book folder or --all")

    chap_range = parse_chapter_range(args.chapters)

    if args.all:
        books = sorted(d for d in SCRIPTURE.iterdir() if d.is_dir() and book_number(d) is not None)
    else:
        bdir = Path(args.book)
        if not bdir.is_absolute():
            bdir = (Path.cwd() / bdir)
        if not bdir.exists():
            bdir = REPO_ROOT / args.book
        books = [bdir.resolve()]

    total, all_fail = 0, []
    for bdir in books:
        print(f"-> {bdir.name}")
        w, f = process_book(bdir, args.translations, chap_range, args.skip_existing)
        total += w
        all_fail += f
        print(f"   wrote {w} file(s)")

    print(f"\nDONE. Files written: {total}")
    if all_fail:
        print(f"FAILURES ({len(all_fail)}):")
        for line in all_fail:
            print(f"  {line}")
        return 1
    print("No failures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
