# `.personal/` — Multi-User Shared Personal Layer

This folder is **intentionally tracked in git**, not gitignored. It's the shared-personal layer of the repo: each user has their own email-named subfolder, and notes are shared via git push/pull. Privacy is by convention.

## Convention

Every user has a folder named by their **email address**:

```
.personal/
├── darren@neese.us/        ← one user's space
├── sarah@church.org/       ← another user's space
├── pastor@firstchurch.org/
└── ...
```

Inside your own folder, organize however you like. The recommended convention mirrors the repo root layout for easy navigation — book studies nest under a `scripture/` subfolder (so 66 book folders don't pile up at your root), and raw inputs that fed a study go in a `sources/` folder inside the book:

```
.personal/<your-email>/
├── journal/
│   └── YYYY-MM-DD.md
├── scripture/               ← book studies, mirroring the repo's scripture/ layout
│   └── 01-Genesis/
│       ├── Genesis-01/
│       │   └── notes.md
│       └── sources/         ← raw inputs: transcripts, chat exports, scans
├── topics/
│   └── prayer.md
├── words/
│   └── hesed.md
├── prayer/
│   └── lists/
└── teaching/                ← if you lead a group
    └── 2026-05-15-discussion.md
```

But that's only a recommendation. Some people do dated journals only. Some people mirror the entire repo. Some keep a single flat folder. Your space, your call.

## How sharing works

When you commit and push files inside `.personal/<your-email>/`, everyone in the group can pull and read them. There's no permission system — sharing is opt-in by what you choose to commit.

If you don't want something shared:

1. **Don't commit it** — keep it as an uncommitted file in your working tree, or
2. **Use `.gitignore` patterns scoped to your folder** — e.g., add `.personal/<your-email>/private/` to a `.gitignore` you maintain, or
3. **Mark it with `# private` or `do-not-share` in the file's frontmatter** — the `compare-notes` skill respects these markers.

The repo deliberately doesn't enforce privacy in code. The two-layer model is honesty plus convention: members extend the trust they want extended.

## Skills that write here

Skills that produce personal output (`personal-reflection`, `prayer-from-passage`) always write to `.personal/<user-email>/`. They never write to the shared layer.

Skills that read across the multi-user space (`compare-notes`) enumerate `.personal/*/` and preserve attribution.

## What does NOT go here

- **Factual reference content** (book overviews, key verses, cross-references, people / places / topics that are widely accepted) belongs in the shared layer at the repo root: `scripture/`, `topics/`, `words/`, `people/`, `places/`, `commentary/`, `theology/`, `resources/`.
- **Denominational position papers and copyrighted-translation extended quotes** don't belong in *either* layer per `CONTRIBUTING.md`.
- **Other people's reflections** — only ever write inside *your own* email folder. Other users' folders are read-only by convention.

## A note on sensitive content

Notes about other people in the group, pastoral observations, prayer requests with names — these can be appropriate in personal study but are sensitive in a shared-personal layer. Default to caution: if you wouldn't say it in front of the named person, don't commit it. Pastoral notes that name names probably belong in a `private/` subfolder you keep gitignored, or outside the repo entirely.
