init offset = -1

init python:
    FONT_MONO = "fonts/ShareTechMono-Regular.ttf"
    FONT_BODY = "fonts/Rajdhani-Regular.ttf"
    FONT_BODY_BOLD = "fonts/Rajdhani-SemiBold.ttf"

    BG_DEEP = "#080C10"
    BG_PANEL = "#0D1117"
    BG_PANEL_ALT = "#111720"
    BG_OVERLAY = "#0D1117ee"

    CYAN = "#00FFD1"
    RED = "#FF2D55"
    GOLD = "#FFD700"
    GREEN = "#00FF88"
    ORANGE = "#FF8C00"

    TEXT_PRIMARY = "#E8E8E8"
    TEXT_DIM = "#7A8A99"
    TEXT_FAINT = "#3A4A55"
    TEXT_INVERSE = "#0D1117"

    DIVIDER_STRONG = "#00FFD122"
    DIVIDER_SUBTLE = "#ffffff11"
    BORDER_ACTIVE = "#00FFD1"

    SIZE_XS = 15
    SIZE_SM = 17
    SIZE_MD = 22
    SIZE_BASE = 20
    SIZE_LG = 25
    SIZE_XL = 32
    SIZE_2XL = 41

style sys_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 32
    bold True
    text_align 0.5
    xalign 0.5

style chapter_title_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#E8E8E8"
    size 74
    bold True
    text_align 0.5
    xalign 0.5

style chapter_subtitle_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 28
    text_align 0.5
    xalign 0.5
    italic True

style hud_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 15
    color "#7A8A99"

style hud_score_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 15
    color "#00FFD1"

style hud_suspicion_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 15
    color "#FF2D55"

style minigame_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 41
    bold True
    text_align 0.5
    xalign 0.5

style minigame_instruction:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 25
    text_align 0.5
    xalign 0.5

style minigame_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 21
    text_align 0.0

style minigame_score:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 28
    bold True
    text_align 0.5
    xalign 0.5

style question_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 30
    text_align 0.5
    xalign 0.5

style answer_button:
    xsize 800
    yminimum 60
    xalign 0.5

style answer_button_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#00FFD1"
    hover_color "#0D1117"
    size 25
    text_align 0.0
    xalign 0.0

style ending_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 55
    bold True
    text_align 0.5
    xalign 0.5

style ending_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 25
    text_align 0.5
    xalign 0.5

style ending_score_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 23
    text_align 0.0

style ending_score_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 23
    bold True
    text_align 1.0

style ending_lesson_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 21
    text_align 0.0

style briefing_header:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#FF2D55"
    size 37
    bold True
    text_align 0.5
    xalign 0.5

style briefing_body:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 25
    text_align 0.5
    xalign 0.5

style briefing_warning:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 23
    italic True
    text_align 0.5
    xalign 0.5

style menu_title_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 60
    bold True
    text_align 0.5
    xalign 0.5

style menu_subtitle_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 23
    italic True
    text_align 0.5
    xalign 0.5

style menu_btn:
    xsize 400
    ysize 55
    xalign 0.5

style menu_btn_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    hover_color "#0D1117"
    size 25
    bold True
    text_align 0.5
    xalign 0.5

style menu_version:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#3A4A5560"
    size 16
    text_align 0.5
    xalign 0.5

style dossier_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 41
    bold True
    text_align 0.5
    xalign 0.5

style dossier_term:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 25
    bold True

style dossier_definition:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 21

style summary_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 41
    bold True
    text_align 0.5
    xalign 0.5

style summary_stat_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 23

style summary_stat_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 23
    bold True

style pause_title_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 67
    bold True
    text_align 0.0

style pause_caption_text:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 21
    text_align 0.0

style pause_btn:
    xsize 430
    ysize 72
    xalign 0.0

style pause_btn_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    hover_color "#0D1117"
    size 28
    bold True
    text_align 0.0

style tree_hud_kicker:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 17
    bold True

style tree_hud_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 28
    bold True

style tree_hud_meta:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 17

style cipher_tile is button:
    xsize 84
    ysize 84
    background Solid("#111720")
    hover_background Solid("#2B2312")
    insensitive_background Solid("#111720")
    top_padding 6
    bottom_padding 6
    left_padding 6
    right_padding 6

style cipher_tile_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 44
    bold True
    color "#FFD700"
    hover_color "#FFD700"
    xalign 0.5
    text_align 0.5

style decoded_tile is button:
    xsize 84
    ysize 76
    background Solid("#0D1117")
    hover_background Solid("#111720")
    insensitive_background Solid("#0D1117")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 39
    bold True
    color "#E8E8E8"
    hover_color "#E8E8E8"
    xalign 0.5
    text_align 0.5

style decoded_tile_correct is button:
    xsize 84
    ysize 76
    background Solid("#0A2A12")
    hover_background Solid("#0E3A18")
    insensitive_background Solid("#0A2A12")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_correct_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 39
    bold True
    color "#00FF88"
    hover_color "#00FF88"
    xalign 0.5
    text_align 0.5

style decoded_tile_active is button:
    xsize 84
    ysize 76
    background Solid("#0A1A2A")
    hover_background Solid("#0D2A3A")
    insensitive_background Solid("#0A1A2A")
    top_padding 4
    bottom_padding 4
    left_padding 6
    right_padding 6

style decoded_tile_active_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 39
    bold True
    color "#00FFD1"
    hover_color "#00FFD1"
    xalign 0.5
    text_align 0.5

style alphabet_cell is button:
    xsize 50
    ysize 42
    background Solid("#0D1117")
    hover_background Solid("#111720")
    insensitive_background Solid("#0D1117")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style alphabet_cell_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 25
    bold True
    color "#7A8A99"
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
    font "fonts/ShareTechMono-Regular.ttf"
    size 25
    bold True
    color "#FFD700"
    hover_color "#FFD700"
    xalign 0.5
    text_align 0.5

style alphabet_cell_highlighted_plain is frame:
    xsize 50
    ysize 42
    background Solid("#003A3A")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style keyboard_key is button:
    xsize 84
    ysize 48
    background Solid("#111720")
    hover_background Solid("#003A3A")
    insensitive_background Solid("#0D1117")
    top_padding 0
    bottom_padding 0
    left_padding 0
    right_padding 0

style keyboard_key_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 25
    bold True
    color "#E8E8E8"
    hover_color "#00FFD1"
    xalign 0.5
    text_align 0.5

style keyboard_key_hover is keyboard_key:
    background Solid("#003A3A")
    hover_background Solid("#005050")

style decrypt_terminal is frame:
    background Solid("#080C10EE")
    top_padding 22
    bottom_padding 18
    left_padding 22
    right_padding 22

style stage_badge is frame:
    background Solid("#0D1117")
    top_padding 8
    bottom_padding 8
    left_padding 14
    right_padding 14

style ctm_field_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 17
    bold True

style ctm_field_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 18

style ctm_threat is button:
    background Solid("#1A0A10")
    hover_background Solid("#2A0A15")
    padding (8, 4)

style ctm_threat_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color "#FF2D55"
    hover_color "#FF6680"

style ctm_cleaned_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color "#00FF88"

style ctm_body_text:
    font "fonts/Rajdhani-Regular.ttf"
    size 18
    color "#E8E8E8"
    line_spacing 4

style ctm_scanner_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 16
    bold True

style ctm_scanner_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 16

style ct_panel_title:
    color "#00FFD1"
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    bold True

style ct_text:
    color "#E8E8E8"
    font "fonts/ShareTechMono-Regular.ttf"
    size 17

style choice_terminal_header:
    font "fonts/ShareTechMono-Regular.ttf"
    size 12
    bold True
    kerning 2

style choice_index_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 13
    bold True
    text_align 0.5
    xalign 0.5

style choice_caption_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 18
    bold True
    line_leading 2
    xmaximum 680
    xalign 0.0
    text_align 0.0

style choice_tag_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 10
    bold True
    kerning 1
    text_align 0.5
    xalign 0.5

style choice_key_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 10
    color "#7A8A99"
    text_align 0.5
    xalign 0.5

style choice_key_label_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 10
    color "#2A3A45"
    text_align 0.0
    xalign 0.0

style mcq_terminal_header:
    font "fonts/ShareTechMono-Regular.ttf"
    size 11
    color "#00FFD14D"
    kerning 2
    text_align 0.0

style mcq_prompt_arrow:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color "#00FFD1"
    bold True
    yoffset -1

style mcq_question_terminal:
    font "fonts/ShareTechMono-Regular.ttf"
    size 21
    color "#E8E8E8"
    line_leading 5
    text_align 0.0

style mcq_helper_terminal:
    font "fonts/Rajdhani-Regular.ttf"
    size 17
    color "#7A8A99"
    line_leading 4
    text_align 0.0

style mcq_option_num:
    font "fonts/ShareTechMono-Regular.ttf"
    size 15
    text_align 0.0
    min_width 34

style mcq_option_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 17
    text_align 0.0

style mcq_result_line:
    font "fonts/ShareTechMono-Regular.ttf"
    size 15
    bold True
    text_align 0.0

style mcq_result_text:
    font "fonts/Rajdhani-Regular.ttf"
    size 17
    color "#7A8A99"
    line_leading 5
    text_align 0.0

style mcq_terminal_continue is button:
    background Solid("#00000000")
    hover_background Solid("#00FFD114")
    insensitive_background Solid("#00000000")
    padding (20, 8)

style mcq_terminal_continue_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 13
    bold True
    color "#00FFD1"
    hover_color "#E8E8E8"
    insensitive_color "#2A3A45"
    kerning 2
    text_align 0.5
    xalign 0.5

style ct_text_dim:
    color "#7A8A99"
    font "fonts/ShareTechMono-Regular.ttf"
    size 15

style ct_danger:
    color "#FF2D55"
    font "fonts/ShareTechMono-Regular.ttf"
    size 17
    bold True

style ct_success:
    color "#00FF88"
    font "fonts/ShareTechMono-Regular.ttf"
    size 17
    bold True

style ct_cmd:
    color "#00FF88"
    font "fonts/ShareTechMono-Regular.ttf"
    size 18

style ct_prompt:
    color "#00FFD1"
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    bold True

style ct_execute_btn is button:
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    padding (30, 14)
    xalign 0.5

style ct_execute_btn_text is button_text:
    color "#00FFD1"
    hover_color "#0D1117"
    font "fonts/ShareTechMono-Regular.ttf"
    size 21
    bold True

style ct_hint_btn is button:
    background Solid("#2A2000")
    hover_background Solid("#3A3000")
    padding (15, 8)

style ct_hint_btn_text is button_text:
    color "#FFD700"
    font "fonts/ShareTechMono-Regular.ttf"
    size 16

style ct_token_btn is button:
    background Solid("#0A1A1A")
    hover_background Solid("#0D2A2A")
    padding (10, 6)

style ct_token_btn_text is button_text:
    color "#00FF88"
    font "fonts/ShareTechMono-Regular.ttf"
    size 17

style ct_breakdown_key:
    color "#00FFD1"
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    bold True

style ct_breakdown_val:
    color "#7A8A99"
    font "fonts/Rajdhani-Regular.ttf"
    size 16

style ct_learn_title:
    color "#FFD700"
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    bold True

style ct_learn_body:
    color "#E8E8E8"
    font "fonts/Rajdhani-Regular.ttf"
    size 18
    line_leading 5

style terminal_screen_bg:
    background "bg_kali_net"

style terminal_text:
    font FONT_MONO
    size 20
    color "#ffffff"
    line_leading 4

style terminal_input_text:
    font FONT_MONO
    size 20
    color "#ffffff"

style terminal_correct_line:
    font FONT_MONO
    size 20
    color "#00ff00"

style terminal_error_line:
    font FONT_MONO
    size 20
    color "#ff0000"

style terminal_learn_line:
    font FONT_MONO
    size 20
    color "#ffffff"

style classified_briefing_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 32
    bold True
    text_align 0.5
    xalign 0.5

style classified_briefing_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 17
    text_align 0.0

style classified_briefing_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 20
    text_align 0.0

style classified_briefing_value_accent:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 20
    bold True
    text_align 0.0

style classified_briefing_body:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 20
    text_align 0.5
    xalign 0.5
    line_leading 6

style classified_briefing_muted:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 17
    text_align 0.5
    xalign 0.5
    line_leading 6
    italic True

style classified_briefing_btn is button:
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    insensitive_background Solid("#003A3A")
    xsize 280
    ysize 48
    padding (30, 14)
    xalign 0.5

style classified_briefing_btn_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    hover_color "#0D1117"
    size 20
    bold True
    text_align 0.5
    xalign 0.5

style chapter_select_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 32
    bold True
    text_align 0.5
    xalign 0.5

style chapter_select_chapter_num:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 20
    bold True
    text_align 0.0

style chapter_select_chapter_num_locked:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#3A4A55"
    size 20
    bold True
    text_align 0.0

style chapter_select_codename:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    size 20
    text_align 0.0

style chapter_select_description:
    font "fonts/Rajdhani-Regular.ttf"
    color "#7A8A99"
    size 17
    text_align 0.0
    line_leading 4

style chapter_select_locked_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#FF2D55"
    size 17
    text_align 0.0

style chapter_select_btn is button:
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    insensitive_background Solid("#003A3A")
    xsize 280
    ysize 48
    padding (30, 14)
    xalign 0.5

style chapter_select_btn_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#00FFD1"
    hover_color "#0D1117"
    size 20
    bold True
    text_align 0.5
    xalign 0.5

style game_over_title:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#FF2D55"
    size 32
    bold True
    text_align 0.5
    xalign 0.5

style game_over_status:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#FF2D55"
    size 41
    bold True
    text_align 0.5
    xalign 0.5

style game_over_body:
    font "fonts/Rajdhani-Regular.ttf"
    color "#E8E8E8"
    size 20
    text_align 0.5
    xalign 0.5
    line_leading 6

style game_over_label:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#7A8A99"
    size 17
    text_align 0.0

style game_over_score_value:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#E8E8E8"
    size 20
    bold True
    text_align 0.0

style game_over_score_danger:
    font "fonts/ShareTechMono-Regular.ttf"
    color "#FF2D55"
    size 20
    bold True
    text_align 0.0

style game_over_btn_primary is button:
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    insensitive_background Solid("#003A3A")
    xsize 280
    ysize 48
    padding (30, 14)
    xalign 0.5

style game_over_btn_secondary is button:
    background Solid("#3A0010")
    hover_background Solid("#FF2D55")
    insensitive_background Solid("#3A0010")
    xsize 280
    ysize 48
    padding (30, 14)
    xalign 0.5

style game_over_btn_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 20
    bold True
    text_align 0.5
    xalign 0.5

style game_over_btn_primary_text is game_over_btn_text:
    color "#00FFD1"
    hover_color "#0D1117"

style game_over_btn_secondary_text is game_over_btn_text:
    color "#FF2D55"
    hover_color "#0D1117"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 6 — STYLES REFERENCE (preferences screen)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

style pref_header_row is frame:
    xfill True
    padding (32, 22)
    background Solid("#00FFD10f")

style pref_header_label is text:
    font FONT_MONO
    size 10
    color "#00FFD18c"
    kerning 2

style pref_header_chapter is text:
    font FONT_MONO
    size 10
    color "#ffffff2e"
    kerning 1

style pref_kbd_chip is frame:
    padding (7, 5)
    background Solid("#ffffff0a")

style pref_kbd_chip_text is text:
    font FONT_MONO
    size 10
    color TEXT_DIM

style pref_tab_bar is frame:
    xfill True
    background Null()
    padding (0, 0)

style pref_tab is button:
    padding (22, 14)
    background Null()
    
style pref_tab_active is button:
    padding (22, 14)
    background Solid("#00FFD10f")

style pref_tab_text is button_text:
    font FONT_MONO
    size 12
    color TEXT_DIM
    kerning 1.4

style pref_tab_text_active is button_text:
    font FONT_MONO
    size 12
    color CYAN
    kerning 1.4

style pref_body_layout is hbox:
    spacing 16
    padding (32, 28)

style pref_left_col is frame:
    xsize 740
    background Null()
    padding (0, 0)

style pref_side_col is frame:
    xsize 260
    background Solid("#00FFD108")
    padding (20, 22)

style pref_tab_content is vbox:
    spacing 10
    xfill True

style pref_label is text:
    font FONT_MONO
    size 10
    color "#00FFD166"
    kerning 1.8

style pref_section_heading is frame:
    background Null()
    padding (0, 0, 0, 10)
    top_margin 8

style pref_row_frame is frame:
    xfill True
    background Solid("#ffffff05")
    padding (18, 16)

style pref_row_button is button:
    xfill True
    background Solid("#ffffff05")
    hover_background Solid("#00FFD10a")
    padding (18, 16)

style pref_row is hbox:
    xfill True
    spacing 14

style pref_icon_frame is frame:
    xsize 38 ysize 38
    background Solid("#00FFD10f")
    padding (0, 0)

style pref_icon_text is text:
    font FONT_MONO
    size 12
    color CYAN
    xalign 0.5 yalign 0.5

style pref_content_block is vbox:
    xsize 420

style pref_title is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 20
    color TEXT_PRIMARY

style pref_desc is text:
    font FONT_BODY
    size 15
    color TEXT_DIM

style pref_toggle_control is hbox:
    xalign 1.0 yalign 0.5
    spacing 8

style pref_slider_control is hbox:
    xalign 1.0 yalign 0.5
    spacing 12

style pref_stepper_control is hbox:
    xalign 1.0 yalign 0.5
    spacing 0

style pref_slider is bar:
    xsize 200 ysize 6
    left_bar Solid("#00FFD1")
    right_bar Solid("#ffffff14")
    thumb Solid("#00FFD1")
    thumb_offset 8
    yalign 0.5

style pref_slider_val is text:
    font FONT_MONO
    size 11
    color TEXT_DIM
    yalign 0.5

style pref_stepper_chip is button:
    padding (10, 14)
    background Null()
    
style pref_stepper_chip_active is button:
    padding (10, 14)
    background Solid("#00FFD114")

style pref_stepper_chip_text is button_text:
    font FONT_MONO
    size 12
    color TEXT_DIM

style pref_stepper_chip_text_active is button_text:
    font FONT_MONO
    size 12
    color CYAN

style pref_toggle_frame_off is frame:
    xsize 64 ysize 32
    background Solid("#ffffff14")
    padding (4, 4)

style pref_toggle_frame_on is frame:
    xsize 64 ysize 32
    background Solid("#00FF8822")
    padding (4, 4)

style pref_toggle_knob_off is frame:
    xsize 22 ysize 22
    background Solid("#CBD5E1")
    xalign 0.0 yalign 0.5

style pref_toggle_knob_on is frame:
    xsize 22 ysize 22
    background Solid("#00FF88")
    xalign 1.0 yalign 0.5

style pref_toggle_label_off is text:
    font FONT_MONO
    size 10
    color TEXT_FAINT
    yalign 0.5

style pref_toggle_label_on is text:
    font FONT_MONO
    size 10
    color CYAN
    yalign 0.5

style pref_side_card is frame:
    xfill True
    background Solid("#ffffff05")
    padding (14, 12)

style pref_side_card_dark is frame:
    xfill True
    background Solid("#00000033")
    padding (14, 14)

style pref_side_card_title is text:
    font FONT_MONO
    size 10
    color "#00FFD166"

style pref_side_card_value is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color TEXT_PRIMARY

style pref_hotkey_val is text:
    font FONT_MONO
    size 10
    color TEXT_DIM
    yalign 0.5

style pref_preset_chip is button:
    padding (12, 10)
    background Null()

style pref_preset_chip_active is button:
    padding (12, 10)
    background Solid("#00FFD10a")

style pref_preset_chip_text is text:
    font FONT_MONO
    size 12
    color TEXT_DIM

style pref_preset_chip_active_text is text:
    font FONT_MONO
    size 12
    color CYAN

style pref_btn_apply is button:
    xfill True
    background Solid("#00FFD1")
    hover_background Solid("#66B3FF")
    padding (0, 12)

style pref_btn_apply_text is button_text:
    font FONT_MONO
    size 13
    color "#040810"
    kerning 1.4
    xalign 0.5

style pref_btn_ghost is button:
    xfill True
    background Null()
    padding (0, 12)

style pref_btn_ghost_text is button_text:
    font FONT_MONO
    size 12
    color TEXT_DIM
    hover_color CYAN
    xalign 0.5

style pref_footer_strip is frame:
    xfill True
    ysize 36
    background Solid("#00000033")
    yalign 1.0

style pref_footer_center is text:
    font FONT_MONO
    size 10
    color TEXT_FAINT
    kerning 1.4

style pref_footer_right is text:
    font FONT_MONO
    size 10
    color TEXT_FAINT
