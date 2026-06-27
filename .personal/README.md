# `.personal/` — your own private study space

This folder is the on-ramp for making this Bible study part of your daily life
— **without ever putting your private notes, or even your email address, on the
public repo.**

Here's the whole idea in one breath: the *shared* material everyone studies
(`scripture/`, `topics/`, `words/`, …) lives in this public repo on GitHub.
Your *personal* journal — reflections, prayer lists, teaching prep — lives in a
folder named by your email **right here inside `.personal/`**, but that folder
is **its own separate, private repo** on **your own** git. The public repo is
told to look away from it (see `.gitignore` in this folder), so your space never
travels to GitHub.

The public repo ships the *instructions and a generator* — never anyone's actual
folder. A folder only ever appears on the machine of the person who made it.

## Set up your space — one command

From the repo root:

```
bash .personal/setup.sh
```

It asks your email, builds `.personal/<your-email>/` from the starter kit
(`_template/`), turns it into its own private repo, and (optionally) links it to
your private git so you can push. Works in Git Bash (Windows), WSL, Linux, and
macOS.

Prefer to do it by hand? Copy `_template/` to `.personal/<your-email>/`, then
inside it: `git init -b main`, commit, and add your own remote.

## What's shared vs. what's private

- **Private (your repo):** your reflections, application, prayer, journal,
  teaching prep, speculative connections. Everything is welcome here.
- **Shared (this public repo, via Pull Request):** the *factual* half — what the
  text says, means, and connects to — but only the lines that clear the bar in
  the main `CONTRIBUTING.md`. Offer those back so everyone benefits.

## Why it's built this way

- Your private study and even your email stay off the public repo — privacy is
  real, not just a convention.
- The public repo stays a clean, inviting front door: clone it, run one command,
  and you're studying — your daily notes flow to *your* git, never to GitHub.
- Each person owns and controls their own history, on whatever host they trust.

## What's in this folder (and travels with the public repo)

- `README.md` — this explainer.
- `setup.sh` — the one-command generator.
- `_template/` — the starter kit your space is copied from.
- `.gitignore` — the rule that makes the public repo ignore every real person's
  folder.

Everything else you see here on *your* machine (an email-named folder) is your
own private repo and is invisible to the public repo.
