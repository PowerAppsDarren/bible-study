#!/usr/bin/env python3
"""Add (or refresh) a "Table of Contents" to a devotional.html in "The Branch"
design system.

For each titled <section> (one with a `.sec-head` h2) it:
  - gives the section a stable `id` (slug of its title) if it lacks one,
  - collects the section's emoji + title,
then injects a styled <nav class="toc"> at the top of `.wrap` (above section 1),
and adds the TOC's CSS into the page's inline <style>.

Run it after a page is written/edited:

    python .claude/skills/_branch_devotional_design/add_toc.py PATH [PATH ...]

SAFE and IDEMPOTENT: a prior TOC nav and prior TOC CSS (both fenced by markers)
are stripped and rebuilt each run, and section ids are reused if already present.
The TOC uses the page's own CSS variables, so it matches every theme automatically.
Pure stdlib; cross-platform.
"""
import html as htmllib
import os
import re
import sys

TOC_CSS = """  .toc{margin:46px 0 8px;border:1px solid var(--line);background:var(--panel);border-radius:16px;padding:24px 28px}
  .toc .toc-h{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:16px}
  .toc ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:4px 24px}
  .toc a{display:flex;gap:12px;align-items:baseline;color:var(--ink-dim);text-decoration:none;padding:8px 10px;border-radius:9px;font-family:var(--serif);font-size:18px;line-height:1.3;transition:background .15s ease,color .15s ease}
  .toc a:hover{background:var(--panel2);color:var(--ink)}
  .toc a .n{font-family:var(--sans);font-size:12px;font-weight:700;color:var(--gold);min-width:22px}
  .toc a .e{font-size:17px;flex:0 0 auto}
  section{scroll-margin-top:24px}"""

TAGS = re.compile(r"<[^>]+>")
SECTION = re.compile(r"<section\b([^>]*)>(.*?)</section>", re.S | re.I)
EMOJI = re.compile(r'<div class="emoji">(.*?)</div>', re.S | re.I)
H2 = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S | re.I)


def slugify(text):
    t = htmllib.unescape(TAGS.sub("", text)).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return ("s-" + t) if t else "s"


def add_toc(html):
    # strip any prior TOC nav + CSS so the run is idempotent
    html = re.sub(r'<nav class="toc">.*?</nav>\n*', "", html, flags=re.S)
    html = re.sub(r"  /\* TOC-CSS-START \*/.*?/\* TOC-CSS-END \*/\n", "", html, flags=re.S)

    entries, seen = [], set()

    def on_section(m):
        attrs, body = m.group(1), m.group(2)
        h2 = H2.search(body)
        if not h2:
            return m.group(0)
        title = htmllib.unescape(TAGS.sub("", h2.group(1)).strip())
        em = EMOJI.search(body)
        emoji = htmllib.unescape(TAGS.sub("", em.group(1)).strip()) if em else ""
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid, new_attrs = idm.group(1), attrs
        else:
            base = slugify(title)
            sid, n = base, 2
            while sid in seen:
                sid, n = f"{base}-{n}", n + 1
            new_attrs = attrs + f' id="{sid}"'
        seen.add(sid)
        entries.append((sid, emoji, title))
        return f"<section{new_attrs}>{body}</section>"

    html = SECTION.sub(on_section, html)
    if not entries:
        return html, 0

    items = []
    for i, (sid, emoji, title) in enumerate(entries, 1):
        e = f'<span class="e">{emoji}</span>' if emoji else ""
        items.append(
            f'    <li><a href="#{sid}"><span class="n">{i:02d}</span>{e}'
            f'<span class="t">{htmllib.escape(title)}</span></a></li>'
        )
    toc = ('<nav class="toc">\n  <div class="toc-h">In This Study</div>\n  <ol>\n'
           + "\n".join(items) + "\n  </ol>\n</nav>\n\n")

    html, n = re.subn(r'(<div class="wrap">[ \t]*\n?)',
                      lambda m: m.group(1) + "\n" + toc, html, count=1)
    if n == 0:  # no .wrap container found; leave ids in place but report nothing inserted
        return html, 0

    css = "  /* TOC-CSS-START */\n" + TOC_CSS + "\n  /* TOC-CSS-END */\n"
    html = re.sub(r"</style>", lambda m: css + m.group(0), html, count=1)
    return html, len(entries)


def main(argv):
    repo = os.popen("git rev-parse --show-toplevel").read().strip() or os.getcwd()
    paths = argv[1:]
    if not paths:
        print("usage: add_toc.py PATH [PATH ...]")
        return 1
    for p in paths:
        with open(p, encoding="utf-8") as f:
            html = f.read()
        new, count = add_toc(html)
        if new != html:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(new)
        print(f"{os.path.relpath(p, repo)}: TOC with {count} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
