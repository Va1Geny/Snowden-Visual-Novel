################################################################################
## DEFINITIONS.RPY — Character Definitions, Flags, Images, Transforms
## Classified: The Snowden Files
################################################################################

init offset = -1

################################################################################
## CHARACTER DEFINITIONS
################################################################################

# === PROTAGONIST ===
define e = Character("EDWARD SNOWDEN",
    color="#00FFD1",
    what_color="#E8E8E8",
    who_size=22,
    what_size=20,
    who_bold=True)

# === JOURNALISTS ===
define greenwald = Character("GLENN GREENWALD",
    color="#FFD700",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define poitras = Character("LAURA POITRAS",
    color="#FF69B4",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ANTAGONISTS / AUTHORITY ===
define nsa_chief = Character("NSA DIRECTOR",
    color="#FF2D55",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define supervisor = Character("SUPERVISOR",
    color="#FF6B35",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ALLIES / NEUTRAL ===
define colleague = Character("COLLEAGUE [[CLASSIFIED]]",
    color="#888888",
    what_color="#CCCCCC",
    who_bold=False,
    who_size=22,
    what_size=20)

define russian_official = Character("RUSSIAN OFFICIAL",
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

# === Minigame State ===
default mg_firewall_score = 0
default mg_decrypt_solved = False
default mg_opsec_score = 0
default mg_trace_solved = False

# === Question Tracking ===
default text_input_attempts = 0


################################################################################
## PARALLAX SYSTEM
################################################################################

init python:
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
image edward neutral:
    "sprites/edward neutral.png"
    zoom 1.02

image supervisor neutral:
    "sprites/supervisor neutral.png"
    zoom 1.0

image colleague neutral:
    "sprites/colleague neutral.png"
    zoom 0.98

image journalist neutral:
    "sprites/journalist neutral.png"
    zoom 1.02

image editor neutral:
    "sprites/editor neutral.png"
    zoom 1.0

image russian_official neutral:
    "sprites/russian official neutral.png"
    zoom 1.0
# === Backgrounds ===
image bg_1:
    "backgrounds/chapter_1/bg_1.png"
    xysize (1920, 1080)

image bg_nsa_main:
    "backgrounds/chapter_1/bg_nsa_main.png"
    xysize (1920, 1080)

image bg_nsa_terminal:
    "backgrounds/chapter_1/bg_nsa_terminal.png"
    xysize (1920, 1080)

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

# === ENTRANCE TRANSFORMS ===

# Slide in from left
transform enter_left:
    xanchor 0.5
    yanchor 1.0
    xpos -0.20 ypos 1.50 alpha 0.0 zoom 1.0
    ease 0.6 xpos 0.20 ypos 1.60 alpha 1.0 zoom 1.18

# Slide in from right
transform enter_right:
    xanchor 0.5
    yanchor 1.0
    xpos 1.20 ypos 1.50 alpha 0.0 zoom 1.0
    ease 0.6 xpos 0.80 ypos 1.60 alpha 1.0 zoom 1.18

# Fade in from center
transform enter_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5 ypos 1.50 alpha 0.0 zoom 1.0
    ease 0.5 xpos 0.5 ypos 1.60 alpha 1.0 zoom 1.18

transform stage_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5
    ypos 1.50

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
