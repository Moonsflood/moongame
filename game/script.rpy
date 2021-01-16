# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Game Design: Aysel
# Art and Charater Design: David
# Story Design: Trin

define a = Character("Moon")

define t = Character("Story Teller")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene colorbk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Moon happy

    # These display lines of dialogue.

    a "Hello, Welcome to my first game."

    a "Right now this is a hard draft. "

    a "Someday this may be a great complete game."

    a "Stick around and you shall see."

    a "Thanks for visiting!"

    a "See you soon! xx"

    a "<3"


    scene workprogress

    a "Oh Hi, you are still here?"

    a "Silly you, we are still not finished here yet!"

    a "hehe..."

    scene garden

    t "Once upon a time there was a girl name moon..."

    t "...she loves the moon, the skies and the universe"


    # This ends the game.

    return
