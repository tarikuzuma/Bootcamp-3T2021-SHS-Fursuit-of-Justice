# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")
define Ben = Character('Benjamin', color="#271c07")
define player = Character('player', color='#30b670')
define Cassie = Character('Cassie', color='#4f16d2bc')
define Lady = Character('Lady', color='#d23c16bc')
define Carl = Character('Carl', color='#905c0ff0')
define Iro = Character('Iro', color='#f6ce03ff')
define Barr = Character('Barretto', color='#7d8782ff')

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
    Ben "{i}sigh{/i}*"
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
    Cassie "{i}sigh{/i}"
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
    Ben "{i}Uhm I think they forgot I'm still here ;-;{/i}"
    player "Well you're still pretty smol, Cassi-"
    show zeil normal
    Ben "Ahem."

    #6th Scene
    Cassie "Ah..."
    player "Uhm..."
    Ben "Oh! Before I forget, congratulations, Cassie! You amazingly won your last case."
    Cassie "(OWO) Thank you sir ^-^ your guidance helped me tremendously <3"
    Ben "Still, you did a spectacular job! I'm so proud of you. "
    Cassie "{i}Blush{/i} Thank you so much, sir... TT-TT"
    show zeil annoyed
    player "{i}For always mocking me, she's still as affected of Ben's praise{/i}"
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
    Ben "Your objective is to see through this to the end."
    Ben "Are you going to accept the case or not?"
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
        Ben "Show them what your mighty Benjamin has taught you!"
        player "Yes, your honor!"
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

#Scene 8
label Case1:
    show black
    hide benjamin
    scene bg courtroom
    show zeil smile2 at center
    player "{i} Finally! I'm in my first official case procedure, I need to make sure that I can fight for the rights of my client! I will not fail you, Benjamin! {/i}"
    "Witnesses, please stand up"
    show zeil normal at left with moveinleft
    show ferret lady at right with moveinright
    Lady "For the trial, all rise. RTC Branch 139 is now in session. Honorable Carl please proceed"
    show carl neutral with moveinbottom
    Carl "Thank you, you may all be seated."
    "{i}Witnesses sits down{/i}"
    Lady "The court is now in session, we call on case number 119190 (Mr. Robert Barreto Versus the Court of Appeals and Ms. Rosa Barreto)"
    hide ferret lady with dissolve
    Carl "Is the Prosecution ready?"
    hide zeil
    hide carl

    #Show IRO with Ms. Baretto.
    show iro neutral with dissolve
    Iro "Arf"
    hide iro
    show carl neutral with dissolve
    Carl "..."
    hide carl with dissolve
    show iro neutral with dissolve
    Iro "..."
    Iro "I mean yes, your honor."
    hide iro
    show carl neutral
    Carl "Is the Defense ready?"
    
    #Show PLAYER with Mr. virgin
    hide carl
    show zeil normal
    player "Yes, your honor."
    hide zeil
    show carl neutral
    Carl "We will now hear the opening of the prosecution"
    hide carl
    show zeil delighted with dissolve
    player "Your honor, I am [povname] and I represent here Mr. Robert Barretto age 24, husband of Ms Rosa Barretto. "
    show zeil normal
    player "To explain the case, Ms Rosa Barretto wanted to annul their wedding due to the lack of intimacy that she experienced with Mr. Robert Barretto in the past 1 year of their marriage."
    player "As we all know, love comes in a different form not only in the act of sexual intercourse. As hard as it may, we would be defending the case, and once we had laid all the facts we hope that you will give us a verdict of DENIED."

    hide zeil
    show carl neutral with dissolve
    Carl "I see..."
    Carl "Would the defense want to make an opening statement?"
    Carl "Or would you rather let the defendant finish with their statement?"
    hide carl with dissolve

    show iro neutral with dissolve
    Iro "Your honor, we would like it for the defense to finish their statement before we make a decision."
    hide iro with dissolve

    show carl neutral with dissolve
    Carl "As per request of the prosecution side. Defense, you may now state your case."
    hide carl with dissolve
    show zeil normal with dissolve
    player "{i}This Iro is just gonna let me defend? He could rebute a lot right now. Should I let him go first?{/i}"

menu:
    "Deny and let him explain his stance":
        show zeil smile
        player "I think I am done with my introduction, I would like to hear the Prosecutor's stance or introduction now."
        #Write a boolean here that states true.
        $ DenyIro = True
        jump IroAdvance

    "Explain Further":
        show zeil smile2
        player "Thank you, I'll take the stage, sir."
        $ DenyIro = False
        jump IroAdvance

label IroAdvance:
    if DenyIro:
        hide zeil with dissolve
        show iro neutral with dissolve
        Iro "Alright, if you wish."
        jump Chap1Iro_Explain
    else:
        hide zeil with dissolve
        show carl neutral with dissolve
        Carl "Go on, [povname]"
        hide carl with dissolve
        jump Chap1Player_Explain

label Chap1Player_Explain:
    show zeil normal with dissolve
    player "Your honor, my client Mr. Barretto truly loves Ms Barretto."
    player "It is no doubt that Mr. Barretto tries to provide the intimate relationship that Ms Barretto wanted but according to his testimony, when such actions are being made, Ms Barretto refused to take one step further."
    hide zeil
    show gina neutral with dissolve
    Barr "Yeah..."
    hide gina
    show iro neutral
    Iro "{i}So much for filing a case, I'm toast{/i}"
    hide iro

    show carl neutral
    Carl "Go on."

    hide carl
    show zeil smile with dissolve
    player "Mr. Barretto also claims, that he forced his wife to have sexual intercourse with him only once but he did not continue because she was shaking and she did not like it."
    show zeil sad
    player "So he stopped to consideration for Ms. Barretto feelings."
    player "After these events, there had been 0 progress regarding their marriage life most especially, sexual life."
    show zeil bored
    player "In addition, a medical record had been made in order to prove that psychological incapacity is not the reason for the couple to not partake in an intimate relationship. His medical record stated that he can fully reproduce and has no problem regarding his libido."
    hide zeil

    show iro neutral with dissolve
    Iro "{i}Mr. Barr has a medical condition... he can't copulate no matter how hard he tries... {/i}"
    Iro "{i}oh my Dalmatians... this case really is a dead end for me.{/i}"
    hide iro

    show zeil normal with dissolve
    player "With respect to Article 68 of the Family Code which hearsay “the husband and wife are obliged to live together, observe mutual love, respect and fidelity, and render mutual help and support.” Mr. Barretto was only exhibiting the statement of Art 68 towards Ms. Barretto."
