#!/usr/bin/env python3
"""Greek/Hebrew word-study engine (Tier 2).

Resolves a Strong's number (or an English-gloss search) into a factual,
shared-layer word study written to `words/<slug>.md`: the original-language
lemma, transliteration, pronunciation, derivation, Strong's definition, and
KJV usage range.

Data source (free, license-clean): OpenScriptures' machine-readable edition of
*Strong's Exhaustive Concordance* (Hebrew 1894 / Greek 1890) — the dictionary
text is public domain; the JSON edition is CC-BY-SA (credited in each file).
The lexicons are downloaded ONCE to a cache OUTSIDE the repo (~/.cache/
bible-study/lexicons) so the repo stays a content repo, not a data dump.

Usage:
    python scripts/word_study.py H8451            # Hebrew "torah" (law)
    python scripts/word_study.py G26              # Greek  "agape" (love)
    python scripts/word_study.py --find law       # search glosses, list matches
    python scripts/word_study.py --find love --lang greek
    python scripts/word_study.py H835 --print     # print, don't write a file

What it does NOT do yet: list every verse a word occurs in (a full
concordance). That needs a Strong's-tagged Bible and is the next increment;
this pass delivers meaning/derivation/usage, which is most of a word study.

Standard library only. Cross-platform (python / python3).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WORDS_DIR = REPO_ROOT / "words"
CACHE = Path.home() / ".cache" / "bible-study" / "lexicons"
UA = "Mozilla/5.0 (compatible; bible-study-wordstudy/1.0)"

SOURCES = {
    "hebrew": ("https://raw.githubusercontent.com/openscriptures/strongs/master/"
               "hebrew/strongs-hebrew-dictionary.js", "strongs-hebrew.json"),
    "greek": ("https://raw.githubusercontent.com/openscriptures/strongs/master/"
              "greek/strongs-greek-dictionary.js", "strongs-greek.json"),
}


def _download(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def load_lexicon(lang: str) -> dict:
    """Download (once) + parse a Strong's .js dictionary into {key: entry}."""
    url, cache_name = SOURCES[lang]
    cache_file = CACHE / cache_name
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))
    CACHE.mkdir(parents=True, exist_ok=True)
    text = _download(url)
    # The .js is a big comment header, then `var ...Dictionary = { ...JSON... };`
    i = text.find("= {")
    start = text.index("{", i if i >= 0 else 0)
    end = text.rindex("}")
    data = json.loads(text[start:end + 1])
    cache_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


def lang_of(strongs: str) -> str:
    return "hebrew" if strongs.upper().startswith("H") else "greek"


def norm_key(s: str) -> str:
    s = s.strip().upper()
    m = re.match(r"^([HG])0*(\d+)$", s)
    return f"{m.group(1)}{int(m.group(2))}" if m else s


def slugify(text: str) -> str:
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    ascii_ = re.sub(r"[^A-Za-z0-9]+", "-", ascii_).strip("-").lower()
    return ascii_ or "word"


def render(key: str, e: dict) -> tuple[str, str]:
    lang = "Hebrew" if key.startswith("H") else "Greek"
    lemma = e.get("lemma", "")
    xlit = e.get("xlit", "")
    pron = e.get("pron", "")
    deriv = e.get("derivation", "").strip()
    sdef = e.get("strongs_def", "").strip()
    kjv = e.get("kjv_def", "").strip()
    title = xlit or lemma or key
    slug = slugify(xlit or key)

    fm = [
        "---", "type: word-study", f"strongs: {key}", f"language: {lang}",
        f"lemma: {lemma}", f"transliteration: {xlit}", "---", "",
    ]
    body = [
        f"# {title} — {lemma}  ·  {key}", "",
        f"**Language:** {lang}  ·  **Strong's:** {key}"
        + (f"  ·  **Pronunciation:** {pron}" if pron else ""), "",
    ]
    if sdef:
        body += ["## Definition", "", sdef, ""]
    if deriv:
        body += ["## Derivation", "", deriv, ""]
    if kjv:
        body += ["## KJV usage", "", kjv, ""]
    body += [
        "## Occurrences", "",
        "_Full concordance (every verse) — next increment (needs a Strong's-tagged Bible)._", "",
        "## Notes", "",
        "<!-- Factual, shared-layer notes. Personal reflection → .personal/<you>/words/. -->", "",
        "---",
        "*Source: Strong's Exhaustive Concordance (Hebrew 1894 / Greek 1890), public domain; "
        "JSON edition © OpenScriptures, CC-BY-SA.*", "",
    ]
    return slug, "\n".join(fm + body)


def cmd_lookup(strongs: str, do_print: bool, force: bool):
    key = norm_key(strongs)
    lang = lang_of(key)
    lex = load_lexicon(lang)
    if key not in lex:
        print(f"Not found: {key}")
        return 1
    slug, md = render(key, lex[key])
    if do_print:
        print(md)
        return 0
    out = WORDS_DIR / lang / f"{slug}.md"
    if out.exists() and not force:
        print(f"exists, skipping (use --force to overwrite): {out.relative_to(REPO_ROOT)}")
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8", newline="\n")
    print(f"wrote {out.relative_to(REPO_ROOT)}  ({key})")
    return 0


def cmd_find(query: str, lang: str | None):
    q = query.lower()
    langs = [lang] if lang else ["hebrew", "greek"]
    hits = []
    for L in langs:
        for k, e in load_lexicon(L).items():
            blob = (e.get("kjv_def", "") + " " + e.get("strongs_def", "")).lower()
            if q in blob:
                hits.append((k, e.get("xlit", ""), e.get("kjv_def", "")[:70]))
    print(f"{len(hits)} match(es) for '{query}':")
    for k, x, d in hits[:40]:
        print(f"  {k:7} {x:18} {d}")
    if len(hits) > 40:
        print(f"  ... +{len(hits)-40} more")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Strong's-based Greek/Hebrew word study.")
    p.add_argument("strongs", nargs="?", help="Strong's number, e.g. H8451 or G26")
    p.add_argument("--find", help="search English glosses for a word")
    p.add_argument("--lang", choices=["hebrew", "greek"], help="limit --find to one language")
    p.add_argument("--print", dest="do_print", action="store_true", help="print instead of writing a file")
    p.add_argument("--force", action="store_true", help="overwrite an existing word file")
    args = p.parse_args(argv)

    try:  # Hebrew/Greek won't print on the Windows cp1252 console otherwise
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if args.find:
        return cmd_find(args.find, args.lang)
    if args.strongs:
        return cmd_lookup(args.strongs, args.do_print, args.force)
    p.error("give a Strong's number or --find <word>")


if __name__ == "__main__":
    sys.exit(main())
