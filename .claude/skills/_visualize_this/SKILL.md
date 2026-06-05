---
name: _visualize_this
description: Turn whatever information is in front of you — a chapter, a passage's literary structure, a teacher's framework, a word's semantic range, a cross-reference web, a chronology, a doctrinal argument, a page of notes — into the single clearest diagram for fast assimilation. Use when the user says "/_visualize_this", "visualize this", "make a diagram / chart / mind map / timeline of this", "map this out", "diagram this", "draw this", "show me this visually", "how do these connect", "help me see / picture this", or asks for a chiasm, argument flow, or relationship web rendered. Produces GitHub- / VS Code- / Obsidian-renderable Mermaid embedded in markdown (mindmap, timeline, flowchart, network graph, sequence, quadrant, journey) or an indented text diagram for chiasms — auto-selecting the form that fits the information's shape. Renders inline by default; saves to the shared layer for reference-quality structure or to `.personal/<email>/` for personal study assimilation.
---

# Visualize This

Take any block of information and render it as the clearest possible diagram — choosing the form that fits the information's *shape* and keeping it small enough to actually assimilate. The medium is **Mermaid embedded in markdown**: it renders inline on GitHub, in VS Code (Markdown Preview Mermaid Support), and in Obsidian, which is where this repo's content is read. For literary structures Mermaid handles poorly (chiasm, inclusio), use an **indented text diagram** instead.

Convenience is the whole point. By default, render inline immediately. Saving and image-rendering are offered, not required.

## Triggers

- "/_visualize_this", "visualize this", "visualize [passage / framework / notes]"
- "Make a diagram / chart / mind map / timeline / flowchart of this"
- "Map this out", "diagram this", "draw this", "sketch this"
- "Show me this visually", "help me see / picture this"
- "How do these connect?", "what's the structure here?"
- "Is there a chiasm here?", "show the argument flow", "map the relationships"

## Repo context

Read `CLAUDE.md` first. Output follows the two-layer model:

- **Shared** (`scripture/<NN-Book>/<Book>-<NN>/`, `topics/`, `words/`, `people/`, `places/`, `resources/`): only when the diagram is factual, reference-quality *structure* — a chapter's chiasm, a book's argument flow, a covenant comparison. Embed it in a `README.md` section or a sibling file (e.g., `structure.md`). Use verse **references** only — never bake extended copyrighted-translation text into a diagram or a rendered image.
- **Personal** (`.personal/<user-email>/visuals/<topic>.md`): study-assimilation diagrams — yours to keep. This is the default destination when the intent is "help *me* absorb this."

Default behavior is governed by the per-repo config below; absent one, render inline and save only on request.

## Configuration (per repo)

Before choosing a destination, read the repo-local config at `.claude/_visualize_this.json`. When present, it governs placement:

| Key | Meaning |
|---|---|
| `visualsDir` | Shared visuals home, repo-relative (e.g. `visuals`) |
| `canvasFile` | Obsidian Canvas index to append diagrams to (e.g. `visuals/Visuals.canvas`) |
| `personalVisualsDir` | Personal-layer home; `{email}` → the user's email |
| `defaultLayer` | `shared` or `personal` — default destination |
| `defaultFormat` | `md` (Mermaid renders in Obsidian / GitHub) or `html` (standalone sheet) |
| `saveByDefault` | If `true`, persist every generated visual instead of inline-only |
| `appendToCanvas` | If `true`, also add the diagram as a node in `canvasFile` |

This repo's config sets `saveByDefault: true`, `defaultFormat: md`, `defaultLayer: shared` → save each diagram as a Markdown note in `visuals/` (Obsidian renders it); personal/devotional visuals still go to `personalVisualsDir`. **Absent a config:** render inline; save to `.personal/<email>/visuals/` only when asked. Never invent a location when a config is present.

## Workflow

1. **Resolve "this."** Identify the source: the content just discussed, a named passage / topic / framework, a repo file, or pasted text. Infer from context; ask one tight question only if genuinely ambiguous.
2. **Read the information's shape.** Classify the dominant structure (see the rubric). Rich content can carry more than one shape — prefer **two focused diagrams over one crowded one**.
3. **Select the form** via the rubric below. When in doubt, pick the simpler form.
4. **Build it** from `references/diagram-catalog.md`, obeying the assimilation rules: ≤ 7±2 nodes per cluster, 1–5 word labels, direction that *means* something, grouping/color that *encodes* something. Every node traces to a verse or source — invent nothing.
5. **Validate before presenting.** Check Mermaid syntax (watch the catalog's gotchas — colons inside timeline events, punctuation inside `[]` labels). Optionally validate/render to an image with the Mermaid Chart MCP (`validate_and_render_mermaid_diagram`); use the Excalidraw MCP for a hand-sketch style. Fix errors first.
6. **Present inline + orient.** Show each diagram in a fenced ` ```mermaid ` block under a short title, then one line of "what to notice."
7. **Offer next steps:** save (per the layer rules), render to an image, or produce an alternate view.

## Selection rubric — information shape → form

| If the information is… | …use | Mermaid type |
|---|---|---|
| A sequence of events in time | Timeline | `timeline` |
| A spiritual / emotional arc with ups and downs | Journey | `journey` |
| One concept broken into its parts | Mind map | `mindmap` |
| A logical argument, process, or cause→effect chain | Flowchart | `flowchart TD` / `LR` |
| A web of relationships among many entities | Network graph | `graph LR` |
| A back-and-forth between parties | Sequence | `sequenceDiagram` |
| A comparison along two dimensions | Quadrant | `quadrantChart` |
| A comparison of items across features | Table | (markdown table) |
| A mirrored literary structure (chiasm, inclusio) | Indented text diagram | (text, not Mermaid) |

Full templates with worked biblical examples and syntax gotchas: `references/diagram-catalog.md`.

## Output modes

Three, in increasing weight. Default to **inline**; offer the others.

1. **Inline markdown** (default — most convenient):
   > **[Title] — [diagram type]**
   >
   > ` ```mermaid ` … ` ``` `
   >
   > *What to notice:* one orienting sentence.

2. **Saved markdown file** — wrap with a `# [Title]` heading, a one-line source note (passage / framework + date), then the diagram(s). Lands in the shared layer (reference-quality structure) or `.personal/<email>/visuals/<topic>.md`. Renders on GitHub / VS Code / Obsidian.

3. **Standalone HTML study sheet** — a self-contained `.html` file that opens in any browser by double-click, no tooling. Use when the user asks for HTML, wants something printable/shareable, or wants several diagrams on one scrollable page (a one-page visual study sheet — e.g., a chapter's timeline + theme mindmap + chiasm together). Build from `references/html-template.html`:
   - Fill `{{TITLE}}`, `{{SOURCE}}`, `{{DATE}}`; add one `<section>` per diagram (`<h2>` title, `<pre class="mermaid">` source, `.notice` caption).
   - **Rendering must be bulletproof** (the #1 failure is a sheet of raw text): the template uses the **classic UMD** Mermaid via a normal `<script src>` — never an ESM `import` / `<script type="module">`, which fails to load over `file://` on locked-down machines. It loads a **vendored `./mermaid.min.js` first** (fully offline), falling back to the CDN only if absent. Vendor it once into the output folder: `Invoke-WebRequest https://cdn.jsdelivr.net/npm/mermaid@10.9.3/dist/mermaid.min.js -OutFile mermaid.min.js`.
   - Put diagram source **flush-left** inside `<pre class="mermaid">`, and **quote any node label containing punctuation** (`A["Awareness: hear it"]`) — an unquoted colon or paren is a parse error and the diagram won't draw. Validate non-trivial diagrams with the Mermaid MCP before shipping.
   - Save to `.personal/<email>/visuals/<topic>.html` by default (HTML is a generated artifact, not reference text — keep it out of the shared markdown layer unless it's a deliberate handout). Surface it with the file-send capability and/or offer to open it.
   - Same rules apply: verse references only, never copyrighted full-translation text in the page.

One diagram per concept; a multi-diagram HTML sheet stacks several concepts, each in its own section.

## Composition with other skills and agents

- **Downstream of content skills.** After `_deep_bible_study_devotional`, `_word_study`, `_cross_reference_map`, `_topic_trace`, `_character_study`, or `_place_study`, "visualize this" turns the output into a diagram.
- **Reads teacher libraries.** Can diagram a teacher's framework straight from `resources/teachers/<slug>/notes.md` (e.g., Winship's Identity Method, or his fear → conflict chain).
- **Feeds `_group_discussion_prep`.** A clean diagram makes a handout.
- **Distinct from `graphify`.** `graphify` builds a persistent, queryable knowledge graph across many files; `_visualize_this` makes one focused, inline diagram of the thing in front of you. Reach for graphify to map the whole corpus; reach for this to understand *this*.

## Avoid

- **Overcrowding** — the #1 failure of assimilation diagrams. If it needs a scrollbar, split it.
- **Decoration without meaning** — every color, shape, and arrow direction must encode something.
- **Inventing structure** — every node traces to the source text; don't manufacture a chiasm that isn't there.
- **Copyrighted full-translation text** baked into diagrams or rendered images — use verse references and short labels.
- **Layer leakage** — personal assimilation diagrams stay in `.personal/<email>/`; shared structure diagrams stay reference-quality and verse-anchored.
- **Shipping broken Mermaid** — validate; mind the catalog's syntax gotchas.
- **Forcing the wrong form** — don't cram a chronology into a mind map because mind maps look nice.
