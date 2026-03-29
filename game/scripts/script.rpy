# Define your characters here. 
# The first string is the name shown in-game, 'color' is the name label color.
define m = Character("Mei", color="#5bc2e7")
define p = Character("[player_name]", color="#ffffff")

# The game starts here.
label start:

    # Show a background. (Requires a 'bg_room.jpg' or similar in the images folder)
    # If you don't have images yet, Ren'Py will show a placeholder.
    image bg_1:
        "backgrounds/bg_1.png" # Ren'Py finds this in /images automatically
        xysize (1920, 1080) # This forces the size to your screen resolution
    scene bg_1 with fade

    "The morning sun filters through the blinds, casting long shadows across the floor."

    # Ask for the player's name
    python:
        player_name = renpy.input("What is your name?", length=12)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Jamie"

    m "Oh, hey [player_name]! I didn't think you'd be awake this early."

    p "I could say the same to you. What's the occasion?"

    m "I was thinking of heading out. Do you want to come along, or are you staying in?"

    # This is a Menu (the choice buttons)
    menu:
        "Go for a walk with Mei.":
            jump go_out

        "Stay home and rest.":
            jump stay_home

# Result of the first choice
label go_out:

    image bg_2:
        "backgrounds/bg_2.png" # Ren'Py finds this in /images automatically
        xysize (1920, 1080) # This forces the size to your screen resolution
    scene bg_2 with fade

    m "Awesome! Grab your coat, the air is a bit chilly today."
    "You decide to head out. It turns out to be a beautiful morning."

    jump end_demo

# Result of the second choice
label stay_home:
    m "Fair enough. I'll bring you back a coffee then!"
    "Mei waves goodbye as she heads out, leaving you to the quiet of the house."
    
    jump end_demo

label end_demo:
    "Thanks for playing this short demo!"
    return # This ends the game and returns to the main menu