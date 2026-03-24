# Snowden Visual Novel — Contribution Guide

## Project Structure
Snowden-Visual-Novel/
├── game/
│ ├── scripts/ # Main story scripts (.rpy files), organized by chapter
│ ├── screens/ # UI screens — main menu, HUD, settings, dialogs
│ ├── characters/ # Character definitions, sprites assignment, personality configs
│ ├── images/
│ │ ├── backgrounds/ # Scene backgrounds (offices, hotels, airports, etc.)
│ │ ├── sprites/ # Character sprites and expressions
│ │ └── ui/ # UI elements, buttons, overlays, icons
│ ├── audio/
│ │ ├── music/ # Background music and ambient tracks
│ │ └── sfx/ # Sound effects (typing, alerts, footsteps, etc.)
│ ├── fonts/ # Custom fonts used in the game
│ └── options.rpy # Global RenPy configuration (resolution, title, etc.)
├── docs/ # Game design documents, character sheets, story outlines
├── .github/
│ ├── ISSUE_TEMPLATE/ # Bug report and feature request templates
│ ├── workflows/ # GitHub Actions CI/CD (automated RenPy build)
│ └── PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── LICENSE
└── README.md


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