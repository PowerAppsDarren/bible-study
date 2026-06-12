# Exchange 01: Is Jamie Winship a teacher agent?

- **Timestamp:** 2026-06-12
- **Context:** Session start. User asking whether a teacher-voice agent exists for Jamie Winship.

## User Input

do we have jamie winship down as a bible teacher?

## AI Response

No — there's no Jamie Winship teacher agent. The current roster of seven teacher-voice agents is:

- `teacher-bill-creasy`
- `teacher-chuck-missler`
- `teacher-john-barnett`
- `teacher-john-bevere`
- `teacher-jonathan-cahn`
- `teacher-perry-stone`
- `teacher-oswald-chambers`

Want me to scaffold one? There's a `_new_teacher_agent` skill that would create `.claude/agents/teacher-jamie-winship.md` and update `TEACHERS.md` and `CLAUDE.md` to keep everything coherent. Jamie Winship's lens (identity rooted in hearing God's voice, fear-to-faith, "Living Fearless") is distinct enough from the existing seven that it'd be a clean addition. Just say the word.

## Tool Calls

- `Glob` `.claude/agents/teacher-*.md` → listed the 7 existing teacher agents.

## Files Read/Modified

None (read-only discovery).
