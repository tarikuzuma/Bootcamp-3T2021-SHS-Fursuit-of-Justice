# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "During a video tutorial, I will have to slay you"
    "Why so?"
    "Because..."
    "*slash*"

label sprites:
    show zeil delighted
    Zeil "But wait, who are you?"
    show zeil angry
    Zeil "I am just sad"
    show zeil laugh
    Zeil "Oh Hello there my dude, may i slap your face?"
    show extra normal at right
    "Random Girl" "No!"

label scene2:
    Zeil "Hello let's go to the mall"
    scene bg gym
    with fade

    show zeil smile2 at left
    Zeil "Did I stutter?"
    Zeil "..."
    Zeil "Sorry that was awkward hehe..."
    show zeil normal
    Zeil "Anyways, do you wanna hang out?"
menu:
    "Sure":
        jump choices1_a

    "No, you are too weird.":
        jump choices1_b

label choices1_a:
    show zeil delighted
    Zeil "Good, I will see you in the mall later, or somewhere else idk "
    jump choiceEnd

label choices1_b:
    show zeil annoyed
    Zeil "Alright do come to school tomorrow for a blasting surprise!!! ;)"
    show zeil laugh
    Zeil "Hahaha! Just kidding, you are definately spared"
    jump choiceEnd

label choiceEnd:
    show zeil smile2
    Zeil "Alright. Goodbye."



label bgm:
    return
