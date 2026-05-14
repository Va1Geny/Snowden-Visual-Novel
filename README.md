# SNOWDEN VISUAL NOVEL

## `TOP SECRET // EDUCATIONAL // INTERACTIVE`

> "The greatest fear I have regarding the outcome of these disclosures is that nothing will change."
>
> Edward Snowden

**Snowden-Visual-Novel** is a cinematic educational visual novel built in **Ren'Py**.  
The project places the player inside the moral, political, and technical pressure of the 2013 Snowden revelations, combining branching narrative, network-security learning, multilingual support, and a surveillance-themed UI system.

The repository name is **Snowden-Visual-Novel**, while the in-game identity currently references **Enemy of the State** and the dossier-style framing **Classified: The Snowden Files**. The README below reflects the project's existing narrative and visual direction as it appears in the codebase.

---

## Overview

This project is not structured as a generic visual novel. It is designed as an **interactive classified dossier**:

- the player navigates Snowden's final turning-point decisions;
- the story teaches real network-security concepts in context;
- the UI imitates secure terminals, mission briefings, branch analysis panels, and surveillance dashboards;
- choices influence trust, suspicion, branching routes, and final outcomes.

The tone is deliberately tense, procedural, and analytical. Instead of a romanticized VN presentation, the experience leans into **state surveillance aesthetics, intelligence-agency language, and digital-forensics atmosphere**.

---

## Core Experience

The game currently includes:

- **5 story chapters** in the main script arc
- **5 endings**: `hero`, `fugitive`, `imprisoned`, `silenced`, `betrayed`
- **branch tracking / story tree** to review discovered paths and replay decisions
- **interactive security challenges** tied to the plot
- **localized UI and dialogue support**
- **voice pipeline with per-language manifests**
- **custom mission screens**, chapter-select interface, game-over states, and classified briefings

The story blends historical inspiration with fictionalized dialogue to create a playable teaching format around:

- surveillance programs
- whistleblowing
- operational risk
- encryption and secure communication
- firewall and traffic analysis
- digital tradecraft under pressure

---

## Gameplay Structure

The narrative starts with Snowden inside the intelligence machine and escalates through discovery, ethical conflict, exfiltration, and aftermath.

Current chapter flow in the codebase:

| Chapter | Codename | Focus |
|---|---|---|
| 01 | `INSIDE THE MACHINE` | Entering the system, surveillance exposure, firewall fundamentals |
| 02 | `DISCOVERY` | Accessing classified material and understanding the scope |
| 03 | `DECISION` | Conscience vs. duty, risk escalation |
| 04 | `EXFILTRATION` | Secure movement, exposure management |
| 05 | `AFTERMATH` | Consequences, endings, legacy |

The chapter select screen intentionally presents later missions as partially classified, reinforcing the project's espionage framing.

---

## Learning Layer

The educational goal is explicit in the project configuration: the game is designed to teach **network-security fundamentals** through narrative interaction.

Topics surfaced directly in scenes and challenge flows include:

- firewall logic
- internal vs. external IP ranges
- ports and protocols
- packet inspection
- selector-based surveillance
- decryption and brute-force style reasoning
- secure channels and operational mistakes
- digital traces, monitoring, and counter-forensics

This makes the project suitable not only as a narrative experiment, but also as a **gamified teaching artifact** for cybersecurity-adjacent learning.

---

## Visual Direction

The interface language is one of the strongest parts of the project. The codebase consistently uses:

- dark intelligence-console backgrounds
- neon cyan for active signals and primary interaction
- warning red for danger, failure, and detection
- muted steel-gray for secondary system text
- gold and green for special states, hints, and successful analysis
- monospaced / system-style typography for terminal readability

The result is closer to a **classified operations console** than a conventional VN skin.

### Design Keywords

`surveillance` · `classified dossier` · `terminal UI` · `forensic HUD` · `cold bureaucracy` · `neon signal accents` · `high-contrast status states`

### Palette Extracted From The UI

| Role | Hex | Usage |
|---|---|---|
| Deep background | `#080C10` | global backdrop, shadowed void |
| Primary panel | `#0D1117` | menus, frames, screen containers |
| Secondary panel | `#111720` | cards, tiles, hover states |
| Accent cyan | `#00FFD1` | active buttons, highlights, system headers |
| Alert red | `#FF2D55` | danger, suspicion, failure, hostile states |
| Signal green | `#00FF88` | success, validation, positive terminal feedback |
| Classified gold | `#FFD700` | ciphers, emphasis, learned concepts |
| Warning orange | `#FF8C00` | caution markers and intermediate alerting |
| Primary text | `#E8E8E8` | body text and critical readable content |
| Muted text | `#7A8A99` | captions, metadata, secondary narration |
| Faint text | `#3A4A55` | inactive, locked, or low-priority UI |

### README Styling Note

This README has been rewritten to match that same identity:

- concise dossier headers
- system-like labels
- emphasis on tone and interface intent
- technical and narrative sections presented as a mission brief rather than a generic product page

---

## Audio And Localization

The project contains a multilingual structure with text catalogs and voice manifests.

### Supported Languages In Code

| Language | Text | Voice |
|---|---|---|
| English | Yes | Yes |
| French | Yes | Yes |
| Dutch | Yes | Yes |
| Ukrainian | Yes | No dedicated voice manifest currently active |

The translation service supports:

- persistent language switching
- UI string translation
- dialogue translation
- template-based text replacement
- automatic voice-language routing where voice assets exist

---

## Narrative Systems And UX Features

Beyond standard VN dialogue flow, the project includes a broader mission-style interface layer:

- **chapter transition cards** with location, date, time, and clearance level
- **classified briefings** before gameplay segments
- **story tree / branch network** for replay analysis
- **HUD counters** for trust, suspicion, and progress-related states
- **game over screens** that preserve theme consistency
- **notebook / dossier-style information flow**
- **terminal-inspired challenge screens**

This is important because the game is not only telling a story; it is presenting the story through a coherent **surveillance-simulation wrapper**.

---

## Tech Stack

- **Ren'Py 8.x**
- **Python 3.x** through the Ren'Py runtime
- `.rpy` scripting for story, UI, and mechanics
- JSON-based translation and voice manifest support

The project is currently configured around a **Windows-first workflow**.

---

## Running The Project

### Requirements

- [Ren'Py SDK 8.x](https://www.renpy.org/latest.html)
- Windows environment

### Launch Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Va1Geny/Snowden-Visual-Novel.git
   cd Snowden-Visual-Novel
   ```

2. Open the **Ren'Py Launcher**.
3. Choose **Open Project** and select this repository folder.
4. Launch the project from the launcher.

### Development Notes

- work from `develop`, not `main`
- avoid committing compiled `.rpyc` files
- test scenes, UI, and branching locally in Ren'Py before opening a PR

For team workflow details, see [CONTRIBUTING.md](/D:/SkilsProject/Snowden-Visual-Novel/CONTRIBUTING.md).

---

## Project Structure

```text
Snowden-Visual-Novel/
├─ game/
│  ├─ audio/
│  │  └─ voice/
│  │     ├─ en/
│  │     ├─ fr/
│  │     └─ nl/
│  ├─ screens/
│  │  ├─ chapter_select.rpy
│  │  ├─ game_over.rpy
│  │  ├─ screens.rpy
│  │  ├─ text_input_question.rpy
│  │  └─ ui_utilities.rpy
│  ├─ scripts/
│  │  ├─ script.rpy
│  │  ├─ endings.rpy
│  │  ├─ minigames.rpy
│  │  ├─ minigame_3.rpy
│  │  ├─ minigame_4.rpy
│  │  ├─ styles.rpy
│  │  ├─ gui.rpy
│  │  ├─ options.rpy
│  │  ├─ story_tree.rpy
│  │  └─ translation_service.rpy
│  └─ tl/
│     ├─ dutch/
│     ├─ french/
│     └─ ukrainian/
├─ docs/
├─ tools/
└─ README.md
```

### Important Files

- `game/scripts/script.rpy` — main narrative flow and chapter logic
- `game/scripts/endings.rpy` — ending routes and consequence states
- `game/scripts/minigames.rpy` — challenge framework and gameplay interactions
- `game/scripts/styles.rpy` — visual language, color constants, text styles
- `game/scripts/gui.rpy` — Ren'Py GUI configuration
- `game/scripts/translation_service.rpy` — localization pipeline
- `game/scripts/story_tree.rpy` — branch-visualization system
- `game/screens/chapter_select.rpy` — mission selection interface

---

## What Makes This Project Distinct

Many educational games explain concepts first and try to attach a story later. This project does the opposite more effectively:

- the **story motivates the lesson**
- the **interface reinforces the politics of surveillance**
- the **mechanics translate abstract security concepts into player action**
- the **branching outcomes give ethical weight to technical decisions**

That combination gives the project a clear identity: **a narrative cybersecurity experience with a coherent intelligence-brief aesthetic**.

---

## Disclaimer

This game is a **fictionalized dramatization** based on publicly known events, journalistic reporting, and the broader public story around Edward Snowden and mass surveillance.

- It is intended for **educational and artistic purposes**.
- Dialogue is dramatized and should not be treated as a historical transcript.
- The project explores ethics, privacy, and security through interactive fiction rather than documentary reconstruction.

---

## Inspiration

- *Permanent Record* — Edward Snowden
- *No Place to Hide* — Glenn Greenwald
- *Citizenfour* — Laura Poitras
- public discourse around PRISM, XKeyscore, state surveillance, and digital privacy

---

## Status

The repository already contains a substantial playable foundation:

- narrative structure is implemented
- chapter flow exists across five labeled acts
- multiple endings are present
- UI identity is strongly defined
- localization scaffolding is active
- voice manifests are present for supported languages

In short: this is already more than a concept. It is a **playable thematic framework with a clear audiovisual identity**, and the README now reflects that level of intent.
