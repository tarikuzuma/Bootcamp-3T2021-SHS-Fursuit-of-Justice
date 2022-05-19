﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")
define Ben = Character('Benjamin', color="#271c07")
define Player = Character('player', color='#30b670')


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
    show zeil normal
    player "I am still a rookie"

    show zeil normal at left
    with moveinleft
    pause (3.0)

    show benjamin at right
    with moveinright
    pause (3.0)
    Ben "WHOA!-hey you scared me there [povname] , I didnt know youd be this early Ho Ho Ho"
    show zeil smile
    scene bg officefirm
    with fade
    show zeil delighted at left
    show benjamin at right
    player "I thought it’d be nice to start the day early today with my first case and all"
    Ben "Ah… yes, of course! That’s the kind of energy this firm needs."
    Ben "This is your first case… to think you were just getting coffee and printing papers just weeks ago…"

    show zeil smile
    player "Well, that’s all thanks to you Ben"
    player "No, really, you made it far with your own hard work."
    Ben "Now let’s catch you up on your case, I'll walk you through it"

    Ben "Okay, let's start the first case, shall we?"
    Ben "What we have here is quite an unusual one, it will require some professionalism so make sure you keep your composure 
    while addressing the case. We don’t want to look silly infront of our clients do you understand?"   

    show zeil smile2
    player "Yes, Your Honor!" 
    show zeil normal
    Ben "Okay, to put in an easier context what we have here is Ms Rosa Barreto wanted to annul her marriage with Mr. Rivero Barreto due to ---- "
    show zeil shocked
    player "Due to what your Honor?"
    Ben "Due to *chuckles*"
    show zeil bored
    player "Sir please say it already your building up the suspense"
    Ben "Due to their relationship failing because Mr Rivero doesn't want to get intimate with Ms. Rosa"
    show zeil normal
    player "sounds melo intense, sire."
    ""
    Ben "So, are you going to accept the case or not?"
    $ RouteChecker = 0

label Chapter1_choice:
menu:
    "Do the case":
        jump Chapter1_con

    "Skip the case":
        Ben "Are you sure you don't want to take this case? I mean lawyers in our firm are pretty occupied now. Your decision is the thing I will fully respect."
        jump Chapter1_dec

label Chapter1_con:
    Ben "Yoyoyo! Baby steps I tell ya! Baby steps."
    show zeil smile2
    player "oh shush!"
    Ben "Seems like a great decision for you to take your first case immediately."
    Ben "Though, are you sure about your decision?"

menu:
    "Yeah, I'm sure. Let's start!":
        $ RouteChecker += 1
        Ben "Great!!!!!!! Let's finally get started then."
        jump Case1
    "Wait, let me think again.":
        Ben "Alright! No problem, just take your time in thinking."
        jump Chapter1_choice

label Chapter1_dec:
    Ben ""
    Ben "But are you sure you don't want to take it? It's pretty essential"

menu:
    "Yep, I don't want to take the case":
        Ben "Understandable, kiddo! Though you're missing up a whole check here."
        Ben "Welp I'll see you later!"
        #Add another route here.
        $ renpy.full_restart()
    "Wait! Lemme think again.":
        Ben "Alrighties, think critically here. Pressure's tight and the opportunity is rare."
        jump Chapter1_choice

label Case1:
    player "Fuck"