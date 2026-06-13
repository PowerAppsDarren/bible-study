# Repository Structure

This repo contains a scaffolded study template for all 66 books of the Protestant Bible, organized into **1,189 chapter folders**, each with its own `README.md` for notes.

## Layout

```
bible-study/
├── scripture/               # All 66 books, numbered 01–66 (SHARED)
│   ├── 01-Genesis/
│   │   ├── Genesis-01/
│   │   │   └── README.md    # Chapter-level shared reference notes
│   │   ├── Genesis-02/
│   │   │   └── README.md
│   │   └── ...
│   ├── 02-Exodus/
│   └── ...
├── topics/                  # Cross-cutting themes and topical studies (SHARED)
│   └── README.md
├── .personal/               # Per-user notes — tracked in git, shared by convention
│   └── <your-email>/        #   (recommended: mirror the repo; books under scripture/)
│       ├── scripture/
│       └── topics/
├── README.md                # Project overview
├── README-TEMPLATE.md       # Template for chapter-level READMEs
├── STRUCTURE.md             # This file
├── CONTRIBUTING.md          # How to use and contribute
├── CHANGELOG.md             # Version history
├── CODE_OF_CONDUCT.md       # Community guidelines
├── LICENSE                  # MIT License
└── .gitignore
```

> **Shared vs. Personal:** Everything outside `.personal/` is shared reference material,
> curated and pushed via pull request. The `.personal/<your-email>/` folders are also
> tracked in git — shared by convention, not gitignored. See
> [README.md](README.md#shared-vs-personal--how-this-repo-works) and
> [CONTRIBUTING.md](CONTRIBUTING.md#the-two-layer-model) for details.

## Old Testament (39 Books)

### Law / Pentateuch

| #  | Book          | Folder              | Chapters |
|----|---------------|----------------------|----------|
| 01 | Genesis       | `01-Genesis`         | 50       |
| 02 | Exodus        | `02-Exodus`          | 40       |
| 03 | Leviticus     | `03-Leviticus`       | 27       |
| 04 | Numbers       | `04-Numbers`         | 36       |
| 05 | Deuteronomy   | `05-Deuteronomy`     | 34       |

### History

| #  | Book           | Folder               | Chapters |
|----|----------------|-----------------------|----------|
| 06 | Joshua         | `06-Joshua`           | 24       |
| 07 | Judges         | `07-Judges`           | 21       |
| 08 | Ruth           | `08-Ruth`             | 4        |
| 09 | 1 Samuel       | `09-1-Samuel`         | 31       |
| 10 | 2 Samuel       | `10-2-Samuel`         | 24       |
| 11 | 1 Kings        | `11-1-Kings`          | 22       |
| 12 | 2 Kings        | `12-2-Kings`          | 25       |
| 13 | 1 Chronicles   | `13-1-Chronicles`     | 29       |
| 14 | 2 Chronicles   | `14-2-Chronicles`     | 36       |
| 15 | Ezra           | `15-Ezra`             | 10       |
| 16 | Nehemiah       | `16-Nehemiah`         | 13       |
| 17 | Esther         | `17-Esther`           | 10       |

### Poetry / Wisdom

| #  | Book              | Folder                  | Chapters |
|----|-------------------|--------------------------|----------|
| 18 | Job               | `18-Job`                 | 42       |
| 19 | Psalms            | `19-Psalms`              | 150      |
| 20 | Proverbs          | `20-Proverbs`            | 31       |
| 21 | Ecclesiastes      | `21-Ecclesiastes`        | 12       |
| 22 | Song of Solomon   | `22-Song-of-Solomon`     | 8        |

### Major Prophets

| #  | Book           | Folder               | Chapters |
|----|----------------|-----------------------|----------|
| 23 | Isaiah         | `23-Isaiah`           | 66       |
| 24 | Jeremiah       | `24-Jeremiah`         | 52       |
| 25 | Lamentations   | `25-Lamentations`     | 5        |
| 26 | Ezekiel        | `26-Ezekiel`          | 48       |
| 27 | Daniel         | `27-Daniel`           | 12       |

### Minor Prophets

| #  | Book        | Folder            | Chapters |
|----|-------------|-------------------|----------|
| 28 | Hosea       | `28-Hosea`        | 14       |
| 29 | Joel        | `29-Joel`         | 3        |
| 30 | Amos        | `30-Amos`         | 9        |
| 31 | Obadiah     | `31-Obadiah`      | 1        |
| 32 | Jonah       | `32-Jonah`        | 4        |
| 33 | Micah       | `33-Micah`        | 7        |
| 34 | Nahum       | `34-Nahum`        | 3        |
| 35 | Habakkuk    | `35-Habakkuk`     | 3        |
| 36 | Zephaniah   | `36-Zephaniah`    | 3        |
| 37 | Haggai      | `37-Haggai`       | 2        |
| 38 | Zechariah   | `38-Zechariah`    | 14       |
| 39 | Malachi     | `39-Malachi`      | 4        |

## New Testament (27 Books)

### Gospels

| #  | Book     | Folder        | Chapters |
|----|----------|---------------|----------|
| 40 | Matthew  | `40-Matthew`  | 28       |
| 41 | Mark     | `41-Mark`     | 16       |
| 42 | Luke     | `42-Luke`     | 24       |
| 43 | John     | `43-John`     | 21       |

### History

| #  | Book | Folder    | Chapters |
|----|------|-----------|----------|
| 44 | Acts | `44-Acts` | 28       |

### Pauline Epistles

| #  | Book              | Folder                  | Chapters |
|----|-------------------|--------------------------|----------|
| 45 | Romans            | `45-Romans`              | 16       |
| 46 | 1 Corinthians     | `46-1-Corinthians`       | 16       |
| 47 | 2 Corinthians     | `47-2-Corinthians`       | 13       |
| 48 | Galatians         | `48-Galatians`           | 6        |
| 49 | Ephesians         | `49-Ephesians`           | 6        |
| 50 | Philippians       | `50-Philippians`         | 4        |
| 51 | Colossians        | `51-Colossians`          | 4        |
| 52 | 1 Thessalonians   | `52-1-Thessalonians`     | 5        |
| 53 | 2 Thessalonians   | `53-2-Thessalonians`     | 3        |
| 54 | 1 Timothy         | `54-1-Timothy`           | 6        |
| 55 | 2 Timothy         | `55-2-Timothy`           | 4        |
| 56 | Titus             | `56-Titus`               | 3        |
| 57 | Philemon          | `57-Philemon`            | 1        |
| 58 | Hebrews           | `58-Hebrews`             | 13       |

### General Epistles

| #  | Book       | Folder         | Chapters |
|----|------------|----------------|----------|
| 59 | James      | `59-James`     | 5        |
| 60 | 1 Peter    | `60-1-Peter`   | 5        |
| 61 | 2 Peter    | `61-2-Peter`   | 3        |
| 62 | 1 John     | `62-1-John`    | 5        |
| 63 | 2 John     | `63-2-John`    | 1        |
| 64 | 3 John     | `64-3-John`    | 1        |
| 65 | Jude       | `65-Jude`      | 1        |

### Prophecy

| #  | Book        | Folder           | Chapters |
|----|-------------|------------------|----------|
| 66 | Revelation  | `66-Revelation`  | 22       |

## Summary

| Statistic        | Count |
|------------------|-------|
| Old Testament    | 39    |
| New Testament    | 27    |
| **Total Books**  | **66**|
| **Total Chapters** | **1,189** |

## Topics of Study

The `topics/` directory is reserved for cross-cutting themes that span multiple books and chapters. Examples include:

- Prayer
- Faith
- Prophecy and fulfillment
- The covenants
- Character studies (Abraham, David, Paul, etc.)

Create a subfolder for each topic and link back to the relevant chapter folders throughout `scripture/`.
