define config.name = _("Enemy of the State")

define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
An educational visual novel where you step into the shoes of Edward Snowden to uncover the truth about network security.
Designed to teach students aged 16-18 the fundamentals of network security through interactive storytelling.

Fictional dramatization for educational purposes.
""")

define build.name = "EnemyOfTheState"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 32

default preferences.afm_time = 15

init python:
    config.keymap['rollback'].append('K_BACKSPACE')

define config.save_directory = "SkillLabsProject-1774359508"

define config.window_icon = "gui/window_icon.png"

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

    config.keymap['rollback'].append('K_BACKSPACE')
