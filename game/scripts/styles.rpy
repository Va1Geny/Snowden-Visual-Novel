################################################################################
## STYLES.RPY — Custom Styles for Classified: The Snowden Files
################################################################################

init offset = -1

################################################################################
## CUSTOM STYLES
################################################################################

# === Chapter Title Card Styles ===
style sys_text:
    font "DejaVuSans.ttf"
    color "#00FF00"
    size 28
    bold True
    text_align 0.5
    xalign 0.5

style chapter_title_text:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 64
    bold True
    text_align 0.5
    xalign 0.5

style chapter_subtitle_text:
    font "DejaVuSans.ttf"
    color "#888888"
    size 24
    text_align 0.5
    xalign 0.5
    italic True

# === HUD Styles ===
style hud_text:
    font "DejaVuSans.ttf"
    size 14
    color "#888888"

style hud_score_text:
    font "DejaVuSans.ttf"
    size 14
    color "#00FFD1"

style hud_suspicion_text:
    font "DejaVuSans.ttf"
    size 14
    color "#FF2D55"

# === Minigame Styles ===
style minigame_title:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style minigame_instruction:
    font "DejaVuSans.ttf"
    color "#E8E8E8"
    size 22
    text_align 0.5
    xalign 0.5

style minigame_label:
    font "DejaVuSans.ttf"
    color "#AAAAAA"
    size 18
    text_align 0.0

style minigame_score:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 24
    bold True
    text_align 0.5
    xalign 0.5

# === Question Screen Styles ===
style question_text:
    font "DejaVuSans.ttf"
    color "#E8E8E8"
    size 26
    text_align 0.5
    xalign 0.5

style answer_button:
    xsize 800
    yminimum 60
    xalign 0.5

style answer_button_text:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    hover_color "#0A0E1A"
    size 22
    text_align 0.0
    xalign 0.0

# === Ending Styles ===
style ending_title:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 48
    bold True
    text_align 0.5
    xalign 0.5

style ending_text:
    font "DejaVuSans.ttf"
    color "#E8E8E8"
    size 22
    text_align 0.5
    xalign 0.5

style ending_score_label:
    font "DejaVuSans.ttf"
    color "#888888"
    size 20
    text_align 0.0

style ending_score_value:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 20
    bold True
    text_align 1.0

style ending_lesson_text:
    font "DejaVuSans.ttf"
    color "#AAAAAA"
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
    color "#E8E8E8"
    size 22
    text_align 0.5
    xalign 0.5

style briefing_warning:
    font "DejaVuSans.ttf"
    color "#FFD700"
    size 20
    italic True
    text_align 0.5
    xalign 0.5

# === Main Menu Custom Styles ===
style menu_title_text:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 52
    bold True
    text_align 0.5
    xalign 0.5

style menu_subtitle_text:
    font "DejaVuSans.ttf"
    color "#888888"
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
    color "#00FFD1"
    hover_color "#0A0E1A"
    size 22
    bold True
    text_align 0.5
    xalign 0.5

style menu_version:
    font "DejaVuSans.ttf"
    color "#444444"
    size 14
    text_align 0.5
    xalign 0.5

# === Dossier / Glossary Styles ===
style dossier_title:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style dossier_term:
    font "DejaVuSans.ttf"
    color "#FFD700"
    size 22
    bold True

style dossier_definition:
    font "DejaVuSans.ttf"
    color "#CCCCCC"
    size 18

# === Chapter Summary Styles ===
style summary_title:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 36
    bold True
    text_align 0.5
    xalign 0.5

style summary_stat_label:
    font "DejaVuSans.ttf"
    color "#888888"
    size 20

style summary_stat_value:
    font "DejaVuSans.ttf"
    color "#00FFD1"
    size 20
    bold True
