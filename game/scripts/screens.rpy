################################################################################
## SCREENS.RPY — Custom UI Screens
## Classified: The Snowden Files
##
## This file replaces the default screens with custom themed screens.
################################################################################

################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
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


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################

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


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## CUSTOM GAME SCREENS — Classified Theme
################################################################################


################################################################################
## MAIN MENU — Classified / Surveillance Theme
################################################################################

screen main_menu():
    tag menu

    # Dark background
    add "#0A0E1A"

    # Animated scanline overlay effect
    frame:
        xfill True
        yfill True
        background None

        # Data stream columns (simulated with text)
        for i in range(20):
            text "01001101":
                color "#00FFD108"
                size 14
                xpos (i * 96 + 10)
                ypos (i * 53 % 1080)

    # Central content
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 15

        # Game title with glitch effect
        text "CLASSIFIED" at title_glitch:
            color "#00FFD1"
            size 72
            bold True
            xalign 0.5
            outlines [(2, "#00FFD140", 0, 0)]

        text "THE SNOWDEN FILES":
            color "#E8E8E8"
            size 36
            bold True
            xalign 0.5

        null height 5

        # Subtitle
        text "\"The truth will always find a way out.\"":
            color "#888888"
            size 20
            italic True
            xalign 0.5

        null height 40

        # Menu buttons styled as terminal commands
        vbox:
            xalign 0.5
            spacing 8

            # START MISSION
            textbutton "> START MISSION":
                xalign 0.5
                action Start()
                text_color "#00FFD1"
                text_hover_color "#0A0E1A"
                text_size 24
                text_bold True
                xsize 400
                ysize 50

            # CONTINUE (only if save exists)
            if renpy.newest_slot():
                textbutton "> CONTINUE":
                    xalign 0.5
                    action FileLoad(renpy.newest_slot(), confirm=False)
                    text_color "#00FFD1"
                    text_hover_color "#0A0E1A"
                    text_size 24
                    text_bold True
                    xsize 400
                    ysize 50

            # DOSSIER
            textbutton "> DOSSIER":
                xalign 0.5
                action ShowMenu("dossier")
                text_color "#00FFD1"
                text_hover_color "#0A0E1A"
                text_size 24
                text_bold True
                xsize 400
                ysize 50

            # SETTINGS
            textbutton "> SETTINGS":
                xalign 0.5
                action ShowMenu("preferences")
                text_color "#00FFD1"
                text_hover_color "#0A0E1A"
                text_size 24
                text_bold True
                xsize 400
                ysize 50

            # EXIT
            if renpy.variant("pc"):
                textbutton "> EXIT":
                    xalign 0.5
                    action Quit(confirm=True)
                    text_color "#FF2D55"
                    text_hover_color "#0A0E1A"
                    text_size 24
                    text_bold True
                    xsize 400
                    ysize 50

    # Version + disclaimer at bottom
    vbox:
        xalign 0.5
        yalign 0.98
        spacing 3

        text "v1.0 — Classified: The Snowden Files":
            color "#333333"
            size 14
            xalign 0.5

        text "Fictional dramatization for educational purposes.":
            color "#333333"
            size 12
            xalign 0.5


################################################################################
## DOSSIER / GLOSSARY SCREEN
################################################################################

screen dossier():
    tag menu

    add "#0A0E1A"

    viewport:
        xfill True yfill True
        scrollbars "vertical"
        mousewheel True

        vbox:
            xalign 0.5
            xsize 1000
            spacing 20
            yoffset 40

            text "// NETWORK SECURITY DOSSIER //" style "dossier_title"

            null height 10

            # Glossary entries
            for term, definition in [
                ("VPN (Virtual Private Network)", "Creates an encrypted tunnel between your device and a server, hiding your traffic from local network surveillance. Essential on untrusted networks like public Wi-Fi."),
                ("PGP (Pretty Good Privacy)", "Asymmetric encryption system using public/private key pairs. Public key encrypts, only the matching private key can decrypt. Used for secure email communication."),
                ("TOR (The Onion Router)", "Anonymization network that routes traffic through multiple relay nodes, each encrypting a layer. Makes it very difficult to trace traffic to its source."),
                ("HTTPS", "HTTP with TLS/SSL encryption. Secures data between your browser and a web server. Look for the padlock icon in your browser's address bar."),
                ("Firewall", "Network security system that monitors and filters incoming and outgoing traffic based on predefined rules. Acts as a barrier between trusted and untrusted networks."),
                ("Metadata", "Data about data — who you communicated with, when, for how long, from where. Does not include the message content but can reveal intimate patterns of life."),
                ("Man-in-the-Middle Attack", "An attacker secretly intercepts communication between two parties. Both parties think they're talking directly to each other. Key verification prevents this."),
                ("Caesar Cipher", "Simple substitution cipher where each letter is shifted by a fixed number. Easy to break but historically significant. Example: ROT-3 shifts A→D, B→E, etc."),
                ("OpSec (Operational Security)", "The practice of protecting critical information by identifying what intelligence the adversary could gather from your actions and taking steps to prevent it."),
                ("Zero-Day Exploit", "A vulnerability in software unknown to the vendor. Called 'zero-day' because there are zero days of notice before it's exploited. No patch exists yet."),
                ("AES-256", "Advanced Encryption Standard with 256-bit key. Military-grade symmetric encryption. Would take billions of years to brute-force with current technology."),
                ("SecureDrop", "Open-source whistleblowing platform that allows anonymous document submission. Used by major news organizations to protect sources."),
                ("PRISM", "NSA surveillance program providing direct access to user data from major tech companies. Exposed by Snowden in 2013."),
                ("XKeyscore", "NSA tool for searching and analyzing internet data. Could search content of emails, browsing history, and social media activity in near real-time."),
            ]:
                frame:
                    xfill True
                    background "#111827"
                    padding (20, 12)

                    vbox:
                        spacing 5
                        text term style "dossier_term"
                        text definition style "dossier_definition"

            null height 30

            textbutton "> RETURN":
                xalign 0.5
                text_color "#00FFD1"
                text_hover_color "#FFFFFF"
                text_size 24
                text_bold True
                action Return()

            null height 40


################################################################################
## BRIEFING SCREEN (Pre-Chapter 1)
################################################################################

screen briefing_screen():
    modal True
    add "#0A0E1A"

    frame:
        xalign 0.5 yalign 0.5
        xsize 1000
        background "#0A0E1A"
        padding (50, 40)

        vbox:
            xalign 0.5
            spacing 20

            text "▓▓▓ CLASSIFIED ▓▓▓" style "briefing_header"

            null height 10

            frame:
                xfill True
                background "#111827"
                padding (30, 25)

                vbox:
                    spacing 15

                    text "// MISSION BRIEFING //" color "#00FF00" size 22 bold True xalign 0.5

                    text "OPERATIVE: Edward Snowden" color "#00FFD1" size 20
                    text "ASSIGNMENT: NSA Systems Administrator" color "#00FFD1" size 20
                    text "CLEARANCE: TS/SCI" color "#00FFD1" size 20

                    null height 10

                    text "MISSION OBJECTIVE:" color "#FF2D55" size 20 bold True
                    text "Navigate the moral and technical challenges of the most significant intelligence leak in modern history." color "#E8E8E8" size 18

                    null height 5

                    text "Your decisions will determine the outcome. Every choice matters. Every answer teaches." color "#E8E8E8" size 18

            null height 10

            text "This is both a story AND a test. Choose wisely." style "briefing_warning"

            null height 15

            textbutton "> ACCEPT MISSION":
                xalign 0.5
                text_color "#00FFD1"
                text_hover_color "#0A0E1A"
                text_size 26
                text_bold True
                action Return()


################################################################################
## CHAPTER TITLE CARD SCREEN
################################################################################

screen chapter_title_screen(number, title, subtitle):
    modal True
    add "#000000"

    vbox:
        align (0.5, 0.5)
        spacing 20

        text "// CLASSIFIED: CHAPTER [number] //" style "sys_text" at chapter_fade_in
        text title style "chapter_title_text" at chapter_fade_in
        text subtitle style "chapter_subtitle_text" at chapter_fade_in

    # Auto-advance after 3 seconds
    timer 3.0 action Return()

    # Or click to skip
    key "dismiss" action Return()


################################################################################
## CHAPTER SUMMARY SCREEN
################################################################################

screen chapter_summary(chapter_num, chapter_name):
    modal True
    add "#0A0E1A"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900
        background "#0A0E1A"
        padding (40, 35)

        vbox:
            xalign 0.5
            spacing 15

            text "// CHAPTER [chapter_num] COMPLETE //" style "sys_text"
            text chapter_name style "summary_title"

            null height 15

            frame:
                xfill True
                background "#111827"
                padding (25, 20)

                vbox:
                    spacing 10

                    text "// CURRENT STATUS //" color "#00FFD1" size 20 bold True xalign 0.5

                    null height 5

                    hbox:
                        xfill True
                        text "Knowledge Score:" style "summary_stat_label"
                        text "[knowledge_score]" style "summary_stat_value" xalign 1.0

                    hbox:
                        xfill True
                        text "Trust Score:" style "summary_stat_label"
                        text "[trust_score]" style "summary_stat_value" xalign 1.0

                    hbox:
                        xfill True
                        text "Suspicion Level:" style "summary_stat_label"
                        text "[suspicion_level]/5" color "#FF2D55" size 20 bold True xalign 1.0

                    hbox:
                        xfill True
                        text "Contacts Secured:" style "summary_stat_label"
                        text "[contacts_secured]" style "summary_stat_value" xalign 1.0

                    hbox:
                        xfill True
                        text "Evidence:" style "summary_stat_label"
                        if evidence_secured:
                            text "SECURED" color "#00FF00" size 20 bold True xalign 1.0
                        else:
                            text "NOT YET" color "#888888" size 20 xalign 1.0

            null height 15

            if chapter_num < 5:
                textbutton "> CONTINUE TO CHAPTER [chapter_num + 1]":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action Return()
            else:
                textbutton "> PROCEED TO FINAL ASSESSMENT":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action Return()


################################################################################
## GAME HUD — Progress Tracker
################################################################################

screen game_hud():
    zorder 50

    if show_hud:
        frame:
            xalign 1.0 yalign 0.0
            xoffset -10 yoffset 10
            xsize 200
            background "#0A0E1A99"
            padding (12, 10)

            vbox:
                spacing 5

                text "CH [current_chapter]/5" color "#666666" size 14
                text "KNOWLEDGE: [knowledge_score]" color "#00FFD1" size 14

                hbox:
                    spacing 5
                    text "SUSPICION:" color "#888888" size 14

                # Suspicion bar
                bar:
                    value suspicion_level
                    range 5
                    xsize 120
                    ysize 8
                    left_bar Solid("#FF2D55")
                    right_bar Solid("#333333")

init python:
    config.overlay_screens.append("game_hud")


################################################################################
## MCQ QUESTION SCREEN
################################################################################

screen mcq_question(question, answers, correct_index, explanation):
    modal True
    default selected = -1
    default answered = False

    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 1000
        background "#0A0E1A"
        padding (40, 35)

        vbox:
            xalign 0.5
            spacing 15

            text "// KNOWLEDGE CHECK //" color "#00FF00" size 22 bold True xalign 0.5

            null height 5

            text question color "#E8E8E8" size 24 xalign 0.5 text_align 0.5

            null height 15

            # Answer buttons
            for i, answer in enumerate(answers):
                $ letter = ["A", "B", "C", "D"][i]

                if not answered:
                    textbutton "[letter]) [answer]":
                        xsize 850
                        xalign 0.5
                        text_size 20
                        text_color "#00FFD1"
                        text_hover_color "#FFFFFF"
                        action [
                            SetScreenVariable("selected", i),
                            SetScreenVariable("answered", True)
                        ]
                else:
                    if i == correct_index:
                        textbutton "[letter]) [answer]":
                            xsize 850
                            xalign 0.5
                            text_size 20
                            text_color "#00FF00"
                            text_bold True
                            action NullAction()
                    elif i == selected and i != correct_index:
                        textbutton "[letter]) [answer]":
                            xsize 850
                            xalign 0.5
                            text_size 20
                            text_color "#FF2D55"
                            action NullAction()
                    else:
                        textbutton "[letter]) [answer]":
                            xsize 850
                            xalign 0.5
                            text_size 20
                            text_color "#555555"
                            action NullAction()

            if answered:
                null height 10

                if selected == correct_index:
                    text "✓ CORRECT!" color "#00FF00" size 22 bold True xalign 0.5
                else:
                    $ correct_letter = ["A", "B", "C", "D"][correct_index]
                    text "✗ INCORRECT — Correct answer: [correct_letter]" color "#FF2D55" size 22 bold True xalign 0.5

                null height 5

                text explanation color "#AAAAAA" size 17 xalign 0.5 text_align 0.5

                null height 15

                textbutton "> CONTINUE":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    if selected == correct_index:
                        action [SetVariable("knowledge_score", knowledge_score + 1), Return()]
                    else:
                        action Return()


################################################################################
## TEXT INPUT QUESTION SCREEN
################################################################################

screen text_input_question_screen(question, correct_answer, hint, explanation):
    modal True
    default user_answer = ""
    default attempts = 0
    default answered_correctly = False
    default show_hint = False
    default show_answer = False
    default submitted = False

    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900
        background "#0A0E1A"
        padding (40, 35)

        vbox:
            xalign 0.5
            spacing 15

            text "// KNOWLEDGE CHECK — TEXT INPUT //" color "#00FF00" size 20 bold True xalign 0.5

            null height 5

            text question color "#E8E8E8" size 22 xalign 0.5 text_align 0.5

            null height 10

            if show_hint:
                text "HINT: [hint]" color "#FFD700" size 18 italic True xalign 0.5

            if not answered_correctly and not show_answer:
                hbox:
                    xalign 0.5
                    spacing 10

                    text "> " color "#00FF00" size 24 yalign 0.5

                    input:
                        value ScreenVariableInputValue("user_answer")
                        length 30
                        color "#00FFD1"
                        size 24

                null height 10

                if submitted and user_answer.strip().upper() != correct_answer.upper():
                    text "✗ INCORRECT. Try again." color "#FF2D55" size 18 xalign 0.5

                textbutton "> SUBMIT":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action [
                        SetScreenVariable("submitted", True),
                        SetScreenVariable("attempts", attempts + 1),
                        If(user_answer.strip().upper() == correct_answer.upper(),
                            true=SetScreenVariable("answered_correctly", True),
                            false=[
                                If(attempts >= 1,
                                    true=SetScreenVariable("show_hint", True)),
                                If(attempts >= 2,
                                    true=SetScreenVariable("show_answer", True)),
                            ]
                        )
                    ]

            if answered_correctly:
                text "✓ CORRECT!" color "#00FF00" size 24 bold True xalign 0.5
                text explanation color "#AAAAAA" size 17 xalign 0.5 text_align 0.5

                null height 10

                textbutton "> CONTINUE":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action [SetVariable("knowledge_score", knowledge_score + 1), Return()]

            if show_answer:
                text "ANSWER: [correct_answer]" color "#FFD700" size 24 bold True xalign 0.5
                text explanation color "#AAAAAA" size 17 xalign 0.5 text_align 0.5

                null height 10

                textbutton "> CONTINUE":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action Return()


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Game Menu screen ############################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################

screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            order_reverse True

            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################

screen history():

    tag menu

    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################

screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"


## Notify screen ###############################################################

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################

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

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

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
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################

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
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
