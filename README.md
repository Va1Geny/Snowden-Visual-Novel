# SNOWDEN VISUAL NOVEL

## `TOP SECRET // EDUCATIONAL // INTERACTIVE`

> "The greatest fear I have regarding the outcome of these disclosures is that nothing will change."
>
> Edward Snowden

**Snowden-Visual-Novel** is a cinematic educational visual novel built in **Ren'Py 8.x**.  
It places the player inside a dramatized version of the Snowden disclosures and turns cybersecurity concepts into narrative pressure, UI language, and playable systems instead of treating them as detached lessons.

The repository is named **Snowden-Visual-Novel**, while the in-game project identity currently blends:

- **Enemy of the State** as the launcher/game title
- **Classified: The Snowden Files** as the dossier framing
- a fictionalized agency wrapper such as **Signal Reach Network** and **The Obsidian Oversight** for safer narrative abstraction

This README documents the project as it currently exists in the codebase: a playable narrative-security experience with custom UI, branching consequences, minigames, localization, voice support, and a surprisingly broad amount of systems work for a VN project.

---

## What This Project Is

This is not a conventional visual novel with static dialogue boxes and occasional choices.

It is designed as an **interactive surveillance dossier** where:

- the player learns network-security concepts inside the plot
- UI behaves like mission software, not a generic VN skin
- technical knowledge changes the emotional weight of decisions
- endings feel tied to operational tradeoffs rather than arbitrary morality flags
- story progression is wrapped in briefing screens, classified metadata, chapter transitions, and branch analysis tools

The result sits somewhere between:

- visual novel
- interactive classroom artifact
- themed cyber-operations simulator
- branching historical-fiction dramatization

---

## Core Identity

The project’s strongest distinguishing feature is that **theme, mechanics, and interface all point in the same direction**.

### Narrative identity

The story puts the player in the role of Snowden during the surveillance revelations and builds tension around:

- insider access
- state surveillance
- trust and whistleblowing
- secure communication
- exfiltration risk
- evidence handling
- the cost of exposure

### Educational identity

The game is explicitly educational. It teaches concepts such as:

- firewalls
- ports and protocols
- internal vs. external IPs
- HTTPS and TLS
- VPN and Tor
- metadata and session tokens
- password hashing and cracking
- operational security
- secure deletion and digital forensics

### Aesthetic identity

The project consistently frames all of this through:

- terminal-style typography
- neon-cyan interaction accents
- alert reds and warning golds
- classified dossier layouts
- surveillance dashboards
- scanlines and signal-line effects
- mission cards, chapter metadata, and status panels

This consistency is what makes the project feel more like a system than a collection of scenes.

---

## Experience Highlights

The current codebase already includes a lot more than “story + choices”.

### Implemented high-level features

- **5 major story chapters**
- **5 endings**
- **4 substantial minigames**
- **multiple MCQ / educational question screens**
- **branch tracking and replay analysis**
- **mission briefings before challenges**
- **chapter transition cinematics**
- **multilingual UI and dialogue routing**
- **voice-language switching where assets exist**
- **field notebook system**
- **network-security dossier / glossary**
- **custom HUD and mission-control style overlays**
- **fullscreen onboarding prompt**
- **accessibility settings and self-voicing support**
- **custom ambient audio channel**
- **loading video screen**
- **developer shortcut menu for testing endings and minigames**

---

## Story Structure

The narrative arc is structured around escalation: access, discovery, doubt, contact, exfiltration, and consequences.

### Current chapter flow

| Chapter | Codename | Focus |
|---|---|---|
| 01 | `INSIDE THE MACHINE` | surveillance exposure, internal systems, firewall fundamentals |
| 02 | `DISCOVERY` | classified access, scale of surveillance, early technical lessons |
| 03 | `DECISION` | journalist contact, OpSec, encryption, trust |
| 04 | `EXFILTRATION` | movement, route planning, trace removal, exposure management |
| 05 | `AFTERMATH` | consequence resolution, ending logic, legacy |

The story is fictionalized rather than documentary-accurate line-for-line, but it deliberately stays anchored to real cybersecurity vocabulary and recognizable public themes from the Snowden case.

---

## Endings

The game currently supports five themed endings:

- `hero`
- `fugitive`
- `imprisoned`
- `silenced`
- `betrayed`

These are not simple cosmetic branches. They are shaped by a mix of:

- `knowledge_score`
- `trust_score`
- `suspicion_level`
- `contacts_secured`
- `evidence_secured`
- `identity_exposed`
- `escape_successful`

This is one of the project’s more interesting narrative choices: outcomes are tied to both ethical choices and technical competence.

---

## Minigames And Learning Design

One of the most unusual strengths of the project is that the educational layer is delivered through **custom-built gameplay**, not just exposition.

### 1. Firewall Breach

File: [game/scripts/minigames.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigames.rpy:367)

Concepts covered:

- internal vs. public IP addresses
- safe vs. suspicious ports
- protocol classification
- allow/block reasoning
- threat analysis under time pressure

Implementation notes:

- packet data is defined in Python dictionaries
- each packet includes explanation text and risk level
- the player is timed per packet
- the UI includes packet signatures, streaks, score, packet logs, and feedback overlays
- success/failure is visualized as a real-time security console rather than a quiz page

### 2. Decrypt The Message

File: [game/scripts/minigames.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigames.rpy:2298)

Concepts covered:

- Caesar ciphers
- key shifting
- pattern recognition
- encryption as an idea, not just a lore term

Implementation notes:

- staged word-by-word flow
- transition popups between rounds
- score aggregation and rating logic
- separate result screen with learning summary

### 3. Brute Force

File: [game/scripts/minigame_3.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigame_3.rpy:656)

Concepts covered:

- dictionary attacks
- John the Ripper workflow
- wordlists
- mutation rules
- bcrypt vs. weak MD5
- why “clever” passwords still fail

Implementation notes:

- custom terminal simulation with typed input
- command validation and acceptable variants
- staged rounds with different security scenarios
- contextual hints after mistakes
- token-level autocomplete on `TAB`
- output queue simulation for terminal feel
- learning summary between rounds and after completion

This is one of the most distinctive systems in the repository because it teaches command-line reasoning inside a narrative minigame.

### 4. Cover Your Tracks

File: [game/scripts/minigame_4.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigame_4.rpy:1040)

Concepts covered:

- browser history deletion
- session tokens
- EXIF stripping
- secure shredding
- MAC randomization
- journal wiping
- shell history cleanup
- cloud-sync evidence risks

Implementation notes:

- 8-trace structure with escalating tension
- multiple interaction modes: guided, assembly, select
- central countdown timer with penalties
- threat meter, waveform widgets, scanlines, faux telemetry
- command breakdown panels and “what you learned” debriefing

This is probably the most elaborate minigame in the project from a UI and systems standpoint.

### Additional educational interaction

Outside the big minigames, the story also includes:

- multiple-choice checks
- embedded system notes
- contextual explanations inside dialogue
- glossary support through the dossier screen

The project consistently tries to teach by **placing concepts under pressure**, not by pausing the story for textbook paragraphs.

---

## Systems That Make The Project Unusual

### Branch Network / Story Tree

File: [game/scripts/story_tree.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\story_tree.rpy:1)

The game includes a dedicated **story tree / branch network** screen that tracks:

- unlocked choices across runs
- active choices in the current run
- chapter completion progress
- unlocked endings
- total branch reconstruction percentage

This turns replay into investigation. Instead of simply replaying scenes, the player reconstructs a branching decision network like an analyst reviewing an operation.

### Network Security Dossier

Defined from `DOSSIER_ENTRIES` in [game/scripts/definitions.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\definitions.rpy:213) and rendered in [game/screens/screens.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\screens\screens.rpy:1968)

The dossier is effectively an in-game cybersecurity reference library:

- glossary entries are curated in Python
- terms are shown in a custom dossier screen
- export to `.txt` is supported
- the screen has its own shell-like styling and animated framing

This is much more deliberate than a standard “help menu”.

### Field Notebook

Screen implementation: [game/screens/screens.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\screens\screens.rpy:906)

The notebook allows players to:

- write their own notes during play
- keep track of names, ideas, and clues
- export notes to `.txt`
- use hotkeys for quick access

This is a small feature on paper, but it strongly supports the dossier fantasy and the educational use case.

### Mission Briefings

File: [game/scripts/screens_briefing.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\screens_briefing.rpy:78)

Every major challenge can be preceded by a highly stylized mission-briefing screen that includes:

- mission ID
- classification
- challenge type
- estimated time
- difficulty bar
- rewards and penalties
- learning objective
- controls reference

This helps the project feel like a coherent operations platform rather than a chain of ad-hoc minigames.

### Chapter Transition Cards

File: [game/scripts/screens_briefing.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\screens_briefing.rpy:74)

Chapters are introduced through cinematic transition screens with:

- codename typing animation
- clearance metadata
- location, date, and time
- animated divider lines
- motion-aware sequencing

This is one of the cleaner examples of how presentation has been custom-built beyond Ren’Py defaults.

### Suspicion Watch / HUD Layer

The project uses overlay screens for ongoing state presentation, including:

- quick menu
- game HUD
- notebook toggle
- suspicion lockdown watch

This is configured in [game/screens/screens.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\screens\screens.rpy:5), which makes the experience feel persistent and instrumented rather than scene-isolated.

---

## UI / UX Direction

The interface language is one of the best-developed parts of the repository.

### Core visual motifs

- dark layered panels instead of flat VN boxes
- monospaced metadata labels
- cyan signal accents for active interaction
- red/pink threat color for suspicion and danger
- steel-gray secondary copy
- scanlines, dividers, framing brackets, and “system” microcopy

### Core palette

| Role | Hex | Use |
|---|---|---|
| Deep background | `#080C10` | void / stage backdrop |
| Primary panel | `#0D1117` | main shells and surfaces |
| Secondary panel | `#111720` | cards, tiles, raised UI |
| Accent cyan | `#00FFD1` | active state, buttons, headers |
| Alert red | `#FF2D55` | danger, failure, suspicion |
| Success green | `#00FF88` | validated actions, success states |
| Classified gold | `#FFD700` | emphasis, difficulty, special labels |
| Muted text | `#7A8A99` | secondary information |
| Faint text | `#3A4A55` | inactive or low-priority labels |

### Typography

The project intentionally mixes:

- **Rajdhani** for body/interface text
- **ShareTechMono** for terminals, tags, and system overlays

This dual-font approach helps separate narrative readability from technical presentation.

### Why the UI feels different

Many VNs reskin the default interface. This project instead builds:

- custom chapter cards
- custom dossier screens
- custom notebook panel
- custom branch web
- custom challenge HUDs
- custom notification styling
- custom mission control / pause hub style flows

That amount of interface work is one of the clearest “non-standard” things about the project.

---

## Audio, Voice, And Atmosphere

The audio layer is more deliberate than a typical prototype.

### Present in the codebase

- sound effects for UI hover, click, notify, success, failure, suspicion
- looping ambient tracks for different environments
- a dedicated `ambient` channel registered in Python
- voice asset structure by language
- loading animation splash flow

### Ambient design

Ambient tracks are separated by scene type, including:

- office ambience
- terminal ambience
- server hum
- Hong Kong street / room / airport environments
- TV-news murmur
- winter wind
- airport sound beds

This matters because the project’s tone depends heavily on procedural tension, not just dialogue writing.

---

## Localization And Language Pipeline

File: [game/scripts/translation_service.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\translation_service.rpy:1)

Localization is not a placeholder layer. The game includes a real translation service with:

- current-language persistence
- revision-based refresh logic
- separate **UI text** and **dialogue** catalogs
- template-aware translation
- language-switch confirmation flow
- voice-language routing
- fallback behavior when assets are missing

### Languages currently represented in the repository

| Language | UI / Text | Dialogue | Voice routing |
|---|---|---|---|
| English | Yes | Yes | Yes |
| French | Yes | Yes | Yes |
| Dutch | Yes | Yes | Yes |
| Ukrainian | Partial repository presence | Partial / scaffold presence | no dedicated active voice routing |

### Interesting implementation detail

The translation layer can compile template-like strings with placeholders, rather than only exact literal matches. That gives the project more flexibility than a naive string-replacement setup.

### Additional text logic

`IMPORTANT_TERMS` are also used to enrich displayed dialogue so cybersecurity terms can be emphasized automatically in rich-text output.

---

## Accessibility And Cross-Context UX

The project includes several thoughtful UX systems that are easy to overlook:

- fullscreen recommendation prompt at startup
- controls-and-shortcuts onboarding screen
- self-voicing toggle
- accessibility menu
- alternate accessibility font application
- high-contrast support hooks
- responsive adjustments for `small`, `touch`, `pc`, `web`, and mobile-related variants

The fullscreen prompt explicitly mentions better fit for:

- minigames
- itch.io embeds
- mobile browsers

That means the project is already being designed with presentation context in mind, not just desktop play.

---

## Technical Architecture

### Runtime stack

- **Ren'Py 8.5.x**
- Python runtime inside Ren'Py
- `.rpy` for story, UI, logic, and systems
- JSON catalogs for translation and voice-related text support

### Important gameplay state

Core progression is tracked through defaults such as:

- `trust_score`
- `knowledge_score`
- `suspicion_level`
- `contacts_secured`
- `evidence_secured`
- `identity_exposed`
- `escape_successful`

There are also dedicated minigame-related defaults for things like:

- firewall results
- decrypt completion
- brute-force progress
- trace removal outcomes

### Fictional abstraction layer

The codebase includes a legal / narrative sanitization layer via variables such as:

- `ag_nsa = "Signal Reach Network"`
- `ag_cia = "The Obsidian Oversight"`
- `ag_fbi = "Bureau of Internal Security"`

That is a subtle but interesting design decision: the game wants the political meaning of the real-world story while preserving some fictional flexibility in the text layer.

### Notifications and feedback

`sfx_notify_stat()` centralizes:

- stat-related notification text
- category-based sound playback
- `renpy.notify()` output

This keeps feedback consistent across story beats and minigames.

### Motion-aware presentation

Several cinematic screens are written with `renpy.variant("reduces_motion")` support, allowing content to degrade more gracefully for users who prefer less animation.

---

## Project Structure

```text
Snowden-Visual-Novel/
├─ game/
│  ├─ audio/
│  │  ├─ sfx/
│  │  └─ voice/
│  │     ├─ en/
│  │     ├─ fr/
│  │     └─ nl/
│  ├─ gui/
│  ├─ images/
│  ├─ screens/
│  │  ├─ chapter_select.rpy
│  │  ├─ game_over.rpy
│  │  ├─ screens.rpy
│  │  ├─ text_input_question.rpy
│  │  └─ ui_utilities.rpy
│  ├─ scripts/
│  │  ├─ definitions.rpy
│  │  ├─ endings.rpy
│  │  ├─ gui.rpy
│  │  ├─ minigames.rpy
│  │  ├─ minigame_3.rpy
│  │  ├─ minigame_4.rpy
│  │  ├─ options.rpy
│  │  ├─ screens_briefing.rpy
│  │  ├─ script.rpy
│  │  ├─ splashscreen.rpy
│  │  ├─ story_tree.rpy
│  │  ├─ styles.rpy
│  │  └─ translation_service.rpy
│  └─ tl/
│     ├─ dutch/
│     ├─ french/
│     └─ ukrainian/
├─ docs/
├─ launcher/
├─ tools/
├─ CONTRIBUTING.md
└─ README.md
```

### Key files

- [game/scripts/script.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\script.rpy:1)  
  Main story flow, chapter progression, scene logic, and where many teaching beats are integrated into the narrative.

- [game/scripts/endings.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\endings.rpy:1)  
  Ending routing, result screens, and developer shortcut logic for testing branches and minigames.

- [game/scripts/minigames.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigames.rpy:1)  
  Shared minigame infrastructure, firewall, decrypt game, and trace-routing challenge content.

- [game/scripts/minigame_3.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigame_3.rpy:1)  
  Terminal-driven password cracking simulation.

- [game/scripts/minigame_4.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\minigame_4.rpy:1)  
  Large-scale anti-forensics minigame with telemetry-heavy UI.

- [game/scripts/definitions.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\definitions.rpy:1)  
  Shared definitions, character declarations, stats, audio helpers, important-term glossary, and dossier data.

- [game/scripts/translation_service.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\translation_service.rpy:1)  
  Localization backend.

- [game/scripts/story_tree.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\story_tree.rpy:1)  
  Branch visualization and persistent route analysis.

- [game/screens/screens.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\screens\screens.rpy:1)  
  Large UI hub for overlays, dossier, notebook, history, settings, HUDs, and many custom screens.

- [game/scripts/screens_briefing.rpy](D:\SkilsProject\Snowden-Visual-Novel\game\scripts\screens_briefing.rpy:1)  
  Mission-style transitions and challenge briefings.

---

## How The Project Is Implemented

At a high level, the implementation follows a very sensible layered structure:

### 1. Story layer

The main dramatic flow lives in `script.rpy`, where:

- chapter labels are defined
- choices are recorded
- stats are modified
- educational scenes are interleaved with branching dialogue
- minigames are inserted at narrative pressure points

### 2. Shared state layer

`definitions.rpy` provides:

- character setup
- global defaults
- important-term metadata
- audio helpers
- reusable glossary content

### 3. Screen / presentation layer

Custom interfaces are split across:

- `screens.rpy`
- `screens_briefing.rpy`
- `chapter_select.rpy`
- game-over and utility screens

This is where the dossier aesthetic really becomes concrete.

### 4. Minigame layer

Each major challenge is implemented as its own gameplay system with:

- bespoke state
- custom rendering
- dedicated result logic
- educational explanation pass

### 5. Localization layer

`translation_service.rpy` acts as a centralized adapter between source strings, translated catalogs, and language-dependent voice behavior.

### 6. Persistence / replay layer

The story tree and ending unlock systems preserve progress across runs, which supports the “reconstruct the operation” replay fantasy.

---

## Running The Project

### Requirements

- [Ren'Py SDK 8.x](https://www.renpy.org/latest.html)
- Windows-first local workflow

### Launch

1. Clone the repository:

   ```bash
   git clone https://github.com/Va1Geny/Snowden-Visual-Novel.git
   cd Snowden-Visual-Novel
   ```

2. Open the project with the **Ren'Py Launcher**.
3. Select this repository folder.
4. Launch the game from the launcher.

### In-game identity note

Depending on where you look, you may see:

- repository branding: `Snowden-Visual-Novel`
- launcher/game title: `Enemy of the State`
- dossier framing: `Classified: The Snowden Files`

That is expected with the current codebase.

---

## Development Notes

### Workflow

- use `develop`, not `main`
- avoid committing generated `.rpyc` files where possible
- test both story flow and minigame flow after UI changes
- verify localized UI if a change touches shared strings

### Why testing matters here

This project mixes:

- branching narrative
- timed interaction
- custom screen logic
- persistent progress
- language-aware text systems

That means regressions can happen in places that normal VN projects never touch.

### Team documentation

See [CONTRIBUTING.md](D:\SkilsProject\Snowden-Visual-Novel\CONTRIBUTING.md) for workflow expectations.

---

## What Makes The Project Distinct

Many educational games bolt lessons onto a story.  
Many visual novels bolt choices onto static dialogue.  
This project does something more integrated:

- **the story motivates the lesson**
- **the UI reinforces the politics of surveillance**
- **the minigames make abstract security concepts tactile**
- **the replay structure treats narrative like intelligence reconstruction**
- **the audiovisual language stays coherent across menus, gameplay, and endings**

That combination is what makes the project memorable.

It is not only “a VN about Snowden”.  
It is a **themed cyber-literacy experience wrapped in a classified operations interface**.

---

## Disclaimer

This game is a **fictionalized dramatization** inspired by public reporting, broader surveillance discourse, and the Snowden revelations.

- It is intended for **educational and artistic use**.
- Dialogue is dramatized and not a historical transcript.
- Real-world technical concepts are used in an interactive fiction context.

---

## Inspiration

- *Permanent Record* — Edward Snowden
- *No Place to Hide* — Glenn Greenwald
- *Citizenfour* — Laura Poitras
- public discussion around PRISM, XKeyscore, metadata collection, privacy, and digital surveillance

---

## Current Status

This repository is already well beyond concept stage.

It already contains:

- a complete thematic direction
- substantial custom UI
- playable multi-chapter narrative flow
- multiple endings
- four distinct minigames
- localization infrastructure
- voice-routing logic
- educational glossary and notebook systems
- replay / branch-tracking support

In short: this is already a **playable, system-rich educational visual novel with a strong identity**, and the most interesting part is how consistently the project makes story, learning, and interface serve the same mission.
