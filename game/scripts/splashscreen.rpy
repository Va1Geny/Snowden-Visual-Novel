image animated_logo:
    "logo.png"
    # Start slightly smaller and transparent
    zoom 0.95 alpha 0.0
    # Fade in and scale up to normal size
    linear 1.0 zoom 1.0 alpha 1.0
    # Begin continuous subtle pulse
    block:
        linear 1.5 zoom 1.02
        linear 1.5 zoom 1.0
        repeat

label splashscreen:
    # Ensure background is black
    scene black
    
    # Show the animated logo in the center
    show animated_logo at truecenter
    
    # Optional loading text or just wait
    pause 3.0
    
    # Fade out smoothly before the main menu
    hide animated_logo
    with dissolve
    
    return

label show_loading_screen:
    $ show_hud = False
    $ quick_menu = False
    window hide
    # This label can be called between chapters
    scene black
    with dissolve
    
    show animated_logo at truecenter
    pause 2.0
    
    hide animated_logo
    with dissolve
    
    return
