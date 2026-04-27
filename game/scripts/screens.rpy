################################################################################
## SCREENS.RPY — Unified UI System
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
    background Solid("#161A2B")

style bar:
    ysize gui.bar_size
    left_bar Solid("#008069")
    right_bar Solid("#232843")

style vbar:
    xsize gui.bar_size
    top_bar Solid("#008069")
    bottom_bar Solid("#232843")

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#232843")
    thumb Solid("#4D5186")

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#232843")
    thumb Solid("#4D5186")

style slider:
    ysize gui.slider_size
    base_bar Solid("#232843")
    thumb Solid("#8B8FCC")

style vslider:
    xsize gui.slider_size
    base_bar Solid("#232843")
    thumb Solid("#8B8FCC")

style shell_nav_button is button:
    xsize 320
    ysize 58
    left_padding 18
    right_padding 18
    background Solid("#1B2034")
    hover_background Solid("#006654")
    selected_background Solid("#002922")
    insensitive_background Solid("#141827")

style shell_nav_button_text is button_text:
    size 22
    color "#EAF4F1"
    hover_color "#F7FFFC"
    selected_color "#F7FFFC"
    insensitive_color "#6F769A"
    xalign 0.0

style modal_action_button is button:
    xsize 440
    ysize 66
    left_padding 22
    right_padding 22
    top_padding 4
    bottom_padding 4
    background Solid("#182033")
    hover_background Solid("#0B6E5F")
    selected_background Solid("#002922")

style modal_action_button_text is button_text:
    size 23
    bold True
    color "#EAF4F1"
    hover_color "#F7FFFC"
    xalign 0.0

style choice_button is button:
    xsize 1120
    yminimum 78
    left_padding 28
    right_padding 28
    top_padding 20
    bottom_padding 20
    background Solid("#182033")
    hover_background Solid("#0B6E5F")
    selected_background Solid("#002922")

style choice_button_text is button_text:
    size 28
    color "#EAF4F1"
    hover_color "#F7FFFC"
    xalign 0.5
    text_align 0.5

style quick_button is button:
    background Solid("#101523CC")
    hover_background Solid("#0B6E5F")
    left_padding 14
    right_padding 14
    top_padding 10
    bottom_padding 10

style quick_button_text is button_text:
    size 18
    color "#AAB0D6"
    hover_color "#F7FFFC"

style game_menu_scrollbar is vscrollbar
style game_menu_viewport is empty
style game_menu_label is label
style game_menu_label_text is label_text


################################################################################
## Shared UI Helpers
################################################################################

screen ui_backdrop():
    add "#131421"

    frame:
        xpos 42
        ypos 0
        xsize 2
        yfill True
        background "#006654"

    frame:
        xalign 1.0
        xoffset -42
        ypos 0
        xsize 2
        yfill True
        background "#4D5186"

    for i in range(24):
        text "01001101":
            color "#00806908"
            size 13
            xpos (i * 86 + 18)
            ypos ((i * 61 + 24) % 1080)


screen shell_header(kicker, title, body=None):
    frame:
        xpos 72
        ypos 54
        xsize 1776
        ysize 116
        background Solid("#0E1220EE")
        padding (34, 24)

        hbox:
            xfill True
            spacing 28

            vbox:
                spacing 4
                yalign 0.5

                text kicker:
                    color "#8B8FCC"
                    size 15
                    bold True

                text title:
                    color "#EAF4F1"
                    size 34
                    bold True

                if body:
                    text body:
                        color "#AAB0D6"
                        size 16
                        xmaximum 860

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
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
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
    background Solid("#002922")

style say_label:
    color "#F7FFFC"
    size 32
    bold True
    xalign 0.0

style say_dialogue:
    color "#EAF4F1"
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

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    color "#8B8FCC"
    size 26

style input:
    color "#F7FFFC"
    size 30
    xmaximum 1544


screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        ypos 310
        spacing 14

        for i in items:
            textbutton i.caption action i.action


################################################################################
## Quick Menu / HUD
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu and not main_menu:
        hbox:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 24
            spacing 8
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Prefs") action ShowMenu("preferences")


screen game_hud():
    zorder 90

    if show_hud:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 76
            xsize 260
            background Solid("#0F1423E6")
            padding (18, 16)

            vbox:
                spacing 10

                text "FIELD STATUS":
                    color "#8B8FCC"
                    size 14
                    bold True

                text "CHAPTER [current_chapter]/5":
                    color "#EAF4F1"
                    size 19
                    bold True

                hbox:
                    xfill True
                    text "Knowledge":
                        color "#AAB0D6"
                        size 16
                    text "[knowledge_score]":
                        color "#8B8FCC"
                        size 16
                        bold True
                        xalign 1.0

                hbox:
                    xfill True
                    text "Trust":
                        color "#AAB0D6"
                        size 16
                    text "[trust_score]":
                        color "#EAF4F1"
                        size 16
                        bold True
                        xalign 1.0

                text "Suspicion":
                    color "#AAB0D6"
                    size 16

                bar:
                    value suspicion_level
                    range 5
                    xsize 210
                    ysize 10
                    left_bar Solid("#8B8FCC")
                    right_bar Solid("#232843")


screen scene_stage_line():
    zorder 5

    if not main_menu and renpy.get_screen("say") and not renpy.get_screen("pause_hub"):
        add Solid("#02030466"):
            xpos 0
            ypos 822
            xsize 1920
            ysize 258

        add Solid("#8B8FCC22"):
            xpos 0
            ypos 816
            xsize 1920
            ysize 2

        add Solid("#00665433"):
            xpos 0
            ypos 804
            xsize 1920
            ysize 12


################################################################################
## Primary Menus
################################################################################

screen main_menu():
    tag menu

    use ui_backdrop
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 820
        background Solid("#0E1321EE")
        padding (54, 42)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            text "CLASSIFIED INTERFACE":
                color "#8B8FCC"
                size 16
                bold True
                xalign 0.5
                kerning 3

            fixed:
                xsize 920
                ysize 170

                text "ENEMY OF THE STATE":
                    xalign 0.5
                    yalign 0.5
                    color "#006654"
                    size 84
                    bold True
                    outlines [(10, "#00665418", 0, 0), (5, "#00806922", 0, 0)]

                text "ENEMY OF THE STATE" at title_glitch:
                    xalign 0.5
                    yalign 0.5
                    color "#EFFFFA"
                    size 84
                    bold True
                    outlines [(4, "#00806988", 0, 0), (12, "#00806918", 0, 0)]

                text "ENEMY OF THE STATE":
                    xalign 0.5
                    yalign 0.5
                    xoffset 2
                    yoffset -2
                    color "#8B8FCC33"
                    size 84
                    bold True

            frame:
                xalign 0.5
                xsize 260
                ysize 2
                background Solid("#008069")

            text "\"The truth will always find a way out.\"":
                color "#8B8FCC"
                size 22
                italic True
                xalign 0.5

            text "Step into a high-stakes whistleblower thriller, track your route through the branch web, and keep the mission alive.":
                color "#AAB0D6"
                size 18
                xalign 0.5
                text_align 0.5
                xmaximum 700

            null height 10

            vbox:
                xalign 0.5
                spacing 12

                textbutton "START":
                    style "modal_action_button"
                    xalign 0.5
                    action Start()

                if renpy.newest_slot():
                    textbutton "CONTINUE":
                        style "modal_action_button"
                        xalign 0.5
                        action FileLoad(renpy.newest_slot(), confirm=False)

                textbutton "DOSSIER":
                    style "modal_action_button"
                    xalign 0.5
                    action ShowMenu("dossier")

                textbutton "STORY TREE":
                    style "modal_action_button"
                    xalign 0.5
                    action ShowMenu("story_tree")

                textbutton "SETTINGS":
                    style "modal_action_button"
                    xalign 0.5
                    action ShowMenu("preferences")

                if renpy.variant("pc"):
                    textbutton "EXIT":
                        style "modal_action_button"
                        xalign 0.5
                        background Solid("#241926")
                        hover_background Solid("#4D5186")
                        action Quit(confirm=True)

            null height 8

            text "v[config.version]":
                color "#4D5186"
                size 15
                xalign 0.5



screen pause_hub():
    tag menu
    modal True

    use ui_backdrop
    use shell_header(
        "ESC MENU",
        "MISSION CONTROL",
        "Resume, save, adjust settings, or inspect the branch map without dropping into the default Ren'Py interface."
    )

    frame:
        xpos 72
        ypos 214
        xsize 620
        ysize 770
        background Solid("#101523EE")
        padding (34, 30)

        vbox:
            spacing 14

            textbutton "RESUME":
                style "modal_action_button"
                action Return()

            textbutton "START":
                style "modal_action_button"
                action Start()

            textbutton "SAVE":
                style "modal_action_button"
                action ShowMenu("save")

            textbutton "SETTINGS":
                style "modal_action_button"
                action ShowMenu("preferences")

            textbutton "STORY TREE":
                style "modal_action_button"
                action ShowMenu("story_tree")

            if renpy.variant("pc"):
                textbutton "EXIT":
                    style "modal_action_button"
                    background Solid("#241926")
                    hover_background Solid("#4D5186")
                    action Quit(confirm=True)

    frame:
        xalign 1.0
        xoffset -72
        ypos 214
        xsize 1080
        ysize 770
        background Solid("#0E1321E6")
        padding (36, 32)

        vbox:
            spacing 18

            text "TACTICAL STATUS":
                color "#8B8FCC"
                size 17
                bold True

            hbox:
                spacing 18

                frame:
                    xsize 320
                    ysize 150
                    background Solid("#002922")
                    padding (22, 18)

                    vbox:
                        spacing 8
                        text "Current chapter":
                            color "#8B8FCC"
                            size 15
                            bold True
                        text "[current_chapter]/5":
                            color "#EAF4F1"
                            size 34
                            bold True
                        text "Operation branch currently in progress.":
                            color "#AAB0D6"
                            size 16

                frame:
                    xsize 320
                    ysize 150
                    background Solid("#171C30")
                    padding (22, 18)

                    vbox:
                        spacing 8
                        text "Knowledge":
                            color "#8B8FCC"
                            size 15
                            bold True
                        text "[knowledge_score]":
                            color "#EAF4F1"
                            size 34
                            bold True
                        text "Educational progress accumulated so far.":
                            color "#AAB0D6"
                            size 16

                frame:
                    xsize 320
                    ysize 150
                    background Solid("#171C30")
                    padding (22, 18)

                    vbox:
                        spacing 8
                        text "Suspicion":
                            color "#8B8FCC"
                            size 15
                            bold True
                        text "[suspicion_level]/5":
                            color "#EAF4F1"
                            size 34
                            bold True
                        text "Operational pressure currently on the player.":
                            color "#AAB0D6"
                            size 16

            frame:
                xfill True
                ysize 1
                background Solid("#232843")

            text "This pause menu now uses the same spacing system as the rest of the UI, so buttons, cards, and text blocks stay aligned on different screens.":
                color "#AAB0D6"
                size 18
                xmaximum 960

    key "game_menu" action Return()


################################################################################
## Story / Learning Screens
################################################################################

screen dossier():
    tag menu

    use ui_backdrop
    use shell_header(
        "REFERENCE DATABASE",
        "NETWORK SECURITY DOSSIER",
        "Core cyber-security concepts presented in one scrollable reference layout."
    )

    frame:
        xpos 72
        ypos 214
        xsize 1776
        ysize 770
        background Solid("#0E1321E6")
        padding (26, 26)

        vbox:
            xfill True
            yfill True
            spacing 18

            viewport:
                xfill True
                ysize 640
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                vbox:
                    spacing 14
                    xfill True
                    xmaximum 1670

                    for term, definition in [
                        ("VPN (Virtual Private Network)", "Creates an encrypted tunnel between your device and a server, hiding your traffic from local network surveillance. Essential on untrusted networks like public Wi-Fi."),
                        ("PGP (Pretty Good Privacy)", "Asymmetric encryption system using public/private key pairs. Public key encrypts, only the matching private key can decrypt. Used for secure email communication."),
                        ("TOR (The Onion Router)", "Anonymization network that routes traffic through multiple relay nodes, each encrypting a layer. Makes it very difficult to trace traffic to its source."),
                        ("HTTPS", "HTTP with TLS/SSL encryption. Secures data between your browser and a web server. Look for the padlock icon in your browser's address bar."),
                        ("Firewall", "Network security system that monitors and filters incoming and outgoing traffic based on predefined rules. Acts as a barrier between trusted and untrusted networks."),
                        ("Metadata", "Data about data — who you communicated with, when, for how long, from where. Does not include the message content but can reveal intimate patterns of life."),
                        ("Man-in-the-Middle Attack", "An attacker secretly intercepts communication between two parties. Both parties think they're talking directly to each other. Key verification prevents this."),
                        ("Caesar Cipher", "Simple substitution cipher where each letter is shifted by a fixed number. Easy to break but historically significant. Example: ROT-3 shifts A to D, B to E, and so on."),
                        ("OpSec (Operational Security)", "The practice of protecting critical information by identifying what intelligence the adversary could gather from your actions and taking steps to prevent it."),
                        ("Zero-Day Exploit", "A vulnerability in software unknown to the vendor. Called zero-day because there are zero days of notice before it is exploited. No patch exists yet."),
                        ("AES-256", "Advanced Encryption Standard with a 256-bit key. Strong symmetric encryption that is effectively impossible to brute-force with current consumer hardware."),
                        ("SecureDrop", "An open-source whistleblowing platform that allows anonymous document submission. Used by major news organizations to protect sources."),
                        ("PRISM", "NSA surveillance program providing direct access to user data from major tech companies. Exposed by Snowden in 2013."),
                        ("XKeyscore", "NSA tool for searching and analyzing internet data. It could search email content, browsing history, and other digital activity in near real time."),
                    ]:
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
                                    background Solid("#006654")
                                    yalign 0.0

                                vbox:
                                    spacing 8
                                    xfill True
                                    xmaximum 1600

                                    text term:
                                        color "#EAF4F1"
                                        size 24
                                        bold True
                                        xfill True

                                    text definition:
                                        color "#AAB0D6"
                                        size 18
                                        xfill True
                                        xmaximum 1540

            frame:
                xfill True
                background Solid("#171C30")
                padding (20, 18)

                hbox:
                    xfill True

                    text "Use the mouse wheel or drag to browse the archive.":
                        color "#AAB0D6"
                        size 17
                        yalign 0.5

                    textbutton "RETURN":
                        style "modal_action_button"
                        xsize 240
                        xalign 1.0
                        action Return()

    key "game_menu" action Return()


screen briefing_screen():
    modal True

    use ui_backdrop

    frame:
        xalign 0.5
        yalign 0.5
        xsize 980
        background Solid("#0E1321F2")
        padding (0, 0)

        vbox:
            spacing 0

            frame:
                xfill True
                ysize 66
                background Solid("#241926")
                padding (28, 0)

                text "CLASSIFIED BRIEFING":
                    color "#EAF4F1"
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

                    text "OPERATIVE: Edward Snowden":
                        color "#EAF4F1"
                        size 24
                        bold True

                    text "ASSIGNMENT: NSA Systems Administrator":
                        color "#AAB0D6"
                        size 20

                    text "CLEARANCE: TS/SCI":
                        color "#8B8FCC"
                        size 20
                        bold True

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#232843")

                    text "Navigate the moral and technical challenges of one of the most significant intelligence leaks in modern history.":
                        color "#EAF4F1"
                        size 22
                        xmaximum 860

                    text "Your decisions affect trust, suspicion, and what information can survive the operation.":
                        color "#AAB0D6"
                        size 18
                        xmaximum 860

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22)

                textbutton "ACCEPT MISSION":
                    style "modal_action_button"
                    xalign 0.5
                    action Return()


screen chapter_title_screen(number, title, subtitle):
    modal True

    use ui_backdrop

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        background Solid("#0E1321EE")
        padding (40, 36)

        vbox:
            xalign 0.5
            spacing 12

            text "CHAPTER [number]":
                color "#8B8FCC"
                size 18
                bold True
                xalign 0.5

            text title:
                color "#EAF4F1"
                size 58
                bold True
                xalign 0.5

            text subtitle:
                color "#AAB0D6"
                size 23
                italic True
                xalign 0.5

    timer 3.0 action Return()
    key "dismiss" action Return()


screen chapter_summary(chapter_num, chapter_name):
    modal True

    use ui_backdrop

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

                    text "CHAPTER [chapter_num] COMPLETE":
                        color "#8B8FCC"
                        size 16
                        bold True
                        xalign 0.5

                    text chapter_name:
                        color "#EAF4F1"
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
                        text "Knowledge Score":
                            color "#AAB0D6"
                            size 21
                        text "[knowledge_score]":
                            color "#EAF4F1"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text "Trust Score":
                            color "#AAB0D6"
                            size 21
                        text "[trust_score]":
                            color "#EAF4F1"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text "Suspicion Level":
                            color "#AAB0D6"
                            size 21
                        text "[suspicion_level]/5":
                            color "#EAF4F1"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text "Contacts Secured":
                            color "#AAB0D6"
                            size 21
                        text "[contacts_secured]":
                            color "#EAF4F1"
                            size 21
                            bold True
                            xalign 1.0

                    hbox:
                        xfill True
                        text "Evidence":
                            color "#AAB0D6"
                            size 21
                        if evidence_secured:
                            text "SECURED":
                                color "#EAF4F1"
                                size 21
                                bold True
                                xalign 1.0
                        else:
                            text "NOT YET":
                                color "#EAF4F1"
                                size 21
                                bold True
                                xalign 1.0

            frame:
                xfill True
                background Solid("#171C30")
                padding (24, 22)

                if chapter_num < 5:
                    textbutton "CONTINUE TO CHAPTER [chapter_num + 1]":
                        style "modal_action_button"
                        xalign 0.5
                        action Return()
                else:
                    textbutton "PROCEED TO FINAL ASSESSMENT":
                        style "modal_action_button"
                        xalign 0.5
                        action Return()


screen mcq_question(question, answers, correct_index, explanation, helper_text=None):
    modal True
    default selected = -1
    default answered = False

    use ui_backdrop

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

                    text "KNOWLEDGE CHECK":
                        color "#EAF4F1"
                        size 24
                        bold True
                        xalign 0.5

                    text "Pick the best answer. Every right call boosts your field knowledge.":
                        color "#8B8FCC"
                        size 15
                        xalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (34, 28)

                vbox:
                    spacing 18

                    text question:
                        color "#EAF4F1"
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
                                color "#8B8FCC"
                                size 18
                                italic True
                                xalign 0.5
                                text_align 0.5
                                xmaximum 920

                    for i, answer in enumerate(answers):
                        $ letter = ["A", "B", "C", "D"][i]

                        if not answered:
                            textbutton "[letter].  [answer]":
                                style "choice_button"
                                xalign 0.5
                                action [
                                    SetScreenVariable("selected", i),
                                    SetScreenVariable("answered", True)
                                ]
                        elif i == correct_index:
                            textbutton "[letter].  [answer]":
                                style "choice_button"
                                xalign 0.5
                                background Solid("#002922")
                                hover_background Solid("#002922")
                                action NullAction()
                        elif i == selected:
                            textbutton "[letter].  [answer]":
                                style "choice_button"
                                xalign 0.5
                                background Solid("#241926")
                                hover_background Solid("#241926")
                                action NullAction()
                        else:
                            textbutton "[letter].  [answer]":
                                style "choice_button"
                                xalign 0.5
                                background Solid("#1A2034")
                                hover_background Solid("#1A2034")
                                action NullAction()

            if answered:
                frame:
                    xfill True
                    background Solid("#171C30")
                    padding (26, 24)

                    vbox:
                        spacing 12
                        xalign 0.5

                        if selected == correct_index:
                            text "Correct - Nice catch":
                                color "#EAF4F1"
                                size 24
                                bold True
                                xalign 0.5
                        else:
                            $ correct_letter = ["A", "B", "C", "D"][correct_index]
                            text "Not quite - Correct answer: [correct_letter]":
                                color "#EAF4F1"
                                size 24
                                bold True
                                xalign 0.5

                        text explanation:
                            color "#AAB0D6"
                            size 18
                            xalign 0.5
                            text_align 0.5
                            xmaximum 920

                        textbutton "CONTINUE":
                            style "modal_action_button"
                            xalign 0.5
                            if selected == correct_index:
                                action [SetVariable("knowledge_score", knowledge_score + 1), Return()]
                            else:
                                action Return()


screen text_input_question_screen(question, correct_answer, hint, explanation, accepted_answers=None, helper_text=None):
    modal True
    default user_answer = ""
    default attempts = 0
    default answered_correctly = False
    default show_hint = False
    default show_answer = False
    default submitted = False
    $ valid_answers = [a.strip().upper() for a in (accepted_answers or [correct_answer])]

    use ui_backdrop

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
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

                    text "TEXT INPUT CHECK":
                        color "#EAF4F1"
                        size 24
                        bold True
                        xalign 0.5

                    text "Short answers work. Hints unlock quickly if you need them.":
                        color "#8B8FCC"
                        size 15
                        xalign 0.5

            frame:
                xfill True
                background Solid("#101523")
                padding (34, 28)

                vbox:
                    spacing 18

                    text question:
                        color "#EAF4F1"
                        size 25
                        xalign 0.5
                        text_align 0.5
                        xmaximum 920

                    if helper_text:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (18, 14)

                            text helper_text:
                                color "#8B8FCC"
                                size 18
                                italic True
                                xalign 0.5
                                text_align 0.5
                                xmaximum 920

                    if show_hint:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (18, 14)

                            text "Hint: [hint]":
                                color "#8B8FCC"
                                size 18
                                italic True
                                xalign 0.5

                    if not answered_correctly and not show_answer:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (22, 18)

                            vbox:
                                spacing 12

                                hbox:
                                    xalign 0.5
                                    spacing 10

                                    text ">":
                                        color "#8B8FCC"
                                        size 25
                                        yalign 0.5

                                    input:
                                        value ScreenVariableInputValue("user_answer")
                                        length 30
                                        color "#EAF4F1"
                                        size 24
                                        xmaximum 700

                                if submitted and user_answer.strip().upper() not in valid_answers:
                                    text "Not quite. Try again.":
                                        color "#AAB0D6"
                                        size 18
                                        xalign 0.5

                        textbutton "SUBMIT":
                            style "modal_action_button"
                            xalign 0.5
                            action [
                                SetScreenVariable("submitted", True),
                                SetScreenVariable("attempts", attempts + 1),
                                If(user_answer.strip().upper() in valid_answers,
                                    true=SetScreenVariable("answered_correctly", True),
                                    false=[
                                        If(attempts >= 1, true=SetScreenVariable("show_hint", True)),
                                        If(attempts >= 2, true=SetScreenVariable("show_answer", True))
                                    ])
                            ]

                    if answered_correctly:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (22, 20)

                            vbox:
                                spacing 10
                                xalign 0.5

                                text "Correct":
                                    color "#EAF4F1"
                                    size 24
                                    bold True
                                    xalign 0.5

                                text explanation:
                                    color "#AAB0D6"
                                    size 18
                                    xalign 0.5
                                    text_align 0.5
                                    xmaximum 920

                                textbutton "CONTINUE":
                                    style "modal_action_button"
                                    xalign 0.5
                                    action [SetVariable("knowledge_score", knowledge_score + 1), Return()]

                    if show_answer:
                        frame:
                            xfill True
                            background Solid("#171C30")
                            padding (22, 20)

                            vbox:
                                spacing 10
                                xalign 0.5

                                text "Answer: [correct_answer]":
                                    color "#EAF4F1"
                                    size 24
                                    bold True
                                    xalign 0.5

                                text explanation:
                                    color "#AAB0D6"
                                    size 18
                                    xalign 0.5
                                    text_align 0.5
                                    xmaximum 920

                                textbutton "CONTINUE":
                                    style "modal_action_button"
                                    xalign 0.5
                                    action Return()


################################################################################
## Menu Shell
################################################################################

screen navigation():
    vbox:
        spacing 12

        if main_menu:
            textbutton _("Start"):
                style "shell_nav_button"
                action Start()
        else:
            textbutton _("History"):
                style "shell_nav_button"
                action ShowMenu("history")

            textbutton _("Save"):
                style "shell_nav_button"
                action ShowMenu("save")

        textbutton _("Load"):
            style "shell_nav_button"
            action ShowMenu("load")

        textbutton _("Preferences"):
            style "shell_nav_button"
            action ShowMenu("preferences")

        textbutton _("Dossier"):
            style "shell_nav_button"
            action ShowMenu("dossier")

        textbutton _("Story Tree"):
            style "shell_nav_button"
            action ShowMenu("story_tree")

        if _in_replay:
            textbutton _("End Replay"):
                style "shell_nav_button"
                action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu"):
                style "shell_nav_button"
                action MainMenu()

        textbutton _("About"):
            style "shell_nav_button"
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help"):
                style "shell_nav_button"
                action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit"):
                style "shell_nav_button"
                background Solid("#241926")
                hover_background Solid("#4D5186")
                action Quit(confirm=not main_menu)


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    tag menu

    use ui_backdrop
    use shell_header(
        "ARCHIVE INTERFACE",
        "[title]",
        "A single menu grid now drives save, load, settings, history, help, and reference screens."
    )

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

                textbutton _("Return"):
                    style "shell_nav_button"
                    action Return()

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


################################################################################
## Standard Menus
################################################################################

screen about():
    tag menu

    use game_menu(_("About"), scroll="viewport", spacing=18):
        frame:
            xfill True
            background Solid("#171C30")
            padding (28, 24)

            vbox:
                spacing 14

                text "[config.name!t]":
                    color "#EAF4F1"
                    size 32
                    bold True

                text "Version [config.version!t]":
                    color "#8B8FCC"
                    size 20

                if gui.about:
                    text "[gui.about!t]":
                        color "#AAB0D6"
                        size 19

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."):
                    color "#AAB0D6"
                    size 18

                text "[renpy.license!t]":
                    color "#AAB0D6"
                    size 16


screen save():
    tag menu
    use file_slots(_("Save"))


screen load():
    tag menu
    use file_slots(_("Load"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

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
                    hover_background Solid("#1B2034")
                    padding (18, 10)
                    action page_name_value.Toggle()

                    input:
                        value page_name_value
                        color "#EAF4F1"
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
                            hover_background Solid("#1B2034")
                            padding (14, 14)
                            action FileAction(slot)

                            has vbox
                            spacing 10

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty slot")):
                                color "#8B8FCC"
                                size 15
                                xalign 0.0

                            text FileSaveName(slot):
                                color "#EAF4F1"
                                size 18
                                xalign 0.0

                            key "save_delete" action FileDelete(slot)

                hbox:
                    xalign 0.5
                    spacing 10

                    textbutton _("<"):
                        style "shell_nav_button"
                        xsize 74
                        action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            style "shell_nav_button"
                            xsize 74
                            action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]":
                            style "shell_nav_button"
                            xsize 74
                            action FilePage(page)

                    textbutton _(">"):
                        style "shell_nav_button"
                        xsize 74
                        action FilePageNext()


screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport", spacing=18):
        hbox:
            spacing 18
            xfill True

            frame:
                xsize 655
                background Solid("#171C30")
                padding (24, 22)

                vbox:
                    spacing 18

                    text "DISPLAY AND FLOW":
                        color "#8B8FCC"
                        size 18
                        bold True

                    if renpy.variant("pc") or renpy.variant("web"):
                        textbutton _("Window"):
                            style "shell_nav_button"
                            action Preference("display", "window")

                        textbutton _("Fullscreen"):
                            style "shell_nav_button"
                            action Preference("display", "fullscreen")

                    textbutton _("Skip Unseen Text"):
                        style "shell_nav_button"
                        action Preference("skip", "toggle")

                    textbutton _("Skip After Choices"):
                        style "shell_nav_button"
                        action Preference("after choices", "toggle")

                    textbutton _("Transitions"):
                        style "shell_nav_button"
                        action InvertSelected(Preference("transitions", "toggle"))

            frame:
                xsize 655
                background Solid("#171C30")
                padding (24, 22)

                vbox:
                    spacing 18

                    text "TEXT AND AUDIO":
                        color "#8B8FCC"
                        size 18
                        bold True

                    text "Text Speed":
                        color "#EAF4F1"
                        size 18
                    bar value Preference("text speed")

                    text "Auto-Forward Time":
                        color "#EAF4F1"
                        size 18
                    bar value Preference("auto-forward time")

                    if config.has_music:
                        text "Music Volume":
                            color "#EAF4F1"
                            size 18
                        bar value Preference("music volume")

                    if config.has_sound:
                        text "Sound Volume":
                            color "#EAF4F1"
                            size 18
                        bar value Preference("sound volume")

                    if config.has_voice:
                        text "Voice Volume":
                            color "#EAF4F1"
                            size 18
                        bar value Preference("voice volume")

                    textbutton _("Mute All"):
                        style "shell_nav_button"
                        action Preference("all mute", "toggle")


screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll="viewport", spacing=14):
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
                                text h.who:
                                    color h.who_args["color"]
                                    size 20
                                    bold True
                                    substitute False
                            else:
                                text h.who:
                                    color "#8B8FCC"
                                    size 20
                                    bold True
                                    substitute False

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            color "#EAF4F1"
                            size 19
                            substitute False
        else:
            frame:
                xfill True
                background Solid("#171C30")
                padding (28, 22)
                text _("The dialogue history is empty."):
                    color "#AAB0D6"
                    size 20


define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport", spacing=18):
        hbox:
            spacing 12

            textbutton _("Keyboard"):
                style "shell_nav_button"
                xsize 190
                action SetScreenVariable("device", "keyboard")

            textbutton _("Mouse"):
                style "shell_nav_button"
                xsize 190
                action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad"):
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
            (_("Enter"), _("Advances dialogue and activates the interface.")),
            (_("Space"), _("Advances dialogue without selecting choices.")),
            (_("Arrow Keys"), _("Navigate the interface.")),
            (_("Escape"), _("Opens the custom mission control menu.")),
            (_("Ctrl"), _("Skips dialogue while held down.")),
            (_("Tab"), _("Toggles dialogue skipping.")),
            (_("Page Up"), _("Rolls back to earlier dialogue.")),
            (_("Page Down"), _("Rolls forward to later dialogue.")),
            ("H", _("Hides the user interface.")),
            ("S", _("Takes a screenshot.")),
            ("V", _("Toggles self-voicing.")),
            (_("Shift+A"), _("Opens the accessibility menu.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#8B8FCC"
                    size 20
                    bold True
                    xsize 220

                text desc:
                    color "#EAF4F1"
                    size 19
                    xfill True


screen mouse_help():
    vbox:
        spacing 12

        for key_name, desc in [
            (_("Left Click"), _("Advances dialogue and activates the interface.")),
            (_("Middle Click"), _("Hides the user interface.")),
            (_("Right Click"), _("Opens the custom mission control menu.")),
            (_("Wheel Up"), _("Rolls back to earlier dialogue.")),
            (_("Wheel Down"), _("Rolls forward to later dialogue.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#8B8FCC"
                    size 20
                    bold True
                    xsize 220

                text desc:
                    color "#EAF4F1"
                    size 19
                    xfill True


screen gamepad_help():
    vbox:
        spacing 12

        for key_name, desc in [
            (_("A / Bottom Button"), _("Advances dialogue and activates the interface.")),
            (_("Left Trigger"), _("Rolls back to earlier dialogue.")),
            (_("Right Shoulder"), _("Rolls forward to later dialogue.")),
            (_("D-Pad / Sticks"), _("Navigate the interface.")),
            (_("Start / B"), _("Opens the custom mission control menu.")),
            (_("Y / Top Button"), _("Hides the user interface.")),
        ]:
            hbox:
                spacing 20
                xfill True

                text key_name:
                    color "#8B8FCC"
                    size 20
                    bold True
                    xsize 320

                text desc:
                    color "#EAF4F1"
                    size 19
                    xfill True

        textbutton _("Calibrate"):
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

    frame:
        xalign 0.5
        yalign 0.5
        xsize 860
        background Solid("#0E1321F2")
        padding (32, 28)

        vbox:
            spacing 22
            xalign 0.5

            text _(message):
                color "#EAF4F1"
                size 28
                bold True
                xalign 0.5
                text_align 0.5
                xmaximum 720

            hbox:
                spacing 14
                xalign 0.5

                textbutton _("Yes"):
                    style "modal_action_button"
                    xsize 220
                    action yes_action

                textbutton _("No"):
                    style "modal_action_button"
                    xsize 220
                    background Solid("#171C30")
                    hover_background Solid("#4D5186")
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
            text _("Skipping"):
                color "#EAF4F1"
                size 18
            text ">>":
                color "#8B8FCC"
                size 18


screen notify(message):
    zorder 100

    frame:
        xalign 1.0
        yalign 0.0
        xoffset -26
        yoffset 28
        background Solid("#0E1321E6")
        padding (16, 12)

        text "[message!tq]":
            color "#EAF4F1"
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
    background Solid("#1B2034")
    hover_background Solid("#006654")
    left_padding 18
    right_padding 18
    top_padding 12
    bottom_padding 12
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    color "#EAF4F1"
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

            textbutton _("Back") action Rollback()
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Menu") action ShowMenu("pause_hub")
