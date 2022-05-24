# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")
define Ben = Character('Benjamin', color="#271c07")
define player = Character('player', color='#30b670')
define Cassie = Character('Cassie', color='#4f16d2bc')


# The game starts here.



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Finally, all my time spent in law school..."
    "All the money I spent..."
    "And the horrid, horrid, HORRIDD bar exam."
    "It has all come into a halt."
    "A new chapter of my life is unfloding."
    "This is not the end, but the beginning."
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

define player = Character("[povname]", color='#3633d7f6')

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
    player "I am still learning the basics"
    player "But that won't stop me!"
    show zeil delighted
    player "let's go to the lawfirm, shall we?"
    hide zeil

    with fade
    scene bg officefirm
    show zeil normal
    player "Hey, is that Benjamin sleeping in the firm?"
    show zeil normal at left
    with moveinleft
    pause (3.0) #Pauses screen and shows better transition till the next line.
    show benjamin neutral at right
    with moveinright
    pause (3.0)
    show zeil smile2

    #3rd Scene

    player "Yeah, it's him alright!"

#Menu to see what player will do to benjamin
menu:

    "Tap him":
        Ben "WAIT WHQAT WHO'S THERE?"
        jump benjaminWake
    
    "Wake him up":
        Ben "AGH I PROMISE I WASN'T SLEEPING!!"
        jump benjaminWake

label benjaminWake:
    show zeil laugh
    Ben "WHOA!-hey you scared me there [povname] , I didnt know youd be this early Ho Ho Ho"
    show zeil smile
    
    show zeil delighted at left
    show benjamin neutral at right
    player "I thought it’d be nice to start the day early today with my first case and all"
    Ben "Ah… yes, of course! That’s the kind of energy this firm needs..."
    Ben "*sigh*"
    Ben "Your first case… to think you were just getting coffee and printing papers just weeks ago…"

    show zeil smile
    player "Well, that’s all thanks to you Ben"
    Ben "No, really, you made it far with your own hard work."
    show zeil shocked
    player "But-"

    #Dito na ako, now going to introduce Cassie
    #ADD TRANSITIONSSS!! 
    #4th Scene
    show cassie neutral at center
    with moveinright
    Cassie "Just accept the compliment, [povname]"
    player "WAHH!!"
    show zeil bored
    player "Cassie, you scared me!"
    show zeil normal
    Cassie "*sigh"
    Cassie "I've been here all this time, dumdum! You were too busy sucking up to Benjamin to notice."
    show zeil annoyed 
    player "I'm greatful! There's a difference"
    Cassie "Sure thing."
    show zeil smug
    player "Even if I was... You'd do the same as well!"
    Cassie "That is SOOOOO not true!"
    show zeil angry
    "Bickering continues..."

    #5th Scene
    Ben "(Uhm I think they forgot I'm still here ;-;)"
    player "Well you're still pretty smol, Cassi-"
    show zeil normal
    Ben "Ahem."

    #6th Scene
    Cassie "Ah..."
    player "Uhm..."
    Ben "Oh! Before I forget, congratulations, Cassie! You amazingly won your last case."
    Cassie "(OWO) Thank you sir ^-^ your guidance helped me tremendously <3"
    Ben "Still, you did a spectacular job! I'm so proud of you. "
    Cassie "*Blush* Thank you so much, sir... TT-TT"
    show zeil annoyed
    player "(For always mocking me, she's still as affected of Ben's praise)"
    show zeil normal

    Ben "Now, I would like to ask you to handle the firm for a bit"
    Cassie "!!!"
    Ben "For now, I will assist [povname] with his first case"
    Cassie "Of course, sir!"
    Ben "Thank you, Cassie. I can always count on you."
    Cassie "Thank you sir ... o//o If you ever need me, I'll be in my office"
    Ben "Now let’s catch you up on your case, [povname] , I'll walk you through it"

    show black
    hide cassie

label chapter1_beforeTalk:

    scene bg isfirm with fade

    #ACT 1
    show zeil normal at left
    with moveinleft
    show benjamin neutral at right
    with moveinleft


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
    $ RouteChecker = 0 #routeChekcer states the amount of routes Taken.

#confirmation of case to see if player will accept or not
label Chapter1_choice:
menu:
    "Do the case":
        jump Chapter1_con #jumps to confirmation

    "Skip the case":
        Ben "Are you sure you don't want to take this case? I mean lawyers in our firm are pretty occupied now. Your decision is the thing I will fully respect."
        jump Chapter1_dec #jumps to declination

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
        jump Case1 #confirms case
    "Wait, let me think again.":
        Ben "Alright! No problem, just take your time in thinking."
        jump Chapter1_choice #goes back to route confirmation

label Chapter1_dec:
    Ben ""
    Ben "But are you sure you don't want to take it? It's pretty essential"

menu:
    "Yep, I don't want to take the case":
        Ben "Understandable, kiddo! Though you're missing up a whole check here."
        Ben "Welp I'll see you later!"
        #Add another route here. Completely declines firm.
        $ renpy.full_restart()
    "Wait! Lemme think again.":
        Ben "Alrighties, think critically here. Pressure's tight and the opportunity is rare."
        jump Chapter1_choice

label Case1:
    player "Fuck"