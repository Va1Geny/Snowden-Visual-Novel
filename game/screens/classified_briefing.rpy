screen classified_briefing():
    tag screen

    add "gui/bg_classified.png" xalign 0.5 yalign 0.5

    add ScanlineOverlay(1920, 1080)

    add Solid("#0D1117", xysize=(1920, 1080))

    frame:
        background Solid("#0D1117")
        xysize (740, 620)
        xalign 0.5
        yalign 0.45
        padding (40, 32)

        vbox:
            spacing 20

            add TypedText(
                "CLASSIFIED BRIEFING",
                font="fonts/ShareTechMono-Regular.ttf",
                size=28,
                color="#00FFD1",
                reveal_speed=0.04
            ) xalign 0.5

            frame:
                background "#00FFD144"
                xysize (680, 1)
                xalign 0.5

            vbox:
                spacing 4

                hbox:
                    spacing 60
                    xalign 0.5

                    vbox:
                        spacing 2
                        text "OPERATIVE:" style "classified_briefing_label"
                        text "[CLASSIFIED]" style "classified_briefing_value_accent"

                hbox:
                    spacing 60
                    xalign 0.5

                    vbox:
                        spacing 2
                        text "ASSIGNMENT:" style "classified_briefing_label"
                        text "NSA Systems Administrator" style "classified_briefing_value"

                hbox:
                    spacing 60
                    xalign 0.5

                    vbox:
                        spacing 2
                        text "CLEARANCE:" style "classified_briefing_label"
                        text "TS/SCI" style "classified_briefing_value_accent"

            frame:
                background "#00FFD144"
                xysize (680, 1)
                xalign 0.5

            text "Navigate the moral and technical challenges of one of the most significant intelligence leaks in modern history." style "classified_briefing_body"

            text "Your decisions affect trust, suspicion, and what information can survive the operation." style "classified_briefing_muted"

            frame:
                background "#00FFD144"
                xysize (680, 1)
                xalign 0.5

            button:
                action Start()
                style "classified_briefing_btn"
                text "[ ACCEPT MISSION ]" style "classified_briefing_btn_text"

    on "show" action SetVariable("_briefing_show_anim", True)

    add DynamicDisplayable(lambda st: Solid("#0D1117", xysize=(1920, 1080))) as briefing_fade:
        alpha (lambda: max(0, 1 - min(1, renpy.get_displayed_screen("classified_briefing"))) if renpy.get_displayed_screen("classified_briefing") else 1)
