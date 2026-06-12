# Exchange 04: Build the library + per-teacher best practices

- **Timestamp:** 2026-06-12
- **Context:** User answers the scope/location question and, mid-work, asks for repo best practices.

## User Input

(AskUserQuestion answers) "The free PDF transcript, The article/interview texts, A links index only, Structured study notes, anything you can get at. keep his materials separate from other teachers, ok?" / Location: "A shareable repo folder"

(then, while working) each teacher should have their own related materials, ok? what would be all the best practices for doing this in a repo like this?

## AI Response

Answered the best-practices question first (it governs placement), then built the library as the reference implementation:

**Best practices for per-teacher materials:**
1. One folder per teacher, named to match the agent slug → `resources/teachers/jamie-winship/`.
2. Use `resources/` — the purpose-built stub for external pointers.
3. Predictable file set: `README.md`, `links.md`, `notes.md`, `quotes.md`.
4. **Copyright is load-bearing:** shared layer = links + transformative summaries + short attributed quotes only; full text → `.personal/`.
5. Stamp provenance (URL + access date + free/paid).
6. Don't auto-download A/V — link it.
7. Cross-link the three faces of a teacher: agent / library / (optional) bio in `people/`.
8. Index + back-links.
9. If it becomes a standing convention, document it (didn't touch published docs unilaterally).

**Built:** `resources/teachers/README.md` (index + convention), `resources/teachers/jamie-winship/{README,links,notes,quotes}.md`, and a back-link in the agent file. The God Hears Her PDF came back as binary (WebFetch can't parse) and was *not* committed (copyright). Article fetches gave attributable frameworks (identity-vs-calling, true/false self, the Identity Prayer "What do you call me when you talk about me?", true-vs-real, four A's of abiding, two worldviews). Quotes kept short + attributed.

## Tool Calls

- `Read` ×3 (skills README, _word_study skill, TEACHERS canon); `ToolSearch` (WebSearch/WebFetch)
- `WebFetch` ×3 (PDF [binary], Christianity Today, Jennie Allen)
- `Bash` (inspect resources/ stub)
- `Write` ×5 (resources/teachers/README.md, jamie-winship/{README,links,notes,quotes}.md)
- `Edit` (agent file back-link)

## Files Read/Modified

- **+** `resources/teachers/README.md`
- **+** `resources/teachers/jamie-winship/{README,links,notes,quotes}.md`
- **~** `.claude/agents/teacher-jamie-winship.md` (resource-library pointer)
