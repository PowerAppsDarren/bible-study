# Visuals

Home for diagrams and visual maps generated in this repo by the `_visualize_this` skill. Everything visual produced *for this repo* lands here (not in any external vault).

## What's here

- **`Visuals.canvas`** — an Obsidian Canvas board. Open it in Obsidian to see the diagrams rendered live (Mermaid renders natively inside canvas text nodes — no plugin, no internet).
- **`*.md`** — individual diagram notes. Mermaid renders in Obsidian and on GitHub.

## Where things go (config-driven)

Placement is governed by `.claude/_visualize_this.json`:

| Key | Current | Meaning |
|---|---|---|
| `visualsDir` | `visuals` | Shared visuals home (this folder) |
| `canvasFile` | `visuals/Visuals.canvas` | Canvas board to append diagrams to |
| `personalVisualsDir` | `.personal/{email}/visuals` | Private visuals (per user) |
| `defaultLayer` | `shared` | Default destination layer |
| `defaultFormat` | `md` | Save as Markdown (Obsidian-renderable) vs `html` |
| `saveByDefault` | `true` | Persist every generated visual here, not just inline |

Private / devotional visuals still go to `.personal/<your-email>/visuals/` (e.g. the standalone HTML study sheet lives there). This folder is the **shared** home.
