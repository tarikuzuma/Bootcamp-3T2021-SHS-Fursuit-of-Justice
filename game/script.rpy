# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")
define Ben = Character('Benjamin', color="#ebdcc1")
define Player = Character('player', color='#322b20')


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "During a video tutorial, I will have to slay you"
    "Why so?"
    "Because..."
    "*slash*"
    with fade

label Start:
    show black
    "I am Player, a rookie lawyer who passed the bar exam not too long ago."
    "I wanted to pursue law because I have this clear sense of justice inside of my head that I want to prove to everyone."
    show zeil delighted
    with fade
    "I'm just starting, but may you please guide me as I progress into being a professional lawyer."
    $ WrongBase = 0

label nameChoose:

define player = Character("[povname]", color='#322b20')

python:
    povname = renpy.input("What's the name you want to give me?", length=32)
    povname = povname.strip()

    if not povname:
        povname = "Player"

show zeil normal

label nameConfirm:
    "Hmm, I see. So my name is [povname] huh?"    
    "..."
    "Are you sure you want my name to be [povname] ? I'll be stuck with this all-throughout the playthrough"

menu:
    
    "Yeah I am sure.":
        jump Chapter1

    "No, nevermind.":
        
        show zeil delighted
        "Sounds too weird, isn't it? Hahaha"
        "Well, nothing wrong with the name, just that I kinda don't dig it if you catch my drift."
        jump wrongEval
        

label wrongEval:
    $ WrongBase += 1
    if WrongBase == 2:
        show zeil annoyed
        "Make up your mind already"
        jump nameChoose
    else:
        jump nameChoose

label Chapter1:
    show zeil delighted
    player "Oki! If that is the name you insisted then I'll go for it <3"
    show zeil angry
    player "But you do know that you have to undergo the tutorial to see me do great right?"
    show zeil laugh
    player "I mean I'm just a rookie lawyer after all!"
    player "I ain't like those OP lawyers you probs see on tv!"
    show extra normal at right
    "Random Girl" "No!"

    show black
    Ben "Okay, let's start the first case, shall we?"
    Ben "What we have here is quite an unusual one, it will require some professionalism so make sure you keep your composure 
    while addressing the case. We don’t want to look silly infront of our clients do you understand?"   
