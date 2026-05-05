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

# === Decrypt Minigame Styles ===
style cipher_tile is button:
    xsize 84
    ysize 84
    background Solid("#161E2A")
    hover_background Solid("#2B2312")
    insensitive_background Solid("#161E2A")
    top_padding 6
    bottom_padding 6
    left_padding 6
    right_padding 6

style cipher_tile_text is button_text:
    font "DejaVuSans.ttf"
    size 38
    bold True
    color "#FFD700"
    hover_color "#FFD700"
    xalign 0.5
    text_align 0.5

style decoded_tile is button:
    xsize 84
    ysize 76
    background Solid("#0F1520")
    hover_background Solid("#152131")
    insensitive_background Solid("#0F1520")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_text is button_text:
    font "DejaVuSans.ttf"
    size 34
    bold True
    color "#E8E8E8"
    hover_color "#E8E8E8"
    xalign 0.5
    text_align 0.5

style decoded_tile_correct is button:
    xsize 84
    ysize 76
    background Solid("#12331A")
    hover_background Solid("#174321")
    insensitive_background Solid("#12331A")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_correct_text is button_text:
    font "DejaVuSans.ttf"
    size 34
    bold True
    color "#39FF14"
    hover_color "#39FF14"
    xalign 0.5
    text_align 0.5

style decoded_tile_active is button:
    xsize 84
    ysize 76
    background Solid("#132330")
    hover_background Solid("#183043")
    insensitive_background Solid("#132330")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_active_text is button_text:
    font "DejaVuSans.ttf"
    size 34
    bold True
    color "#00FFD1"
    hover_color "#00FFD1"
    xalign 0.5
    text_align 0.5

style alphabet_cell is button:
    xsize 50
    ysize 42
    background Solid("#111820")
    hover_background Solid("#18212B")
    insensitive_background Solid("#111820")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style alphabet_cell_text is button_text:
    font "DejaVuSans.ttf"
    size 22
    bold True
    color "#A4B8C5"
    hover_color "#E8E8E8"
    xalign 0.5
    text_align 0.5

style alphabet_cell_highlighted_cipher is button:
    xsize 50
    ysize 42
    background Solid("#3A2912")
    hover_background Solid("#4D3418")
    insensitive_background Solid("#3A2912")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style alphabet_cell_highlighted_cipher_text is button_text:
    font "DejaVuSans.ttf"
    size 22
    bold True
    color "#FFD700"
    hover_color "#FFD700"
    xalign 0.5
    text_align 0.5

style alphabet_cell_highlighted_plain is frame:
    xsize 50
    ysize 42
    background Solid("#003E38")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style keyboard_key is button:
    xsize 84
    ysize 48
    background Solid("#161E2A")
    hover_background Solid("#0D3440")
    insensitive_background Solid("#10161E")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style keyboard_key_text is button_text:
    font "DejaVuSans.ttf"
    size 22
    bold True
    color "#E8E8E8"
    hover_color "#00FFD1"
    xalign 0.5
    text_align 0.5

style keyboard_key_hover is keyboard_key:
    background Solid("#0D3440")
    hover_background Solid("#125568")

style decrypt_terminal is frame:
    background Solid("#0C1018EE")
    top_padding 22
    bottom_padding 18
    left_padding 22
    right_padding 22

style stage_badge is frame:
    background Solid("#111820")
    top_padding 8
    bottom_padding 8
    left_padding 14
    right_padding 14

# === Clean the Message Minigame Styles ===

style ctm_field_label:
    font "DejaVuSans.ttf"
    color "#5A7080"
    size 15
    bold True

style ctm_field_value:
    font "DejaVuSans.ttf"
    color "#B8C8D8"
    size 16

style ctm_threat is button:
    background Solid("#1A1018")
    hover_background Solid("#2A1420")
    padding (8, 4)

style ctm_threat_text is button_text:
    font "DejaVuSans.ttf"
    size 16
    color "#FF3355"
    hover_color "#FF6680"

style ctm_cleaned_text:
    font "DejaVuSans.ttf"
    size 16
    color "#00FF88"

style ctm_body_text:
    font "DejaVuSans.ttf"
    size 16
    color "#B8C8D8"
    line_spacing 4

style ctm_scanner_label:
    font "DejaVuSans.ttf"
    color "#5A7080"
    size 14
    bold True

style ctm_scanner_value:
    font "DejaVuSans.ttf"
    color "#D8E4F0"
    size 14

# === Cover Your Tracks — Minigame 4 Terminal Styles ===

style ct_panel_title:
    color "#00FFD1"
    font "DejaVuSans.ttf"
    size 14
    bold True

style ct_text:
    color "#E8E8E8"
    font "DejaVuSans.ttf"
    size 15

style ct_text_dim:
    color "#7A8A99"
    font "DejaVuSans.ttf"
    size 13

style ct_danger:
    color "#FF2D55"
    font "DejaVuSans.ttf"
    size 15
    bold True

style ct_success:
    color "#00FF88"
    font "DejaVuSans.ttf"
    size 15
    bold True

style ct_cmd:
    color "#A8FF78"
    font "DejaVuSans.ttf"
    size 16

style ct_prompt:
    color "#00FFD1"
    font "DejaVuSans.ttf"
    size 16
    bold True

style ct_execute_btn is button:
    background Solid("#003A2A")
    hover_background Solid("#005A40")
    padding (30, 14)
    xalign 0.5

style ct_execute_btn_text is button_text:
    color "#00FFD1"
    font "DejaVuSans.ttf"
    size 18
    bold True

style ct_hint_btn is button:
    background Solid("#2A2000")
    hover_background Solid("#3A3000")
    padding (15, 8)

style ct_hint_btn_text is button_text:
    color "#FFD700"
    font "DejaVuSans.ttf"
    size 14

style ct_token_btn is button:
    background Solid("#1A2A2A")
    hover_background Solid("#2A3A3A")
    padding (10, 6)

style ct_token_btn_text is button_text:
    color "#A8FF78"
    font "DejaVuSans.ttf"
    size 15

style ct_breakdown_key:
    color "#00FFD1"
    font "DejaVuSans.ttf"
    size 14
    bold True

style ct_breakdown_val:
    color "#7A8A99"
    font "DejaVuSans.ttf"
    size 14

style ct_learn_title:
    color "#FFD700"
    font "DejaVuSans.ttf"
    size 14
    bold True

style ct_learn_body:
    color "#CCCCCC"
    font "DejaVuSans.ttf"
    size 16
    line_leading 5
