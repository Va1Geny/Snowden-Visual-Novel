################################################################################
## GAME OVER SCREEN
## classified: The Snowden Files
## Shown when player reaches a bad ending
##
## Uses shared displayable from ui_utilities.rpy:
##   - RedScanlineOverlay: Red-tinted scanline effect
################################################################################

screen game_over(narrative_text=""):
    tag screen
    
    # Background with red tint
    add Solid("#080C10", xysize=(1920, 1080))
    
    # Red-tinted scanline overlay
    add RedScanlineOverlay(1920, 1080)
    
    # Red semi-transparent overlay for danger aesthetic
    add Solid("#3A001055", xysize=(1920, 1080))
    
    # Main content card
    frame:
        background Solid("#0D1117")
        xysize (740, 680)
        xalign 0.5
        yalign 0.45
        padding (40, 32)
        
        vbox:
            spacing 20
            
            # Header with red accent
            text "OPERATION COMPROMISED" style "game_over_title"
            
            # Top divider - red tinted
            frame:
                background "#FF2D5544"
                xysize (660, 1)
                xalign 0.5
            
            # Large status text
            text "IDENTITY EXPOSED" style "game_over_status"
            
            # Narrative line (passed as parameter)
            if narrative_text:
                text narrative_text style "game_over_body"
            
            # Metadata divider
            frame:
                background "#FF2D5533"
                xysize (660, 1)
                xalign 0.5
            
            # Score display
            vbox:
                spacing 8
                xalign 0.5
                
                hbox:
                    spacing 120
                    xalign 0.5
                    
                    vbox:
                        spacing 2
                        xalign 0.0
                        
                        text "KNOWLEDGE:" style "game_over_label"
                        text "[knowledge_score]/100" style "game_over_score_value"
                
                hbox:
                    spacing 120
                    xalign 0.5
                    
                    vbox:
                        spacing 2
                        xalign 0.0
                        
                        text "SUSPICION:" style "game_over_label"
                        text "[suspicion_level]/100" style "game_over_score_danger"
            
            # Bottom divider
            frame:
                background "#FF2D5544"
                xysize (660, 1)
                xalign 0.5
            
            # Button container
            hbox:
                spacing 16
                xalign 0.5
                
                button:
                    action Return("restart")
                    style "game_over_btn_primary"
                    text "[ TRY AGAIN ]" style "game_over_btn_primary_text"
                
                button:
                    action Return("main_menu")
                    style "game_over_btn_secondary"
                    text "[ MAIN MENU ]" style "game_over_btn_secondary_text"
    
    # Entry animation - slow dissolve
    on "show" action SetVariable("_game_over_show_anim", True)
