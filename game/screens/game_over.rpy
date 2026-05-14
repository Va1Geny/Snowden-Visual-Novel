screen game_over(narrative_text=""):
    tag screen

    add Solid("#080C10", xysize=(1920, 1080))

    add RedScanlineOverlay(1920, 1080)

    add Solid("#3A001055", xysize=(1920, 1080))

    frame:
        background Solid("#0D1117")
        xysize (740, 680)
        xalign 0.5
        yalign 0.45
        padding (40, 32)

        vbox:
            spacing 20

            text t("OPERATION COMPROMISED") style "game_over_title"

            frame:
                background "#FF2D5544"
                xysize (660, 1)
                xalign 0.5

            text t("IDENTITY EXPOSED") style "game_over_status"

            if narrative_text:
                text t(narrative_text) style "game_over_body"

            frame:
                background "#FF2D5533"
                xysize (660, 1)
                xalign 0.5

            vbox:
                spacing 8
                xalign 0.5

                hbox:
                    spacing 120
                    xalign 0.5

                    vbox:
                        spacing 2
                        xalign 0.0

                        text t("KNOWLEDGE:") style "game_over_label"
                        text t("[knowledge_score]/100") style "game_over_score_value"

                hbox:
                    spacing 120
                    xalign 0.5

                    vbox:
                        spacing 2
                        xalign 0.0

                        text t("SUSPICION:") style "game_over_label"
                        text t("[suspicion_level]/100") style "game_over_score_danger"

            frame:
                background "#FF2D5544"
                xysize (660, 1)
                xalign 0.5

            hbox:
                spacing 16
                xalign 0.5

                button:
                    action Return("restart")
                    style "game_over_btn_primary"
                    text t("[ TRY AGAIN ]") style "game_over_btn_primary_text"

                button:
                    action Return("main_menu")
                    style "game_over_btn_secondary"
                    text t("[ MAIN MENU ]") style "game_over_btn_secondary_text"

    on "show" action SetVariable("_game_over_show_anim", True)
