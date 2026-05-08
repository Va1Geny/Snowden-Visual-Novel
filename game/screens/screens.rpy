################################################################################
## SCREENS.RPY â€” Unified UI System
## Classified: The Snowden Files
################################################################################

init offset = -1

define config.game_menu_action = ShowMenu("pause_hub")


################################################################################
## Shared Setup
################################################################################

init python:
    config.character_id_prefixes.append("namebox")
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("game_hud")
    config.overlay_screens.append("scene_stage_line")
    config.overlay_screens.append("notebook_toggle")
    config.overlay_screens.append("suspicion_lockdown_watch")

    def menu_return_screen():
        return "main_menu" if main_menu else "pause_hub"

    def display_mode_is_windowed():
        return not preferences.fullscreen

    def display_mode_is_fullscreen():
        return preferences.fullscreen

    def toggle_all_audio():
        target_muted = not all_audio_muted()
        for mixer in ("music", "sfx", "voice"):
            preferences.set_mute(mixer, target_muted)
        renpy.restart_interaction()

    def all_audio_muted():
        return all(preferences.get_mute(mixer) for mixer in ("music", "sfx", "voice"))


default quick_menu = True


################################################################################
## Base Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style frame:
    padding gui.frame_borders.padding
    background Solid("#0D1117")

style bar:
    ysize gui.bar_size
    left_bar Solid("#00FFD1")
    right_bar Solid("#111720")

style vbar:
    xsize gui.bar_size
    top_bar Solid("#00FFD1")
    bottom_bar Solid("#111720")

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#111720")
    thumb Solid("#3A4A55")

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#111720")
    thumb Solid("#3A4A55")

style slider:
    ysize gui.slider_size
    base_bar Solid("#111720")
    thumb Solid("#00FFD1")

style vslider:
    xsize gui.slider_size
    base_bar Solid("#111720")
    thumb Solid("#00FFD1")

style shell_nav_button is button:
    xsize 320
    ysize 58
    left_padding 18
    right_padding 18
    background Solid("#0D1117")
    hover_background Solid("#003A3A")
    selected_background Solid("#001A1A")
    insensitive_background Solid("#080C10")

style shell_nav_button_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 22
    color "#E8E8E8"
    hover_color "#00FFD1"
    selected_color "#00FFD1"
    insensitive_color "#3A4A55"
    xalign 0.0

style modal_action_button is button:
    xsize 520
    ysize 74
    left_padding 22
    right_padding 22
    top_padding 4
    bottom_padding 4
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    selected_background Solid("#001A1A")

style modal_action_button_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 23
    bold True
    color "#00FFD1"
    hover_color "#0D1117"
    selected_color "#0D1117"
    xalign 0.5
    text_align 0.5

style choice_button is button:
    xsize 1120
    yminimum 78
    left_padding 28
    right_padding 28
    top_padding 20
    bottom_padding 20
    background Solid("#0D1117")
    hover_background Solid("#003A3A")
    selected_background Solid("#001A1A")

style choice_button_text is button_text:
    font "fonts/Rajdhani-Regular.ttf"
    size 28
    color "#E8E8E8"
    hover_color "#00FFD1"
    xalign 0.5
    text_align 0.5

style quick_button is button:
    background Solid("#080C10CC")
    hover_background Solid("#003A3A")
    left_padding 14
    right_padding 14
    top_padding 10
    bottom_padding 10

style quick_button_text is button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color "#7A8A99"
    hover_color "#00FFD1"

style game_menu_scrollbar is vscrollbar
style game_menu_viewport is empty
style game_menu_label is label
style game_menu_label_text is label_text


################################################################################
## Shared UI Helpers
################################################################################

screen ui_backdrop():
    add "#131421"


screen shell_header(kicker, title, body=None):
    $ compact = is_compact_layout()
    $ header_xpos = 24 if compact else 32
    $ header_ypos = 24 if compact else 44
    $ header_xsize = 1872 if compact else 1856
    $ header_ysize = 142 if compact else 116
    $ header_padding_x = 24 if compact else 34
    $ header_padding_y = 20 if compact else 24
    $ kicker_size = 17 if compact else 15
    $ title_size = 30 if compact else 34
    $ body_size = 18 if compact else 16
    $ body_max = 1120 if compact else 860

    frame:
        xpos header_xpos
        ypos header_ypos
        xsize header_xsize
        ysize header_ysize
        background Solid("#0E1220EE")
        padding (header_padding_x, header_padding_y)

        hbox:
            xfill True
            spacing 28

            vbox:
                spacing 4
                yalign 0.5

                text t(kicker):
                    color "#7A8A99"
                    size kicker_size
                    bold True
                    substitute False

                text t(title):
                    color "#E8E8E8"
                    size title_size
                    bold True
                    substitute False

                if body:
                    text t(body):
                        color "#7A8A99"
                        size body_size
                        xmaximum body_max
                        substitute False

            if body:
                null width 80


################################################################################
## Dialogue Screens
################################################################################

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    substitute False

        text what id "what":
            substitute False

    if not renpy.variant("small"):
        $ edward_pov_bgs = ["bg_nsa_terminal", "bg_prism", "bg_prism1", "bg_hong_kong_terminal"]
        if not (renpy.get_say_image_tag() == "edward" and any(bg in renpy.get_showing_tags("master") for bg in edward_pov_bgs)):
            add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 292
    background Solid("#0D1220E8")
    top_padding 28
    bottom_padding 34

style namebox:
    xpos 188
    ypos 24
    xpadding 22
    ypadding 8
    background Solid("#001A1A")

style say_label:
    color "#00FFD1"
    size 32
    bold True
    xalign 0.0

style say_dialogue:
    color "#E8E8E8"
    size 32
    xpos 188
    ypos 84
    xsize 1544
    line_spacing 3
    adjust_spacing False


screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xpos 188
            ypos 84
            xsize 1544
            spacing 14

            text t(prompt) style "input_prompt":
                substitute False
            input id "input"


style input_prompt is default

style input_prompt:
    color "#7A8A99"
    size 26

style input:
    color "#00FFD1"
    size 30
    xmaximum 1544


screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14

        for i in items:
            textbutton t(i.caption) action i.action


################################################################################
## Quick Menu / HUD
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu and not main_menu:
        $ medium_layout = is_medium_layout()
        $ quick_xalign = 0.5 if medium_layout else 1.0
        $ quick_xoffset = 0 if medium_layout else -30
        $ quick_yoffset = 18 if medium_layout else 24
        hbox:
            xalign quick_xalign
            yalign 0.0
            xoffset quick_xoffset
            yoffset quick_yoffset
            spacing 8
            style_prefix "quick"

            textbutton t("Back") action Rollback()
            textbutton t("History") action ShowMenu("history")
            textbutton t("Notes") action Show("notebook_panel")
            textbutton t("Save") action ShowMenu("save")
            textbutton t("Prefs") action ShowMenu("preferences")

    key "ctrl_K_i" action ShowMenu("dossier")


screen game_hud():
    zorder 90

    if show_hud:
        $ compact = is_medium_layout()
        $ status_title_size = 16 if compact else 14
        $ chapter_size = 22 if compact else 19
        $ stat_size = 17 if compact else 16
        $ suspicion_bar_xsize = 280 if compact else 210

        frame:
            if compact:
                xalign 0.98
                yalign 0.02
                xsize 330
                padding (16, 14)
            else:
                xalign 1.0
                yalign 0.0
                xoffset -30
                yoffset 76
                xsize 260
                padding (18, 16)
            background Solid("#0F1423E6")

            vbox:
                spacing 10

                text t("FIELD STATUS"):
                    color "#7A8A99"
                    size status_title_size
                    bold True

                text t("CHAPTER [current_chapter]/5"):
                    color "#E8E8E8"
                    size chapter_size
                    bold True

                hbox:
                    xfill True
                    text t("Knowledge"):
                        color "#7A8A99"
                        size stat_size
                    text t("[knowledge_score]"):
                        color "#7A8A99"
                        size stat_size
                        bold True
                        xalign 1.0

                hbox:
                    xfill True
                    text t("Trust"):
                        color "#7A8A99"
                        size stat_size
                    text t("[trust_score]"):
                        color "#E8E8E8"
                        size stat_size
                        bold True
                        xalign 1.0

                hbox:
                    xfill True
                    text t("Notes"):
                        color "#7A8A99"
                        size stat_size
                    text t("[notebook_entry_count()]"):
                        color "#E8E8E8"
                        size stat_size
                        bold True
                        xalign 1.0

                text t("Suspicion"):
                    color "#7A8A99"
                    size stat_size

                bar:
                    value suspicion_level
                    range 5
                    xsize suspicion_bar_xsize
                    ysize 10
                    left_bar Solid("#7A8A99")
                    right_bar Solid("#111720")

screen notebook_panel():
    modal True
    zorder 210

    $ compact = is_compact_layout()
    $ viewport_width, viewport_height = current_viewport_size()
    $ notebook_xsize = min(1460 if compact else 1820, max(520, viewport_width - 48))
    $ notebook_ysize = min(860 if compact else 920, max(620, viewport_height - 48))
    $ notebook_title_size = 26 if compact else 30
    $ notebook_body_size = 18 if compact else 20
    $ notebook_body_max = notebook_xsize - 100
    $ notebook_input_size = 24 if compact else 26
    $ notebook_entry_size = 19 if compact else 21
    $ notebook_empty_size = 24 if compact else 28
    $ notebook_hint_max = min(860 if compact else 1260, notebook_xsize - 180)

    $ max_middle_height = notebook_ysize - 84 - 200

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize notebook_xsize
        background Solid("#0E1321F2")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 84
                background Solid("#001A1A")
                padding (28, 0)

                hbox:
                    xfill True
                    yalign 0.5

                    text t("FIELD NOTEBOOK"):
                        color "#E8E8E8"
                        size notebook_title_size
                        bold True
                        yalign 0.5

                    text t("[notebook_entry_count()] entries"):
                        color "#7A8A99"
                        size 18
                        bold True
                        xalign 1.0
                        yalign 0.5

            frame:
                xfill True
                ymaximum max_middle_height
                background Solid("#101523")
                padding (28, 24)

                vbox:
                    spacing 18
                    xfill True

                    text t("Write short reminders for yourself while you play. Important clues, terms, and decisions can live here."):
                        color "#7A8A99"
                        size notebook_body_size
                        xmaximum notebook_body_max

                    frame:
                        xfill True
                        background Solid("#171C30")
                        padding (18, 16)

                        vbox:
                            spacing 12

                            text t("New note"):
                                color "#7A8A99"
                                size 18
                                bold True

                            input:
                                value VariableInputValue("notebook_draft")
                                length 180
                                color "#00FFD1"
                                size notebook_input_size
                                xfill True

                    frame:
                        xfill True
                        yfill True
                        background Solid("#171C30")
                        padding (18, 16)

                        if notebook_entries:
                            viewport:
                                xfill True
                                yfill True
                                mousewheel True
                                draggable True
                                scrollbars "vertical"

                                vbox:
                                    spacing 10
                                    xfill True

                                    for index, entry in enumerate(notebook_entries, 1):
                                        frame:
                                            xfill True
                                            background Solid("#101523")
                                            padding (16, 14)

                                            hbox:
                                                spacing 12
                                                xfill True

                                                text t("[index]."):
                                                    color "#7A8A99"
                                                    size 20
                                                    bold True

                                                text entry:
                                                    color "#E8E8E8"
                                                    size notebook_entry_size
                                                    xfill True
                        else:
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10

                                text t("No notes yet."):
                                    color "#E8E8E8"
                                    size notebook_empty_size
                                    bold True
                                    xalign 0.5

                                text t("Use the field notebook to capture names, tools, and decisions that matter."):
                                    color "#7A8A99"
                                    size notebook_body_size
                                    text_align 0.5
                                    xalign 0.5
                                    xmaximum notebook_hint_max

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22, 24, 40)

                vbox:
                    spacing 12
                    xfill True

                    text t("Exports are saved as plain .txt files. A standard save dialog should let you choose folder and filename."):
                        color "#7A8A99"
                        size 16
                        xalign 0.5
                        text_align 0.5
                        xmaximum 1100

                    hbox:
                        spacing 12
                        box_wrap True
                        box_wrap_spacing 12
                        xalign 0.5

                        textbutton t("EXPORT TXT"):
                            style "modal_action_button"
                            xfill True
                            xmaximum 260
                            background Solid("#244C2F")
                            hover_background Solid("#3A7A58")
                            action Function(export_notebook_txt)

                        textbutton t("SAVE NOTE"):
                            style "modal_action_button"
                            xfill True
                            xmaximum 300
                            action [Function(add_notebook_entry, notebook_draft), SetVariable("notebook_draft", "")]

                        textbutton t("CLEAR"):
                            style "modal_action_button"
                            xfill True
                            xmaximum 220
                            background Solid("#241926")
                            hover_background Solid("#3A4A55")
                            action Function(clear_notebook_entries)

                        textbutton t("CLOSE"):
                            style "modal_action_button"
                            xfill True
                            xmaximum 220
                            background Solid("#171C30")
                            hover_background Solid("#3A4A55")
                            action Hide("notebook_panel")

    key "game_menu" action Hide("notebook_panel")
    key "ctrl_K_n" action Hide("notebook_panel")
    key "K_RETURN" action [Function(add_notebook_entry, notebook_draft), SetVariable("notebook_draft", "")]
    key "K_KP_ENTER" action [Function(add_notebook_entry, notebook_draft), SetVariable("notebook_draft", "")]
screen notebook_toggle():
    zorder 95

    if show_hud and not main_menu and not renpy.get_screen("pause_hub"):
        hbox:
            xalign 1.0
            xoffset 48
            yalign 1.0
            yoffset 54
            spacing 10
            at Transform(zoom=0.5, alpha=0.85)

            fixed:
                fit_first True

                imagebutton:
                    idle Transform("images/ui/notebook_closed.png", matrixcolor=TintMatrix("#003A3A"))
                    hover Transform("images/ui/notebook_open.png", matrixcolor=TintMatrix("#003A3A"))
                    selected_idle Transform("images/ui/notebook_open.png", matrixcolor=TintMatrix("#003A3A"))
                    selected_hover Transform("images/ui/notebook_open.png", matrixcolor=TintMatrix("#003A3A"))
                    selected renpy.get_screen("dossier") is not None
                    focus_mask True
                    action ShowMenu("dossier")
                    tooltip t("Dossier (Ctrl+I)")

                text t("DOSSIER"):
                    align (0.5, 0.45)
                    color "#00FFD1"
                    size 28
                    bold True
                    outlines [(2, "#001A1A", 0, 0)]

            fixed:
                fit_first True

                imagebutton:
                    idle "images/ui/notebook_closed.png"
                    hover "images/ui/notebook_open.png"
                    selected_idle "images/ui/notebook_open.png"
                    selected_hover "images/ui/notebook_open.png"
                    selected renpy.get_screen("notebook_panel") is not None
                    focus_mask True
                    action ToggleScreen("notebook_panel")
                    tooltip t("Notebook (Ctrl+N)")

                text t("NOTEBOOK"):
                    align (0.5, 0.45)
                    color "#7A8A99"
                    size 28
                    bold True
                    outlines [(2, "#101523", 0, 0)]

        key "ctrl_K_n" action ToggleScreen("notebook_panel")


screen suspicion_lockdown_watch():
    zorder 300

    if (
        show_hud
        and suspicion_level >= 5
        and not suspicion_lockdown_triggered
        and not main_menu
    ):
        timer 0.01 action [SetVariable("suspicion_lockdown_triggered", True), Jump("max_suspicion_game_over")]


screen scene_stage_line():
    zorder 5

    if not main_menu and renpy.get_screen("say") and not renpy.get_screen("pause_hub"):
        add Solid("#02030466"):
            xpos 0
            ypos 822
            xsize 1920
            ysize 258

        add Solid("#003A3A22"):
            xpos 0
            ypos 804
            xsize 1920
            ysize 8


################################################################################
## Primary Menus
################################################################################

## Pulsing dot for the "SYSTEM ONLINE" indicator
transform mm_pulse_dot:
    alpha 1.0
    easeout 0.9 alpha 0.35
    easein 0.9 alpha 1.0
    repeat

## Subtle drift on the side accent bars
transform mm_accent_drift:
    alpha 0.55
    easeout 1.6 alpha 1.0
    easein 1.6 alpha 0.55
    repeat


screen main_menu():
    tag menu

    $ compact = is_medium_layout()
    $ menu_frame_xsize = 1840 if compact else 1500
    $ menu_frame_ysize = 990 if compact else 1020
    $ menu_padding_x = 36 if compact else 56
    $ menu_padding_y = 30 if compact else 44
    $ menu_content_max = 1660 if compact else 940
    $ menu_spacing = 12 if compact else 14
    $ title_fixed_xsize = 1500 if compact else 880
    $ menu_title_size = 60 if compact else 72
    $ menu_desc_size = 22 if compact else 18
    $ menu_desc_max = 1200 if compact else 740
    $ menu_quote_size = 24 if compact else 18
    $ corner_size = 22

    use ui_backdrop

    ## ── Ambient backdrop accents ────────────────────────────────────
    add Solid("#003A3A0E"):
        xsize 480
        ysize 1080
        xpos 0
    add Solid("#003A3A0E"):
        xsize 480
        ysize 1080
        xalign 1.0

    add Solid("#7A8A9918"):
        xsize 1920
        ysize 2
        ypos 96

    add Solid("#7A8A9918"):
        xsize 1920
        ysize 2
        ypos 982

    ## â”€â”€ Top status bar â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    fixed:
        xpos 0
        ypos 28
        xsize 1920
        ysize 36

        hbox:
            xpos 60
            yalign 0.5
            spacing 18

            frame:
                background Solid("#00FF8826")
                xsize 12
                ysize 12
                yalign 0.5
                at mm_pulse_dot

            text t("SYSTEM ONLINE"):
                color "#00FF88"
                size 14
                bold True
                kerning 3
                yalign 0.5

            text t("·"):
                color "#3A4A55"
                size 16
                yalign 0.5

            text t("SECURE CHANNEL // AES-256"):
                color "#7A8A99"
                size 13
                bold True
                kerning 2
                yalign 0.5

        hbox:
            xalign 1.0
            xoffset -60
            yalign 0.5
            spacing 18

            text t("CLEARANCE: TS//SCI"):
                color "#FFD700"
                size 13
                bold True
                kerning 2
                yalign 0.5

            text t("·"):
                color "#3A4A55"
                size 16
                yalign 0.5

            text t("NODE 0451"):
                color "#7A8A99"
                size 13
                bold True
                kerning 2
                yalign 0.5

    ## â”€â”€ Primary panel â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    fixed:
        xalign 0.5
        yalign 0.5
        xsize menu_frame_xsize
        ysize menu_frame_ysize

        ## Outer halo â€” soft tinted edge for depth
        frame:
            xfill True
            yfill True
            background Solid("#003A3A18")

        ## Main panel surface
        frame:
            xpos 4
            ypos 4
            xsize (menu_frame_xsize - 8)
            ysize (menu_frame_ysize - 8)
            background Solid("#0E1321C0")
            padding (menu_padding_x, menu_padding_y)

            ## Animated accent rails
            add Solid("#003A3A"):
                xsize 3
                ysize (menu_frame_ysize - 160)
                xpos 0
                yalign 0.5
                at mm_accent_drift
            add Solid("#003A3A"):
                xsize 3
                ysize (menu_frame_ysize - 160)
                xalign 1.0
                yalign 0.5
                at mm_accent_drift

            ## Corner brackets — terminal aesthetic
            add Solid("#003A3A"):
                xsize corner_size
                ysize 3
                xpos 12
                ypos 12
            add Solid("#003A3A"):
                xsize 3
                ysize corner_size
                xpos 12
                ypos 12

            add Solid("#003A3A"):
                xsize corner_size
                ysize 3
                xalign 1.0
                xoffset -12
                ypos 12
            add Solid("#003A3A"):
                xsize 3
                ysize corner_size
                xalign 1.0
                xoffset -12
                ypos 12

            add Solid("#003A3A"):
                xsize corner_size
                ysize 3
                xpos 12
                yalign 1.0
                yoffset -15
            add Solid("#003A3A"):
                xsize 3
                ysize corner_size
                xpos 12
                yalign 1.0
                yoffset -12

            add Solid("#003A3A"):
                xsize corner_size
                ysize 3
                xalign 1.0
                xoffset -12
                yalign 1.0
                yoffset -15
            add Solid("#003A3A"):
                xsize 3
                ysize corner_size
                xalign 1.0
                xoffset -12
                yalign 1.0
                yoffset -12

            vbox:
                xalign 0.5
                yalign 0.5
                xmaximum menu_content_max
                spacing menu_spacing

                ## Kicker line: classified label between ticks
                hbox:
                    xalign 0.5
                    spacing 12

                    add Solid("#003A3A"):
                        xsize 48
                        ysize 1
                        yalign 0.5

                    text t("// CLASSIFIED INTERFACE //"):
                        color "#7A8A99"
                        size 16
                        bold True
                        text_align 0.5
                        kerning 4

                    add Solid("#003A3A"):
                        xsize 48
                        ysize 1
                        yalign 0.5

                add "images/logo.png":
                    xalign 0.5
                    ysize 128
                    fit "contain"

                fixed:
                    xsize title_fixed_xsize
                    ysize 100
                    xalign 0.5

                    text t("ENEMY OF THE STATE"):
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        color "#0C5D52"
                        size menu_title_size
                        bold True
                        outlines [(6, "#003A3A14", 0, 0), (3, "#00FFD116", 0, 0)]

                    text t("ENEMY OF THE STATE") at title_glitch:
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        color "#EFFFFA"
                        size menu_title_size
                        bold True
                        outlines [(2, "#00FFD155", 0, 0), (6, "#00FFD10E", 0, 0)]

                    text t("ENEMY OF THE STATE"):
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        xoffset 2
                        yoffset -2
                        color "#7A8A9924"
                        size menu_title_size
                        bold True

                ## Refined separator under title
                hbox:
                    xalign 0.5
                    spacing 8

                    add Solid("#3A4A5580"):
                        xsize 80
                        ysize 1
                        yalign 0.5

                    add Solid("#003A3A"):
                        xsize 6
                        ysize 6
                        yalign 0.5

                    add Solid("#3A4A5580"):
                        xsize 80
                        ysize 1
                        yalign 0.5

                text t("A visual novel about surveillance, trust, and digital security under pressure."):
                    color "#7A8A99"
                    size menu_desc_size
                    xalign 0.5
                    text_align 0.5
                    xmaximum menu_desc_max

                text t("\"The truth will always find a way out.\""):
                    color "#7A8A99"
                    size menu_quote_size
                    italic True
                    xalign 0.5
                    text_align 0.5

                null height 4

                vbox:
                    xalign 0.5
                    spacing 8

                    textbutton t("â–¸ START"):
                        style "modal_action_button"
                        xalign 0.5
                        action Start()

                    if renpy.newest_slot():
                        textbutton t("â–¸ CONTINUE"):
                            style "modal_action_button"
                            xalign 0.5
                            action FileLoad(renpy.newest_slot(), confirm=False)

                    textbutton t("â–¸ DOSSIER"):
                        style "modal_action_button"
                        xalign 0.5
                        action ShowMenu("dossier")

                    textbutton t("â–¸ STORY TREE"):
                        style "modal_action_button"
                        xalign 0.5
                        action ShowMenu("story_tree")

                    textbutton t("â–¸ SETTINGS"):
                        style "modal_action_button"
                        xalign 0.5
                        action ShowMenu("preferences")

                    if renpy.variant("pc"):
                        textbutton t("Ã— EXIT"):
                            style "modal_action_button"
                            xalign 0.5
                            background Solid("#241926")
                            hover_background Solid("#3A4A55")
                            action Quit(confirm=True)

                null height 6

                ## Footer line: build tag + version
                hbox:
                    xalign 0.5
                    spacing 14

                    text t("BUILD STABLE"):
                        color "#3A4A55"
                        size 13
                        bold True
                        kerning 2
                        yalign 0.5

                    text t("·"):
                        color "#3A4A55"
                        size 14
                        yalign 0.5

                    text t("v[config.version]"):
                        color "#7A8A99"
                        size 14
                        yalign 0.5



screen pause_hub():
    tag menu
    modal True

    $ compact = is_compact_layout()

    use ui_backdrop
    use shell_header(
        "ESC MENU",
        "MISSION CONTROL",
        "Resume, save, adjust settings, or inspect the branch map without dropping into the default Ren'Py interface."
    )

    if compact:
        frame:
            xpos 24
            ypos 188
            xsize 1872
            ysize 844
            background Solid("#0E1321EE")
            padding (24, 24)

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 18
                    xfill True

                    frame:
                        xfill True
                        background Solid("#101523EE")
                        padding (22, 20)

                        vbox:
                            spacing 12

                            text t("MISSION ACTIONS"):
                                color "#7A8A99"
                                size 18
                                bold True

                            textbutton t("RESUME"):
                                style "modal_action_button"
                                xfill True
                                action Return()

                            textbutton t("OPEN NOTEBOOK"):
                                style "modal_action_button"
                                xfill True
                                action Show("notebook_panel")

                            textbutton t("DOSSIER"):
                                style "modal_action_button"
                                xfill True
                                action ShowMenu("dossier")

                            textbutton t("SAVE"):
                                style "modal_action_button"
                                xfill True
                                action ShowMenu("save")

                            textbutton t("SETTINGS"):
                                style "modal_action_button"
                                xfill True
                                action ShowMenu("preferences")

                            textbutton t("STORY TREE"):
                                style "modal_action_button"
                                xfill True
                                action ShowMenu("story_tree")

                            textbutton t("START OVER"):
                                style "modal_action_button"
                                xfill True
                                action Start()

                            if renpy.variant("pc"):
                                textbutton t("EXIT"):
                                    style "modal_action_button"
                                    xfill True
                                    background Solid("#241926")
                                    hover_background Solid("#3A4A55")
                                    action Quit(confirm=True)

                    text t("TACTICAL STATUS"):
                        color "#7A8A99"
                        size 18
                        bold True

                    for title, value, body, accent in [
                        ("Current chapter", "[current_chapter]/5", "Operation branch currently in progress.", "#001A1A"),
                        ("Knowledge", "[knowledge_score]", "Educational progress accumulated so far.", "#171C30"),
                        ("Trust", "[trust_score]", "Relationship capital built during the mission.", "#171C30"),
                        ("Suspicion", "[suspicion_level]/5", "Operational pressure currently on the player.", "#171C30"),
                        ("Notebook", "[notebook_entry_count()]", "Personal notes saved for quick review.", "#171C30"),
                    ]:
                        frame:
                            xfill True
                            background Solid(accent)
                            padding (22, 18)

                            vbox:
                                spacing 8
                                text title:
                                    color "#7A8A99"
                                    size 16
                                    bold True
                                text value:
                                    color "#E8E8E8"
                                    size 34
                                    bold True
                                text body:
                                    color "#7A8A99"
                                    size 17
    else:
        frame:
            xpos 32
            ypos 190
            xsize 620
            ysize 850
            background Solid("#101523CC")
            padding (34, 30)

            vbox:
                spacing 14

                textbutton t("RESUME"):
                    style "modal_action_button"
                    action Return()

                textbutton t("OPEN NOTEBOOK"):
                    style "modal_action_button"
                    action Show("notebook_panel")

                textbutton t("DOSSIER"):
                    style "modal_action_button"
                    action ShowMenu("dossier")

                textbutton t("START"):
                    style "modal_action_button"
                    action Start()

                textbutton t("SAVE"):
                    style "modal_action_button"
                    action ShowMenu("save")

                textbutton t("SETTINGS"):
                    style "modal_action_button"
                    action ShowMenu("preferences")

                textbutton t("STORY TREE"):
                    style "modal_action_button"
                    action ShowMenu("story_tree")

                if renpy.variant("pc"):
                    textbutton t("EXIT"):
                        style "modal_action_button"
                        background Solid("#241926")
                        hover_background Solid("#3A4A55")
                        action Quit(confirm=True)

        frame:
            xalign 1.0
            xoffset -32
            ypos 190
            xsize 1196
            ysize 850
            background Solid("#0E1321C0")
            padding (36, 32)

            vbox:
                spacing 18

                text t("TACTICAL STATUS"):
                    color "#7A8A99"
                    size 17
                    bold True

                hbox:
                    spacing 18

                    frame:
                        xsize 320
                        ysize 150
                        background Solid("#001A1A")
                        padding (22, 18)

                        vbox:
                            spacing 8
                            text t("Current chapter"):
                                color "#7A8A99"
                                size 15
                                bold True
                            text t("[current_chapter]/5"):
                                color "#E8E8E8"
                                size 34
                                bold True
                            text t("Operation branch currently in progress."):
                                color "#7A8A99"
                                size 16

                    frame:
                        xsize 320
                        ysize 150
                        background Solid("#171C30")
                        padding (22, 18)

                        vbox:
                            spacing 8
                            text t("Knowledge"):
                                color "#7A8A99"
                                size 15
                                bold True
                            text t("[knowledge_score]"):
                                color "#E8E8E8"
                                size 34
                                bold True
                            text t("Educational progress accumulated so far."):
                                color "#7A8A99"
                                size 16

                    frame:
                        xsize 320
                        ysize 150
                        background Solid("#171C30")
                        padding (22, 18)

                        vbox:
                            spacing 8
                            text t("Suspicion"):
                                color "#7A8A99"
                                size 15
                                bold True
                            text t("[suspicion_level]/5"):
                                color "#E8E8E8"
                                size 34
                                bold True
                            text t("Operational pressure currently on the player."):
                                color "#7A8A99"
                                size 16

                frame:
                    xfill True
                    ysize 1
                    background Solid("#111720")

                text t("This pause menu now uses the same spacing system as the rest of the UI, so buttons, cards, and text blocks stay aligned on different screens."):
                    color "#7A8A99"
                    size 18
                    xmaximum 960

    key "game_menu" action Return()


################################################################################
## Story / Learning Screens
################################################################################

screen dossier():
    tag menu

    $ compact = is_compact_layout()
    $ dossier_xpos = 24 if compact else 72
    $ dossier_ypos = 188 if compact else 214
    $ dossier_xsize = 1872 if compact else 1776
    $ dossier_ysize = 844 if compact else 770
    $ dossier_viewport_ysize = 694 if compact else 640
    $ dossier_term_size = 26 if compact else 24
    $ dossier_definition_size = 20 if compact else 18
    $ dossier_footer_size = 19 if compact else 17

    use ui_backdrop
    add "logo_watermark"
    use shell_header(
        "REFERENCE DATABASE",
        "NETWORK SECURITY DOSSIER",
        "Core cyber-security concepts presented in one scrollable reference layout."
    )

    frame:
        xpos dossier_xpos
        ypos dossier_ypos
        xsize dossier_xsize
        ysize dossier_ysize
        background Solid("#0E1321E6")
        padding (26, 26)

        vbox:
            xfill True
            yfill True
            spacing 18

            viewport:
                xfill True
                ysize dossier_viewport_ysize
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                vbox:
                    spacing 14
                    xfill True
                    xmaximum 1670

                    for term, definition in DOSSIER_ENTRIES:
                        frame:
                            xfill True
                            xmaximum 1670
                            background Solid("#171C30")
                            padding (24, 20)

                            hbox:
                                spacing 18
                                xfill True

                                frame:
                                    xsize 4
                                    ysize 76
                                    background Solid("#003A3A")
                                    yalign 0.0

                                vbox:
                                    spacing 8
                                    xfill True
                                    xmaximum 1600

                                    text t(term):
                                        color "#E8E8E8"
                                        size dossier_term_size
                                        bold True
                                        xfill True
                                        substitute False

                                    text t(definition):
                                        color "#7A8A99"
                                        size dossier_definition_size
                                        xfill True
                                        xmaximum 1540
                                        substitute False

            frame:
                xfill True
                background Solid("#171C30")
                padding (20, 18)

                vbox:
                    spacing 10
                    xfill True

                    text t("Exports are saved as plain .txt files to an exports folder or to your user profile if needed."):
                        color "#7A8A99"
                        size dossier_footer_size
                        xalign 0.5
                        text_align 0.5
                        xmaximum 1400
                        substitute False

                    hbox:
                        spacing 12
                        xfill True

                        textbutton t("EXPORT TXT"):
                            style "modal_action_button"
                            xsize 220
                            background Solid("#244C2F")
                            hover_background Solid("#3A7A58")
                            action Function(export_dossier_txt)

                        null xfill True

                        textbutton t("RETURN"):
                            style "modal_action_button"
                            xsize 240
                            action Return()

    key "game_menu" action Return()


screen intro_fullscreen_prompt():
    modal True

    $ compact = is_compact_layout()
    $ intro_xsize = 1820 if compact else 1080
    $ intro_title_size = 30 if compact else 26
    $ intro_text_size = 22 if compact else 19
    $ intro_text_max = 1600 if compact else 920

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize intro_xsize
        background Solid("#0E1321F2")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 66
                background Solid("#241926")
                padding (28, 0)

                text t("DISPLAY MODE"):
                    color "#E8E8E8"
                    size 26
                    bold True
                    xalign 0.5
                    yalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (36, 30)

                vbox:
                    spacing 18

                    text t("Fullscreen recommended"):
                        color "#E8E8E8"
                        size intro_title_size
                        bold True

                    text t("For the best experience, play in fullscreen mode. This helps dialogue, menus, and minigames fit better on itch.io embeds and mobile browsers."):
                        color "#7A8A99"
                        size intro_text_size
                        xmaximum intro_text_max

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22)

                hbox:
                    spacing 14
                    xalign 0.5

                    textbutton t("GO FULLSCREEN"):
                        style "modal_action_button"
                        xsize 320
                        action [Preference("display", "fullscreen"), Return()]

                    textbutton t("SKIP"):
                        style "modal_action_button"
                        xsize 260
                        background Solid("#171C30")
                        hover_background Solid("#3A4A55")
                        action Return()


screen intro_shortcuts_screen():
    modal True

    $ compact = is_compact_layout()
    $ intro_xsize = 1820 if compact else 1080
    $ intro_title_size = 30 if compact else 26
    $ intro_control_size = 20 if compact else 18
    $ intro_control_label_xsize = 520 if compact else 330

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize intro_xsize
        background Solid("#0E132188")
        padding (0, 0)

        vbox:
            spacing 0
            

            frame:
                xfill True
                ysize 66
                background Solid("#001A1A")
                padding (28, 0)
                

                text t("CLASSIFIED BRIEFING"):
                    color "#E8E8E8"
                    size 26
                    bold True
                    xalign 0.5
                    yalign 0.5
                    

            frame:
                xfill True
                background Solid("#10152380")
                padding (36, 30)
                

                vbox:
                    spacing 18

                    text t("Controls & shortcuts"):
                        color "#E8E8E8"
                        size intro_title_size
                        bold True

                    frame:
                        xfill True
                        background Solid("#171C3080")
                        padding (24, 20)

                        vbox:
                            spacing 10

                            text t("Controls"):
                                color "#7A8A99"
                                size 22
                                bold True

                            for control, description in [
                                ("Click / Enter / Space", "Advance dialogue and confirm UI actions."),
                                ("Esc / Right Click / MENU", "Open mission control and game settings."),
                                ("Back / Page Up", "Review previous dialogue."),
                                ("Ctrl+N", "                   Open / close the field notebook."),
                                ("Ctrl+I", "                   Open the network security dossier."),
                                ("Notebook", "              Save your own reminders while playing."),
                            ]:
                                hbox:
                                    spacing 14
                                    xfill True

                                    text control:
                                        color "#E8E8E8"
                                        size intro_control_size
                                        bold True
                                        xsize intro_control_label_xsize

                                    text description:
                                        color "#7A8A99"
                                        size intro_control_size
                                        xfill True

            frame:
                xfill True
                background Solid("#171C3080")
                padding (24, 22)

                hbox:
                    spacing 14
                    xalign 0.5

                    textbutton t("BEGIN MISSION"):
                        style "modal_action_button"
                        xsize 320
                        action Return()


screen briefing_screen():
    modal True

    $ compact = is_compact_layout()
    $ briefing_xsize = 1820 if compact else 980
    $ briefing_title_size = 26 if compact else 24
    $ briefing_meta_size = 22 if compact else 20
    $ briefing_body_size = 24 if compact else 22
    $ briefing_body2_size = 20 if compact else 18
    $ briefing_body_max = 1600 if compact else 860

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize briefing_xsize
        background Solid("#0E1321F2")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 66
                background Solid("#241926")
                padding (28, 0)

                text t("CLASSIFIED BRIEFING"):
                    color "#E8E8E8"
                    size 26
                    bold True
                    xalign 0.5
                    yalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (36, 30)

                vbox:
                    spacing 18

                    text t("OPERATIVE: [[CLASSIFIED]"):
                        color "#E8E8E8"
                        size briefing_title_size
                        bold True

                    text t("ASSIGNMENT: NSA Systems Administrator"):
                        color "#7A8A99"
                        size briefing_meta_size

                    text t("CLEARANCE: TS/SCI"):
                        color "#7A8A99"
                        size briefing_meta_size
                        bold True

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#111720")

                    text t("Navigate the moral and technical challenges of one of the most significant intelligence leaks in modern history."):
                        color "#E8E8E8"
                        size briefing_body_size
                        xmaximum briefing_body_max

                    text t("Your decisions affect trust, suspicion, and what information can survive the operation."):
                        color "#7A8A99"
                        size briefing_body2_size
                        xmaximum briefing_body_max

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22)

                textbutton t("ACCEPT MISSION"):
                    style "modal_action_button"
                    xalign 0.5
                    action Return()


screen chapter_title_screen(number, title, subtitle):
    modal True

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        background Solid("#0E1321EE")
        padding (40, 36)

        vbox:
            xalign 0.5
            spacing 12

            text t("CHAPTER [number]"):
                color "#7A8A99"
                size 18
                bold True
                xalign 0.5

            text title:
                color "#E8E8E8"
                size 58
                bold True
                xalign 0.5

            text subtitle:
                color "#7A8A99"
                size 23
                italic True
                xalign 0.5

    timer 3.0 action Return()
    key "dismiss" action Return()


screen chapter_summary(chapter_num, chapter_name):
    modal True

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 980
        background Solid("#0E1321F0")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 80
                background Solid("#171C30")
                padding (30, 0)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 4

                    text t("CHAPTER [chapter_num] COMPLETE"):
                        color "#7A8A99"
                        size 16
                        bold True
                        xalign 0.5

                    text chapter_name:
                        color "#E8E8E8"
                        size 28
                        bold True
                        xalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (34, 28)

                vbox:
                    spacing 16

                    hbox:
                        xfill True
                        text t("Knowledge Score"):
                            color "#7A8A99"
                            size 21
                        text t("[knowledge_score]"):
                            color "#E8E8E8"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text t("Trust Score"):
                            color "#7A8A99"
                            size 21
                        text t("[trust_score]"):
                            color "#E8E8E8"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text t("Suspicion Level"):
                            color "#7A8A99"
                            size 21
                        text t("[suspicion_level]/5"):
                            color "#E8E8E8"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text t("Contacts Secured"):
                            color "#7A8A99"
                            size 21
                        text t("[contacts_secured]"):
                            color "#E8E8E8"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text t("Evidence"):
                            color "#7A8A99"
                            size 21
                        if evidence_secured:
                            text t("SECURED"):
                                color "#E8E8E8"
                                size 21
                                bold True
                                xalign 1.0
                        else:
                            text t("NOT YET"):
                                color "#E8E8E8"
                                size 21
                                bold True
                                xalign 1.0

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22)

                if chapter_num < 5:
                    textbutton t("CONTINUE TO CHAPTER [chapter_num + 1]"):
                        style "modal_action_button"
                        xalign 0.5
                        action Return()
                else:
                    textbutton t("PROCEED TO FINAL ASSESSMENT"):
                        style "modal_action_button"
                        xalign 0.5
                        action Return()


screen mcq_question(question, answers, correct_index, explanation, helper_text=None):
    modal True
    default selected = -1
    default answered = False

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        background Solid("#0E1321F0")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 76
                background Solid("#171C30")
                padding (28, 0)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 2

                    text t("KNOWLEDGE CHECK"):
                        color "#E8E8E8"
                        size 24
                        bold True
                        xalign 0.5

                    text t("Pick the best answer. Every right call boosts your field knowledge."):
                        color "#7A8A99"
                        size 15
                        xalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (34, 28)

                vbox:
                    spacing 18

                    text question:
                        color "#E8E8E8"
                        size 25
                        xalign 0.5
                        text_align 0.5
                        xmaximum 980

                    if helper_text:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (18, 14)

                            text helper_text:
                                color "#7A8A99"
                                size 18
                                italic True
                                xalign 0.5
                                text_align 0.5
                                xmaximum 920

                    for i, answer in enumerate(answers):
                        $ letter = ["A", "B", "C", "D"][i]

                        if not answered:
                            textbutton t("[letter].  [answer]"):
                                style "choice_button"
                                xalign 0.5
                                action [
                                    SetScreenVariable("selected", i),
                                    SetScreenVariable("answered", True)
                                ]
                        elif i == correct_index:
                            textbutton t("[letter].  [answer]"):
                                style "choice_button"
                                xalign 0.5
                                background Solid("#001A1A")
                                hover_background Solid("#001A1A")
                                action NullAction()
                        elif i == selected:
                            textbutton t("[letter].  [answer]"):
                                style "choice_button"
                                xalign 0.5
                                background Solid("#241926")
                                hover_background Solid("#241926")
                                action NullAction()
                        else:
                            textbutton t("[letter].  [answer]"):
                                style "choice_button"
                                xalign 0.5
                                background Solid("#0D1117")
                                hover_background Solid("#0D1117")
                                action NullAction()

            if answered:
                frame:
                    xfill True
                    background Solid("#111720")
                    padding (26, 24)

                    vbox:
                        spacing 12
                        xalign 0.5

                        if selected == correct_index:
                            text t("Correct - Nice catch"):
                                color "#00FF88"
                                size 24
                                bold True
                                xalign 0.5
                        else:
                            $ correct_letter = ["A", "B", "C", "D"][correct_index]
                            text t("Not quite - Correct answer: [correct_letter]"):
                                color "#E8E8E8"
                                size 24
                                bold True
                                xalign 0.5

                        text explanation:
                            color "#7A8A99"
                            size 18
                            xalign 0.5
                            text_align 0.5
                            xmaximum 920

                        textbutton t("CONTINUE"):
                            style "modal_action_button"
                            xalign 0.5
                            if selected == correct_index:
                                action [SetVariable("knowledge_score", knowledge_score + 1), Return()]
                            else:
                                action Return()

################################################################################
## Menu Shell
################################################################################

screen navigation():
    vbox:
        spacing 12

        if main_menu:
            textbutton t("Start"):
                style "shell_nav_button"
                action Start()
        else:
            textbutton t("History"):
                style "shell_nav_button"
                action ShowMenu("history")

            textbutton t("Save"):
                style "shell_nav_button"
                action ShowMenu("save")

        textbutton t("Load"):
            style "shell_nav_button"
            action ShowMenu("load")

        textbutton t("Preferences"):
            style "shell_nav_button"
            action ShowMenu("preferences")

        textbutton t("Dossier"):
            style "shell_nav_button"
            action ShowMenu("dossier")

        textbutton t("Story Tree"):
            style "shell_nav_button"
            action ShowMenu("story_tree")

        if _in_replay:
            textbutton t("End Replay"):
                style "shell_nav_button"
                action EndReplay(confirm=True)
        elif not main_menu:
            textbutton t("Main Menu"):
                style "shell_nav_button"
                action MainMenu()

        textbutton t("About"):
            style "shell_nav_button"
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton t("Help"):
                style "shell_nav_button"
                action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton t("Quit"):
                style "shell_nav_button"
                background Solid("#241926")
                hover_background Solid("#3A4A55")
                action Quit(confirm=not main_menu)


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    tag menu

    $ compact = is_compact_layout()

    use ui_backdrop
    use shell_header(
        "ARCHIVE INTERFACE",
        "[title]",
        "A single menu grid now drives save, load, settings, history, help, and reference screens."
    )

    if compact:
        frame:
            xpos 24
            ypos 188
            xsize 1872
            ysize 844
            background Solid("#0E1321EE")
            padding (20, 20)

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 18
                    xfill True

                    frame:
                        xfill True
                        background Solid("#101523")
                        padding (18, 18)

                        vbox:
                            spacing 14

                            use navigation

                            textbutton t("Notes"):
                                style "shell_nav_button"
                                xfill True
                                action Show("notebook_panel")

                            textbutton t("Return"):
                                style "shell_nav_button"
                                xfill True
                                action ShowMenu(menu_return_screen())

                    frame:
                        xfill True
                        background Solid("#101523")
                        padding (24, 24)

                        if scroll == "viewport":
                            viewport:
                                style "game_menu_viewport"
                                yinitial yinitial
                                xfill True
                                yfill True
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                pagekeys True

                                vbox:
                                    spacing spacing
                                    xfill True
                                    transclude

                        elif scroll == "vpgrid":
                            vpgrid:
                                cols 1
                                yinitial yinitial
                                xfill True
                                yfill True
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                pagekeys True
                                spacing spacing

                                transclude

                        else:
                            transclude
    else:
        hbox:
            xpos 72
            ypos 214
            spacing 20

            frame:
                xsize 360
                ysize 770
                background Solid("#0E1321EE")
                padding (20, 20)

                vbox:
                    spacing 18

                    use navigation

                    null height 6

                    textbutton t("Notes"):
                        style "shell_nav_button"
                        action Show("notebook_panel")

                    textbutton t("Return"):
                        style "shell_nav_button"
                        action ShowMenu(menu_return_screen())

            frame:
                xsize 1396
                ysize 770
                background Solid("#0E1321EE")
                padding (24, 24)

                if scroll == "viewport":
                    viewport:
                        style "game_menu_viewport"
                        yinitial yinitial
                        xfill True
                        yfill True
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        vbox:
                            spacing spacing
                            xfill True
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        xfill True
                        yfill True
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        spacing spacing

                        transclude

                else:
                    transclude

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action ShowMenu("pause_hub")


################################################################################
## Standard Menus
################################################################################

screen about():
    tag menu

    use game_menu(t("About"), scroll="viewport", spacing=18):
        frame:
            xfill True
            background Solid("#171C30")
            padding (28, 24)

            vbox:
                spacing 14

                text t("[config.name!t]"):
                    color "#E8E8E8"
                    size 32
                    bold True

                text t("Version [config.version!t]"):
                    color "#7A8A99"
                    size 20

                if gui.about:
                    text t("[gui.about!t]"):
                        color "#7A8A99"
                        size 19

                text t("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."):
                    color "#7A8A99"
                    size 18

                text t("[renpy.license!t]"):
                    color "#7A8A99"
                    size 16


screen save():
    tag menu
    use file_slots(t("Save"))


screen load():
    tag menu
    use file_slots(t("Load"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=t("Page {}"), auto=t("Automatic saves"), quick=t("Quick saves"))

    use game_menu(title, scroll="viewport", spacing=18):
        frame:
            xfill True
            background Solid("#171C30")
            padding (24, 22)

            vbox:
                spacing 18

                button:
                    xalign 0.5
                    background Solid("#101523")
                    hover_background Solid("#0D1117")
                    padding (18, 10)
                    action If(FileCurrentPage() == "chapter", NullAction(), page_name_value.Toggle())

                    if FileCurrentPage() == "chapter":
                        text t("Chapter saves"):
                            color "#E8E8E8"
                            size 22
                            xalign 0.5
                            text_align 0.5
                    else:
                        input:
                            value page_name_value
                            color "#E8E8E8"
                            size 22
                            xalign 0.5
                            text_align 0.5

                grid gui.file_slot_cols gui.file_slot_rows:
                    xalign 0.5
                    spacing 18

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1

                        button:
                            xsize 414
                            ysize 330
                            background Solid("#101523")
                            hover_background Solid("#0D1117")
                            padding (14, 14)
                            action FileAction(slot)

                            has vbox
                            spacing 10

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=t("{#file_time}%A, %B %d %Y, %H:%M"), empty=t("Empty slot")):
                                color "#7A8A99"
                                size 15
                                xalign 0.0

                            text FileSaveName(slot):
                                color "#E8E8E8"
                                size 18
                                xalign 0.0

                            key "save_delete" action FileDelete(slot)

                hbox:
                    xalign 0.5
                    spacing 10

                    if FileCurrentPage() == "chapter":
                        textbutton t("<"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage("auto")
                    else:
                        textbutton t("<"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePagePrevious()

                    if config.has_autosave:
                        textbutton t("{#auto_page}A"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage("auto")

                    textbutton t("{#chapter_page}C"):
                        style "shell_nav_button"
                        xsize 74
                        action FilePage("chapter")

                    if config.has_quicksave:
                        textbutton t("{#quick_page}Q"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage("quick")

                    for page in range(1, 10):
                        textbutton t("[page]"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage(page)

                    if FileCurrentPage() == "chapter":
                        textbutton t(">"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage(1)
                    else:
                        textbutton t(">"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePageNext()


screen preferences():
    tag menu

    use game_menu(t("Preferences"), scroll="viewport", spacing=18):
        hbox:
            spacing 18
            xfill True

            frame:
                xsize 655
                background Solid("#171C30")
                padding (24, 22)

                vbox:
                    spacing 18

                    text t("DISPLAY AND FLOW"):
                        color "#7A8A99"
                        size 18
                        bold True

                    if renpy.variant("pc") or renpy.variant("web"):
                        textbutton t("Window"):
                            style "shell_nav_button"
                            selected display_mode_is_windowed()
                            action Preference("display", "window")

                        textbutton t("Fullscreen"):
                            style "shell_nav_button"
                            selected display_mode_is_fullscreen()
                            action Preference("display", "fullscreen")

                    textbutton t("Skip Unseen Text"):
                        style "shell_nav_button"
                        action Preference("skip", "toggle")

                    textbutton t("Skip After Choices"):
                        style "shell_nav_button"
                        action Preference("after choices", "toggle")

                    textbutton t("Transitions"):
                        style "shell_nav_button"
                        action InvertSelected(Preference("transitions", "toggle"))

            frame:
                xsize 655
                background Solid("#171C30")
                padding (24, 22)

                vbox:
                    spacing 18

                    text t("TEXT AND AUDIO"):
                        color "#7A8A99"
                        size 18
                        bold True

                    text t("Text Speed"):
                        color "#E8E8E8"
                        size 18
                    bar value Preference("text speed")

                    text t("Auto-Forward Time"):
                        color "#E8E8E8"
                        size 18
                    bar value Preference("auto-forward time")

                    if config.has_music:
                        text t("Music Volume"):
                            color "#E8E8E8"
                            size 18
                        bar value Preference("music volume")

                    if config.has_sound:
                        text t("Sound Volume"):
                            color "#E8E8E8"
                            size 18
                        bar value Preference("sound volume")

                    if config.has_voice:
                        text t("Voice Volume"):
                            color "#E8E8E8"
                            size 18
                        bar value Preference("voice volume")

                    textbutton t("Mute All"):
                        style "shell_nav_button"
                        selected all_audio_muted()
                        action Function(toggle_all_audio)

        ## â”€â”€ LANGUAGE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        ## English is the default (language=None). Dutch/French/Ukrainian
        ## switch to the matching translation under game/tl/<name>/. If a
        ## translation folder is missing, Ren'Py falls back to the original
        ## English text â€” the picker is safe to use either way.
        frame:
            xfill True
            background Solid("#171C30")
            padding (24, 22)

            vbox:
                spacing 18

                text t("LANGUAGES"):
                    color "#7A8A99"
                    size 18
                    bold True

                text t("Choose the language used across menus and dialogue."):
                    color "#7A8A99"
                    size 15

                hbox:
                    spacing 14
                    xfill True

                    textbutton t("English"):
                        style "shell_nav_button"
                        xsize 312
                        selected current_translation_language() is None
                        action language_change_action(None)

                    textbutton t("Nederlands"):
                        style "shell_nav_button"
                        xsize 312
                        selected current_translation_language() == "dutch"
                        action language_change_action("dutch")

                    textbutton t("FranÃ§ais"):
                        style "shell_nav_button"
                        xsize 312
                        selected current_translation_language() == "french"
                        action language_change_action("french")

                    textbutton t("УкраїнÑька"):
                        style "shell_nav_button"
                        xsize 312
                        selected current_translation_language() == "ukrainian"
                        action language_change_action("ukrainian")


screen history():
    tag menu
    predict False

    use game_menu(t("History"), scroll="viewport", spacing=14):
        if _history_list:
            for h in _history_list:
                frame:
                    xfill True
                    background Solid("#171C30")
                    padding (22, 18)

                    vbox:
                        spacing 8

                        if h.who:
                            if "color" in h.who_args:
                                text t(h.who):
                                    color h.who_args["color"]
                                    size 20
                                    bold True
                                    substitute False
                            else:
                                text t(h.who):
                                    color "#7A8A99"
                                    size 20
                                    bold True
                                    substitute False

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text trich(what):
                            color "#E8E8E8"
                            size 19
                            substitute False
        else:
            frame:
                xfill True
                background Solid("#171C30")
                padding (28, 22)
                text t("The dialogue history is empty."):
                    color "#7A8A99"
                    size 20


define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


screen help():
    tag menu
    default device = "keyboard"

    use game_menu(t("Help"), scroll="viewport", spacing=18):
        hbox:
            spacing 12

            textbutton t("Keyboard"):
                style "shell_nav_button"
                xsize 190
                action SetScreenVariable("device", "keyboard")

            textbutton t("Mouse"):
                style "shell_nav_button"
                xsize 190
                action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton t("Gamepad"):
                    style "shell_nav_button"
                    xsize 190
                    action SetScreenVariable("device", "gamepad")

        frame:
            xfill True
            background Solid("#171C30")
            padding (24, 22)

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            else:
                use gamepad_help


screen keyboard_help():
    vbox:
        spacing 12

        for key_name, desc in [
            (t("Enter"), t("Advances dialogue and activates the interface.")),
            (t("Space"), t("Advances dialogue without selecting choices.")),
            (t("Arrow Keys"), t("Navigate the interface.")),
            (t("Escape"), t("Opens the custom mission control menu.")),
            (t("Ctrl"), t("Skips dialogue while held down.")),
            (t("Tab"), t("Toggles dialogue skipping.")),
            (t("Page Up"), t("Rolls back to earlier dialogue.")),
            (t("Page Down"), t("Rolls forward to later dialogue.")),
            ("H", t("Hides the user interface.")),
            ("S", t("Takes a screenshot.")),
            ("V", t("Toggles self-voicing.")),
            (t("Shift+A"), t("Opens the accessibility menu.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#7A8A99"
                    size 20
                    bold True
                    xsize 220

                text desc:
                    color "#E8E8E8"
                    size 19
                    xfill True


screen mouse_help():
    vbox:
        spacing 12

        for key_name, desc in [
            (t("Left Click"), t("Advances dialogue and activates the interface.")),
            (t("Middle Click"), t("Hides the user interface.")),
            (t("Right Click"), t("Opens the custom mission control menu.")),
            (t("Wheel Up"), t("Rolls back to earlier dialogue.")),
            (t("Wheel Down"), t("Rolls forward to later dialogue.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#7A8A99"
                    size 20
                    bold True
                    xsize 220

                text desc:
                    color "#E8E8E8"
                    size 19
                    xfill True


screen gamepad_help():
    vbox:
        spacing 12

        for key_name, desc in [
            (t("A / Bottom Button"), t("Advances dialogue and activates the interface.")),
            (t("Left Trigger"), t("Rolls back to earlier dialogue.")),
            (t("Right Shoulder"), t("Rolls forward to later dialogue.")),
            (t("D-Pad / Sticks"), t("Navigate the interface.")),
            (t("Start / B"), t("Opens the custom mission control menu.")),
            (t("Y / Top Button"), t("Hides the user interface.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#7A8A99"
                    size 20
                    bold True
                    xsize 320

                text desc:
                    color "#E8E8E8"
                    size 19
                    xfill True

        textbutton t("Calibrate"):
            style "shell_nav_button"
            xsize 220
            action GamepadCalibrate()


################################################################################
## Utility Screens
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    use ui_backdrop
    add "logo_watermark"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 860
        background Solid("#0E1321F2")
        padding (32, 28)

        vbox:
            spacing 22
            xalign 0.5

            text t(message):
                color "#E8E8E8"
                size 28
                bold True
                xalign 0.5
                text_align 0.5
                xmaximum 720
                substitute False

            hbox:
                spacing 14
                xalign 0.5

                textbutton t("Yes"):
                    style "modal_action_button"
                    xsize 220
                    action yes_action

                textbutton t("No"):
                    style "modal_action_button"
                    xsize 220
                    background Solid("#171C30")
                    hover_background Solid("#3A4A55")
                    action no_action

    key "game_menu" action no_action


screen skip_indicator():
    zorder 100

    frame:
        xpos 28
        ypos 24
        background Solid("#0E1321E6")
        padding (16, 10)

        hbox:
            spacing 8
            text t("Skipping"):
                color "#E8E8E8"
                size 18
            text t(">>"):
                color "#7A8A99"
                size 18


screen notify(message):
    zorder 300

    frame:
        xalign 1.0
        yalign 0.0
        xoffset -26
        yoffset 28
        background Solid("#0E1321E6")
        padding (16, 12)

        text t("[message!tq]"):
            color "#E8E8E8"
            size 18

    timer 3.25 action Hide("notify")


################################################################################
## NVL / Bubble
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Solid("#0E1321F0")
    padding (24, 24, 24, 24)

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign

style nvl_button:
    background Solid("#0D1117")
    hover_background Solid("#003A3A")
    left_padding 18
    right_padding 18
    top_padding 12
    bottom_padding 12
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    color "#E8E8E8"
    size 22


screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc


style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left": {
        "window_background": Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding": 27,
    },
    "bottom_right": {
        "window_background": Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding": 27,
    },
    "top_left": {
        "window_background": Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding": 27,
    },
    "top_right": {
        "window_background": Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding": 27,
    },
    "thought": {
        "window_background": bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left": (0, 0, 0, 22),
    "bottom_right": (0, 0, 0, 22),
    "top_left": (0, 22, 0, 0),
    "top_right": (0, 22, 0, 0),
    "thought": (0, 0, 0, 0),
}


################################################################################
## Mobile Variants
################################################################################

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu and not main_menu:
        hbox:
            xalign 0.5
            yalign 1.0
            yoffset -18
            spacing 10
            style_prefix "quick"

            textbutton t("Back") action Rollback()
            textbutton t("Notes") action Show("notebook_panel")
            textbutton t("Save") action ShowMenu("save")
            textbutton t("Menu") action ShowMenu("pause_hub")
