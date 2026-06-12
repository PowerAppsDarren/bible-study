# Exchange 09: Make it local + global; commit + push (ff02b07)

- **Timestamp:** 2026-06-12
- **Context:** User wants the skill in both this repo and globally, confirms HTML, and says save/commit/push.

## User Input

make this skill local to this repo AND make it global. did you update the skill to use html output? yes... save... yes, commit... yes, push

## AI Response

Installed both. The repo copy stays Bible-specific; the **global copy is genericized** (the repo's "save to scripture/.personal" rules would misfire in other projects). Created `~/.claude/skills/_visualize_this/` with a domain-agnostic `SKILL.md`, copied the catalog, and a generic `html-template.html`. Confirmed HTML mode was already added (Exchange 08).

Committed the repo work as `ff02b07` ("feat(skills): add _visualize_this skill with markdown + HTML output", 6 files incl. demo) and **pushed** to `main`. The global skill lives outside the repo (not committed).

## Tool Calls

- `Bash` git status; `Bash` mkdir global dir + copy catalog
- `Write` global SKILL.md (genericized); `Write` global html-template.html
- `Bash` git add/commit `ff02b07`; `git push`

## Files Read/Modified

- **+** `~/.claude/skills/_visualize_this/{SKILL.md, references/diagram-catalog.md, references/html-template.html}` (global, not committed)
- Commit `ff02b07` pushed (repo skill + indexes + demo).
