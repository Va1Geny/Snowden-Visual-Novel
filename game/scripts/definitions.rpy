################################################################################
## DEFINITIONS.RPY — Character Definitions, Flags, Images, Transforms
## Classified: The Snowden Files
################################################################################

init offset = -1

################################################################################
## CHARACTER DEFINITIONS
################################################################################

# === PROTAGONIST ===
define e = Character("You",
    image="edward",
    color="#00FFD1",
    what_color="#E8E8E8",
    who_size=22,
    what_size=20,
    who_bold=True)

# === JOURNALISTS ===
define greenwald = Character("Grayson Wardell",
    image="greenwald",
    color="#FFD700",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define poitras = Character("Leah Portman",
    image="poitras",
    color="#FF69B4",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ANTAGONISTS / AUTHORITY ===
define nsa_chief = Character("Director Marcus Hale",
    image="nsa_chief",
    color="#FF2D55",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define supervisor = Character("Supervisor Daniel Cross",
    image="supervisor",
    color="#FF6B35",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ALLIES / NEUTRAL ===
define colleague = Character("COLLEAGUE [[CLASSIFIED]]",
    image="colleague",
    color="#888888",
    what_color="#CCCCCC",
    who_bold=False,
    who_size=22,
    what_size=20)

define russian_official = Character("Agent Viktor Malenkov",
    image="russian_official",
    color="#CC2222",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === SYSTEM / NARRATOR ===
define sys = Character("// SYSTEM //",
    color="#00FF00",
    what_color="#00FF00",
    who_bold=True,
    who_size=20,
    what_size=18)

define narrator_voice = Character(None,
    what_color="#AAAAAA",
    what_italic=True,
    what_size=22)

define im = Character("INTERNAL MONOLOGUE",
    what_prefix="*",
    what_suffix="*",
    color="#888888",
    what_color="#AAAAAA",
    who_size=18,
    what_size=20)


################################################################################
## STORY FLAGS
################################################################################

# === Core Metrics ===
default trust_score = 0
default knowledge_score = 0
default suspicion_level = 0
default contacts_secured = 0
default evidence_secured = False
default identity_exposed = False
default escape_successful = False

# === Chapter Completion Flags ===
default ch1_outcome = ""
default ch2_outcome = ""
default ch3_outcome = ""
default ch4_outcome = ""

# === Ending Tracker ===
default ending_type = ""

# === UI State ===
default current_chapter = 1
default show_hud = True
default notebook_entries = []
default notebook_draft = ""
default suspicion_lockdown_triggered = False

# === Minigame State ===
default mg_firewall_score = 0
default mg_decrypt_solved = False
default mg_opsec_score = 0
default mg_trace_solved = False
default cover_wiped = 0
default cover_failed = 0

# === Question Tracking ===
default text_input_attempts = 0


################################################################################
## PARALLAX SYSTEM
################################################################################

init python:
    import re
    import os
    from datetime import datetime
    import store

    IMPORTANT_TERMS = [
        "USA FREEDOM Act",
        "Virtual Private Network",
        "The Onion Router",
        "man-in-the-middle",
        "Inspector General",
        "reverse shell",
        "traffic correlation attack",
        "Domain Name System",
        "Boundless Informant",
        "SecureDrop",
        "Edward Snowden",
        "national security",
        "private IP ranges",
        "public Wi-Fi",
        "foreign intelligence",
        "domestic surveillance",
        "encryption fingerprints",
        "network security",
        "mass surveillance",
        "XKeyscore",
        "metadata",
        "firewall",
        "VPN",
        "PGP",
        "PRISM",
        "Tor",
        "TLS",
        "SSH",
        "RDP",
        "DNS",
        "HTTP",
        "HTTPS",
        "Telnet",
        "AES-256",
        "OpSec",
        "zero-day",
        "FISA",
        "NSA",
        "CIA",
    ]

    def current_viewport_size():
        width = config.screen_width
        height = config.screen_height

        try:
            physical_size = renpy.get_physical_size()
            if physical_size:
                width, height = physical_size
        except Exception:
            pass

        return width, height

    def fullscreen_prompt_supported():
        return renpy.variant("pc") or renpy.variant("web")

    def should_prompt_for_fullscreen():
        return fullscreen_prompt_supported() and not preferences.fullscreen

    def is_compact_layout():
        width, height = current_viewport_size()
        return renpy.variant("small") or width <= 1280 or height <= 760

    def is_medium_layout():
        width, height = current_viewport_size()
        return renpy.variant("touch") or width <= 1600 or height <= 900

    def notebook_entry_count():
        return len(store.notebook_entries)

    def add_notebook_entry(text):
        entry = (text or "").strip()
        if not entry:
            renpy.notify("Write a note first.")
            return

        store.notebook_entries = list(store.notebook_entries) + [entry]
        store.notebook_draft = ""
        renpy.notify("Saved to notebook.")
        renpy.restart_interaction()

    def clear_notebook_entries():
        store.notebook_entries = []
        store.notebook_draft = ""
        renpy.notify("Notebook cleared.")
        renpy.restart_interaction()

    def get_notebook_export_text():
        header = "FIELD NOTEBOOK\nClassified: The Snowden Files\n\n"
        body = "\n".join(f"{index}. {entry}" for index, entry in enumerate(store.notebook_entries, 1))
        return header + body

    def get_notebook_export_dir():
        paths = [
            os.path.join(config.basedir, "exports"),
            os.path.join(os.path.expanduser("~"), "RenPyNotebookExports"),
        ]

        for path in paths:
            try:
                os.makedirs(path, exist_ok=True)
                return path
            except Exception:
                pass

        return None

    def choose_notebook_export_path(default_filename="field_notebook.txt"):
        root = None

        try:
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            root.update_idletasks()
            root.lift()
            root.focus_force()

            path = filedialog.asksaveasfilename(
                title="Save notebook as...",
                initialdir=os.path.expanduser("~"),
                initialfile=default_filename,
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            )

            root.destroy()
            return path
        except Exception:
            try:
                if root is not None:
                    root.destroy()
            except Exception:
                pass

        if hasattr(renpy, "filepicker"):
            try:
                path = renpy.filepicker(
                    title="Save notebook as...",
                    save=True,
                    default=default_filename,
                )
                if path is None:
                    return ""
                return path
            except TypeError:
                try:
                    path = renpy.filepicker(
                        title="Save notebook as...",
                        save=True,
                    )
                    if path is None:
                        return ""
                    return path
                except Exception:
                    pass
            except Exception:
                pass

        return None

    def export_notebook_txt():
        if not store.notebook_entries:
            renpy.notify("No notes to export.")
            return

        default_filename = datetime.now().strftime("field_notebook_%Y%m%d_%H%M%S.txt")
        path = choose_notebook_export_path(default_filename)

        if path == "":
            renpy.notify("Notebook export canceled.")
            return

        if path is None:
            export_dir = get_notebook_export_dir()
            if not export_dir:
                renpy.notify("Could not determine a writable export location.")
                return

            path = os.path.join(export_dir, default_filename)
            renpy.notify("Could not open a save dialog. Exporting to the default exports folder.")

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(get_notebook_export_text())

            renpy.notify(f"Notebook exported to {path}")
        except Exception as exc:
            renpy.notify(f"Failed to export notebook: {exc}")

    # ─── RUNTIME DIALOGUE TRANSLATION ────────────────────────────────────
    # Ren'Py's built-in `translate <lang> strings:` only fires for strings
    # wrapped in `_(...)`. Wrapping every dialogue line is impractical here,
    # so instead we hook into config.say_menu_text_filter (the same pipeline
    # that adds {b} tags to important terms) and substitute the dialogue
    # text from a per-language JSON dictionary BEFORE highlighting runs.
    #
    # Translation files live at game/tl/<lang>/dialogue.json with the
    # shape { "english string": "translated string", ... }. Missing entries
    # silently fall back to the English original — the game never breaks
    # because of a partial translation.

    _DIALOGUE_TRANSLATIONS = {}
    _TEXT_TRANSLATIONS = {}
    _TEXT_TRANSLATION_TEMPLATES = {}
    _TRANSLATION_DEBUG_SEEN = set()

    def _load_dialogue_translation(lang):
        if lang in _DIALOGUE_TRANSLATIONS:
            return _DIALOGUE_TRANSLATIONS[lang]
        data = {}
        try:
            import json, os
            path = os.path.join(config.gamedir, "tl", lang, "dialogue.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as fp:
                    raw = json.load(fp)
                # Accept either {en: tr} or list[{src, text, tr_<lang>}].
                if isinstance(raw, dict):
                    data = raw
                elif isinstance(raw, list):
                    for entry in raw:
                        if isinstance(entry, dict) and "text" in entry and "tr" in entry:
                            data[entry["text"]] = entry["tr"]
        except Exception:
            data = {}
        _DIALOGUE_TRANSLATIONS[lang] = data
        return data

    def _load_text_translation(lang):
        if lang in _TEXT_TRANSLATIONS:
            return _TEXT_TRANSLATIONS[lang]

        exact = {}
        templates = []

        try:
            import json, os
            path = os.path.join(config.gamedir, "tl", lang, "text.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as fp:
                    raw = json.load(fp)

                if isinstance(raw, dict):
                    for src, tr in raw.items():
                        if not isinstance(src, str) or not isinstance(tr, str):
                            continue

                        src = src.strip()
                        tr = tr.strip()

                        if not src or not tr:
                            continue

                        if "[" in src and "]" in src:
                            placeholders = re.findall(r"(\[[^\]]+\])", src)
                            parts = re.split(r"(\[[^\]]+\])", src)
                            pattern = "^"
                            for part in parts:
                                if not part:
                                    continue
                                if re.match(r"\[[^\]]+\]", part):
                                    pattern += "(.+?)"
                                else:
                                    pattern += re.escape(part)
                            pattern += "$"
                            templates.append((re.compile(pattern), placeholders, tr))
                        else:
                            exact[src] = tr
        except Exception:
            exact = {}
            templates = []

        templates.sort(key=lambda item: len(item[0].pattern), reverse=True)
        _TEXT_TRANSLATIONS[lang] = exact
        _TEXT_TRANSLATION_TEMPLATES[lang] = templates
        return exact

    def _translate_text_template(text, lang, depth=0):
        if depth > 3:
            return text

        _load_text_translation(lang)
        templates = _TEXT_TRANSLATION_TEMPLATES.get(lang, [])

        for pattern, placeholders, translated_template in templates:
            match = pattern.match(text)
            if not match:
                continue

            result = translated_template

            for index, placeholder in enumerate(placeholders, 1):
                replacement = _translate_display_text(match.group(index), lang, depth + 1)
                result = result.replace(placeholder, replacement)

            return result

        return text

    def _translate_display_text(text, lang=None, depth=0):
        if not text:
            return text

        if lang is None:
            try:
                lang = _preferences.language
            except Exception:
                lang = None

        if not lang:
            return text

        try:
            import os
            sample = text.strip()
            if sample and len(_TRANSLATION_DEBUG_SEEN) < 40 and sample not in _TRANSLATION_DEBUG_SEEN:
                _TRANSLATION_DEBUG_SEEN.add(sample)
                with open(os.path.join(config.basedir, "translation_debug.log"), "a", encoding="utf-8") as fp:
                    fp.write("%s\t%s\n" % (lang, sample))
        except Exception:
            pass

        exact = _load_text_translation(lang)
        if text in exact:
            return exact[text]

        return _translate_text_template(text, lang, depth)

    def translated_dialogue(text):
        """Map English source to current-language translation, if any."""
        if not text:
            return text
        try:
            lang = _preferences.language
        except Exception:
            lang = None
        if not lang:
            return text
        catalog = _load_dialogue_translation(lang)
        try:
            import os
            if text in (
                "The year is 2013.",
                "The United States government operates the most sophisticated surveillance network in human history.",
            ):
                with open(os.path.join(config.basedir, "translation_dialogue_debug.log"), "a", encoding="utf-8") as fp:
                    fp.write("%s\t%s\t%s\n" % (lang, text, text in catalog))
        except Exception:
            pass
        translated = catalog.get(text)
        if translated is not None:
            return translated
        return _translate_display_text(text, lang)

    def highlighted_dialogue(text):
        if not text:
            return text

        # Translate FIRST — highlighting runs on the localized text so
        # important terms still get bolded in any language.
        result = translated_dialogue(text)

        try:
            import os
            sample = text.strip()
            if sample and len(_TRANSLATION_DEBUG_SEEN) < 80 and sample not in _TRANSLATION_DEBUG_SEEN:
                _TRANSLATION_DEBUG_SEEN.add(sample)
                with open(os.path.join(config.basedir, "translation_debug.log"), "a", encoding="utf-8") as fp:
                    fp.write("FILTER\t%s\t%s\t=>\t%s\n" % (_preferences.language, sample, result.strip()))
        except Exception:
            pass

        for term in sorted(IMPORTANT_TERMS, key=len, reverse=True):
            pattern = re.compile(r"(?<!\{b\})(%s)(?!\{/b\})" % re.escape(term), re.IGNORECASE)
            result = pattern.sub(lambda match: "{b}%s{/b}" % match.group(1), result)

        return result

    config.say_menu_text_filter = highlighted_dialogue
    config.replace_text = _translate_display_text

    # ─── ACTIVE SPEAKER HIGHLIGHTING ──────────────────────────────────────
    # Brighten the current speaker, dim everyone else. The earlier version
    # was disabled because `renpy.show(tag, at_list=[active_char])` REPLACED
    # the at_list — the entry transform (enter_left/stage_center/...) was
    # discarded and characters snapped to (0, 0).
    #
    # This version preserves position by reading the live at_list with
    # `renpy.get_at_list`, stripping any prior state transform, and re-
    # applying `[position_transform, state_transform]`. Because Ren'Py
    # treats the same transform reference as state-preserving, the entry
    # animation isn't restarted — only the state layer is swapped.
    SPEAKER_HIGHLIGHT_TAGS = (
        "edward",
        "supervisor",
        "colleague",
        "greenwald",
        "poitras",
        "journalist",
        "editor",
        "nsa_chief",
        "russian_official",
    )

    def _strip_speaker_state(at_list):
        # We assume the first transform is the position/entry transform
        # Everything else is previous state transforms which we strip
        return at_list[:1] if at_list else []

    def speaker_dimmer(event, interact=True, **kwargs):
        if not interact or event != "begin":
            return

        speaker_tag = renpy.get_say_image_tag()

        for tag in SPEAKER_HIGHLIGHT_TAGS:
            if not renpy.showing(tag):
                continue

            try:
                current = renpy.get_at_list(tag, "master")
            except Exception:
                current = None

            position_transforms = _strip_speaker_state(list(current or ()))

            # If we have no position context, skip — re-applying with an
            # empty position list would default the character to (0, 0).
            if not position_transforms:
                continue

            new_state = active_char if tag == speaker_tag else inactive_char
            renpy.show(tag, at_list=position_transforms + [new_state])

    config.character_callback = speaker_dimmer


    def autosave_chapter(chapter_num):
        """Autosave after a chapter completes and show a notification."""
        try:
            # Save to a dedicated 'chapter' page so it gets its own tab in the Load screen
            renpy.save("chapter-%d" % chapter_num, extra_info="Chapter %d" % chapter_num)
            renpy.notify("Chapter %d autosave complete." % chapter_num)
        except Exception:
            renpy.notify("Autosave failed.")

    def mouse_parallax(trans, st, at):
        # Provide a subtle parallax based on mouse
        # Ren'Py get_mouse_pos() might return a tuple
        import pygame
        x, y = renpy.get_mouse_pos()
        
        # Calculate offset from center (assuming 1920x1080)
        trans.xoffset = (960 - x) * 0.02
        trans.yoffset = (540 - y) * 0.02
        return 0

transform parallax:
    zoom 1.05
    align (0.5, 0.5)
    function mouse_parallax

################################################################################
## IMAGE DEFINITIONS
################################################################################

# === Character Sprites ===

# -- Edward --
# NOTE: "neutral" sprites are 630x1394 (character fills the canvas), while every
# other expression is 1024x1024 (character occupies a central ~980px strip).
# Without compensation, neutral renders ~35% taller — that's the visible "jump"
# when changing emotions. We lower the neutral zoom so the on-screen character
# height matches the square expressions, and add yoffset so the feet line up.
image edward neutral:
    "sprites/edward neutral.png"
    zoom 0.76
    yoffset 9
image edward thoughtful:
    "sprites/edward thoughtful.png"
    zoom 1.02
image edward concerned:
    "sprites/edward concerned.png"
    zoom 1.02
image edward shocked:
    "sprites/edward shocked.png"
    zoom 1.02
image edward tense:
    "sprites/edward tense.png"
    zoom 1.02
image edward determined:
    "sprites/edward determined.png"
    zoom 1.02
image edward defiant:
    "sprites/edward defiant.png"
    zoom 1.02
image edward sad:
    "sprites/edward sad.png"
    zoom 1.02
image edward tired:
    "sprites/edward tired.png"
    zoom 1.02
image edward relieved:
    "sprites/edward relieved.png"
    zoom 1.02

# -- Supervisor --
image supervisor neutral:
    "sprites/supervisor neutral.png"
    zoom 0.75
    yoffset 21
image supervisor stern:
    "sprites/supervisor stern.png"
    zoom 1.0
image supervisor authoritative:
    "sprites/supervisor authoritative.png"
    zoom 1.0
image supervisor suspicious:
    "sprites/supervisor suspicious.png"
    zoom 1.0
image supervisor annoyed:
    "sprites/supervisor annoyed.png"
    zoom 1.0
image supervisor cold:
    "sprites/supervisor cold.png"
    zoom 1.0

# -- Colleague --
image colleague neutral:
    "sprites/colleague neutral.png"
    zoom 0.74
    yoffset 19
image colleague casual:
    "sprites/colleague casual.png"
    zoom 0.98
image colleague amused:
    "sprites/colleague amused.png"
    zoom 0.98
image colleague smug:
    "sprites/colleague smug.png"
    zoom 0.98
image colleague uneasy:
    "sprites/colleague uneasy.png"
    zoom 0.98
image colleague cautious:
    "sprites/colleague cautious.png"
    zoom 0.98

# -- Greenwald --
image greenwald neutral:
    "sprites/greenwald neutral.png"
    zoom 1.02
image greenwald skeptical:
    "sprites/greenwald skeptical.png"
    zoom 1.02
image greenwald confused:
    "sprites/greenwald confused.png"
    zoom 1.02
image greenwald curious:
    "sprites/greenwald curious.png"
    zoom 1.02
image greenwald shocked:
    "sprites/greenwald shocked.png"
    zoom 1.02
image greenwald serious:
    "sprites/greenwald serious.png"
    zoom 1.02
image greenwald resolved:
    "sprites/greenwald resolved.png"
    zoom 1.02
image greenwald concerned:
    "sprites/greenwald concerned.png"
    zoom 1.02

# -- Poitras --
image poitras neutral:
    "sprites/poitras neutral.png"
    zoom 1.02
image poitras focused:
    "sprites/poitras focused.png"
    zoom 1.02
image poitras cautious:
    "sprites/poitras cautious.png"
    zoom 1.02
image poitras serious:
    "sprites/poitras serious.png"
    zoom 1.02
image poitras concerned:
    "sprites/poitras concerned.png"
    zoom 1.02
image poitras resolved:
    "sprites/poitras resolved.png"
    zoom 1.02

# -- Russian Official --
image russian_official neutral:
    "sprites/russian official neutral.png"
    zoom 0.76
    yoffset 34
image russian_official smug:
    "sprites/russian official smug.png"
    zoom 1.0
image russian_official calculating:
    "sprites/russian official calculating.png"
    zoom 1.0
image russian_official cold:
    "sprites/russian official cold.png"
    zoom 1.0
image russian_official pressuring:
    "sprites/russian official pressuring.png"
    zoom 1.0
image russian_official confident:
    "sprites/russian official confident.png"
    zoom 1.0

# -- NSA Chief --
image nsa_chief neutral:
    "sprites/nsa chief neutral.png"
    zoom 1.0
image nsa_chief authoritative:
    "sprites/nsa chief authoritative.png"
    zoom 1.0
image nsa_chief angry:
    "sprites/nsa chief angry.png"
    zoom 1.0
image nsa_chief cold:
    "sprites/nsa chief cold.png"
    zoom 1.0

# -- Journalist --
image journalist neutral:
    "sprites/journalist neutral.png"
    zoom 0.77
    yoffset 20
image journalist skeptical:
    "sprites/journalist skeptical.png"
    zoom 1.02
image journalist focused:
    "sprites/journalist focused.png"
    zoom 1.02
image journalist serious:
    "sprites/journalist serious.png"
    zoom 1.02
image journalist shocked:
    "sprites/journalist shocked.png"
    zoom 1.02
image journalist resolved:
    "sprites/journalist resolved.png"
    zoom 1.02
image journalist concerned:
    "sprites/journalist concerned.png"
    zoom 1.02

# -- Editor --
# Editor only ships with the tall format, so we just normalize its size to
# match the rest of the cast — there's no other expression to "jump" to.
image editor neutral:
    "sprites/editor neutral.png"
    zoom 0.76

# === Logo Watermark ===
image logo_watermark:
    "images/logo.png"
    xalign 0.5
    yalign 0.5
    zoom 1.15
    alpha 0.15

# === Backgrounds ===
image bg_1:
    "backgrounds/chapter_1/bg_1.png"
    xysize (1920, 1080)

image bg_nsa_main:
    "backgrounds/chapter_1/bg_nsa_main.png"
    xysize (1920, 1080)

image bg_nsa_terminal = Movie(play="images/backgrounds/chapter_1/bg_nsa_terminal.webm", loop=True)

image bg_nsa_servers:
    "backgrounds/chapter_2/bg_nsa_servers.png"
    xysize (1920, 1080)

image bg_nsa_exterior = Movie(play="images/backgrounds/chapter_1/bg_nsa_exterior.webm", loop=True)
image bg_nsa_checkpoint = Movie(play="images/backgrounds/chapter_1/bg_nsa_checkpoint.webm", loop=True)

image bg_prism:
    "backgrounds/chapter_2/bg_prism.png"
    xysize (1920, 1080)

image bg_prism1:
    "backgrounds/chapter_2/bg_prism1.png"
    xysize (1920, 1080)

image bg_hong_kong:
    "backgrounds/chapter_3/bg_hong_kong.png"
    xysize (1920, 1080)

image bg_hong_kong_street:
    "backgrounds/chapter_3/bg_hong_kong_street.png"
    xysize (1920, 1080)

image bg_hong_kong_terminal:
    "backgrounds/chapter_3/bg_hong_kong_terminal.png"
    xysize (1920, 1080)

image bg_hk_airport:
    "backgrounds/chapter_4/bg_hk_airport.png"
    xysize (1920, 1080)

image bg_hong_kong_hotel:
    "backgrounds/chapter_4/bg_hong_kong_hotel.png"
    xysize (1920, 1080)

image bg_leak:
    "backgrounds/chapter_4/bg_leak.png"
    xysize (1920, 1080)

image bg_moscow_apartment:
    "backgrounds/chapter_5/bg_moscow_apartment.png"
    xysize (1920, 1080)

image bg_moscow_winter_epilogue:
    "backgrounds/chapter_5/bg_moscow_winter_epilogue.png"
    xysize (1920, 1080)

image bg_sheremetyevo:
    "backgrounds/chapter_5/bg_sheremetyevo.png"
    xysize (1920, 1080)


################################################################################
## ATL TRANSFORMS — Character Animations
################################################################################

# === ACTIVE / INACTIVE STATES ===
# PURE state transforms: only saturation, alpha, and a tiny zoom delta for the
# speaker pop. They do NOT touch position (no xanchor/yanchor/xpos/ypos), so
# they can be safely chained ON TOP of an entry/stage transform via at_list
# without overwriting the character's position. The speaker_dimmer callback
# reads the live at_list and applies [position, state] each time the speaker
# changes.

transform active_char:
    ease 0.3 matrixcolor SaturationMatrix(1.0) alpha 1.0 zoom 1.02

transform inactive_char:
    ease 0.3 matrixcolor SaturationMatrix(0.35) alpha 0.8 zoom 0.97

# === ENTRANCE TRANSFORMS ===

# Slide in from left
transform enter_left:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos -0.20 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.6 xpos 0.15 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.15 ypos 1.50 alpha 1.0 zoom 1.40

# Slide in from right
transform enter_right:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos 1.40 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.6 xpos 0.85 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.85 ypos 1.50 alpha 1.0 zoom 1.40

# Fade in from center
transform enter_center:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos 0.3 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.5 xpos 0.5 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.5 ypos 1.50 alpha 1.0 zoom 1.40

transform stage_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5
    ypos 1.15


# === IDLE TRANSFORMS ===

# Subtle breathing idle animation
transform idle_breathe:
    zoom 1.0
    linear 2.0 zoom 1.01
    linear 2.0 zoom 1.0
    repeat

# === EXIT TRANSFORMS ===

# Slide out to left
transform exit_left:
    ease 0.5 xpos -0.4 alpha 0.0

# Slide out to right
transform exit_right:
    ease 0.5 xpos 1.4 alpha 0.0

# Fade out
transform exit_fade:
    ease 0.4 alpha 0.0

# Nervous/tense exit (for high suspicion moments)
transform exit_panic:
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 xoffset 3
    linear 0.1 xoffset 0
    ease 0.3 xpos 1.4 alpha 0.0

# === MENU / UI TRANSFORMS ===

# Title glitch effect
transform title_glitch:
    alpha 1.0
    pause 3.0
    alpha 0.85
    pause 0.05
    alpha 1.0
    pause 0.1
    alpha 0.9
    pause 0.05
    alpha 1.0
    repeat

# Button hover glow
transform btn_glow:
    linear 0.2 zoom 1.02
    linear 0.2 zoom 1.0
    repeat

# Scanline effect for UI
transform scanline_move:
    ypos 0.0
    linear 4.0 ypos 1.0
    ypos 0.0
    repeat

# Fade in for chapter cards
transform chapter_fade_in:
    alpha 0.0
    linear 1.0 alpha 1.0

# Fade out for chapter cards
transform chapter_fade_out:
    alpha 1.0
    linear 1.0 alpha 0.0

# Typing cursor blink
transform cursor_blink:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat


################################################################################
## SCENE TRANSITIONS
################################################################################

# Between dialogue segments
define fade_quick = Fade(0.3, 0.0, 0.3)

# Between chapters (more dramatic)
define chapter_transition = Fade(1.0, 0.5, 1.0, color="#000000")

# Glitch-style cut
define glitch_cut = Fade(0.1, 0.05, 0.1, color="#00FFD1")


################################################################################
## PERSISTENT STORY-TREE INITIALISATION
## (ensures all tree vars exist before the screen tries to read them)
################################################################################

init python:
    _tree_choice_map = {
        'choice_ch1_1': ("protocol", "explore"),
        'choice_ch1_2': ("report", "silent"),
        'choice_ch2_1': ("trust", "alone"),
        'choice_ch2_2': ("copy", "notes"),
        'choice_ch3_0': ("bluff", "accelerate"),
        'choice_ch3_1': ("pgp", "email", "wait"),
        'choice_ch3_2': ("full", "partial", "vague"),
        'choice_ch4_1': ("hotel", "mobile"),
        'choice_ch4_2': ("airport", "russia", "ecuador", "embassy", "stay"),
        'choice_ch5_1': ("encourage", "caution", "refuse"),
    }
    _tree_endings = ("hero", "fugitive", "imprisoned", "silenced", "betrayed")

    _tree_defaults = {
        'choice_ch1_1': '', 'choice_ch1_2': '',
        'choice_ch2_1': '', 'choice_ch2_2': '',
        'choice_ch3_0': '', 'choice_ch3_1': '', 'choice_ch3_2': '',
        'choice_ch4_1': '', 'choice_ch4_2': '',
        'choice_ch5_1': '',
        'tree_ch_reached': 0,
        'tree_ending': '',
        'tree_ending_unlocked': [],
    }

    for _choice_var in _tree_choice_map:
        _tree_defaults[_choice_var + "_unlocked"] = []

    for _tk, _tv in _tree_defaults.items():
        if getattr(persistent, _tk, None) is None:
            setattr(persistent, _tk, _tv)

    for _choice_var in _tree_choice_map:
        _current_value = getattr(persistent, _choice_var, "")
        _unlocked_name = _choice_var + "_unlocked"
        _unlocked_values = list(getattr(persistent, _unlocked_name, []) or [])
        if _current_value and _current_value not in _unlocked_values:
            _unlocked_values.append(_current_value)
            setattr(persistent, _unlocked_name, _unlocked_values)

    _ending_value = getattr(persistent, "tree_ending", "")
    _ending_unlocked = list(getattr(persistent, "tree_ending_unlocked", []) or [])
    if _ending_value and _ending_value not in _ending_unlocked:
        _ending_unlocked.append(_ending_value)
        setattr(persistent, "tree_ending_unlocked", _ending_unlocked)

    def tree_record_choice(choice_var, value):
        setattr(persistent, choice_var, value)
        unlocked_name = choice_var + "_unlocked"
        unlocked_values = list(getattr(persistent, unlocked_name, []) or [])
        if value not in unlocked_values:
            unlocked_values.append(value)
            setattr(persistent, unlocked_name, unlocked_values)
        renpy.save_persistent()

    def tree_reset_current_run():
        for _name in _tree_choice_map:
            setattr(persistent, _name, "")
        setattr(persistent, "tree_ch_reached", 0)
        setattr(persistent, "tree_ending", "")
        renpy.save_persistent()

    def tree_choice_is_unlocked(choice_var, value):
        return value in list(getattr(persistent, choice_var + "_unlocked", []) or [])

    def tree_unlocked_choice_count():
        total = 0
        for _name in _tree_choice_map:
            total += len(list(getattr(persistent, _name + "_unlocked", []) or []))
        return total

    def tree_total_choice_count():
        return sum(len(_values) for _values in _tree_choice_map.values())

    def tree_record_ending(value):
        setattr(persistent, "tree_ending", value)
        unlocked_endings = list(getattr(persistent, "tree_ending_unlocked", []) or [])
        if value not in unlocked_endings:
            unlocked_endings.append(value)
            setattr(persistent, "tree_ending_unlocked", unlocked_endings)
        renpy.save_persistent()

    def tree_ending_is_unlocked(value):
        return value in list(getattr(persistent, "tree_ending_unlocked", []) or [])

    del _tree_defaults, _tk, _tv, _choice_var, _current_value, _unlocked_name, _unlocked_values, _ending_value, _ending_unlocked
