image loading_animation = Movie(play="images/ui/loading_animation.webm", loop=True)

label splashscreen:
    $ apply_accessibility_font()
    $ apply_high_contrast()
    scene black
    show loading_animation at truecenter
    pause 8.0
    hide loading_animation
    with dissolve
    return

label show_loading_screen:
    $ show_hud = False
    $ quick_menu = False
    window hide
    scene black
    with dissolve
    show loading_animation at truecenter
    pause 8.0
    hide loading_animation
    with dissolve
    return
