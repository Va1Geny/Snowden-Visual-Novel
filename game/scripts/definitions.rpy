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
## IMAGE DEFINITIONS
################################################################################

# === Character Sprites ===
image edward neutral:
    "sprites/edward neutral.png"
    zoom 0.7

image supervisor neutral:
    "sprites/supervisor neutral.png"
    zoom 0.7

image colleague neutral:
    "sprites/colleague neutral.png"
    zoom 0.7

image journalist neutral:
    "sprites/journalist neutral.png"
    zoom 0.7

image editor neutral:
    "sprites/editor neutral.png"
    zoom 0.7

image russian_official neutral:
    "sprites/russian official neutral.png"
    zoom 0.7

# === Backgrounds ===
image bg_nsa:
    "backgrounds/Working inside the NSA's surveillance apparatus.png"
    xysize (1920, 1080)

image bg_prism:
    "backgrounds/Discovering the PRISM mass surveillance program.png"
    xysize (1920, 1080)

image bg_hong_kong:
    "backgrounds/The escape to Hong Kong and contact with journalists.png"
    xysize (1920, 1080)

image bg_leak:
    "backgrounds/The Leak and Global Fallout.png"
    xysize (1920, 1080)

image bg_russia:
    "backgrounds/Asylum in Russia — and life as a fugitive.png"
    xysize (1920, 1080)


################################################################################
## ATL TRANSFORMS — Character Animations
################################################################################

# === ENTRANCE TRANSFORMS ===

# Slide in from left
transform enter_left:
    xpos -0.3 alpha 0.0
    ease 0.6 xpos 0.15 alpha 1.0

# Slide in from right
transform enter_right:
    xpos 1.3 alpha 0.0
    ease 0.6 xpos 0.75 alpha 1.0

# Fade in from center
transform enter_center:
    xpos 0.4 alpha 0.0 zoom 0.9
    ease 0.5 xpos 0.4 alpha 1.0 zoom 1.0

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
