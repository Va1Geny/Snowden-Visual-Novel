init python:
    tiq_current_answer = ""
    tiq_show_result    = False
    tiq_is_correct     = False
    tiq_attempts       = 0
    tiq_max_chars      = 20

    def tiq_reset():
        store.tiq_current_answer = ""
        store.tiq_show_result    = False
        store.tiq_is_correct     = False
        store.tiq_attempts       = 0

    def tiq_add_char(ch):
        if len(store.tiq_current_answer) < store.tiq_max_chars:
            store.tiq_current_answer += ch
            renpy.restart_interaction()

    def tiq_delete_char():
        store.tiq_current_answer = store.tiq_current_answer[:-1]
        renpy.restart_interaction()

    def tiq_add_space():
        if len(store.tiq_current_answer) < store.tiq_max_chars:
            store.tiq_current_answer += " "
            renpy.restart_interaction()

    def tiq_check_answer(correct_answer):
        store.tiq_attempts += 1
        if store.tiq_current_answer.strip().upper() == correct_answer.strip().upper():
            store.tiq_is_correct = True
        else:
            store.tiq_is_correct = False
        store.tiq_show_result = True
        renpy.restart_interaction()

    def tiq_retry():
        store.tiq_current_answer = ""
        store.tiq_show_result = False
        store.tiq_is_correct = False
        renpy.restart_interaction()

    class VerticalGradient(renpy.Displayable):
        def __init__(self, width, height, top_color, bottom_color, **kw):
            super(VerticalGradient, self).__init__(**kw)
            self.g_width = int(width)
            self.g_height = int(height)
            self.top_color = top_color
            self.bottom_color = bottom_color
        def render(self, width, height, st, at):
            r = renpy.Render(self.g_width, self.g_height)
            c = r.canvas()
            tr, tg, tb, ta = self.top_color
            br, bg, bb, ba = self.bottom_color
            for y in range(self.g_height):
                f = y / float(max(self.g_height - 1, 1))
                c.line((int(tr+(br-tr)*f), int(tg+(bg-tg)*f), int(tb+(bb-tb)*f), int(ta+(ba-ta)*f)), (0, y), (self.g_width, y))
            return r
        def visit(self):
            return []

transform blink_cursor:
    block:
        alpha 1.0
        0.4
        alpha 0.0
        0.4
        repeat

transform pulse_dot:
    block:
        alpha 1.0
        linear 0.6 alpha 0.4
        linear 0.6 alpha 1.0
        repeat

transform fade_in_card:
    alpha 0.0
    linear 0.25 alpha 1.0

screen text_input_question(chapter_num="01", chapter_name="Mission", question_text="", hint_text="", check_type="Text Input", difficulty="Easy", reward_label="+1 Knowledge", reward_color="green", correct_answer="", explanation="", allow_skip=True):
    modal True

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "screenshot" action NullAction()

    $ store.tiq_max_chars = len(correct_answer)
    $ _rc = {"green": "#00FF88", "cyan": "#00FFD1", "gold": "#FFD700"}.get(reward_color, "#00FFD1")
    $ _dc = {"Easy": "#00FF88", "Medium": "#FFD700", "Hard": "#FF2D55"}.get(difficulty, "#7A8A99")
    $ _typed_set = set(tiq_current_answer.upper())
    $ _progress = min(1.0, len(tiq_current_answer) / float(max(len(correct_answer), 1)))
    $ _bar_w = int(480 * _progress)
    $ _panel_width = 1380
    $ _panel_height = 744
    $ _left_panel_width = 460
    $ _right_panel_width = 919
    $ _keyboard_gap = 8
    $ _keyboard_unit = int((_right_panel_width - 80 - (_keyboard_gap * 9)) / 10.0)
    $ _keyboard_rows = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O"], ["A", "S", "D", "F", "G", "H", "J", "K", "L"], ["P", "Z", "X", "C", "V", "B", "N", "M"]]

    if not tiq_show_result:
        for _k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            key "K_" + _k.lower() action Function(tiq_add_char, _k)
            key ["shift_K_" + _k.lower()] action Function(tiq_add_char, _k)
        for _n in "0123456789":
            key "K_" + _n action Function(tiq_add_char, _n)
        key "K_SPACE" action Function(tiq_add_space)
        key "K_BACKSPACE" action Function(tiq_delete_char)
        key "K_RETURN" action Function(tiq_check_answer, correct_answer)
        key "K_KP_ENTER" action Function(tiq_check_answer, correct_answer)
    elif tiq_show_result and tiq_is_correct:
        key "K_RETURN" action Return("continue")
        key "K_KP_ENTER" action Return("continue")

    add Solid("#040810", xysize=(1920, 1080))

    add Solid("#001E3208", xysize=(1200, 800)) xalign 0.5 yalign 0.5
    add Solid("#001E3212", xysize=(800, 500)) xalign 0.5 yalign 0.5

    add ScanlineOverlay(1920, 1080)

    frame:
        xalign 0.5
        ypos 188
        xsize 1100
        ysize 24
        background None
        hbox:
            spacing 28
            xalign 0.0

            vbox:
                spacing 2
                text t("INPUT - IN PROGRESS"):
                    font "fonts/ShareTechMono-Regular.ttf"
                    size 9
                    color "#00FFD1"
                if not tiq_show_result:
                    frame:
                        xsize 140
                        ysize 2
                        background "#00FFD1"
                elif tiq_is_correct:
                    frame:
                        xsize 140
                        ysize 2
                        background "#00FF88"
                else:
                    frame:
                        xsize 140
                        ysize 2
                        background "#FF2D55"
            vbox:
                spacing 2
                text t("INPUT > CORRECT"):
                    font "fonts/ShareTechMono-Regular.ttf"
                    size 9
                    color "#2A3A45"
                frame:
                    xsize 110
                    ysize 1
                    background None
            vbox:
                spacing 2
                text t("INPUT > EXTRA"):
                    font "fonts/ShareTechMono-Regular.ttf"
                    size 9
                    color "#2A3A45"
                frame:
                    xsize 100
                    ysize 1
                    background None

    frame:
        xalign 0.5 yalign 0.5
        xsize (_panel_width + 8) ysize (_panel_height + 8)
        background Solid("#00FFD108")
        padding (0,0)
    frame:
        xalign 0.5 yalign 0.5
        xsize (_panel_width + 4) ysize (_panel_height + 4)
        background Solid("#00FFD112")
        padding (0,0)

    frame:
        xalign 0.5
        ypos 208
        xsize 1100 ysize 1
        background "#00FFD150"
    frame:
        xalign 0.5
        ypos 209
        xsize 800 ysize 4
        background "#00FFD108"

    frame:
        xalign 0.5 yalign 0.5
        xsize _panel_width ysize _panel_height
        background Solid("#06090F")
        padding (0, 0)
        hbox:
            spacing 0

            frame:
                xsize _left_panel_width
                ysize _panel_height
                background Solid("#080F1A")
                padding (44, 44)

                frame:
                    xpos 20 ypos 20
                    xsize 40 ysize 1
                    background "#00FFD130"
                frame:
                    xpos 20 ypos 20
                    xsize 1 ysize 40
                    background "#00FFD130"

                vbox:
                    spacing 0
                    xalign 0.0
                    yalign 0.5

                    hbox:
                        spacing 10
                        xalign 0.0
                        frame:
                            yalign 0.5
                            xsize 28 ysize 1
                            background "#00FFD1B0"
                        text t("CHAPTER [chapter_num] - [chapter_name]"):
                            font "fonts/ShareTechMono-Regular.ttf"
                            size 10
                            color "#00FFD1C0"
                            yalign 0.5

                    null height 8

                    text t("// MISSION QUESTION"):
                        font "fonts/ShareTechMono-Regular.ttf"
                        size 9
                        color "#00FFD130"
                        xalign 0.0

                    null height 6

                    text t(question_text):
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 21
                        color "#E8E8E8"
                        text_align 0.0
                        xalign 0.0
                        xmaximum 370
                        line_spacing 8

                    null height 16

                    if hint_text:
                        frame:
                            xalign 0.0
                            xmaximum 370
                            ysize 85
                            background Solid("#00FFD103")
                            padding (0, 0)
                            hbox:
                                spacing 0

                                frame:
                                    xsize 2 yfill True
                                    background "#00FFD155"

                                frame:
                                    background Solid("#00FFD106")
                                    padding (14, 12)
                                    xfill True yfill True
                                    vbox:
                                        spacing 6
                                        hbox:
                                            spacing 6
                                            xalign 0.0
                                            text t("{font=fonts/ShareTechMono-Regular.ttf}{size=10}{color=#00FFD180}FIELD HINT{/color}{/size}{/font}"):
                                                yalign 0.5
                                        text t(hint_text):
                                            font "fonts/Rajdhani-Regular.ttf"
                                            size 15
                                            italic True
                                            color "#00FFD18C"
                                            text_align 0.0
                                            xalign 0.0
                                            line_spacing 5

                        null height 16

                    hbox:
                        spacing 8
                        xalign 0.0

                        vbox:
                            spacing 8

                            frame:
                                xsize 164
                                background Solid("#ffffff06")
                                padding (1, 1, 1, 1)
                                frame:
                                    background Solid("#080F1A")
                                    padding (12, 10)
                                    xfill True
                                    vbox:
                                        spacing 4
                                        text t("CHECK TYPE"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 9
                                            color "#2A3A45"
                                        text t(check_type):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 14
                                            color "#00FFD1"

                            frame:
                                xsize 164
                                background Solid("#ffffff06")
                                padding (1, 1, 1, 1)
                                frame:
                                    background Solid("#080F1A")
                                    padding (12, 10)
                                    xfill True
                                    vbox:
                                        spacing 4
                                        text t("REWARD"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 9
                                            color "#2A3A45"
                                        text t(reward_label):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 14
                                            color _rc

                        vbox:
                            spacing 8

                            frame:
                                xsize 164
                                background Solid("#ffffff06")
                                padding (1, 1, 1, 1)
                                frame:
                                    background Solid("#080F1A")
                                    padding (12, 10)
                                    xfill True
                                    vbox:
                                        spacing 4
                                        text t("DIFFICULTY"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 9
                                            color "#2A3A45"
                                        text t(difficulty):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 14
                                            color "#7A8A99"

                            frame:
                                xsize 164
                                background Solid("#ffffff06")
                                padding (1, 1, 1, 1)
                                frame:
                                    background Solid("#080F1A")
                                    padding (12, 10)
                                    xfill True
                                    vbox:
                                        spacing 4
                                        text t("ATTEMPTS"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 9
                                            color "#2A3A45"
                                        text t("Unlimited"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 14
                                            color "#7A8A99"

                    null height 14

                    if tiq_attempts > 0:
                        frame:
                            xalign 0.0
                            background None
                            hbox:
                                spacing 6
                                xalign 0.0
                                for _d in range(5):
                                    frame:
                                        xsize 8 ysize 8
                                        if _d < tiq_attempts:
                                            background "#00FFD1"
                                            at pulse_dot
                                        else:
                                            background "#00FFD118"
                                null width 8
                                text t("[tiq_attempts] attempts used"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 10
                                    color "#2A3A45"
                                    yalign 0.5

            frame:
                xsize 1 ysize _panel_height
                background "#00FFD115"

            frame:
                xsize _right_panel_width ysize _panel_height
                background Solid("#06090F")
                padding (40, 32, 40, 24)

                vbox:
                    spacing 0
                    xalign 0.0

                    hbox:
                        xfill True
                        text t("// ENTER ANSWER"):
                            font "fonts/ShareTechMono-Regular.ttf"
                            size 10
                            color "#7A8A99"
                            yalign 0.5
                        hbox:
                            spacing 6
                            xalign 1.0
                            yalign 0.5
                            if not tiq_show_result:
                                frame:
                                    xsize 5 ysize 5
                                    background "#00FFD1"
                                    yalign 0.5
                                    at pulse_dot
                                text t("INPUT ACTIVE"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 9
                                    color "#00FFD160"
                                    yalign 0.5
                            elif tiq_is_correct:
                                frame:
                                    xsize 5 ysize 5
                                    background "#00FF88"
                                    yalign 0.5
                                text t("MATCH FOUND"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 9
                                    color "#00FF8899"
                                    yalign 0.5
                            else:
                                frame:
                                    xsize 5 ysize 5
                                    background "#FF2D55"
                                    yalign 0.5
                                    at pulse_dot
                                text t("MISMATCH"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 9
                                    color "#FF2D5599"
                                    yalign 0.5

                    null height 18

                    hbox:
                        spacing 6
                        xalign 0.0
                        for _i in range(max(len(correct_answer), len(tiq_current_answer), 1)):
                            if _i < len(tiq_current_answer):

                                frame:
                                    xsize 40 ysize 52
                                    if tiq_show_result and tiq_is_correct:
                                        background Solid("#00FF8830")
                                    elif tiq_show_result and not tiq_is_correct:
                                        background Solid("#FF2D5525")
                                    else:
                                        background Solid("#00FFD115")
                                    padding (1, 1, 1, 2)
                                    frame:
                                        xfill True yfill True
                                        if tiq_show_result and tiq_is_correct:
                                            background Solid("#00FF8808")
                                        elif tiq_show_result and not tiq_is_correct:
                                            background Solid("#FF2D5506")
                                        else:
                                            background Solid("#00FFD106")
                                        text tiq_current_answer[_i]:
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 22
                                            if tiq_show_result and tiq_is_correct:
                                                color "#00FF88"
                                            elif tiq_show_result and not tiq_is_correct:
                                                color "#FF2D55"
                                            else:
                                                color "#E8E8E8"
                                            xalign 0.5 yalign 0.5
                            elif _i == len(tiq_current_answer) and not tiq_show_result:

                                frame:
                                    xsize 40 ysize 52
                                    background Solid("#ffffff08")
                                    padding (1, 1, 1, 2)
                                    frame:
                                        xfill True yfill True
                                        background Solid("#ffffff02")
                                        frame:
                                            xalign 0.5 yalign 0.5
                                            xsize 2 ysize 34
                                            background "#00FFD1"
                                            at blink_cursor
                            else:

                                frame:
                                    xsize 40 ysize 52
                                    background Solid("#ffffff08")
                                    padding (1, 1, 1, 2)
                                    frame:
                                        xfill True yfill True
                                        background Solid("#ffffff02")

                    null height 14

                    hbox:
                        spacing 0
                        if _bar_w > 0:
                            frame:
                                xsize _bar_w ysize 2
                                if tiq_show_result and tiq_is_correct:
                                    background "#00FF88"
                                elif tiq_show_result and not tiq_is_correct:
                                    background "#FF2D55"
                                else:
                                    background "#00FFD1"
                        if (480 - _bar_w) > 0:
                            frame:
                                xsize (480 - _bar_w) ysize 2
                                background "#00FFD107"

                    null height 16

                    if tiq_show_result and not tiq_is_correct:
                        frame:
                            xfill True
                            ysize 52
                            background Solid("#FF2D5504")
                            padding (0, 0)
                            at fade_in_card
                            hbox:
                                spacing 0
                                frame:
                                    xsize 3 yfill True
                                    background "#FF2D5599"
                                frame:
                                    background Solid("#FF2D5508")
                                    padding (14, 12)
                                    xfill True yfill True
                                    hbox:
                                        spacing 10
                                        text t("X"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 14 color "#FF2D55" bold True yalign 0.5
                                        text t("INCORRECT - TRY AGAIN"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 11 color "#FF2D55" yalign 0.5
                        null height 12

                    if not (tiq_show_result and tiq_is_correct):
                        for _row in _keyboard_rows:
                            hbox:
                                spacing _keyboard_gap
                                xalign 0.0
                                for _k in _row:
                                    button:
                                        xsize _keyboard_unit ysize 54
                                        if _k in _typed_set:
                                            background Solid("#00FFD122")
                                        else:
                                            background Solid("#ffffff07")
                                        hover_background Solid("#00FFD115")
                                        action Function(tiq_add_char, _k)
                                        padding (0, 0, 0, 2)
                                        text _k:
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 16
                                            if _k in _typed_set:
                                                color "#00FFD1"
                                            else:
                                                color "#7A8A99"
                                            hover_color "#00FFD1"
                                            xalign 0.5 yalign 0.5

                                if _row[0] == "P":
                                    button:
                                        xsize ((_keyboard_unit * 2) + _keyboard_gap) ysize 54
                                        background Solid("#FF2D5510")
                                        hover_background Solid("#FF2D5522")
                                        action Function(tiq_delete_char)
                                        padding (0, 0, 0, 2)
                                        text t("DEL"):
                                            font "fonts/ShareTechMono-Regular.ttf"
                                            size 13
                                            color "#FF2D55C0"
                                            hover_color "#FF2D55"
                                            xalign 0.5 yalign 0.5
                            null height 8

                        hbox:
                            spacing _keyboard_gap
                            xalign 0.0
                            button:
                                xsize ((_keyboard_unit * 3) + (_keyboard_gap * 2)) ysize 54
                                background Solid("#ffffff05")
                                hover_background Solid("#ffffff0A")
                                action Function(tiq_add_space)
                                text t("SPACE"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 13
                                    color "#2A3A45"
                                    hover_color "#7A8A99"
                                    xalign 0.5 yalign 0.5
                            if tiq_show_result and not tiq_is_correct:
                                button:
                                    xfill True ysize 44
                                    background Solid("#FF2D55CC")
                                    hover_background Solid("#FF2D55")
                                    action Function(tiq_retry)
                                    text t("RETRY >"):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 13
                                        color "#040810"
                                        bold True
                                        xalign 0.5 yalign 0.5
                            else:
                                button:
                                    xfill True ysize 44
                                    background Solid("#00FFD1")
                                    hover_background Solid("#33FFE0")
                                    action Function(tiq_check_answer, correct_answer)
                                    text t("SUBMIT >"):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 13
                                        color "#040810"
                                        bold True
                                        xalign 0.5 yalign 0.5

                    if tiq_show_result and tiq_is_correct:
                        frame:
                            xfill True
                            ysize 130
                            background Solid("#00FF8804")
                            padding (0, 0)
                            at fade_in_card
                            hbox:
                                spacing 0
                                frame:
                                    xsize 3 yfill True
                                    background "#00FF8899"
                                frame:
                                    background Solid("#00FF8808")
                                    padding (20, 18)
                                    xfill True yfill True
                                    vbox:
                                        spacing 12
                                        hbox:
                                            spacing 10
                                            text t("CORRECT - INTELLIGENCE CONFIRMED"):
                                                font "fonts/ShareTechMono-Regular.ttf"
                                                size 11
                                                color "#00FF88"
                                                bold True
                                                yalign 0.5
                                            frame:
                                                background Solid("#00FF8818")
                                                padding (8, 4)
                                                yalign 0.5
                                                text t(reward_label):
                                                    font "fonts/ShareTechMono-Regular.ttf"
                                                    size 10
                                                    color _rc
                                                    bold True
                                        frame:
                                            xfill True ysize 1
                                            background "#00FF8818"
                                        if explanation:
                                            text t(explanation):
                                                font "fonts/Rajdhani-Regular.ttf"
                                                size 16
                                                color "#7A8A99"
                                                text_align 0.5
                                                xalign 0.5
                                                xmaximum 440
                                                line_spacing 2

                    null height 12

                    hbox:
                        spacing 10
                        xalign 0.0
                        if allow_skip and not (tiq_show_result and tiq_is_correct):
                            button:
                                xsize 100 ysize 38
                                background Solid("#ffffff06")
                                hover_background Solid("#ffffff0F")
                                action Return("skip")
                                text t("SKIP"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 11
                                    color "#2A3A45"
                                    hover_color "#7A8A99"
                                    xalign 0.5 yalign 0.5
                        if tiq_show_result and tiq_is_correct:
                            button:
                                xsize 100 ysize 38
                                background Solid("#ffffff06")
                                hover_background Solid("#ffffff0F")
                                action Return("skip")
                                text t("SKIP"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 11
                                    color "#2A3A45"
                                    hover_color "#7A8A99"
                                    xalign 0.5 yalign 0.5
                            button:
                                xsize 220 ysize 38
                                background Solid("#00FFD1")
                                hover_background Solid("#33FFE0")
                                action Return("continue")
                                text t("CONTINUE MISSION >"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 11
                                    color "#040810"
                                    bold True
                                    xalign 0.5 yalign 0.5
