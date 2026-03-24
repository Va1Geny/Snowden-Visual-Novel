# Contributing to Snowden Visual Novel

## Getting Started

1. Install [RenPy SDK 8.x](https://www.renpy.org/latest.html) on Windows
2. Clone the repository:
   ```bash
   git clone https://github.com/Va1Geny/Snowden-Visual-Novel.git
   cd Snowden-Visual-Novel
   ```
3. Open RenPy Launcher → click **"Open Project"** → select the cloned folder
4. Press **"Launch Project"** to run the game locally
5. Always work from `develop` — never from `main`

## Branch Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable release only — never commit directly |
| `develop` | Active development — base for all work |
| `feature/*` | New scenes, chapters, mechanics |
| `fix/*` | Bug fixes |
| `assets/*` | Images, audio, fonts |

## Daily Workflow

```bash
# 1. Pull latest develop
git checkout develop
git pull origin develop

# 2. Create your branch
git checkout -b feature/your-feature-name

# 3. Make changes and commit
git add .
git commit -m "feat: describe what you did"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

On GitHub: open Pull Request → set base to `develop` → fill the template → request a reviewer.

## Commit Convention

| Prefix | Use for |
|---|---|
| `feat:` | New scene, chapter, character |
| `fix:` | Bug fix in script or UI |
| `assets:` | Images, audio, fonts |
| `docs:` | Documentation changes |
| `chore:` | Config, project structure |

**Examples:**

feat: add chapter 02 Hong Kong escape scene
fix: correct dialogue skip on scene 03
assets: add NSA office background


## Project Structure

**`game/scripts/`** — Story scripts (.rpy files), one file per chapter

**`game/screens/`** — UI screens: main menu, HUD, settings

**`game/characters/`** — Character definitions and sprite assignments

**`game/images/backgrounds/`** — Scene backgrounds (offices, hotels, airports)

**`game/images/sprites/`** — Character sprites and expressions

**`game/images/ui/`** — Buttons, overlays, icons

**`game/audio/music/`** — Background music and ambient tracks

**`game/audio/sfx/`** — Sound effects (typing, alerts, footsteps)

**`game/fonts/`** — Custom fonts

**`docs/`** — Game design documents, character sheets, story outlines

## Rules

- Never push directly to `main` or `develop` — always use a Pull Request
- Every PR must be reviewed and approved before merging
- Link your Jira ticket in every PR (e.g. `NSV-12`)
- Do not include `.rpyc` compiled files in commits
- Test your changes locally in RenPy SDK before opening a PR
- The game targets **Windows only** — do not add web or mobile configs