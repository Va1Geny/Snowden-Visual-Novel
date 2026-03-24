# Snowden Visual Novel — Contribution Guide

## Project Structure
**`Snowden-Visual-Novel/`**

**`game/scripts/`** — Main story scripts (.rpy files), organized by chapter

**`game/screens/`** — UI screens: main menu, HUD, settings, dialogs

**`game/characters/`** — Character definitions, sprite assignments, personality configs

**`game/images/backgrounds/`** — Scene backgrounds (offices, hotels, airports, etc.)

**`game/images/sprites/`** — Character sprites and expressions

**`game/images/ui/`** — UI elements, buttons, overlays, icons

**`game/audio/music/`** — Background music and ambient tracks

**`game/audio/sfx/`** — Sound effects (typing, alerts, footsteps, etc.)

**`game/fonts/`** — Custom fonts used in the game

**`game/options.rpy`** — Global RenPy configuration (resolution, title, etc.)

**`docs/`** — Game design documents, character sheets, story outlines

**`.github/ISSUE_TEMPLATE/`** — Bug report and feature request templates

**`.github/workflows/`** — GitHub Actions CI/CD (automated RenPy build)

## Branch Strategy

- `main` — stable, production-ready branch. Never commit directly. Requires **2 approvals**.
- `develop` — active development branch. All work is merged here first. Requires **1 approval**.
- `feature/*` — new features or chapters (e.g. `feature/chapter-02`)
- `fix/*` — bug fixes (e.g. `fix/dialogue-skip-bug`)
- `setup/*` — project configuration and tooling

**All commits go to `develop` first. Never push directly to `main`.**

## Commit Message Convention

Use the following prefixes:

| Prefix | When to use |
|---|---|
| `feat:` | New scene, chapter, character, or mechanic |
| `fix:` | Bug fix in script logic or UI |
| `chore:` | Config, tooling, project structure |
| `assets:` | Adding or updating images, audio, fonts |
| `docs:` | Changes to documentation |
| `ci:` | GitHub Actions workflow changes |


## Workflow

1. Pull latest `develop` before starting work:
   ```bash
   git checkout develop
   git pull origin develop
   ```
2. Create a new branch from `develop`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make changes, commit using the convention above
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request on GitHub — base branch must be `develop`
6. Fill in the PR template below
7. Request a reviewer — wait for approval before merging

---

## Pull Request Template

**Description of changes**
<!-- What was done and why? -->

**Type of change**
- [ ] New scene / chapter
- [ ] Dialogue or logic fix
- [ ] UI / screens
- [ ] Assets (images, audio, fonts)
- [ ] Bug fix
- [ ] Configuration / tooling

**Checklist before merging**
- [ ] No RenPy syntax errors (tested in RenPy SDK locally)
- [ ] Label and variable names follow project conventions
- [ ] New assets placed in correct folders
- [ ] No `.rpyc` compiled files included in the commit
- [ ] Tested full playthrough of affected scenes
- [ ] PR targets `develop`, not `main`
<<<<<<< HEAD

## What was done?
<!-- Briefly describe your changes -->

## Type of change
- [ ] New scene / chapter
- [ ] Dialogue or logic fix
- [ ] UI / screens
- [ ] Assets (images, audio, fonts)
- [ ] Bug fix
- [ ] Configuration / tooling

## Checklist
- [ ] Tested locally in RenPy SDK
- [ ] No .rpyc files included in commit
- [ ] New assets placed in correct folders
- [ ] PR targets `develop`, not `main`

## Jira ticket
<!-- NSV-XX -->
=======
>>>>>>> 23e7e5608b5a7c080a175e26fd18fce263fae2bc
