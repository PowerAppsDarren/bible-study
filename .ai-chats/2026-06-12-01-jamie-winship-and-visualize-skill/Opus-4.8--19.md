# Exchange 19: Will tab layouts persist across workstations?

- **Timestamp:** 2026-06-12
- **Context:** User asks about the consequence of ignoring workspace.json.

## User Input

does that mean my tab layouts won't persist between workstations?

## AI Response

Explained the trade-off honestly: same workstation → layout persists fine (file still on disk, just untracked); across workstations via git → no, layout won't travel (each machine keeps its own). `workspace.json` is exactly that layout file; it's ignored to avoid multi-user conflicts. Offered the choice by use-case: solo/multi-workstation → re-track it (`git add -f`); shared group vault → leave it ignored. Asked whether to re-track.

## Tool Calls

None.

## Files Read/Modified

None.
