# Exchange 14: What is GitDoc and why is it interfering?
- **Timestamp:** 2026-06-27
- **Context:** After the first wrap-up; user wants to understand the auto-committer before deciding its fate. (/effort set to high, saved as default.)

## User Input
what is gitDoc and why is it in here interfering with us?

## AI Response
Explained in plain English: **GitDoc** is a VS Code extension (`vsls-contrib.gitdoc`) that turns a git repo into an auto-saving document — like AutoSave that also stamps a permanent version: when on, it auto-**commits** file changes on a timer and can auto-**push**, with Copilot-written messages. It's installed **globally** in VS Code and was switched on, so it applied to whatever folder was open (bible-study). It interfered because **two writers** hit the same repo: me (deliberate batches + commits) and GitDoc (timer-driven auto-commits) — git allows one writer at a time (the lock file), so they collided (`.git/index.lock`) and GitDoc slipped in unsigned commits. Disabling via settings didn't fully stop it because its on/off state lives in VS Code's running memory until reload. Offered: (a) uninstall [recommended], (b) disable, (c) leave.

## Tool Calls
- None (explanatory answer)

## Files Read/Modified
- None
