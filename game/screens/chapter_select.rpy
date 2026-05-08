################################################################################
## CHAPTER SELECT SCREEN
## classified: The Snowden Files
## Allows player to select which chapter to play
################################################################################

screen chapter_select():
    tag screen
    
    # Background
    add Solid("#080C10", xysize=(1920, 1080))
    
    # Scanline overlay
    add ScanlineOverlay(1920, 1080)
    
    # Semi-transparent overlay
    add Solid("#0D1117ee", xysize=(1920, 1080))
    
    # Main content container
    frame:
        background Solid("#0D1117")
        xysize (900, 800)
        xalign 0.5
        yalign 0.45
        padding (40, 32)
        
        vbox:
            spacing 24
            
            # Header
            text "MISSION SELECT" style "chapter_select_title"
            
            # Top divider
            frame:
                background "#00FFD144"
                xysize (820, 1)
                xalign 0.5
            
            # Chapter list in scrollable area
            viewport:
                xsize 820
                ysize 620
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 12
                    
                    # Chapter 1
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
                                
                                # Cyan indicator for current chapter
                                frame:
                                    background "#00FFD1"
                                    xysize (4, 60)
                                
                                vbox:
                                    spacing 2
                                    
                                    hbox:
                                        spacing 20
                                        text "CHAPTER 01" style "chapter_select_chapter_num"
                                        text "[INFILTRATION]" style "chapter_select_codename"
                                    
                                    text "Assume your identity as NSA contractor." style "chapter_select_description"
                    
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
                                        text "CHAPTER 02" style "chapter_select_chapter_num"
                                        text "[DISCOVERY]" style "chapter_select_codename"
                                    
                                    text "Access classified PRISM files." style "chapter_select_description"
                    
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
                                        text "CHAPTER 03" style "chapter_select_chapter_num"
                                        text "[DECISION]" style "chapter_select_codename"
                                    
                                    text "Choose between personal conscience and duty." style "chapter_select_description"
                    
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
                                        text "CHAPTER 04" style "chapter_select_chapter_num_locked"
                                        text "[EXFILTRATION]" style "chapter_select_codename"
                                    
                                    text "[CLASSIFIED]" style "chapter_select_locked_text"
                    
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
                                        text "CHAPTER 05" style "chapter_select_chapter_num_locked"
                                        text "[AFTERMATH]" style "chapter_select_codename"
                                    
                                    text "[CLASSIFIED]" style "chapter_select_locked_text"
            
            # Bottom divider
            frame:
                background "#00FFD144"
                xysize (820, 1)
                xalign 0.5
            
            # Return button
            button:
                action Return()
                style "chapter_select_btn"
                text "[ RETURN ]" style "chapter_select_btn_text"
