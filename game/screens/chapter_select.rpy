screen chapter_select():
    tag screen

    add Solid("#080C10", xysize=(1920, 1080))

    add ScanlineOverlay(1920, 1080)

    add Solid("#0D1117ee", xysize=(1920, 1080))

    frame:
        background Solid("#0D1117")
        xysize (900, 800)
        xalign 0.5
        yalign 0.45
        padding (40, 32)

        vbox:
            spacing 24

            text t("MISSION SELECT") style "chapter_select_title"

            frame:
                background "#00FFD144"
                xysize (820, 1)
                xalign 0.5

            viewport:
                xsize 820
                ysize 620
                scrollbars "vertical"
                mousewheel True

                vbox:
                    spacing 12

                    button:
                        action Jump("chapter_1")
                        xysize (780, 100)
                        background Solid("#111720")
                        hover_background Solid("#1A2A3A")
                        padding (20, 16)

                        vbox:
                            spacing 4

                            hbox:
                                spacing 20

                                frame:
                                    background "#00FFD1"
                                    xysize (4, 60)

                                vbox:
                                    spacing 2

                                    hbox:
                                        spacing 20
                                        text t("CHAPTER 01") style "chapter_select_chapter_num"
                                        text t("[INFILTRATION]") style "chapter_select_codename"

                                    text t("Assume your identity as NSA contractor.") style "chapter_select_description"

                    button:
                        action Jump("chapter_2")
                        xysize (780, 100)
                        background Solid("#111720")
                        hover_background Solid("#1A2A3A")
                        padding (20, 16)

                        vbox:
                            spacing 4

                            hbox:
                                spacing 20

                                frame:
                                    background "#3A4A55"
                                    xysize (4, 60)

                                vbox:
                                    spacing 2

                                    hbox:
                                        spacing 20
                                        text t("CHAPTER 02") style "chapter_select_chapter_num"
                                        text t("[DISCOVERY]") style "chapter_select_codename"

                                    text t("Access classified PRISM files.") style "chapter_select_description"

                    button:
                        action Jump("chapter_3")
                        xysize (780, 100)
                        background Solid("#111720")
                        hover_background Solid("#1A2A3A")
                        padding (20, 16)

                        vbox:
                            spacing 4

                            hbox:
                                spacing 20

                                frame:
                                    background "#3A4A55"
                                    xysize (4, 60)

                                vbox:
                                    spacing 2

                                    hbox:
                                        spacing 20
                                        text t("CHAPTER 03") style "chapter_select_chapter_num"
                                        text t("[DECISION]") style "chapter_select_codename"

                                    text t("Choose between personal conscience and duty.") style "chapter_select_description"

                    button:
                        action NullAction()
                        xysize (780, 100)
                        background Solid("#0D0D0D")
                        hover_background Solid("#0D0D0D")
                        padding (20, 16)

                        vbox:
                            spacing 4

                            hbox:
                                spacing 20

                                frame:
                                    background "#3A4A55"
                                    xysize (4, 60)

                                vbox:
                                    spacing 2

                                    hbox:
                                        spacing 20
                                        text t("CHAPTER 04") style "chapter_select_chapter_num_locked"
                                        text t("[EXFILTRATION]") style "chapter_select_codename"

                                    text t("[CLASSIFIED]") style "chapter_select_locked_text"

                    button:
                        action NullAction()
                        xysize (780, 100)
                        background Solid("#0D0D0D")
                        hover_background Solid("#0D0D0D")
                        padding (20, 16)

                        vbox:
                            spacing 4

                            hbox:
                                spacing 20

                                frame:
                                    background "#3A4A55"
                                    xysize (4, 60)

                                vbox:
                                    spacing 2

                                    hbox:
                                        spacing 20
                                        text t("CHAPTER 05") style "chapter_select_chapter_num_locked"
                                        text t("[AFTERMATH]") style "chapter_select_codename"

                                    text t("[CLASSIFIED]") style "chapter_select_locked_text"

            frame:
                background "#00FFD144"
                xysize (820, 1)
                xalign 0.5

            button:
                action Return()
                style "chapter_select_btn"
                text t("[ RETURN ]") style "chapter_select_btn_text"
