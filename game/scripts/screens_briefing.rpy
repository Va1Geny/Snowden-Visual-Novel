init python:

    FONT_MONO  = "fonts/ShareTechMono-Regular.ttf"
    FONT_BODY  = "fonts/Rajdhani-Regular.ttf"

    BG_DEEP    = "#080C10"
    BG_PANEL   = "#0D1117"
    CYAN       = "#00FFD1"
    RED        = "#FF2D55"
    GOLD       = "#FFD700"
    GREEN      = "#00FF88"
    TEXT_PRIMARY = "#E8E8E8"
    TEXT_DIM     = "#7A8A99"

    if not renpy.loadable(FONT_MONO): FONT_MONO = "DejaVuSans.ttf"
    if not renpy.loadable(FONT_BODY): FONT_BODY = "DejaVuSans.ttf"

    if not "ScanlineOverlay" in globals():
        class ScanlineOverlay(renpy.Displayable):
            def __init__(self, **kwargs):
                super(ScanlineOverlay, self).__init__(**kwargs)
            def render(self, width, height, st, at):
                rv = renpy.Render(width, height)
                return rv

transform trans_fade_in(t):
    alpha 0.0
    linear t alpha 1.0

transform trans_expand_x(t):
    xzoom 0.0
    linear t xzoom 1.0

transform trans_slide_fade(xoff, end_xoff, t):
    xoffset xoff
    alpha 0.0
    parallel:
        easeout t xoffset end_xoff
    parallel:
        linear t alpha 1.0

style transition_btn is button:
    background Solid("#003A3A")
    hover_background Solid("#00FFD1")
    padding (40, 16)
    xsize 360
    xalign 0.5

style transition_btn_text is button_text:
    font FONT_MONO
    size 18
    color "#00FFD1"
    hover_color "#0D1117"
    xalign 0.5
    text_align 0.5
    bold True

style transition_btn_left is transition_btn:
    xalign 0.0

style transition_btn_left_text is transition_btn_text:
    xalign 0.5

screen CornerBrackets(screen_w, screen_h, bracket_size, c_color, margin):

    add Solid(c_color) xpos margin ypos margin xsize bracket_size ysize 1
    add Solid(c_color) xpos margin ypos margin xsize 1 ysize bracket_size

    add Solid(c_color) xpos screen_w-margin-bracket_size ypos margin xsize bracket_size ysize 1
    add Solid(c_color) xpos screen_w-margin-1 ypos margin xsize 1 ysize bracket_size

    add Solid(c_color) xpos margin ypos screen_h-margin-1 xsize bracket_size ysize 1
    add Solid(c_color) xpos margin ypos screen_h-margin-bracket_size xsize 1 ysize bracket_size

    add Solid(c_color) xpos screen_w-margin-bracket_size ypos screen_h-margin-1 xsize bracket_size ysize 1
    add Solid(c_color) xpos screen_w-margin-1 ypos screen_h-margin-bracket_size xsize 1 ysize bracket_size

screen DifficultyBar(level, max_level=5):
    hbox:
        spacing 4
        for i in range(max_level):
            if i < level:
                $ c = GREEN if level <= 2 else GOLD if level == 3 else "#FF8C00" if level == 4 else RED
                add Solid(c) xsize 28 ysize 10
            else:
                add Solid("#1A2A3A") xsize 28 ysize 10

screen chapter_transition(chapter_num, codename, location, date, time_str, clearance, description, status, bg_image):
    default t_bg = renpy.variant("reduces_motion")
    default t_deco = renpy.variant("reduces_motion")
    default t_chap = renpy.variant("reduces_motion")
    default t_div_top = renpy.variant("reduces_motion")
    default t_typing = renpy.variant("reduces_motion")
    default typing_idx = len(codename) if renpy.variant("reduces_motion") else 0
    default t_div_bot = renpy.variant("reduces_motion")
    default t_meta = renpy.variant("reduces_motion")
    default t_desc = renpy.variant("reduces_motion")
    default t_btn = renpy.variant("reduces_motion")

    if not renpy.variant("reduces_motion"):
        timer 0.01 action [SetScreenVariable("t_bg", True), Play("audio", "audio/sfx/transition.wav")]
        timer 0.3 action SetScreenVariable("t_deco", True)
        timer 0.5 action SetScreenVariable("t_chap", True)
        timer 0.6 action SetScreenVariable("t_div_top", True)
        timer 0.8 action SetScreenVariable("t_typing", True)

        if t_typing:
            if typing_idx < len(codename):
                timer 0.06 action [SetScreenVariable("typing_idx", typing_idx + 1), Play("audio", "audio/sfx/click_single.wav")] repeat True
            else:
                if not t_div_bot:
                    timer 0.01 action SetScreenVariable("t_div_bot", True)

        if t_div_bot:
            timer 0.3 action SetScreenVariable("t_meta", True)
            timer 0.5 action SetScreenVariable("t_desc", True)
            timer 0.7 action SetScreenVariable("t_btn", True)

    if t_bg:
        fixed:
            at trans_fade_in(0.6)
            add bg_image
            add Solid("#000000B8")
            add ScanlineOverlay()

    if t_deco:
        fixed:
            at trans_fade_in(0.4)
            text t("CLASSIFIED // TS/SCI // [codename]"):
                font FONT_MONO
                size 12
                color "#3A4A55"
                xpos 48
                yalign 0.5
                at transform:
                    rotate -90
            text t("[date] // SRN // EYES ONLY"):
                font FONT_MONO
                size 12
                color "#3A4A55"
                xalign 1.0
                xoffset -48
                yalign 0.5
                at transform:
                    rotate 90

            add Solid("#00FFD133") xsize 1920 ysize 1 ypos 80
            add Solid("#00FFD133") xsize 1920 ysize 1 ypos 1000

            use CornerBrackets(1920, 1080, 40, "#00FFD166", 24)

    vbox:
        xalign 0.5
        yalign 0.48
        xsize 900
        spacing 24

        if t_chap:
            hbox:
                xalign 0.5
                spacing 40
                at trans_fade_in(0.2)
                text t("CHAPTER %02d" % int(chapter_num)):
                    font FONT_MONO
                    size 14
                    color TEXT_DIM
                    yalign 0.5

                frame:
                    yalign 0.5
                    padding (10, 4)
                    if status == "ACTIVE":
                        background Solid("#00FF8822")
                    elif status == "CLASSIFIED":
                        background Solid("#FFD70022")
                    else:
                        background Solid("#3A4A5522")

                    text t(status):
                        font FONT_MONO
                        size 12
                        bold True
                        if status == "ACTIVE":
                            color GREEN
                        elif status == "CLASSIFIED":
                            color GOLD
                        else:
                            color TEXT_DIM
        else:
            null height 30

        if t_div_top:
            add Solid("#00FFD133"):
                ysize 1
                xsize 600
                xalign 0.5
                at trans_expand_x(0.4)
        else:
            null height 1

        if t_typing:
            text t(codename[:typing_idx] + ("_" if typing_idx < len(codename) else "")):
                font FONT_MONO
                size 42
                color TEXT_PRIMARY
                bold True
                xalign 0.5
        else:
            null height 50

        if t_div_bot:
            add Solid("#00FFD133"):
                ysize 1
                xsize 600
                xalign 0.5
                at trans_expand_x(0.4)
        else:
            null height 1

        if t_meta:
            hbox:
                spacing 120
                xalign 0.5
                at trans_fade_in(0.3)

                vbox:
                    spacing 16
                    vbox:
                        text t("LOCATION"):
                            font FONT_MONO
                            size 12
                            color TEXT_DIM
                            xalign 0.5 text_align 0.5
                        text t(location):
                            font FONT_MONO
                            size 16
                            color TEXT_PRIMARY
                            xalign 0.5 text_align 0.5
                    vbox:
                        text t("TIME"):
                            font FONT_MONO
                            size 12
                            color TEXT_DIM
                            xalign 0.5 text_align 0.5
                        text t(time_str):
                            font FONT_MONO
                            size 16
                            color TEXT_PRIMARY
                            xalign 0.5 text_align 0.5

                vbox:
                    spacing 16
                    vbox:
                        text t("DATE"):
                            font FONT_MONO
                            size 12
                            color TEXT_DIM
                            xalign 0.5 text_align 0.5
                        text t(date):
                            font FONT_MONO
                            size 16
                            color TEXT_PRIMARY
                            xalign 0.5 text_align 0.5
                    vbox:
                        text t("CLEARANCE"):
                            font FONT_MONO
                            size 12
                            color TEXT_DIM
                            xalign 0.5 text_align 0.5
                        text t(clearance):
                            font FONT_MONO
                            size 16
                            color CYAN
                            xalign 0.5 text_align 0.5
        else:
            null height 100

        if t_desc:
            text t(description):
                font FONT_BODY
                size 17
                color TEXT_DIM
                line_leading 8
                xsize 780
                xalign 0.5
                text_align 0.5
                at trans_fade_in(0.3)
        else:
            null height 80

        if t_btn:
            textbutton t("[[ ENTER CHAPTER ]"):
                style "transition_btn"
                action Return()
                at trans_fade_in(0.3)
        else:
            null height 60

screen minigame_briefing(challenge_title, subtitle, mission_id, classification, challenge_type, estimated_time, difficulty, difficulty_label, succeed_reward, fail_penalty, learn_concept, briefing_text, controls):
    modal True
    on "show" action [SetVariable("quick_menu", False), SetVariable("show_hud", False)]
    on "hide" action [SetVariable("quick_menu", True), SetVariable("show_hud", True)]

    default t_left = renpy.variant("reduces_motion")
    default t_right = renpy.variant("reduces_motion")
    default t_content = renpy.variant("reduces_motion")
    default t_typing = renpy.variant("reduces_motion")
    default typing_idx = len(challenge_title) if renpy.variant("reduces_motion") else 0
    default t_sub = renpy.variant("reduces_motion")
    default t_brief = renpy.variant("reduces_motion")
    default t_btn = renpy.variant("reduces_motion")

    if not renpy.variant("reduces_motion"):
        timer 0.1 action SetScreenVariable("t_left", True)
        timer 0.2 action SetScreenVariable("t_right", True)
        timer 0.45 action SetScreenVariable("t_content", True)
        timer 0.5 action SetScreenVariable("t_typing", True)

        if t_typing:
            if typing_idx < len(challenge_title):
                timer 0.06 action [SetScreenVariable("typing_idx", typing_idx + 1), Play("audio", "audio/sfx/click_single.wav")] repeat True
            else:
                if not t_sub:
                    timer 0.01 action SetScreenVariable("t_sub", True)

        if t_sub:
            timer 0.2 action SetScreenVariable("t_brief", True)
            timer 0.5 action SetScreenVariable("t_btn", True)

    add Solid(BG_DEEP)
    add ScanlineOverlay()

    if t_left or t_right:
        add Solid("#00FFD126") xpos 750 ypos 0 xsize 1 ysize 1080

    if t_left:
        frame:
            xsize 560
            xpos 160
            yalign 0.5
            background Solid(BG_PANEL)
            padding (32, 28)
            at trans_slide_fade(-40, 0, 0.35)

            vbox:
                spacing 0
                add Solid(CYAN) xsize 496 ysize 2
                null height 8
                text t("// CHALLENGE INITIATED //"):
                    font FONT_MONO
                    size 13
                    color CYAN
                null height 16

                if t_content:
                    vbox:
                        spacing 12
                        at trans_fade_in(0.2)

                        vbox:
                            text t("MISSION ID"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(mission_id):
                                font FONT_MONO
                                size 15
                                color TEXT_PRIMARY

                        vbox:
                            text t("CLASSIFICATION"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(classification):
                                font FONT_MONO
                                size 15
                                color CYAN

                        vbox:
                            text t("CHALLENGE TYPE"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(challenge_type):
                                font FONT_MONO
                                size 15
                                color TEXT_PRIMARY

                        vbox:
                            text t("ESTIMATED TIME"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(estimated_time):
                                font FONT_MONO
                                size 15
                                color TEXT_PRIMARY

                        vbox:
                            text t("DIFFICULTY"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            use DifficultyBar(difficulty)
                            text t(difficulty_label):
                                font FONT_MONO
                                size 13
                                color (GREEN if difficulty <=2 else GOLD if difficulty==3 else "#FF8C00" if difficulty==4 else RED)

                        null height 8
                        add Solid("#3A4A55") xsize 496 ysize 1
                        null height 8

                        vbox:
                            text t("IF YOU SUCCEED"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(succeed_reward):
                                font FONT_MONO
                                size 14
                                color GREEN
                            null height 8
                            text t("IF YOU FAIL"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(fail_penalty):
                                font FONT_MONO
                                size 14
                                color RED

                        null height 8
                        add Solid("#1A2A3A") xsize 496 ysize 1
                        null height 8

                        vbox:
                            text t("YOU WILL LEARN"):
                                font FONT_MONO
                                size 11
                                color TEXT_DIM
                            text t(learn_concept):
                                font FONT_BODY
                                size 15
                                color TEXT_DIM
                                line_leading 6

    if t_right:
        frame:
            xsize 920
            xpos 780
            yalign 0.5
            background Solid("#111720")
            padding (40, 32)
            at trans_slide_fade(40, 0, 0.35)

            vbox:
                spacing 0
                add Solid(GOLD) xsize 840 ysize 2
                null height 16

                if t_typing:
                    text t(challenge_title[:typing_idx] + ("_" if typing_idx < len(challenge_title) else "")):
                        font FONT_MONO
                        size 36
                        color TEXT_PRIMARY
                        bold True
                else:
                    null height 40

                null height 8

                if t_sub:
                    text t(subtitle):
                        font FONT_BODY
                        size 18
                        color TEXT_DIM
                        italic True
                        at trans_fade_in(0.2)
                else:
                    null height 22

                null height 24

                if t_sub:
                    add Solid("#3A4A55") xsize 840 ysize 1
                else:
                    null height 1

                null height 24

                if t_sub:
                    text t("M I S S I O N   B R I E F I N G"):
                        font FONT_MONO
                        size 13
                        color GOLD
                else:
                    null height 18

                null height 16

                if t_brief:
                    text t(briefing_text):
                        font FONT_BODY
                        size 17
                        color TEXT_PRIMARY
                        line_leading 10
                        xfill True
                        at trans_fade_in(0.4)
                else:
                    null height 200

                null height 24

                if t_brief:
                    add Solid("#1A2A3A") xsize 840 ysize 1
                else:
                    null height 1

                null height 20

                if t_btn:
                    hbox:
                        spacing 32
                        at trans_fade_in(0.3)
                        for k, desc in controls:
                            hbox:
                                spacing 8
                                text t("[[ [k] ]"):
                                    font FONT_MONO
                                    size 14
                                    color GOLD
                                text t(desc):
                                    font FONT_MONO
                                    size 14
                                    color TEXT_DIM

                    null height 32

                    hbox:
                        spacing 20
                        at trans_fade_in(0.3)

                        textbutton t("[[ BEGIN CHALLENGE ]"):
                            xsize 340
                            style "transition_btn_left"
                            action Return()

                        textbutton t("[[ SKIP MINIGAME ]"):
                            xsize 340
                            style "transition_btn_left"
                            text_color "#ff4444"
                            text_hover_color "#ff0000"
                            action Return(False)

    use block_shortcuts_and_skip(False, show_skip_button=False)
