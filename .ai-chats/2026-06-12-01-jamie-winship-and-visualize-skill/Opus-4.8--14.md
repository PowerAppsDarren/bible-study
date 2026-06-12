# Exchange 14: Where are the visuals stored?

- **Timestamp:** 2026-06-12
- **Context:** User asks where the visuals generated for them in this repo actually live.

## User Input

now, where are all the visuals you generate for me here?

## AI Response

Gave the honest inventory (checked disk first, didn't guess): **only one** saved visual in the repo — `.personal/darren@neese.us/visuals/abiding-winship.html` (+ its 3.3 MB `mermaid.min.js`). The other HTML files found weren't mine (`_deep_bible_study_devotional/overview.html`, `graphify-out/graph.html`). Why so little: by design the skill renders inline and only writes a file on request, so every diagram shown in chat was inline-only (nothing lost — those two diagrams are in the demo). And the Canvas I made is in the *other* vault, not this repo. Concluded there's no real "visuals home" yet and proposed: a `visuals/` folder at root (shared) + `.personal/.../visuals/` (private) + a `Visuals.canvas` index, with a default-save habit. Asked which location to make default (recommended `visuals/` at root).

## Tool Calls

- `Bash` inventory: `.personal/.../visuals/`, `*.canvas`, `*.html` (excl. skill template)

## Files Read/Modified

None (read-only).
