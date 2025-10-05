# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Stormy -> Purple
define stormy = Character("Stormy", color="#9D3BFF")

# Stormy -> Yellow
define sparky = Character("Sparky", color="#F5BF2A")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    $ ai_response = call_gemini("Your name is Stormy. Say Hi to the world, and state what AI language model you're actually based on.")

    stormy "[ai_response]"

    sparky "Hi! I'm sparky. Don't be shocked!"

    # This ends the game.

    return
