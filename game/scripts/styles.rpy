################################################################################
## STYLES.RPY — Custom Styles for Classified: The Snowden Files
## Palette:
##   #002922  Evergreen      — deep panel backgrounds
##   #006654  Emerald Depths — secondary accent / hover
##   #008069  Jungle Teal    — primary accent (active, selected)
##   #8B8FCC  Soft Periwinkle — info / knowledge elements
##   #4D5186  Dusty Grape    — borders, inactive, mid-tone
##   #212339  Space Indigo   — main background
################################################################################

init offset = -1

################################################################################
## CUSTOM STYLES
################################################################################

# === Chapter Title Card Styles ===
style sys_text:
    font "DejaVuSans.ttf"
    color "#008069"
    size 28
    bold True
    text_align 0.5
    xalign 0.5

style chapter_title_text:
    font "DejaVuSans.ttf"
    color "#EDFAF5"
    size 64
    bold True
    text_align 0.5
    xalign 0.5

style chapter_subtitle_text:
    font "DejaVuSans.ttf"
    color "#4D5186"
    size 24
    text_align 0.5
    xalign 0.5
    italic True

# === HUD Styles ===
style hud_text:
    font "DejaVuSans.ttf"
    size 13
    color "#4D5186"

style hud_score_text:
    font "DejaVuSans.ttf"
    size 13
    color "#008069"

style hud_suspicion_text:
    font "DejaVuSans.ttf"
    size 13
    color "#FF2D55"

# === Minigame Styles ===
style minigame_title:
    font "DejaVuSans.ttf"
    color "#008069"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style minigame_instruction:
    font "DejaVuSans.ttf"
    color "#C8D8D0"
    size 22
    text_align 0.5
    xalign 0.5

style minigame_label:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 18
    text_align 0.0

style minigame_score:
    font "DejaVuSans.ttf"
    color "#008069"
    size 24
    bold True
    text_align 0.5
    xalign 0.5

# === Question Screen Styles ===
style question_text:
    font "DejaVuSans.ttf"
    color "#C8D8D0"
    size 26
    text_align 0.5
    xalign 0.5

style answer_button:
    xsize 800
    yminimum 60
    xalign 0.5

style answer_button_text:
    font "DejaVuSans.ttf"
    color "#008069"
    hover_color "#212339"
    size 22
    text_align 0.0
    xalign 0.0

# === Ending Styles ===
style ending_title:
    font "DejaVuSans.ttf"
    color "#008069"
    size 48
    bold True
    text_align 0.5
    xalign 0.5

style ending_text:
    font "DejaVuSans.ttf"
    color "#C8D8D0"
    size 22
    text_align 0.5
    xalign 0.5

style ending_score_label:
    font "DejaVuSans.ttf"
    color "#4D5186"
    size 20
    text_align 0.0

style ending_score_value:
    font "DejaVuSans.ttf"
    color "#008069"
    size 20
    bold True
    text_align 1.0

style ending_lesson_text:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 18
    text_align 0.0

# === Briefing Screen Styles ===
style briefing_header:
    font "DejaVuSans.ttf"
    color "#FF2D55"
    size 32
    bold True
    text_align 0.5
    xalign 0.5

style briefing_body:
    font "DejaVuSans.ttf"
    color "#C8D8D0"
    size 22
    text_align 0.5
    xalign 0.5

style briefing_warning:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 20
    italic True
    text_align 0.5
    xalign 0.5

# === Main Menu Custom Styles ===
style menu_title_text:
    font "DejaVuSans.ttf"
    color "#008069"
    size 52
    bold True
    text_align 0.5
    xalign 0.5

style menu_subtitle_text:
    font "DejaVuSans.ttf"
    color "#4D5186"
    size 20
    italic True
    text_align 0.5
    xalign 0.5

style menu_btn:
    xsize 400
    ysize 55
    xalign 0.5

style menu_btn_text:
    font "DejaVuSans.ttf"
    color "#008069"
    hover_color "#212339"
    size 22
    bold True
    text_align 0.5
    xalign 0.5

style menu_version:
    font "DejaVuSans.ttf"
    color "#4D518660"
    size 14
    text_align 0.5
    xalign 0.5

# === Dossier / Glossary Styles ===
style dossier_title:
    font "DejaVuSans.ttf"
    color "#008069"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style dossier_term:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 22
    bold True

style dossier_definition:
    font "DejaVuSans.ttf"
    color "#A8B8C0"
    size 18

# === Chapter Summary Styles ===
style summary_title:
    font "DejaVuSans.ttf"
    color "#008069"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style summary_stat_label:
    font "DejaVuSans.ttf"
    color "#4D5186"
    size 20

style summary_stat_value:
    font "DejaVuSans.ttf"
    color "#008069"
    size 20
    bold True

# === Pause Hub / Story Tree HUD Styles ===
style pause_title_text:
    font "DejaVuSans.ttf"
    color "#EAF4F1"
    size 58
    bold True
    text_align 0.0

style pause_caption_text:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 18
    text_align 0.0

style pause_btn:
    xsize 430
    ysize 72
    xalign 0.0

style pause_btn_text:
    font "DejaVuSans.ttf"
    color "#EAF4F1"
    hover_color "#F2FFFC"
    size 24
    bold True
    text_align 0.0

style tree_hud_kicker:
    font "DejaVuSans.ttf"
    color "#8B8FCC"
    size 15
    bold True

style tree_hud_value:
    font "DejaVuSans.ttf"
    color "#EAF4F1"
    size 24
    bold True

style tree_hud_meta:
    font "DejaVuSans.ttf"
    color "#AAB0D6"
    size 15
