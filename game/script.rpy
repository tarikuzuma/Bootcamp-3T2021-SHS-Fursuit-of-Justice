# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5


define e = Character("Eileen")
define Zeil = Character('Zeil', color="#0000FF")
define Ben = Character('Benjamin', color="#271c07")
define player = Character('player', color='#30b670')
define Cassie = Character('Cassie', color='#4f16d2bc')
define Lady = Character('Baliff Lady', color='#d23c16bc')
define Carl = Character('Carl', color='#905c0ff0')
define Iro = Character('Iro', color='#f6ce03ff')
define Barr = Character('Mrs. Barretto (Gina)', color='#7d8782ff')
define Chi = Character('Mr. Barretto (Chi)', color='#7d8782ff')
define Bmom = Character('Beaverra Rivera', color='#4e4409ff')
define Nugget = Character('Nugget', color='#4e4409ff')
define Stumpy = Character('Stumpy', color='#4e4409ff')
define Paddles = Character('Paddles', color='#4e4409ff')
define Sheep = Character('Sheep De Lune', color='#fa01c4ff')
define Celtic = Character('Celtic of Dunrar Mifflin', color='#27ccc1ff')
define Witness = Character('Witness', color='#1caaa1ff')
define Beary = Character('Beary Bear', color='#47464bff')
define Crew = Character('Crew', color='#1caaa1ff')
define Guard = Character('Guard', color='#1caaa1ff')
define Hog = Character('Indigenous Hedgehog', color='#aa1c53ff')
define unk = Character('???', color='#290505ff')
define Felipe = Character('Felipe Fevidal', color='#290505ff')
define Tristan = Character('Tristan', color='#ff0000ff')
define Terisita = Character('Terisita', color='#00ff22ff')
define Theodora = Character('Theodora', color='#2c7f92ff')
define Bunoy = Character('Bunoy', color='#bc1eceff')
define Bryan = Character('Bryan', color='#40cc0dff')
define Totoy = Character('Totoy', color='#5087e7ff')
define Analyn = Character('Analyn', color='#a9bbdcff')
define John = Character('John', color='#8be681ff')
define Maria = Character('Maria', color='#2b8a21ff')
define Angel = Character('Angel', color='#a9701aff')
define Cesar = Character('Cesar', color='#94c481ff')

# The game starts here.

image splash = "splash.png"

label splashscreen:
    scene beach 
    with Pause(1)

    play sound "audio/sfx/sfx_seagull.wav" fadein 1.0

    show splash with dissolve
    with Pause(4.3)

    scene black with dissolve
    with Pause(3)

    stop music fadeout 3.0
    return


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "Finally, all my time spent in law school..."
    "All the money I spent..."
    "And the horrid, horrid, HORRIDD bar exam."
    "It has all come into a halt."
    "A new chapter of my life is unfolding."
    play music "audio/bgm_silence.wav" fadein 3.0 volume 0.3 #MUSIC BUTTON

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
    player "Okie! If that is the name you insisted then I'll go for it <3"
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

    play music "audio/bgm_lawfirm.mp3" fadein 3.0 volume 0.3 loop #MUSIC BUTTON

    scene bg officefirm with Fade(0.5, 0.0, 0.5)
    show zeil normal
    player "Hey, is that Benjamin sleeping in the firm?"
    show zeil normal at left
    with moveinleft
    pause (3.0) #Pauses screen and shows better transition till the next line.
    show benjamin sleep at right
    with dissolve
    pause (3.0)
    show zeil smile2

    

    #3rd Scene

    player "Yeah, it's him alright!"

#Menu to see what player will do to benjamin
menu:

    "Tap him":
        show benjamin neutral
        Ben "WAIT WHAT WHO'S THERE?" 
        jump benjaminWake
    
    "Wake him up":
        show benjamin neutral
        Ben "ARGH I PROMISE I WASN'T SLEEPING!!"
        jump benjaminWake


label benjaminWake:
    show zeil laugh
    Ben "WHOA!-hey you scared me there [povname] , I didnt know youd be this early Ho Ho Ho"
    show zeil smile
    show benjamin happy

    show zeil delighted at left
    show benjamin neutral at right

    player "I thought it’d be nice to start the day early today with my first case and all"
    Ben "Ah… yes, of course! That’s the kind of energy this firm needs..."

    show benjamin neutral
    Ben "{bt=2}{i}*sigh*{/i}{/bt}"
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

    show cassie mad
    Cassie "{i}sigh{/i}"
    Cassie "I've been here all this time, dumdum! You were too busy sucking up to Benjamin to notice."
    show zeil annoyed 
    player "I'm grateful! There's a difference"

    show cassie neutral
    Cassie "Sure thing."

    show zeil smug
    show cassie shocked
    player "Even if I was... You'd do the same as well!"

    show cassie mad
    Cassie "That is SOOOOO not true!"
    show zeil angry
    "Bickering continues..."

    #5th Scene
    Ben "{i}Uhm I think they forgot I'm still here ;-;{/i}"
    player "Well you're still pretty small, Cassi-"
    show zeil normal
    show cassie neutral
    Ben "Ahem."

    #6th Scene
    Cassie "Ah..."
    player "Uhm..."

    show benjamin happy
    Ben "Oh! Before I forget, congratulations, Cassie! You amazingly won your last case."
    show benjamin neutral
    show cassie happy
    Cassie "(OWO) Thank you sir ^-^ your guidance helped me tremendously <3"

    show benjamin happy
    show cassie blush
    Ben "Still, you did a spectacular job! I'm so proud of you. "
    
    Cassie "{i}Blush{/i} Thank you so much, sir... TT-TT"
    show zeil annoyed
    player "{i}For always mocking me, she's still as affected of Ben's praise{/i}"
    show zeil normal
    
    show benjamin neutral
    Ben "Now, I would like to ask you to handle the firm for a bit"

    show cassie shocked
    Cassie "!!!"

    show cassie neutral 
    Ben "For now, I will assist [povname] with his first case"

    show cassie happy
    Cassie "Of course, sir!"

    show benjamin happy
    Ben "Thank you, Cassie. I can always count on you."

    show cassie blush
    Cassie "Thank you sir ... o//o If you ever need me, I'll be in my office"

    show benjamin neutral
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
    Ben "Okay, to put in an easier context what we have here is Ms Rosa Barreto wanted to annul her marriage with Mr. Robert Barreto due to ---- "
    show zeil shocked
    player "Due to what your Honor?"


    show benjamin happy
    Ben "Due to {bt=2}*chuckles*{/bt}"
    show zeil bored
    show benjamin neutral
    player "Sir please say it already your building up the suspense"
    Ben "Due to their relationship failing because Mr Robert doesn't want to get intimate with Mrs. Rosa"
    show zeil normal
    player "sounds melo intense, sire."
    Ben "Your objective is to see through this to the end."
    Ben "Are you going to accept the case or not?"
    $ RouteChecker = 0 #routeChekcer states the amount of routes Taken.
    $ Objection_FirstCase = False

#confirmation of case to see if player will accept or not
label Chapter1_choice:
menu:
    "Do the case":
        jump Chapter1_con #jumps to confirmation

    "Skip the case":
        Ben "Are you sure you don't want to take this case? I mean lawyers in our firm are pretty occupied now. Your decision is the thing I will fully respect."
        jump Chapter1_dec #jumps to declination

label Chapter1_con: 
    show benjamin happy 
    Ben "Yoyoyo! Baby steps I tell ya! Baby steps."
    show zeil smile2
    player "oh shush!"
    Ben "Seems like a great decision for you to take your first case immediately."

    show benjamin neutral
    Ben "Though, are you sure about your decision?"

menu:
    "Yeah, I'm sure. Let's start!":
        $ RouteChecker += 1

        show benjamin happy 
        Ben "Great!!!!!!! Let's finally get started then."
        Ben "Show them what your mighty Benjamin has taught you!"
        player "Yes, your honor!"
        stop music fadeout 1.0
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
        stop music fadeout 1.0
        jump Chap1_Ending
    "Wait! Lemme think again.":
        Ben "Alrighties, think critically here. Pressure's tight and the opportunity is rare."
        jump Chapter1_choice

    

#Scene 8
label Case1:
    $ PlayerDoneChap1 = False
    $ IroDoneChap1 = False
    hide benjamin
    show black
    "[povname] went to court to defend Mr. Barretto regarding the annulment."
    

    show zeil smile2 at center with dissolve
    player "{i} Finally! I'm in my first official case procedure, I need to make sure that I can fight for the rights of my client! I will not fail you, Benjamin! {/i}"
    scene bg courtroom with fade
    "Witnesses, please stand up"

    play music "audio/bgm_courtroom.mp3" fadein 3.0 volume 0.3 loop #MUSIC BUTTON

    show zeil normal at left with moveinleft
    show baliff neutral at right with moveinright
    Lady "For the trial, all rise. RTC Branch 139 is now in session. Honorable Carl please proceed"
    show carl neutraltable with moveinbottom
    Carl "Thank you, you may all be seated."

    show carl neutraltable hammer
    play sound "audio/sfx/sfx_gavel1tap.wav"

    "{i}Witnesses sits down{/i}"

    show carl neutraltable
    Lady "The court is now in session, we call on case number 119190 (Mr. Robert Barreto Versus the Court of Appeals and Mrs. Rosa Barreto)"
    hide baliff neutral with dissolve
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
    Carl "We will now hear the opening of the Defense"
    hide carl

    show chi right at left with dissolve
    show zeil delighted with dissolve
    player "Your honor, I am [povname] and I represent here Mr. Robert Barretto age 24, husband of Ms Rosa Barretto. "
    Chi "Hello I'm Chi, also known as Mr. Barretto."
    hide chi with dissolve

    menu:
        "Explain the Case":
            show zeil normal
            player "To explain the case, Ms Rosa Barretto wanted to annul their wedding due to the lack of intimacy that she experienced with Mr. Robert Barretto in the past 1 year of their marriage."
            player "As we all know, love comes in a different form not only in the act of sexual intercourse. As hard as it may, we would be defending the case, and once we had laid all the facts we hope that you will give us a verdict of {b}DENIED.{/b}"
    

    hide zeil
    show carl neutral with dissolve
    Carl "I see..."
    Carl "Would the prosecution want to make an opening statement?"
    Carl "Or would you rather let the defendant finish with their statement?"
    hide carl with dissolve

    show iro neutral with dissolve
    Iro "Your honor, we would like it for the defense to finish their statement before we make a decision."
    hide iro with dissolve

    show carl neutral with dissolve
    Carl "As per request of the prosecution side. Defense, you may now state your case."
    hide carl with dissolve
    show zeil normal with dissolve
    player "{i}This Iro is just gonna let me defend? He could rebute a lot right now. I think it's best if I deny his humble advances... or should I risk it and explain further?{/i}"

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

    show iro mad
    Iro "{i}So much for filing a case if you're just gonna agree to that, Gina.{/i}"
    hide iro

    show carl neutral
    Carl "Go on."

    hide carl

    if not DenyIro:
        $ Objection_FirstCase = False
    if not Objection_FirstCase:
        show zeil smile with dissolve
        player "Mr. Barretto also claims, that he forced his wife to have sexual intercourse with him only once but he did not continue because she was shaking and she did not like it."
        
        show zeil sad
        player "So he stopped to consideration for Mrs. Barretto feelings."
        player "After these events, there had been 0 progress regarding their marriage life most especially, sexual life."
        
        show zeil bored
        player "In addition, a medical record had been made in order to prove that psychological incapacity is not the reason for the couple to not partake in an intimate relationship. His medical record stated that he can fully reproduce and has no problem regarding his libido."
        hide zeil

        show iro neutral with dissolve
        Iro "{i}Mr. Barr has {b}NO medical condition{/b}... he can copulate and concieve a baby...{/i}"
        Iro "{i}Based on Gina's explanations, he couldn't so I guess she was lying. {/i}"
        Iro "{i}oh my Dalmatians... this case really is a dead end for me.{/i}"
        hide iro
    elif Objection_FirstCase:
        show zeil smile with dissolve
        player "To restate what I said in my earleir objection..."
        player "Mr. Barretto also alleges that he forced his wife to engage in sexual activity with him only once, but that he did not continue because she was shivering and did not like it."
        player " So he came to a halt to evaluate Mrs. Barretto's sentiments. Following these incidents, they made little progress in their marriage, particularly in their sexual lives."
        show zeil normal
        player "In addition, a medical record was created to show that the couple's inability to have an intimate connection is not due to psychological incapacity. He can completely procreate and has no libido issues, according to his medical records."
        hide zeil

        show iro neutral with dissolve
        Iro "{i}Heh, nice tactic of repetition, rookie! I'm toast now.{/i}"
        hide iro

    show zeil normal with dissolve

    menu:
        "Mention Article 68 of the Family Code":
            player "With respect to Article 68 of the Family Code which hearsay “the husband and wife are obliged to live together, observe mutual love, respect and fidelity, and render mutual help and support.” Mr. Barretto was only exhibiting the statement of Art 68 towards Mrs. Barretto."

    show zeil sad
    player "Finally, the Catholic marriage tribunals stated, that a senseless and stubborn refusal an action to procreate is considered a sign of psychological incapacity."

    show zeil normal
    player "Which is what exactly Mrs. Barretto was doing whenever Mr. Barretto would initiate a move. With all due respect, I believe that Mr. Barretto doesn’t deserve the treatment that has been happening here."

    show zeil shocked
    player "Your honor, today you have heard our testimony regarding the annulment of Mrs. and Mr. Barretto. I would like to remind you of important information that you should think about before you make a decision."

    show zeil normal
    player "Mr. Barretto do truly loves Mrs. Barretto, he even initiated an intimate action for the two of them but Ms Barretto refused to continue, yes he might have gotten forceful but he considered Mrs. Barretto feelings and decided to cease his motives."
    player "His medical records show no difficulty with intimacy and do not fit the criteria into being psychological incapacity. When you decide your verdict, please find the petition to be denied."

    show zeil smile
    player "Thank you."
    hide zeil with dissolve

    $ PlayerDoneChap1 = True
    jump Chapter1_Checker

label Chapter1_Checker:
    if PlayerDoneChap1 and IroDoneChap1:
        jump Chapter1_Judge
    elif PlayerDoneChap1 and not IroDoneChap1:
        show carl neutral with dissolve
        Carl "The defense had finished their claim. Prosecution, your opening statement please, and all of your testimonies and findings."
        hide carl
        jump Chap1Iro_Explain
    elif not PlayerDoneChap1 and IroDoneChap1:
        show carl neutral with dissolve
        Carl "The Prosecution had finished their claim. Defense your opening statement please, and all of your testimonies and findings."
        hide carl
        jump Chap1Player_Explain

label Chap1Iro_Explain:
    show iro neutral with dissolve
    show gina neutral at right with dissolve
    Iro "Yes your honor, I am Iro Lockheart and I represent here Mrs. Rosa Barretto age 23, wife of Mr. Robert Barretto."
    Barr "Hello, I am Gina, also known as Mrs. Barretto."
    hide gina with dissolve

    Iro "To further elaborate the case, Mrs. Barretto  wanted to annul their wedding due to the lack of intimacy that she experienced with Mr. Barretto in the past 1 year of their marriage."

    if not DenyIro:
        Iro "Opposing earlier statement of [povname] it is very clear that Mr. Barretto doesn’t show any affection toward his wife and it would just lead to a failed relationship for the two."
    
    Iro "To make things easier for my client Mrs. Barretto decided to just close the marriage. As hard as it may, we would like to push forward the motion of the case, and once we had laid all the facts we hope that you will give us a verdict of {b}ACCEPTED.{/b}"

    hide iro with dissolve
    show carl neutral with dissolve
    Carl "You may proceed to layout all of your pieces of evidence and statements."
    hide carl

    show iro neutral with dissolve
    Iro "Thank you your honor. To start things off..."

    if not DenyIro:
        Iro "Putting the blame on Mrs. Barretto for being psychologically incapacitated is quite absurd. It’s clear that Mr. Barretto does not want to coitus with Mrs. Barretto because of his physical disorders. "
        Iro "However... I guess it's possible that Mr. Barretto cannot set the mood due to his uhm... short comings?"
        hide iro

        show chi neutral with dissolve
        Chi "Rude!"
        hide chi
        show iro neutral

    elif DenyIro:
        Iro "It’s impossible to think that for quite a long time, Mr. Barretto is not setting some mood to get intimate."

    if DenyIro:
        hide iro
        show zeil bored with dissolve
        player "{i}Now is my time to {b}OBJECT{/b} Iro's statement. I have something to say regarding Mr. Barretto's assumed disorders."

        menu:
            "OBJECTION!":
                $ Objection_FirstCase = True
                show zeil shocked with vpunch
                player "OBJECTION!"
                hide zeil

                show carl neutral with dissolve
                Carl "What is it, Mr. [povname] ?"
                hide carl

                show zeil normal with dissolve
                player "Mr. Barreto has had this situation ever since his marriage with Mrs. Barretto."
                player "Mr. Barretto claims that he forced his wife to have sexual intercourse with him only once but he did not continue because she was shaking and she did not like it."

                show zeil sad
                player "So he stopped to consideration for Mrs. Barretto feelings."
                player "After these events, there had been 0 progress regarding their marriage life most especially, sexual life."
                
                show zeil bored
                player "In addition, a medical record had been made in order to prove that psychological incapacity is not the reason for the couple to not partake in an intimate relationship. His medical record stated that he can fully reproduce and has no problem regarding his libido."
                hide zeil

                show carl neutral with dissolve
                Carl "Oh... is that so? What does the proescutor have to say regarding this?"
                hide carl
                show iro surprised with dissolve

            "Let it be":
                $ Objection_FirstCase = False
                show zeil smile
                "{i}I'll see where this goes.{/i}"
                hide zeil
                show iro neutral with dissolve

    if Objection_FirstCase:
        Iro "Oh uhm... {i}I was not expecting that{/i}"
        Iro "{i}I have a reallllyy high possibility of being toasted tonight! Might as well go on and see where this goes ... hays ...{/i}"
        show iro neutral
    elif not Objection_FirstCase:
        Iro "To strenghten our claims..."

    Iro "For a long time that Mr. and Mrs. Barretto were married only 2 attempts were made for them to have sexual intercourse."
    Iro "That count is relatively low for the time that they were together. It had even come to the point that Mrs. Barretto would initiate a honeymoon for them but ended up failing because of Mr. Barretto‘s action of inviting the whole family."
    Iro "They have separate rooms for the guest and the couple but for the whole duration of the trip, not at least one interaction was made for them to get intimate."

    if not Objection_FirstCase and DenyIro:
        Iro "This can’t be just a mere refusal, it's clear that Mr. Barretto might have not only a physical disorder but also be physiologically incapacitated."

    if not Objection_FirstCase and DenyIro:
        Iro "Lastly, procreating children is based on the universal principle that the procreation of children through sexual cooperation is the basic end of a marriage."
        Iro "Mr. Barretto failed to execute such action proving that Mr. Barretto does lack in a specific aspect of his body."
        hide iro

        show zeil normal with dissolve
        player "Here is my chance to {b}object{/b} once more. I have to say this!"
        menu:
            "OBJECTION!":
                $ Objection_FirstCase = True
                show zeil shocked with vpunch
                player "OBJECTION!"
                hide zeil

                show carl neutral with dissolve
                Carl "What is it, Mr. [povname] ?"
                hide carl

                show zeil normal with dissolve
                player "Mr. Barreto has had this situation ever since his marriage with Mrs. Barretto."
                player "Mr. Barretto also claims that he forced his wife to have sexual intercourse with him only once but he did not continue because she was shaking and she did not like it."

                show zeil sad
                player "So he stopped to consideration for Mrs. Barretto feelings."
                player "After these events, there had been 0 progress regarding their marriage life most especially, sexual life."
                
                show zeil bored
                player "In addition, a medical record had been made in order to prove that psychological incapacity is not the reason for the couple to not partake in an intimate relationship. His medical record stated that he can fully reproduce and has no problem regarding his libido."
                hide zeil

                show carl neutral with dissolve
                Carl "Oh... is that so? What does the proescutor have to say regarding this?"
                hide carl

                show iro surprised with dissolve
                Iro "{i}OH MY DALMATIANSSSSS!!!!!!!!{/i}"
                Iro "{i}An objection, right I was about to end the case...{/i}"
                Iro "{i}You've got to be kidding me, arfies. Oh well, I'll see where this goes.{/i}"
                Iro "I would like to make my closing statement."


            "Let it be":
                $ Objection_FirstCase = False
                "{i}I'll see where this goes.{/i}"
                hide zeil
                show iro neutral with dissolve

    Iro "Your honor, I have provided all of my statements in today's hearing, I would like to remind you that Mr. Barretto claims are weak to act as evidence or claims in opposition to our statements."
    Iro "Mrs. Barretto did nothing wrong in the relationship and just only wants the best for their marriage and family."
    Iro "When you decide your verdict, please find the petit  ion to be accepted."
    Iro "Thank you."
    hide iro with dissolve

    $ IroDoneChap1 = True
    jump Chapter1_Checker

label Chapter1_Judge:
    show carl neutral
    Carl "Hays... a tough case... roughly took us 1 hour to end it."
    Carl "I need to make a verdict though."
    Carl "This Court, looking at the consequences of the failed relationship in which the Mrs. and Mr. Barretto found themselves trapped in its mire of unfulfilled vows and unconsummated marital obligations."
    Carl "Hays... we can do no less but sustain the studied judgment of respondent appellate court."
    Carl "With the current conditions that we are in. The Court of Appeals' decision dated on November 23, 2020 is hereby {b}AFFIRMED{/b} in all aspects, and the petition is hereby {b}DENIED{/b} for lack of merit."
    
    play sound "audio/sfx/sfx_gavel1tap.wav"
    show carl hammer with vpunch #MAKE SOUND EFFECT
    "*Hammer Noise*"
    stop music fadeout 1.0
    hide carl with Fade(1.5, 0.0, 0.5)

label AfterChap1:
    show zeil smile2 at left with dissolve
    show benjamin neutral at right with dissolve

    play music "audio/bgm_victory.wav" fadein 3.0 volume 0.3 loop
    player "{i}I did it, Benjamin! I won my first case!{/i}"

    show benjamin happy
    Ben "Nice one, kiddo! I knew you could do it!"
    Ben "My pride has further established dominance!" 
    Ben "Tonight we shall celebr-"

    show zeil normal
    show benjamin neutral
    "{bt=2}Benjamin's Phone Vibrates{/bt}"

    Ben "Heh... looks like I gotta do something important, kiddo."
    player "What is it, Ben-"

    show benjamin happy 
    Ben "Gotta blast!"
    hide benjamin with moveoutleft

    show zeil annoyed
    player "That's weird, I swore that he had time for me..."
    
    pause (1.5)
    show zeil sad
    pause (1.5)
    player "..."

    show zeil smile
    player "Oh well, I'll just surprise him in the firm-"
    
    show zeil shocked with hpunch
    Chi "I swear I love you, Gina!"
    hide zeil

    #I tried adding a scene for the rabbits. I based it off something that would happen in real life haha fuck 
    show chi right at left with dissolve
    show gina neutral at right with dissolve
    Barr "You don't! You always make things awkward!"
    Chi "Honey, you know I'm trying hard to make this work, right?"
    Barr "Oh yeah, if you are, then EXPLAIN TO ME WHY WE'RE IN COURT RIGHT NOW!"
    Chi "Well.. I-"
    Barr "You're so gullible and cute, at the same time you're so casual!"
    Barr "It's like you don't love me :("
    Chi "Honey..."
    Barr "Don't honey me!"
    hide gina with easeoutright

    Chi "Hays..."
    Chi "I swear, I'll make this marriage work!"
    hide chi with easeoutright

    show zeil normal with dissolve
    player "Tough times..."
    player "Welp, I gotta get back now."

    stop music fadeout 3.0 
    hide zeil with moveoutleft 
    
label Chap1_Ending:
    scene bg isfirm with Fade(1.5, 0.0, 0.5)
    play music "audio/bgm_sneakyben.mp3" fadein 3.0 volume 0.3 loop
    "{i}Inside the firm in a silent evening...{/i}"
    show benjamin serious at left with dissolve
    Ben "Hmm..."
    Ben "So that's what's happening in cout de Forest..."

    if RouteChecker == 0:
        Ben "Case asside, ashamed to see my student bail his first case."
        Ben "Opportunities are rare."
        Ben "What a bad time to be in."
    play sound "audio/sfx/sfx_knock.wav"
    "{i}Knock Knock{/i}"

    show benjamin neutral
    Ben "Come in!"

    show cassie neutral at right with easeinright
    Cassie "Sir, here is your requested coffee"

    show benjamin happy
    Ben "Thank you, Cassie."

    show benjamin neutral
    Ben "{i}I'll have to fix this case fast...{/i}"
    Cassie "..."
    Cassie "Sir, if you don’t mind me asking, what are you working at right now?"
    Cassie "It looks like you’re not getting a decent rest and it feels like you are in a tight position."
    pause (3.0)
    Cassie "By any chance, is there something that I could do to make you feel at ease?"

    show benjamin happy
    Ben "You worry too much, child."
    Ben "Thank you for asking, but this is realllly nothing."

    show benjamin neutral
    Ben "How about you head out for tonight, don’t worry about me I’ll take a decent rest after I’m done with this."
    Cassie "Alright sir, good work for today!"

    show benjamin neutral
    hide cassie with easeoutright
    pause (3.0)
    show benjamin serious with dissolve
    Ben "Okay... back to my leads."
    "Benjamin continued working all night with a case no one knows about."
    stop music fadeout 5.0

    show black with Dissolve(3.0, alpha=False, time_warp=None)
    "- - - End of Act 1 - - -"
    "This is a good time to save your data."
    "To save your data, press the Q.Save Button below the screen to overwrite old ones."
    "To load past data, press the escape button, or press Q. Load"
    "After all, this is a visual novel. You have the right to reload old and new ones."
    "Or if you want, you can save here."
    menu:
        "Quick Save!":
            $ renpy.force_autosave(take_screenshot=False, block=False)
        "I Already Saved!":
            "Alright"

    "Would you like to continue the story?"

    menu:
        "Continue":
            "Have fun!"
        "Leave":
            "Good bye ^ - ^"
            $ renpy.full_restart(target="_main_menu")

label Chapter2_Start:
    scene bg osfirm with Fade(1.0, 1.5, 0.5)
    play music "audio/bgm_lawfirm.mp3" fadein 3.0 volume 0.3 loop
    show zeil smile2 with dissolve
    player "I feel so pumped after winning that first case!"
    player "I'm going to share the details with benjamin today."

    show zeil smile
    player "I wonder if he's busy for that?"

    show zeil normal
    player "I have to ask him."
    hide zeil with easeoutright

    scene bg isfirm with dissolve
    show zeil smile2 with dissolve
    player "Good morning sir!"

    show zeil shocked
    player "Oh, he's not here..."

    show zeil annoyed
    player "I wonder where he is..."
    hide zeil with dissolve

    scene bg officefirm
    show zeil smile at left with dissolve
    player "Oh.. Cassie, good morning!"

    show cassie sad at right with dissolve
    Cassie "..."

    show cassie neutral
    Cassie "G..good morning, [povname]"

    show cassie sad
    show zeil normal
    player "{i}Cassie looks worried...{/i}"

    show zeil smile
    player "Benjamin isn’t in yet? That’s new. He’s usually the first to be here."
    Cassie "Well... he was the {b}latest{/b} to leave yesterday."
    player "Maybe he had a late night and slept in."

    show zeil smile2
    player "I’m sure he’ll text or email us when he’s awake."
    Cassie "Yeah... you're right."
    pause (1.0)

    if Objection_FirstCase: #Route if Player objected. Cassie Kilig moments
        show cassie happy
        Cassie "Oh right! Before I forget, you handled your first case well."

        show zeil normal
        player "Really?"
        Cassie "Yep, you let the prosecuter explain first, which gave you chance to object."
        Cassie "Psychologically, that's dangerous."

        show zeil delighted
        player "Welp looks like I learned quite a lot in lawschool!"

        show cassie neutral
        Cassie "You used to be that nerdy guy with a hoodie in class."

        show zeil annoyed
        Cassie "Look at you now."
        player "Really? Nerdy?"

        show cassie mad
        Cassie "That's a compliment!"

        show zeil smug
        player "Oh yeah, if I'm a nerd then you're a midget!"
        Cassie "Hey, stop- {move}stop that!!{/move}"

        show zeil smile2
        player "Hah! Just teasing you! You've gotten more confident, you know?"


        show cassie blush
        Cassie "{i}Blush{/i} Y-yeah..."
        "..."
        Cassie "Thanks, [povname] ... I guess 'confident' is a better compliment than 'nerdy'"
        player "heh, don't mention it"

    show cassie happy
    show zeil smile
    Cassie "Oh, right! I stopped by that cafe that just newly opened."
    player "Oh yeah, the one right by the elementary school? How was it?"
    show zeil smile2
    Cassie "Yeah, that one!"
    Cassie "Their pandesal is a taste of heaven on earth"
    show zeil laugh
    player "Really? Well, one of these days, I'll try them!"
    Cassie "They sell them in packages, and actually… "

    show cassie neutral
    Cassie "Uhm..."
    Cassie "I may have bought too many?"

    show zeil shocked
    player "Really? Who sells pandesals in packages?!"
    Cassie "Hmp! Them appearantly."
    show zeil laugh
    player "Hahaha! Good one, Cassie!"
    pause (1.0)

    "....."
    "......."
    show zeil normal
    "........."

    Cassie "So..."
    Cassie "You can have the rest of them"

    show zeil shocked
    player "For real?! You shouldn't have."
    Cassie "It’s nothing big…"

    show zeil smile
    player "You'd think that but it's actually really sweet of you to do me a favour!"
    player "I haven't eaten breakfast!"

    show cassie tsunblush
    Cassie "HEY! I-- I would've given Ben as well if he were here!"
    Cassie ">:( So don't feel special, alright?!"

    show zeil laugh
    player "Whatever, thank you Cassie!!"
    player "I should treat you sometime too <3"

    show cassie blush
    Cassie "Th..that would be nice :)"

    "..."
    "...."
    show zeil normal
    show cassie neutral
    "......"
    
    Cassie "Anyways..."
    player "Yeah..."

    Cassie "Oh! I didn't flip the 'Open' sign. I should do that."
    show zeil smile
    player "Ah no! Let me, I was the last to arrive anyways."
    Cassie "Oh okay, do that..."
    Cassie "Uhm... I'll be in my office if you need me."
    player "Yeah me too."
    show zeil normal
    player "I mean I'll be in my office"
    player "After this, I mean"
    Cassie "See ya."
    hide cassie with dissolve
    pause(1.0)

    player "{i}{sc}{move}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/move}{/sc}{/i}"
    player "Hays.. that was awkward."
    hide zeil with dissolve

    scene bg reccomp with dissolve
    show zeil normal with dissolve
    player "{i}That was extremely awkward!{/i}"

    show zeil smile
    player "{i}But despite us always bickering, it’s nice to know she does care about Ben and I.{/i}"
    player "Speaking of Ben, I should message him and see if he's alright."

    stop music fadeout 3.0
    play music "audio/bgm_bmomworry.wav" volume 0.3 fadein 3.0 loop #MUSIC INPUT
    show zeil shocked at left with easeinleft

    play sound "audio/sfx/sfx_knock.wav"
    "{i}KNOCK KNOCK{/i}"

    "Hello? Is someone in?"
    player "Oh yes, would you like to talk?"
    "Yes please..."

    show zeil normal
    player "Come in, come in."

    show mommabeaver neutral at right with easeinright
    player "Please, take a seat and make yourself comfortable. How may I help you today?"
    show mommabeaver cry
    show zeil shocked
    Bmom "Please, my kids have gotten into a national situation and need help."
    player "I'm all ears. Please tell me what happened."

    show zeil bored
    player "{i}Her situation seems serious.{/i}"

    show zeil sad
    show mommabeaver sad
    Bmom "They let a petition sign all over the City, and thousands of people agreed to stop the continued cutting of virgin forests all around the country. My children are going into a fight with a big company, and they’re not going down without a fight."
    player "{i}I've heard about this issue... thought it was poorly explained by the media. These kids are brave.{/i}"
    Bmom "Will you please help them?"

label Chapter2_Choice:
    show zeil normal
    player "{i}Think, [povname] , this situation is big. It's so big that this might take me quite a while to finish.{/i}"
    player "{i}Should I take it? I barely have any experience...{/i}"

    show zeil sad
    player "{i}I might mess this up...{/i}"

    menu:
        "Take the case":
            show zeil angry
            player "{i}I have a concept of justice. I must uphold this view 'till the end.{/i}"
            jump Chapter2_Con
        "Reject the case":
            show zeil normal
            player "{i}The case is big, I don't think I can handle it...{/i}"
            jump Chapter2_Dec

label Chapter2_Con:
    player "I'm willing to take the case, ma'am."

    show mommabeaver shocked
    show zeil smile2
    player "Your kids are very brave, you must very proud."

    show mommabeaver neutral
    Bmom "T-thank you!! Though are you sure you'll help me 'till the end?"
    Bmom "This case is just... life-draining, and I can't find anyone who can help me!"

menu:
    "Yeah, I'm sure. Let's do it!":
        player "Yeah, I'm sure of it, ma'am!"

        show mommabeaver shocked
        Bmom "WAIT YOU ARE?!"

        show zeil shocked
        player "Y-yeah?"

        show zeil normal
        show mommabeaver cry
        Bmom "N-No one has ever agreed to help me..."
        Bmom "I'm getting all emotional now T-T"
        Bmom "Every Lawfirm agreed to back me down."
        Bmom "But your lawfirm is special..."

        show zeil shocked
        show mommabeaver cry at left with easeinright
        Bmom "I have nothing to say but thank you! {i}{bt} cries and hugs [povname] {/bt}{/i}"
        player "Woah there hehe we'll try whatever we can to help you"

        show zeil smile2
        show mommabeaver cry at center with moveinleft
        Bmom "Yes! I'll do whatever I can to help you."

        $ RouteChecker += 1

        jump Case2_BeforeTalk

    "Wait, let me think again.":
        show zeil normal
        player "Wait, let me think again."
        Bmom "Alright.., take your time"
        jump Chapter2_Choice



label Chapter2_Dec:
    player "I'm not willing to help you, ma'am..."
    player "The burden is too big for a rookie like me..."

    show mommabeaver sad
    Bmom "Aww, I'm sure you can do it ! :("
    Bmom "I need anyone right now :("

menu:
    "Sorry, I cant.":
        show zeil shocked
        show mommabeaver neutral
        Bmom "O..Okay :) I.... I understand {i}sobs{/i}"

        show zeil sad
        Bmom "I'll be leaving now, Good bye !"
        hide mommabeaver cry with moveoutright

        player "That was hard..."
        stop music fadeout 2.0
        $ renpy.full_restart() #ADD more scenes here PLEASE
    "Wait, let me think again.":
        show zeil normal
        player "Wait, let me think again."
        Bmom "Alright.., take your time"
        jump Chapter2_Choice

label Case2_BeforeTalk:
    scene bg isfirm with dissolve
    show zeil normal at left with dissolve
    show mommabeaver neutral at right with dissolve

    player "So how exactly did they get into this mess?"
    Bmom "They circled a petition all around the country..."
    player "A petition about what?"

    show zeil smug
    player "{i}A petition huh... I bet they didn't even reach a thousand.{/i}"
    player "Go on..."

    show mommabeaver sad
    Bmom "They wanted to stop the extremete logging activities Dunrar Mifflin is conducting..."

    #add effect that adds silent when these lines catch up.
    show zeil shocked
    player "Dunrar Miffl-..."
    player "YOU MEAN THE {b}BIGGEST{/b} {sc}PAPER COMPANY IN THE COUNTRY?!{/sc}"
    Bmom "Y-yeah..."
    player "Ma'am... we're up against something really big..."

    show zeil normal
    player "When you stated 'Virgin Forests' I thought you meant that we're stopping a small company with little amounts of power..."

    show mommabeaver cry
    Bmom "{bt}I'm so-sorry I didn't tell you!!{/bt}"

    player "It's okay, ma'am"

    show mommabeaver neutral
    player "Can you tell me more about this petition? How many did they reach?"

    

    show zeil shocked
    show mommabeaver shocked
    Bmom "Surprisingly, they reached over hundreds of thousands of signatures in 1 month!"
    player "W-WAIT! {sc}OVER A THOUSAND?!{/sc}"

    show mommabeaver cry
    Bmom "Y-YEAH!!!!! T-T That is why most lawfirms don't accept us!"

    show zeil normal
    player "Miss, is it okay if we just dodge this fight? To be fair, it's just a harmless petition."

    show mommabeaver sad
    Bmom "We can't..."
    player "Why so?"
    Bmom "Because a lot of people are hoping for this activity to stop"
    Bmom "and..."
    Bmom "Dunrar Mifflin is hiring a fierce lawyer..."
    
    show zeil bored
    Bmom "A lawyer who graduated as valedectorian in the University of the Philippines"

    show zeil shocked
    player "A {sc=1}l-law{/sc}{sc=3}yer...{/sc}{sc=5}A VALEDICTORIAN from UP?!{/sc}"
    player "{sc=1}{i}Think, [povname] ... {/i}{/sc}"
    
    show zeil normal
    player "{sc=1}{i}this isn't your usual annulment or rundown restraining order.{/i}{/sc}"
    player "{sc=1}{i}We're talking about a big company who has made Billions...{/i}{/sc}"

    show zeil sad
    player "{sc=1}{i}Chri-Christ... I'm trembling{/i}{/sc}"

    show zeil normal
    player "{sc=3}I'ma just {/sc}{sc=1}calm down{/sc} now..."
    player "Ma'am, has the company pressed charges yet?"

    show mommabeaver neutral
    Bmom "Not yet..."

    show zeil bored
    player "{i}I think they're waiting for us to take the initiative and charge them first.{/i}"
    player "Seems like we're gonna handle quite a lot of loopholes here."
    player "The halting of deforestations..."
    player "Moreover.... to represent a generation..."

    show zeil smile
    player "I was never wrong into thinking that your kids are brave!"

    show mommabeaver cry
    Bmom "T-thank you :("
    player "I'll try my best to handle this case, ma'am."

    show zeil delighted
    player "I'm doing this for the future of our environment!"

    show zeil smile2
    Bmom "You are indeed doing all of us a favour..."
    Bmom "You're the bravest lawyer I've met so far."

    show zeil normal
    player "I hope for good things to come at us, ma'am."
    player "I'll study the case for further details."

    show black with dissolve
    "and so, [povname] studied the case for three weeks straight."

    jump Case2

label Case2:
    show black with Fade (0.5, 0.5, 0.5)
    stop music fadeout 3.0
    "Three Weeks Later..."
    "Court day."
    "It's advisable that you quick save here."
    "A series of wrong decisions will restart the game."

    play music "audio/bgm_review.wav" volume 0.3 fadein 3.0 loop #MUSIC INPUT
    scene bg courtroom with Fade(2.0, 0.0, 0.5)
    player "The Judge isn't here yet..."

    show zeil normal with dissolve
    player "The courtroom seems to be empty."

    show zeil delighted
    player "To be fair, I entered 30 minutes early."
    player "I'll just find a spot and study my case. Ms. Rivera was kind enough to help me research information."
    player "{i}Sits down{/i}"
    hide zeil with dissolve


label Case2_BeforeReview:
    show letter chapter2 with dissolve
    player "Let's have an overall review."
    window hide
    pause
    window show
    player "Heh, I like the footer."
    player "So... Ms. Rivera's kids acquired {b}105,923 petitioners{/b}."
    player "She wasn't kidding. I even have the petition documents in my suitcase."
    player "Do they also want these laws to be implemented? Dang, they're asking for a lot."
    player "Last but not least, we'll heavily base our actions on {b}Article 2, Section 16{/b}. The right to have a healthy environment"
    hide letter chapter2 with dissolve

    show zeil delighted with dissolve
    player "Welp, I'm all fired up!"

    show zeil smile
    player "{b}It seems like I have to base my answers on what's written in this leaflet. I have to memorize them to sound confident!{/b}"

    show zeil sad
    player "I don't wanna sound like a clown in court."

    show zeil normal
    player "Am I ready?"

    window hide
menu:
    "Start The Case.":
        window show
        player "I guess I'm ready! Time to go to unknown grounds."
        player "I'll wait for the bell to star-"

        show zeil shocked at left with easeinleft
        Bmom "[povname] !!!"

        show mommabeaver neutral at right with easeinright
        show zeil smile2
        player "WOAHH!! Good morning, ma'am!"
        Bmom "Good morning to you too!!"
        player "I was just reading our case hehe. What brings you here?"
        Bmom "Hehe glad to hear you're diligent with the case."

        show zeil normal
        Bmom "I want you to meet my children!"
        hide zeil with dissolve
        hide mommabeaver with dissolve

        show nugget neutral with dissolve
        Bmom "This is Nugget! He's the youngest in our family."
        Nugget "E..h :("
        Bmom "Go on, Nugget. Say hello!"
        Nugget "He-Hello!"
        Bmom "Louder!!"
        Nugget "{rotat}hellwo!!{/rotat}"
        player "Cute!!!!"
        hide nugget with dissolve

        show paddles neutral with dissolve
        Bmom "She's Paddles, the second child."
        Paddles "Good day, sir."
        Bmom "She has good manners!"
        Paddles "M-mister [povname] !"
        player "Yeah?"
        Paddles "Someday, I want to be a lawyer like you!"
        player "Aww! I'm sure you'll get there!"
        hide paddles with dissolve

        show stumpy neutral with dissolve
        Bmom "Last but not least, this is my responsible Stumpy! The eldest among all."
        Stumpy "Good morning. Pleased to meet you, Mr. [povname]."
        Bmom "Fancy!"
        Stumpy "Sir, I hope to work with you soon. Let us win this case! For the better good of many."
        player "Y-you bet!"
        hide stumpy with dissolve

        show mommabeaver neutral at right with dissolve
        show zeil smile at left with dissolve
        Bmom "Let's give it our all, team!"
        show zeil smile2
        player "Let's do this!"
        player "{i}I gotta give it my all! For them.{/i}"
        jump Case2_Start

    "Wait, review more.":
        window show
        show zeil annoyed
        player "Sheeeesh I gotta learn more."
        hide zeil with dissolve
        jump Case2_BeforeReview

label Case2_Start:
    stop music fadeout 3.0
    scene bg courtroom with Fade(0.5, 0.5, 0.5)
    play music "audio/bgm_courtroom2.wav" volume 0.3 fadein 3.0 loop
    show carl neutraltable with dissolve
    show baliff neutral at right with dissolve

    #Player Health Indicator
    $ PlayerChance = 3

    #Boolean to Check if Player or Sheep has already explained
    $ Chap2Player_Explain = False
    $ Chap2Sheep_Explain = False

    pause (1.5)
    show carl neutraltable hammer
    play sound "audio/sfx/sfx_gavel1tap.wav"
    Carl "As you may know, every court has a national law. These aren't just basic rules we have to follow idly, but rules we have to follow for our lives! It is justice! "
    Lady "Whoa there your hono-"

    show carl neutral
    Carl "Hehe I’m just kidding. But jokes aside, we have to follow the national rules. Stand up, witnesses!"
    "{fi}witnesses stand up{/fi}"
    Lady "I *state your name* solemnly, sincerely and truly declare and affirm that the evidence I shall give shall be the truth the whole truth and nothing but the truth." 
    hide carl
    hide baliff

    show zeil normal with dissolve
    player "I [povname] solemnly, sincerely and truly declare and affirm that the evidence I shall give shall be the truth the whole truth and nothing but the truth." 
    hide zeil

    show sheep neutral with dissolve
    Sheep "I Sheep De Lune solemnly, sincerely and truly declare and affirm that the evidence I shall give shall be the truth the whole truth and nothing but the truth." 
    hide sheep 
    
    show zeil annoyed with dissolve
    player "{i}So that's Sheep De Lune. For a lawyer, her style looks flashy.{/i}"
    hide zeil

    show carl neutral with dissolve
    show baliff neutral at right with dissolve
    Lady "For the trial, all rise. Trial 101083 in now in session. Honorable Carl Cabales please proceed"
    hide baliff with dissolve

    Carl "Thank you! You may all be seated."
    Carl "Is the prosecutor ready?"
    hide carl

    show zeil normal
    player "Yes, your honor."
    hide zeil

    show carl neutral
    Carl "How about the defense?"
    hide carl

    show sheep neutral
    Carl "Yes, your honor."
    hide sheep

    show carl neutral
    Carl "Great! We will now hear the opening statement of the prosecution."
    Carl "[povname] , may you please explain your stance?"
    hide carl

    show zeil delighted at right with dissolve
    show triplet neutral at left with dissolve
    player "Your honor, I have 3 humble clients today all having the same age: 16."
    player "They’re siblings accompanied today by their mother as you may see in the audience."
    Paddles "Hi mom! I'm wearing my favorite tophat today!"

    show zeil smile2
    Bmom "Gooo guys! <3"

    show zeil smile
    player "As I may explain, these young enthusaists care for the environment."
    hide triplet neutral with dissolve

    show zeil normal at center with easeinright
    player "Needless to say, each generation owes it to the next to maintain that rhythm and harmony in order to fully enjoy the benefits of a balanced and healthy ecological."
    player "Based on..."

    show zeil 
    player "{i}Christ, I am {sc=1}shaking {/sc} What article or sectiom gives people the purpose to maintain a balanced and healthy ecology again?{/i}"

    show zeil annoyed
    player "{i}I can't mess up or else this Sheep De Lune will bug me allthroughout the session.{/i}"
    hide zeil with dissolve
    window hide


    menu:
        "Section 2 of Republic Act No. 2874": #Wrong
            show zeil normal with dissolve
            player "Based on Section 2 on Republic Act No. 2874, the act states otherwise"
            hide zeil

            show sheep neutral
            Sheep "Sorry to interrupt your sentence, Mr. [povname] . To avoid misleading everyone, Section 2 of Republic Act No. 2874 states that..."
            Sheep "timber and mineral lands shall be governed by special laws and nothing in this Act provided shall be understood or construed to charge or-modify the government and disposition of the lands commonly called 'friar lands "
            Sheep "This does not correlate with the law you stated earlier. Frankly, this act of ignorance is against my standard of court."
            $ PlayerChance -= 2
            hide sheep with dissolve

            show zeil annoyed
            player "{i}Pfft she does bug me.{/i}"

            show zeil normal
            player "My apologies. What I meant was Section 16, Article II of the 1987 Constitution."
            

        "Section 2, Article II of the 1987 Constitution": #Wrong
            show zeil normal with dissolve
            player "Based on Section 2, Article II of the 1987 Constitution, the act states otherwise"
            hide zeil

            show sheep neutral
            Sheep "Sorry to interrupt your sentence, Mr. [povname] . To avoid misleading everyone, Section 2, Article II of the 1987 Constitution states that..."
            Sheep "The Philippines renounces war as an instrument of national policy, adopts the generally accepted principles of international law as part of the law of the land. "
            Sheep "and it adheres to the policy of peace, equality, justice, freedom, cooperation, and amity with all nations."
            Sheep "They are in the same constitution, but please, do not get them mixed up. We're talking about ecological health here, not land laws."
            Sheep "This does not correlate with the law you stated earlier. Frankly, this act of ignorance is against my standard of court."
            $ PlayerChance -= 2
            hide sheep with dissolve

            show zeil annoyed
            player "{i}Pfft she does bug me.{/i}"

            show zeil normal
            player "My apologies. What I meant was Section 16, Article II of the 1987 Constitution."
        "Section 16, Article II of the 1987 Constitution": #Right
            show zeil normal with dissolve
            player "Based on Section 16, Article II of the 1987 Constitution, the act states otherwise"

    show zeil delighted
    player "To put it another way, the minors' assertion of their right to a healthy environment is also the fulfillment of their responsibilities to guarantee that that right is protected for future generations."
            
    show zeil angry
    player "In terms of the right to a balanced and healthy ecological, their ability to sue on behalf of future generations can only be founded on the idea of intergenerational responsibility."

    show zeil normal
    player "On the environmental behalf of the {b}generation that is unborn{/b}, my clients will represent them"
    player "The same was filed for themselves and others who are equally concerned about the preservation of the virgin tropical forests."
    player "The opposition is ordering defendant, his agents, representatives and other persons acting in his behalf to:"

    menu:
        "State the Acts They Want Implemented.":
            show zeil delighted
            player "(1) Cancel all existing timber license agreements in the country;
                    (2) Cease and desist from receiving, accepting, processing, renewing or approving new timber license agreements.
                    "
    
    show zeil smile
    player "That is all."
    hide zeil with dissolve

    show sheep neutral with dissolve
    Sheep "{i}I admire these kids' energy... to represent a generation they haven't met is bonkers. But... I like that.{/i}"
    hide sheep with dissolve

    show carl neutral with dissolve
    Carl "These kids are representing a whole generation huh?"
    Carl "That’s a bit ideal, though I can’t wait to see what you guys have to offer today."
    Carl "Would the defense want to make an opening statement or do you want the prosecution to take the stand until their case is finished?"
    hide carl 

    show sheep neutral at right with dissolve
    show wolf neutral at left with dissolve
    Sheep "Your honor, we would like to make an opening statement to the defendant."
    Sheep "I am Sheep De Lune, and I represent Celtic, the President of Dunrar Mifflin."
    Celtic "Good day, your honor."
    Sheep "I’ll state what their side intends to prove and what their version of the story has in store. I assure you that Mr. Celtic is not guilty of this accused crime of not being ecological of cutting trees. "
    hide wolf with dissolve
    show sheep at center with easeinright
    
    Sheep "The company they wish to sue is {b}one of the leading paper companies in our country.{/b} "
    Sheep "The quality they pursue is as good that simple water cannot penetrate it."
    Sheep "The same company perhaps makes the paper you’re reading on?"
    Sheep "We'll never know."
    Sheep "But anyway, isn’t it normal for a company that makes the paper to cut trees?"
    hide sheep 

    show carl neutral
    Carl "Mrs. De Lune-"
    hide carl

    show sheep neutral
    Sheep "It's Ms., not Mrs."
    hide sheep 

    show carl neutral
    Carl "Oh my bad. Ms. De Lune, what are you implying?"
    hide carl 

    show sheep neutral
    Sheep "What I’m implying is that Mr. Celtic is in legal terms with the law. In fact, a law is backed up regarding it."
    Sheep "Section 68 of PD 705 of the law states that any person who shall cut, gather, collect, or remove timber or other forest products from any forest land, or timber from alienable and disposable public lands..."
    Sheep  "... or from private lands, without any authority under a license agreement, lease, license or permit, shall be guilty of qualified theft as defined and punished under Articles 309 and 310 of the Revised Penal Code."
    hide sheep 

    show zeil normal
    player "{i}We basically can't sue them since they're backed up in law...{/i}"
    player "{i}That is if they have a license.{/i}"

    show zeil annoyed
    player "{i}Damn, she's more assertive than Iro Lockheart{/i}"
    player "{i}She didn't even check her notes. Looks like she 100 percent knows what she's doing.{/i}"

    show zeil normal
    player "Ms. Sheep, that is indeed understandable in your part."
    player "{i}Should I ask a witness regarding their products? Or should I let it be?{/i}"
    player "{i}If I summon a witness, I get the initiative of asking. But if I keep on going, I can probably squeeze in the information she gives.{/i}"
    player "{i}Both decisions are risky since Sheep De Lune is an assertive lawyer.{/i}"
    hide zeil

    #Cheecks if Sheep Delune acts firsst
    $ SheepFirst = False

    menu:
        "Inspect Ms. Sheep's Words":
            $ PlayerChance -= 2

            show zeil smile2
            player "I would like to listen to Ms. Sheep's words"
            hide zeil

            if PlayerChance <= 0:
                show sheep neutral with dissolve
                Sheep "You're supposed to go first [povname] but alright. Give in to this."
                hide sheep
                jump Chapter2_GameOver

            show sheep neutral with dissolve
            Sheep "{i}Pfft, he should've summoned a witness. You're the one attacking, not us{/i}"
            Sheep "{i}Get ready, for you will experience how Sheep De Lune takes care of her cases.{/i}"
            Sheep "{i}A lawyer should always cross examine.{/i}"
            hide sheep neutral with dissolve

            $ SheepFirst = True
            jump Chapter2_Stumpy
        "Summon a witness for further inspection":
            jump Chapter2_Witness

    
        

label Chapter2_Witness:
    show zeil normal with vpunch
    player "May I speak with your witness? I have a few questions regarding the company's movements."
    hide zeil 

    if not SheepFirst:
        show sheep neutral
        Sheep "{i}Nice thinking for summoning a witness. You're the one attacking so go for it, Rookie.{/i}"
        Sheep "{i}However, I prepared Dunrar Mifflin's most powerful Product Manager as a witness.{/i}"
    elif SheepFirst:
        show sheep neutral
        Sheep "{i}You summon a witness right after I summoned yours?{/i}"
        Sheep "{i}I'm not saying it's wrong but I hope you squeezed in the information you need, based on my advances.{/i}"
        Sheep "{i}Plus, you're the opposition. You should be the one asking the witness first. Hays, you're indeed a rookie.{/i}"
        Sheep "{i}However, I prepared Dunrar Mifflin's most powerful Product Manager as a witness.{/i}"


    Sheep "Gladly, Mr. [povname], though I don’t think you’ll be getting the answer these environmentalists want."
    hide sheep 

    show zeil annoyed
    player "{i}Here she is talkin' smack{/i}"
    hide zeil

    show goose neutral at left with moveinright
    Witness "{i}Walks to chair{/i}"

    show zeil smug at right with dissolve
    player "Miss Witness, may you please explain your stance with Mr. Celtic, and how did you exactly meet him?"
    Witness "Oh uhm… quack I'm pretty much the quality manager of their product."
    Witness "I think it's pretty obvious how I met Celtic: through a professional hiring process... quack"

    show zeil normal
    Witness "But anyway, I ensure that no laws prohibit mass-producing our famous paper. I have been doing the job for over three years now which makes me their oldest quack product manager."
    Witness "In the past few years, I've quacked and compiled their licenses and permits in one folder to show investors, law people, and environmentalists such as these our legitimacy."
    Witness "Nothing sketchy with quack, right? Our licensed workers cut trees on a private property. We make sure that each tree is cut right, for it will be a waste of nature if we don't do quack. "

    player "{i}Judging by her body movements, she seems to be telling the truth.{/i}"
    player "{i}To be sure, should I ask to view their permit?{/i}"

    menu:
        "View Permit":
            player "May I view your said permits?"
            Witness "Sure, here you go"
            hide zeil with dissolve
            hide goose with dissolve
            jump Chapter2_Minigame
            #Jumps to Minigame

        "Believe their stance.":
            $ PlayerChance -= 2
            player "I believe she's telling the truth... I'll let this slide.."
            hide goose with dissolve

            show sheep neutral at left with dissolve
            Sheep "This is exactly why we hired a permit agent to be our proof reader. Mr. [povname] ,as a lawyer, you should always question your opponent."

            if PlayerChance <= 0:
                jump Chapter2_GameOver

            Sheep "Mr. Beary Bear, may you please come and proofread for us?"
            hide zeil with dissolve

            show bear at right with moveinright
            Beary "Alright, Mrs. Sheep"
            Sheep "It's Miss Shee-"

            jump Chapter2_PermExam
            #Jumps to BIR agent
        
label Chapter2_Minigame:
    show permit1 chapter2 with dissolve
    player "{i}So I gotta memorize the permit numbers.{/i}"
    player "{i}And then I'll input these numbers into a permit verification application.{/i}"
    player "{i}I only got one chance of pulling this off. So I gotta memorize this ASAP.{/i}"
    window hide
    pause
    pause
    player "Hmm... I didn't expect Felipe Fabregas, an official, to approve of this permit."
    player "He must have tons of power..."
    player "Wait, should he even sign that?"
    player "Hmm... I guess it makes sense since Dunrar Mifflin is the country's top 1 paper company."
    hide permit1 with dissolve

    show zeil smile with dissolve
    player "{i}I just need to remember what those numbers are.{/i}"

    show zeil annoyed 
    player "{i}I don't want that Sheep messing me up.{/i}"

    show zeil normal
    
    #Check if number input is correct and if wrong, executes FALSE
    python:
        permitnum1 = renpy.input("Input Permit Number 1", length=32)
        permitnum1 = permitnum1.strip()

        if not permitnum1:
            permitnum1 = "Null"

        if permitnum1 == "6882094328":
            permitnum1_Check = True
        else:
            permitnum1_Check = False

    if permitnum1_Check:
        show zeil smile2
        player "{i}Nice, I put the right number!{/i}"
        player "{i}Huh? Seems like the permit is legal.{/i}"
    else:
        show zeil normal
        $ PlayerChance -= 1
        player "{i}Crap, I think I put the wrong numb-{/i}"
        hide zeil

        if PlayerChance <= 0:
            jump Chapter2_GameOver


        show sheep neutral
        Sheep "Anything wrong, Mr. [povname] ? If you mess up, we'll have to call an actual verifier."
        hide sheep

        show zeil annoyed
        player "Nothin, Ms. De Lune."
        show zeil normal
        player "{i}The number was actually 6882094328{/i}"
        player "{i}I'll just put that and...{/i}"
        player "{i}Huh? Seems like the permit is legal. The number was right all along.{/i}"

    player "Onto the next permit."
    hide zeil with dissolve

    show permit2 chapter2 with dissolve
    player "{i}So I gotta memorize the permit numbers.{/i}"
    player "{i}I only got one chance of pulling this off. So I gotta memorize this ASAP.{/i}"
    window hide
    pause
    pause
    player "Hmm... Felipe Fabregas again?"
    player "This guy does have power"
    hide permit2 with dissolve

    show zeil smile with dissolve
    player "{i}Same process, input the numbers in the application.{/i}"

    show zeil annoyed 
    player "{i}Or else this 'lil Sheep will bug me again{/i}"

    show zeil normal

    #Check if number input is correct and if wrong, executes FALSE
    python:
        permitnum2 = renpy.input("Input Permit Number 2", length=32)
        permitnum2 = permitnum2.strip()

        if not permitnum2:
            permitnum1 = "Null"

        if permitnum2 == "4405189312":
            permitnum2_Check = True
        else:
            permitnum2_Check = False
        
    if permitnum2_Check:
        show zeil smile2
        player "{i}Nice, I put the right number!{/i}"
        show zeil normal
        player "{i}Huh? Seems like the permit is legal again.{/i}"
    else:
        show zeil normal
        $ PlayerChance -= 1
        player "{i}Crap, I think I put the wrong numb-{/i}"
        hide zeil

        if PlayerChance <= 0:
            jump Chapter2_GameOver

        show sheep neutral
        Sheep "Anything wrong, Mr. [povname] ? If you mess up, we'll have to call an actual verifier."
        hide sheep

        show zeil annoyed
        player "Nothin, Ms. De Lune."
        show zeil normal
        player "{i}The number was actually 4405189312{/i}"
        player "{i}I'll just put that and...{/i}"
        player "{i}Huh? Seems like the permit is legal again... The numbers are right all along.{/i}"

    player "Seems like all of the given permits are legalized."
    hide zeil

    show goose neutral
    Witness "Quack, told you so"
    hide goose
    
    show zeil smile
    player "I understand that may be true, but do you guys maintain the safe practices of Section 4 of E.O. No. 192 and Section 16, Article II of the 1987 of the law?"
    player "Which is basically  the right of the people to a balanced and healthful ecology on all forms of life and land corresponding to your area? That is the point of this debate after all."
    hide zeil

    show goose neutral
    Witness "Yes we do, we replant trees two times more than we cut. Our farms are circled with tons of trees. If you want to visit them, here’s our address: {i}Shows address{/i}"
    hide goose

    show zeil sad
    player "Oh..."
    hide zeil

    show sheep neutral with dissolve
    Sheep "To prove that the examination Mr. [povname] conducted is true, we have Mr. Beary, a permit inspector, to verify."
    hide sheep with dissolve

    show bear with dissolve
    Beary "As you may all know, I am a Permit agent sponsored by this company and the whole city."
    Beary "I am their {b}official agent {/b}in reading legitimacy. Their number 1. {i}Shows ID{/i} "
    Beary "As you may see, permit numbers 4405189312, 6882094328, and License ID 94445 are in our 50-level encrypted database."
    Beary "So yeah, they're legit"
    hide bear with dissolve

    show zeil annoyed with dissolve
    player "{i}Jeez they even hired an official reader.{/i}"
    player "{i}Sheep is such an extra{/i}"
    hide zeil with dissolve

    show carl neutral
    Carl "Does that conclude the cross examination of the propesition?"
    hide carl

    show zeil smile
    player "Yes, your honor."
    hide zeil

    $ Chap2Player_Explain = True
    jump Chapter2_Checker

    #Jump to RouteCheck if Sheep has already explained her stance.

label Chapter2_PermExam:
    hide sheep with dissolve
    show bear at center with easeinright
    Beary "As you may all know, I am a Permit agent sponsored by this company and the whole city."
    Beary "I am their {b}official agent {/b}in reading legitimacy. Their number 1. {i}Shows ID{/i} "
    Beary "Give me 5 mins or so to read these permits. I require FULL silence."
    hide bear with dissolve

    show zeil annoyed with dissolve
    player "{i}Jeez they even hired an official reader.{/i}"
    player "{i}Sheep is so assertive that she had the guts to correct me mid-sentence{/i}"
    hide zeil with dissolve

    "Five Minutes Later"

    show bear with dissolve
    Beary "Reading the permits and license, I can confirm that they are right. "
    Beary "They’re stored in our database correctly."
    Beary "As you may see, permit numbers 4405189312, 6882094328, and License ID 94445 are in our 50-level encrypted database."
    hide bear with dissolve

    show goose neutral
    Witness "Quack, told you so"
    hide goose
    
    show zeil smile
    player "I understand that may be true, but do you guys maintain the safe practices of Section 4 of E.O. No. 192 and Section 16, Article II of the 1987 of the law?"
    player "Which is basically  the right of the people to a balanced and healthful ecology on all forms of life and land corresponding to your area? That is the point of this debate after all."
    hide zeil

    show goose neutral
    Witness "Yes we do, we replant trees two times more than we cut. Our farms are circled with tons of trees. If you want to visit them, here’s our address: {i}Shows address{/i}"
    hide goose

    show zeil sad
    player "Oh..."
    hide zeil

    show carl neutral
    Carl "Does that conclude the cross examination of the propesition?"
    hide carl

    show zeil smile
    player "Yes, your honor."
    hide zeil

    $ Chap2Player_Explain = True
    jump Chapter2_Checker

    #Jump to RouteCheck if Sheep has already explained her stance.
        
label Chapter2_Checker: #Checks route if player has already answered
    if Chap2Player_Explain and Chap2Sheep_Explain: #If Sheep and Player has asked both witness, it jumps to judge
        show carl neutral
        Carl "Seems like both parties have explained their stance."
        Carl "Do both parties have no more additional rebutals or arguments?"
        hide carl 
        jump Chapter2_Judge
    elif Chap2Player_Explain and not Chap2Sheep_Explain: #Else if player has asked witness but not sheep, it jumps to Stumpy
        show carl neutral
        Carl "So that finishes the opposition's cross examination."
        Carl "Your turn, Ms. Sheep"
        hide carl
        jump Chapter2_Stumpy
    elif not Chap2Player_Explain and Chap2Sheep_Explain: #Else if sheep has asked witnes sbut not player, it jumps oto Witness
        show carl neutral
        Carl "So that concludes the... defense's cross examination."
        Carl "Your turn, Mr. [povname]"
        hide carl
        jump Chapter2_Witness
            

label Chapter2_Stumpy:
    show carl neutral 
    Carl "It's time for your cross examination, Ms. Sheep"
    hide carl

    show sheep neutral
    Sheep "Yes your honor! Now we would like to call a witness of the other side."
    hide sheep

    show triplet neutral at left
    show zeil normal at right
    Paddles "Oh no, is she pertaining to us?"
    player "She is..."
    Stumpy "I volunteer to be our witness."
    Nugget "G-good luck, big sis!"
    hide zeil 
    hide triplet

    show stumpy neutral at left with moveinright
    show sheep neutral at right with easeinright
    Sheep "Alright, Ms. Stumpy. May I ask what motivated you to sue this company, knowing that we have the right to cut trees around the forest that is considered ours? We even have a license to prove it."
    Stumpy "Well… by using ppetitions to convince the public, we widespread informtaion."
    Stumpy "This petition concerns Filipinos' right to a balanced and healthy environment, which the petitioners link to the twin concepts of ‘inter-generational responsibility’ and ‘inter-generational justice.’"
    Stumpy "It specifically addresses whether the petitioners have a cause of action to ‘prevent the misappropriation or impairment’ of Philippine rainforests and ‘arrest the unabated hemorrhage of the country's vital life support systems and infrastructure.’"
    Sheep "{i}Hmp, looks like she did her research.{/i}"
    hide stumpy
    hide sheep

    show carl neutral
    Carl "The Court explicitly states that petitioners have the locus standi necessary to sustain the bringing and, maintenance of this suit (Decision, pp. 11-12). Locus standi is not a function of petitioners' claim that their suit is properly regarded as a class suit. "
    hide carl

    show stumpy neutral at left
    show sheep neutral at right
    Stumpy "I understand locus standi to refer to the legal interest which a plaintiff must have in the subject matter of the suit."
    Stumpy "Because of the very broadness of the concept of 'class' here involved — membership in this 'class' appears to embrace everyone living in the country whether now or in the future."
    Stumpy "it appears to me that everyone who may be expected to benefit from the course of action petitioners seek to require public respondents to take, is vested with the necessary locus standi."
    hide stumpy
    hide sheep

    show zeil shocked
    player "{i}Stumpy defended herself with ease. She's professinally powerful on herself.{/i}"
    hide zeil

    show stumpy neutral at left
    show sheep neutral at right
    Sheep "I understand your endeavors, Miss Stumpy."
    Sheep "However, even tho we are the number 1 tree cutter, the logic of law backs us. We have the application for Tree Cutting Permits so as the license to conserve land."
    Sheep "We have authenticated private land ownership; we harvest with a sure environmental plan. We also have an application form that is backed up with permit agents."
    Sheep "We have what every tree cutting company has. However, we take extreme precautions on cutting and replanting trees. After all, this is a business: we cut trees and make paper = we gain money; we lose money if we lose natural stock, AKA trees."
    Sheep "We also follow the Department of Environmental and Natural resources guidelines in their endeavors for a more fantastic future."
    hide stumpy
    hide sheep

    show carl neutral
    Carl "Ms. Sheep is right. The Court may be seen therefore to be recognizing a beneficiaries' right of action in the field of environmental protection. "
    Carl "as against both the public administrative agency directly concerned and the private persons or entities operating in the field or sector of activity involved. "
    hide carl

    show zeil normal
    player "{i}Seems like thier plot of land is near a site for indigenous people.{/i}"
    player "{i}I should ask if this sort of productivity colldies wiht their way of living.{/i}"

    show zeil smile 
    player "We have noticed something, and it’s that your plot of land is near a tribe of indigenous people. In any case whatsoever, does cutting trees near their site damage their way of living? If not, may you please justify?"
    hide zeil

    show sheep neutral
    Sheep "Well, the proximity of tree cutting is indeed followed by our agents. We have people from official agencies who stop workers from cutting in a particular site. Plus, we practice selective cutting."
    Sheep "If, somehow, old and big trees are seen in an area: people are refrained from cutting century-old endemic trees such as dipterocarps because they believe that these trees harbor the spirits of their ancestors."
    Sheep "Before cutting old trees, they conduct rituals to seek their ancestors' permission. A shaman locally known as mumbaki directs the rituals."
    hide sheep

    show zeil smile2
    player "Thank you!"
    hide zeil

    $ Chap2Sheep_Explain = True
    jump Chapter2_Checker

label Chapter2_GameOver:
    hide zeil
    hide carl
    hide triplet
    hide goose
    hide stumpy

    show sheep neutral
    Sheep "Seems like you messed up too much, [povname]"
    Sheep "I'm not the type to call it bad with my opponent, but you are too ignorant for my tastes."
    hide sheep

    show carl neutral
    Carl "You have given a lot of wrong information today, [povname] ..."
    Carl "This is a bit embarassing"
    hide carl

    show wolf neutral
    Celtic "Pfft, you call this a lawyer?"
    Celtic "I guess I got this case in the bag, boss."
    hide wolf 

    show triplet neutral
    Stumpy "Oh no, we are toast..."
    Nugget "I - thwink we are d-dead"
    Paddles "Justice for the future... gone..."
    hide triplet

    show zeil sad
    player "{i}Christ... I've dissapointed them... my will to keep going is slowing down. Plus I have this persuasive sheep as my opponent {/i}"
    hide zeil

    show black with Fade(2.0,0.5,1.0)

    $ renpy.full_restart()

label Chapter2_Judge:
    show sheep neutral with dissolve
    Sheep "None, your honor."
    hide sheep

    show zeil normal with dissolve
    player "{sc=2}Sweating{/sc} {i}At this pase, we are gonna ennd up a stalemate, both cases will be dismissed … and these beavers will never get what they want to achieve for us.{/i}"
    player "None, your honor."
    hide zeil

    show carl neutral
    Carl "Understandable, you may now present thine closing statements."
    hide carl with dissolve

    show zeil delighted
    player "I hereby dub the company Dunrar Mifflin with more questions since the case is not yet optimal nor finished."

    show zeil normal
    player "While the right to a balanced and healthy ecological is found in the Declaration of Principles and State Policies rather than the Bill of Rights, it is no less vital than any of the civil and political rights included in the latter."
    player "Such a right belongs to a separate category of rights entirely, for it is concerned with nothing less than self-preservation and self-perpetuation..."
    player "as the petitioners so eloquently and correctly emphasize, and its progress may even be claimed to precede all governments and constitutions."
    
    show zeil smile2
    player "These fundamental rights, in fact, do not need to be put into the Constitution since they have been presumed from the dawn of time."
    hide zeil

    show sheep neutral
    Sheep "Thank you for your attention in this matter. There is a difference between “illegally cutting and cutting with ethics."
    Sheep "There is a difference between not planting and replanting. And there is a difference between what constitutes reasonable doubt and what amounts to just excuses by the defendant."
    Sheep "The law doesn’t allow a man to cut without a permit to establish a company solely for creating excellent paper without it. We proclaim that Dunrar Mifflin is not guilty of its environmentally-secured actions since we plant more than we cut. "
    Sheep "We understand your view for a better future, but we are one of the significant economic contributors in the market, and we also sell good paper."
    hide sheep

    show carl neutraltable
    Carl "Whether such beneficiaries' right of action may be found under any and all circumstances, or whether some failure to act, in the first instance, on the part of the governmental agency concerned must be shown ('prior exhaustion of administrative remedies')"
    Carl "is not discussed in the decision and presumably is left for future determination in an appropriate case. "
    Carl "Because of the Rebutal of an actual permit over the cutting of trees, so as the will to give the future generation better air to breathe, this court case has come to a stalemate for btooh sides have prooven equal yet stale points."
    Carl "This is a tough decision for both… so we, as court, need more time to think about this, This court session is now dismissed."
    Carl "{b}Dismissed but will resume sometime!{/b}"
    show carl neutraltable hammer with vpunch

    play sound "audio/sfx/sfx_gavel1tap.wav"
    "{i}HAMMER NOISE{/i}"

    stop music fadeout 3.0
    stop audio fadeout 3.0
    stop sound fadeout 3.0
    hide carl with Fade(1.7, 2.0, 1.5)

    "The Case Ended With a Stalemate"

label Chapter2_OverLay:
    scene bg officefirm with Fade(1.5, 2.0, 1.7)
    show zeil normal at right with easeinright
    show mommabeaver sad at center with easeinright
    show triplet neutral at left with easeinright

    play music "audio/bgm_lawfirm.mp3" volume 0.3 fadein 3.0 loop
    Bmom "We had a stalemate huh..."

    show zeil sad
    player "Yeah seems like it. Both lawyers provided a good point, and the judge couldn't decide which to choose."

    show zeil normal
    Paddles "But why? We are fighting for the future of our generation! That’s the gweater good than most of the stuff they’re doin'"

    show mommabeaver neutral
    player "I know… but they have been backed up by law, making them legal. It’s hard to terminate them, especially if we have no witnesses that prove their harmful environmental doings"
    
    show zeil shocked 
    show mommabeaver shocked
    Stumpy "We got to find a way to somewhat expose them! We need an infultrator to see their actions from the inside!"
    Nugget "Buz siz, isnt that iwwegal?"

    show zeil smile
    show mommabeaver neutral
    player "Wait, your sister may have a good idea... "
    Bmom "But who are we going to rely on? This situation is sticky, and we can’t interfere… don’t tell me we’re sending my children?"
    Nugget "Oh yeah! An infultrating adventure awaits us mah bros! Let’s start runnin and blasting!! <3"

    show mommabeaver mad 
    Bmom "Nugget no!"

    show zeil smile2
    if RouteChecker >= 2:
        player "I think I might know someone. It will require a bit of convincing though."
    else:
        player "This office has sponsored an inspector. He's aso a lawyer that Cassie defeated. It will require a bit of convincing though."
        
    scene bg reccomp with dissolve
    show zeil smile with dissolve

    player "{i}Calls on the Phone{/i}"
    player "{i}Ringing{/i}"
    player "{i}Someone answers{/i}"

    if RouteChecker >= 2:
        player "Hello, is this my good old Iro "
    else:
        player "Hello, is this Iro the Inspector?"

    Iro "{bt=1}J-just wait a second,{/bt}"
    show zeil normal

    Iro "{bt=2}. ..  i think my cat answered the phone– {sc=1}wOoo{/sc} {sc=3}ooAHH {/sc}{/bt}"
    show zeil shocked

    Iro "{move}WAAAAAAAAAAA *falls of the stairs*{/move}"
    player "Woah there, are you okay?"
    Iro "Aoo Arf arf fhchh welp {sc=2}Ocuh{/sc}, woudl you look at that, i fell down haha! That’s the funny man right there!"

    show zeil normal
    player "Jeez, are you okay?"

    show zeil smile
    Iro "you bet! So who’s this handsome voice callin from here ey?"

    if RouteChecker >= 2:
        player "It's me, [povname] . I Came to-"

        show zeil shocked
        Iro "{sc}WOAHHH [povname]? OMG!! {/sc}{rotat}Long time NO HEAr!!{/rotat} "

        show zeil smile2
        Iro "{bt}KUMUSTA KA NA?{/bt}"
        Iro "{sc=1}DO YOU WANNA KNOW{/sc} {sc=2}HOW MANY DALMATIONS I HAVE NA? {/sc} {sc=4}IT’S 2 DIGITSS!!{/sc}"

        show zeil smile
        player " haha! You never change at all, you cute doggo."
        Iro "Haha! I sure won’t alright! So how’s it goin?"
        player "You see, I came to call for some investigating help. "
        Iro "Investigating help huh… Welp, you called the right place since I got the team and skills. Whatcha lookin for, buddy?"


    else:
        player "Hello, I am [povname] . I walk in the same lawfirm as Cassie The Lawyer."
        Iro "Ahh Cassie, the one who arfed me out of this world with her {rotat}crazy law skills{/rotat}"

        show zeil smile2
        player "Yeah, she's a smooth killer indeed! Fast and silent"
        Iro "HOHOHO! Sounds like you like her"

        show zeil shocked
        player "No! I just admire her sk-"
        Iro "Welp, you called the right place for investigations since I got the team and skills. Whatcha lookin for, buddy?"

    hide zeil with dissolve
    scene bg officefirm with Dissolve(2.0, alpha=False, time_warp=None)
    show zeil normal at right with dissolve
    show mommabeaver neutral at left with dissolve

    Bmom "I hope the one you sent to investigate goes well."

    show zeil delighted
    player "Don’t worry, he’s a top investigator of his time. He’s smooth as a pillar, and fast as a fox. Some may even call him a man’s best friend"
    Bmom "So he’s a dog?"

    show zeil smile2
    player "Yep! He got the skills. He’s  currently seeing the company in the inside."

    show mommabeaver shocked
    Bmom "Isn't that illegal"

    show mommabeaver neutral
    player "Not really, he has a permit for proof. But I do wonder how’s he goin right now?"

    stop music fadeout 2.0

label IroInspect: #Iro Inspeciton Era wow lezgo iro

    scene bg factory3 with Fade(1.7, 2.0, 1.5)
    show iro surprised at left with moveinleft

    play music "audio/bgm_iroinspecting.wav" volume 0.3 fadein 3.0 loop

    Iro "Woah! This company big! Welp I better start my inverstigation somewhere."
    show iro neutral 
    show goose2 neutral at right with moveinright
    Guard "State your business, Dog!"
    Iro "Arf."
    Guard "..."
    Iro "..."
    Iro "Oh hey, I’m an investigadorrr as you may see with this badge and permit! I love tackling the law with my job, and I hope to properly inspect this area."
    Guard "An inspector huh… we didn’t expect one to come today."
    Iro  "Welp guess who’s here now."
    hide goose2

    show goosewalky left at right
    Guard "Hmm... {bt=2}*gets radio*{/bt} We got Mr. Inspector comin here at any moment."
    Guard "We let him in?"
    Guard "Okay, got it."
    hide goosewalky left

    show goose2 neutral at right
    Guard "Boss said to get in, Dog."
    Iro "Thank you my good man"
    Guard "Our crew will be accompanying you"
    Iro "With pleasure!"
    hide iro with moveoutright
    hide goose2 with moveoutright

    scene bg factory1 with Dissolve(1.0, alpha=False,time_warp=None)
    show iro surprised at left with moveinleft
    show goose2 neutral at right with moveinleft
    Iro "WOAHH!  YOU GUYS SURE HAVE TONS OF PAPER, WOOD, AND MILFS HERE"
    Crew "..."

    show iro happy
    Iro "I mean Mills."
    Iro "Hehehe"
    Iro "I didn't know y'all are geese!"

    show iro neutral
    Iro "{i}Anyways, what to inspect first?{/i}"
    $ MillCheck = False
    $ StorageCheck = False

    menu:
        "Mills":
            Iro "I shall inspect the mills first!"
            Crew "Ok."
            jump Chapter2_Mills


        "Paper and Wood Storage":
            Iro "I shall inspect your storage first!"
            Crew "Ok."
            jump Chapter2_Storage

label Chapter2_IroEval:
    scene bg factory3 with dissolve
    show iro neutral at center with moveinright
    show goose2 neutral at right with moveinright
    Iro "Seems like I inspected that one!"
    if MillCheck and StorageCheck:
        Iro "Oh wow that's all of it..."
        jump Chapter2_IroDone
    elif MillCheck and not StorageCheck: #If Mills has been inspected, go to storage
        Iro "Welp, I guess there's only one thing left to do!"
        menu:
            "Inspect Storage":
                jump Chapter2_Storage
    elif not MillCheck and StorageCheck: #If storage has been inspected, go to Mills.
        Iro "Welp, looks like I gotta explore the milfs now!"
        menu:
            "Inspect Mills":
                jump Chapter2_Mills


label Chapter2_Mills:
    scene bg factory1 with dissolve
    show iro neutral at left with moveinleft
    show goose2 neutral at right with moveinleft
    Iro "So this is the mill, my good sir?"
    Crew "Yes, but to be more specific, this is a sawmill. Im pretty sure you know how it works."
    Iro "I've cut some {sc=4}heads {/sc}in the past"
    Crew "..."

    show iro happy
    Iro "{rotat}Just kidding!! {/rotat}haha!"
    hide goose2 with dissolve
    hide iro with dissolve

    Iro "Hmm.. everything here seems to be intact."
    Iro "And the mill seems to be working fine."
    Iro "Look at this baby chop wood! Smooth as a criminal"

    show iro neutral at left with dissolve
    show goose2 neutral at right with dissolve
    Iro " yeahh, this baby seems to be working. Do you have a permit to use this?"
    Iro "We have a licencse."
    Iro "Hmm... Good enough!"
    $ MillCheck = True

    jump Chapter2_IroEval

label Chapter2_Storage:
    scene bg factory2 with dissolve
    show iro neutral at left with moveinleft
    show goose2 neutral at right with moveinleft
    Iro "Ohh so this is where you keep your logs."
    Crew "Yeah"
    Iro "Mind if I inspect it?"
    Crew "Yes"
    Iro "Don't mind if I dooooo"
    Crew "..."
    hide goose2 with dissolve
    hide iro with dissolve

    Iro "Hmm the screws are doing neat"
    Iro "Oh look, a chicken wing!"
    Iro "Other than that, theese storage systems seem to be organized, safe, and hmm it looks like a good place to chill."

    show iro neutral at left with dissolve
    show goose2 neutral at right with dissolve
    Iro "Everything seems to be intact. No infestation, risks were kept at a minimal, and seems like yall even hid some cards here."
    Crew "sorry bout the cards, boss"

    show iro happy
    Iro "Haha! That's okay, I too bring playing cards in my office"

    show iro neutral 
    $ StorageCheck = True

    jump Chapter2_IroEval

label Chapter2_IroDone:
    Iro "{i} Seems like I’ve inspected everything on the inside {/i}"

    show iro happy
    Iro "Great interior! Everything seems to be intact, and … everyhting has a damn permit indeed haha! Y’all sure are operating under the law"
    Crew "k"

    show iro sad
    Iro "{i}Man, everything here is so intact. They are, under all permits and licenses, legal to operate. I can’t seem to see anything to exploit… I’ve even contacted my BIR friends regarding their permits… {/i}"
    Iro "{i}I’m cornered with the truth that they are legit… sorry [povname] {/i}"
    Iro "......."

    show iro neutral 
    Iro "Aight my good sir, I will get going now."
    Crew "k bye"
    
    show iro neutral at left with easeinright
    Iro "Adios amigo-"
    pause (1.0)
    Iro "..."
    Iro "{i}{bt=2}*Spots Big Door*{/bt}{/i}"
    Iro "{bt=3}Heyyyaaa {/bt}if you don’t mind me asking, what’s inside that {b}big door?{/b} Another exit perhaps"
    Crew "Yeah you can go there, but we prefer if you exit the normal way"
    Iro "do you mind if I check what’s inside of {bt=2}thaaaaaaaaaaaaaaaaaaaat {/bt}door?"
    Crew "I mind, you need to have a lumberjack’s license to enter there."
    Iro "Well I'm {rotat=13}investigadorrr {/rotat}, I have the rights to go in there don’t I?"
    Crew "..."
    Iro "I’ll take that as a yes! {i}approaches the door{/i}"
    Crew "Hey, you haven’t investigated our comfort rooms yet"
    Iro "{bt}Nahhhhh{/bt}this big door looks more interesting than your tiny comfort rooms my good sir"

    hide iro with easeoutleft
    Crew "Wait."
    hide goose2 with easeoutleft
    
    show iro neutral at center with moveinright
    show goose2 neutral at right with moveinright
    Crew "{bt=2}*Grasps Iro's arm*{/bt} Listen, you really shouldn't be going there."
    Iro "why cant i? it’s an investigator’s job to meddle at thine operational affairs based on Presidential Decree No. 442 of 1974"
    Iro "Which is that DOLE shall be solely responsible for the administration and enforcement of occupational safety and health laws, regulations and standards in all establishments and workplaces wherever they may be located."
    Iro "I gotta see this or else y'all are toast too"
    Crew "..... {bt=2}*Sneakily gets a hammer and hides it in his pocket*{/bt}"
    Iro "Aight silent means yes! {bt=3}*enters big door*{/bt}"
    hide iro neutral with moveoutleft
    hide goose2
    show goosewalky left at right
    Crew "{bt=2}*Gets radio*{/bt} In coming inspector, sir."
    hide goosewalky left
    show goose2 neutral at right
    hide goose2 neutral with moveoutleft

    scene bg deforest with Fade(1.0, 1.0, 0.5)
    Iro "{rotat}Damn!{/rotat} So that explains why you got lots of logs. You {b}immensely{/b} cut these trees!"
    show iro neutral at right with easeinleft
    show goose neutral at left with easeinleft

    show iro mad 
    Iro "Where’s the ‘selective logging’ here?"
    Crew "Everything here is part of our pirvate plot. Nothing here is sacred. If you want to see more trees, I recommend you go deeper, investigador."

    show iro happy
    Iro "Okay!"
    hide iro with easeoutright
    hide goose with easeoutright

    scene bg deforest2 with dissolve
    show iro neutral at right with easeinleft
    show goose neutral at left with easeinleft

    show iro mad
    Iro "Still looking pretty dead here!"

    show iro neutral
    Iro "How often do you cut trees?"
    Crew "we don’t replant trees instantly. That will hinder their space for growth."
    Crew "We have to calculate the space in between the trees. We usually plant every month."

    show iro happy 
    Iro "Okay."

    show iro mad
    Iro "You seem to have cut a lot in this area, that is what I am {sc}sussy{/sc} about"
    Crew "Those at the background are the new trees. We usually cut deep within, but the trees we have cut have recently been replanted."
    Crew "We replant because it's close to an indigenous tri- I mean a ecological property such as lakes. We gotta conserve those areas ASAP unlike here."

    show iro neutral 
    Iro "Hmmm I'll be the judge of that."
    hide iro with easeoutright

    Crew "{i}Damn I wanna smack your head, dog.{/i}"
    hide goose with easeoutright

    scene bg deforest3 with dissolve
    Iro "Oh I see what you mean, you did replant on this area"
    show iro neutral at right with easeinleft
    show goose neutral at left with easeinleft
    Crew "Yeah."

    show iro happy
    Iro "Based on ecological standards, you somewhat maintained selective logging huh."
    Crew "That is what we do as a company"
    Iro "Alrighties, mi amigo. I'll inspect this forest even more!"
    hide iro with easeoutright

    Crew "{bt=2}*Sweats*{/bt}"

    #Make it so that the crew is holding a walkiee talkie

    hide goose
    show goosewalky right at left
    Crew "{bt=2}*Gets radio*{/bt} Boss, the inspector is going deeper"
    Crew "Huh? You want me to what?"
    Crew "....."
    Crew "Hmm. Alright, I'll trust you with that."
    hide goosewalky right


    show goose neutral at left
    hide goose with easeoutright

    
    scene bg dforest with dissolve
    Iro "This part of the forest is somewhat deforestated. I see that you’re replanting them though. Great job for proving that."
    show iro neutral at center with easeinleft
    show goose neutral at left with easeinleft
    Crew "...."
    Iro "Wait what’s that big tree over there?"
    show iro neutral at right with moveinleft
    Crew "We’re not allowed to go there, indigenous ppl live there."
    Iro "Hmm.. That's why there are tons of trees here."
    Iro "How far are we from the tribe?"
    Crew "Above 10Km. This is as far as this company can cut."

    show iro sad
    Iro "I see...{i}{sc=2}Cripes, they're legal... I can't go further since I might be disrupting those people.{/sc}{/i}"

    show iro neutral
    Iro "So this is as far as we could go huh?"
    Crew "Yes. I would appreciate it if we go back now."
    Iro "You betcha, fella-"
    stop music fadeout 1.0

    #Insert Scream Audio
    show iro surprised at right with hpunch
    "{sc=4}SCREAMING IN THE BACKGROUND{/sc}"
    "....."
    pause (1.0)
    Iro "Hey did someone scream?"
    Crew "I didn’t hear anything."

    show iro neutral
    Iro "If you didn't then why were you startled?"
    Crew "I startle a lot."
    Iro "..."

    show iro mad
    Iro "{sc=1}Sussy baka!{/sc}"
    hide iro with easeoutright

    play music "audio/bgm_irorunaway1.wav" fadein 3.0 volume 0.3 loop
    Crew "HEY! Don't think you're getting out of here safely! {bt=2}*Gets hammer from pocket*{/bt}"

    Iro "And you call yourself a lumberjack?! {bt=2}*Runs Deeper into the Forest*{/bt}"
    Crew "I'm from human resources!"
    hide goose with easeoutright 
    
label Chap2QS:
    "It's advisable that you quicksave here."
    "A wrong choice can kill Iro."
    "It will put the game into a gameover."
    ""
    "Have you quicksaved yet?"
    menu:
        "Yeah, let's go!":
            "-Game Shall Resume-"
            pause(1.2)
        "No, not yet.":
            "Quicksave now!"
            jump Chap2QS

    show iro neutral with moveinleft
    Iro "{bt=2}*Pants*{/bt} Oh my gulay, where to now? There's a lake blocking me from that big tree"

    
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
label questiontime1:
    
    label menu1:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer

        $ IroSwim = False

        menu:
            "Go swim":
                hide iro with dissolve
                hide screen countdown
                $ IroSwim = True                  ### stop the timer
                jump Escape1
            "Run on the fallen tree":
                hide iro with dissolve
                hide screen countdown                  ### stop the timer
                jump Escape1

    label menu1_slow:
        jump IroCaught

label IroCaught:
    hide iro with dissolve
    hide goose with dissolve

    show goose neutral with dissolve
    Crew "Hah! There you are, dog!"
    hide goose

label IroCaught2:

    show iro neutral at center with dissolve
    Iro "Ahhhhhhhh cripes"
    
    show goose neutral at left with easeinleft
    Crew "I told 'ya you ain't comin back safely! {sc}STRANGGLES IRO{/sc}"
    Iro "{sc}HEY WAIT WE CAN TALK TH-{/sc}"

    show goose neutral at center with easeinleft
    Iro "{sc}*TRIPS DOWN*{/sc}"
    Crew "{sc=1}I{/sc} {sc=2}warned{/sc} {sc=3}you,{/sc} {sc=4}you {/sc} {sc=6}sun of a gun!{/sc} {sc=6}*Hits Iro with a hammer*{/sc}"

    show blood2 at truecenter with hpunch
    Iro "{sc=6} AAAGH {/sc}"
    Crew "{sc=2}HOHOHO I'M GONNA TAKE MY SWEET TIME! {/sc}"

    show blood1 with vpunch
    Crew "{sc=5}TAKE THAT!{/sc}"
    Iro "{sc=6}AAAARF ST-STOP-- AAAAAAAAAAAAAAA{/sc}"

    show blood3 at truecenter with hpunch
    Crew "{sc}*Pants{/sc}"
    Crew "{sc=10}MWAHAHAHHA{/sc}"

    show blood5 with vpunch
    Crew "{sc=20}MOREEEEEE!!!!{/sc}"

    show blood4 with hpunch
    Crew "{sc=30}YOU FUCKING DOG!{/sc}"

    show blood6 with vpunch
    Crew "{sc=30}MWHAHAHAHAHAHAHAHAA{/sc}"

    show blood7 at truecenter with hpunch
    Iro "{sc=5}AAAAA{/sc}{sc=3}AAAAAAAAAAaaa{/sc}{sc=1}aaaa....{/sc}"

    show blood8 at left with vpunch
    Crew "{sc}I'll bring you to the boss beaten up now. I am satisfied.{/sc}"

    show black with Fade(4.0,2.0,1.0)
    "Iro Died With Suspicion."
    "He was missing for 5 years until he was found dead."
    "He was burried in mud deep within the forest, near the indigenous tribes."
    "Justice for the Beavers was never given."
    "..."
    "The game will restart now."
    menu:
        "Restart":
            $ renpy.full_restart()

label Escape1:
    if IroSwim:
        show iro happy at center with easeinbottom
        Iro "Arf arf! I feel like a pup again!"
    else:
        show iro surprised at center with easeinleft
        Iro "Woah, gotta balance!"
    
    show iro neutral 
    Iro "Hays, now that's done!"

    show iro surprised 
    Crew "{sc=1}COME BACK HERE YOU LITTLE DOG!{/sc}"

    show iro neutral
    Iro "Oopsies, gotta blasties!"
    hide iro with easeoutright

    show goose neutral with easeinleft
    Crew "Co... {sc=1}*pants* {/sc}come back here!"
    hide goose with easeoutright

    show iro neutral with moveinleft
    Iro "Oh gosh, he's catching up to me!"

    show iro mad
    Iro "Gagh, there are rocks everywhere!"

    show iro sad
    Iro "Agh, they hurt my feet."

    show iro neutral
    Iro "Should I take it slow or run fast?"

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
label questiontime2:
    
    label menu2:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer


        menu:
            "Slow and Steady Wins the Race!":
                hide screen countdown    
                Iro "Welp I don't want my paws to get hurt, so I gotta take it slow"
                show iro neutral at right with easeinleft
                Iro "I don't wanna be toooo harsh"

                show iro happy 
                Iro "I bet he can't even walk here hehe!"

                show iro surprised 
                Iro "Hey is that goose flying?"
                Iro "Oh Dalmatians, he is flyin-"
                Iro "and i oop-"
                show iro neutral at right with vpunch
                Iro "{sc}trips down{/sc}"         
                jump IroCaught
            "Run like the wind!":
                hide iro with dissolve
                hide screen countdown                 
                jump Escape2

    label menu2_slow:
        jump IroCaught

label Escape2:
    show iro neutral at left with moveinleft
    show iro neutral at left with hpunch
    Iro "Ouch"
    show iro neutral at center with moveinleft
    show iro neutral at center with hpunch
    Iro "Ouch"
    show iro neutral at right with moveinleft
    show iro neutral at right with hpunch
    Iro "Oof that hurts, but I'm going as fast as I can"

    show goose neutral at left with moveintop
    Crew "Heh, I forgot that I could fly"
    Iro "You gotta be kidding me aaaa!"
    hide iro with moveoutright

    Crew "W-wait... {sc=1}*pants*{/sc}"
    Crew "Gosh Give me a break! I have little feet you nitwit!"
    Iro "You call yourself human resources with that speed!"
    Crew "I'm a goose, you dog!"
    hide goose with moveoutright

    show iro neutral at right with moveinleft
    Iro "Oh Dalmatians, I can see the tree from here!"
    Crew "Not so fast!"
    show goose neutral at left with moveinleft

    show iro happy
    Iro "Heh, guess you've caught up with me."

    show iro neutral
    Crew "Wait... {sc=2}*pants*{/sc}"
    Crew "I.... {sc=2}*pants*{/sc}"
    Crew "I ain't {sc=2}*pants*{/sc}"
    Crew "Going down without a figh...t"
    Iro "Then let's go, Jose!"

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.00000001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
label questiontime3:
    
    label menu3:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer

        menu:
            "Punch his belly":
                hide screen countdown                 ### stop the timer
                Iro "{bt}Hiyyaaaaaaaaaaa!!!!{/bt}"
                show iro neutral at left with moveinright
                Iro "{sc}{i}Attempts to Kick his belly{/i}{/sc}"
                Crew "{sc}{i}Dodges{/i}{/sc}"
                Crew "They don't call me shaolin HR for no reason."
                hide goose with dissolve

                jump IroCaught2
            "Break his feet":
                hide screen countdown                  ### stop the timer
                Iro "{bt}Hiyyaaaaaaaaaaa!!!!{/bt}"
                show iro neutral at center with moveinright
                Iro "{sc=1}{i}*Attempts to break his feet but trips instead*{/i}{/sc}"
                Iro "Arf"
                Crew "..."
                Crew "Really? Welp at least you tried."
                hide goose with dissolve

                jump IroCaught2
            "Kick his snout":
                hide screen countdown
                jump Escape3

    label menu3_slow:
        jump IroCaught2

label Escape3:
    Iro "{bt}I hope you like feet!!!!!{/bt}"
    show iro mad at left with moveinright
    Iro "{sc}{i}*Front Kicks his snout*{/i}{/sc}"
    Crew "{sc}{i}*Attempts to dodge but beak is too long*{/i}{/sc}"

    show goose neutral with vpunch
    Crew "{sc}OUCH!{/sc}"
    Iro "Heh! Take this!"

    show goose neutral with hpunch
    Crew "{sc}Gah!!{/sc}"

    show iro sad
    Iro "Okay I beated you too much, I'm sorry! Please forgive me when this is all done!"
    hide iro with easeoutright

    Crew "{sc=1}I... I'll catch up with you later...{/sc}"

label IroBigTree:
    scene bg bigtree with Dissolve(1.5)
    show iro neutral at left with moveinleft
    Iro "So....."

    show iro mad
    Iro "{b}THIS {/b}is what you're hiding under the big tree!?"

    show hog neutral at center with moveinright
    show iro surprised 
    Hog "HELP! THESE PPPL WANT OUR PLOT OF LAND AND WE CAN’T DO ANYTHING TO STOP TH-"

    show goose2 neutral at center with moveinright
    show goose2 neutral at center with vpunch
    Guard "{sc}*Slaps Hedgehog*{/sc}"
    Iro "Hey!"

    hide hog with dissolve
    "{bt=2}*Clap, Clap, Clap*{/bt}"

    show iro mad
    Iro "Who's there?!"
    Celtic "Hello, Iro."
    show wolf neutral at right with moveinright
    show iro surprised
    Iro "Celtic...? {sc=1}I thought you were in the city?{/sc}"

    if RouteChecker == 1:
        Celtic "I knew you'd be here. Didn't you recently lose in court?"
    else:
        Celtic "I heard you lost your latest court case… and you lost it to the one you're currently {b}HELPING{/b}."

    show iro mad
    Iro "Justice should be served, Celtic! You know that!"
    Celtic "Alright, lil pup. Enough fun and games. This is my turf and these people aren’t going anywhere. They are mine. And their plot of land shall be mine too!"
    Iro "Under the human rights law nu-"
    Celtic "Oh shut up. Take care of him, bois."
    hide wolf with moveoutright

    Iro "I ain’t going down without a -"

    Crew "SUMMMMERSAULTTT!"

    show iro neutral 
    Iro "Oh what the arf"
    show goose neutral at left with moveintop
    show goose neutral with vpunch
    "{sc=5}*Head gets hit*{/sc}"

    stop music fadeout 2.0

label PlayerFirm:
    scene bg officefirm with Fade(1.5, 2.0, 1.5)
    show zeil normal with dissolve
    play music "audio/bgm_sneakyben.mp3" fadein 3.0 volume 0.3 loop
    player "{i}Where is iro? It’s been 10 hours… he should've given us an update.{/i}"
    show zeil at left with moveinright
    show mommabeaver sad at right with moveinright
    Bmom "How's the situation?"

    show zeil sad
    player "Don’t be too surprised alright, but the situation isn’t great…"

    show zeil normal 
    show mommabeaver shocked
    Bmom "What??! Where is Iro?"
    player "That’s the thing I want to know too. He hasn’t responded to my texts since this morning. "

    show mommabeaver neutral 
    Bmom "Last time we called, he said that he’s entering base…"
    player "This sounds risky. He usually sends a reply stat. He must be insanely focused right now though."
    Bmom "I don’t know… should we go visit him?"
    player "I don't think we can. He's too deep within the catacombs. Either he must've found something nasty or he's focusing"

    show mommabeaver mad
    Bmom "Whatever it is, he brought his camera to help him."
    player "Indeed! Let’s have faith in Iro. He’s a feisty dog, after all."

    show mommabeaver
    Bmom "I’m still skeptical… but let’s see where he goes. Anyways, what can we rebute to this company’s arguments now?"
    player "I’m thinking that their licenses are fake. Forged, or somewhat stolen. "

    show mommabeaver shocked
    Bmom "What makes you say that?"
    player "Check this. A photographer took a photo of the scenery. This photo includes the plot of land Dunrar Miflin has. Some of the trees aren't replanted, and there seems to be a forest fire."

    Bmom "is he licensed enough to do that?"

    show mommabeaver neutral 
    player "He is, but he didn't know that this plot of land is so private that even a professional photographer can't take photos of it. Only an inspector like Iro can do such."

    Bmom "That's crazy. Even Dunrar Mifflin owns a foresty plot of land? That's like a significant portion of the space, yet photos shouldn't be taken."

    player "Indeed. Helicopters can't go over it too. The worst part is that I think they got officials guarding their backs. It's like these officials are also shareholders of said company. Isn't it strange?"

    Bmom "Officials… higher-ups with actual ties with the law? That's overboard! Despite that being speculation, we gotta do something about this."

    player "No, we have to be careful since everyone in the court is in danger, especially if this happens now. Your kids, who have eyes for justice, can be in trouble too… we don't know who we're messing with. We'll have to fight them slowly…"

    show mommabeaver sad
    Bmom "This is honestly scary..."

    player "These strong people with power are abusing mother nature for money. In all honesty, I'm more worried about the indigenous people nearby."
    player "They are at risk of losing their homes, especially if they win this case; They may expand real hard and soon take over their land."
    Bmom "They have the utilities to do so…"
    player "Yep, the only thing stopping them from adjusting their devious plans is us. We filed a case, and they have to halt their expansion."

    show mommabeaver neutral
    Bmom "So you're telling me, if your speculation is correct, we're not only fighting a company but also a large organization of officials and criminals?"
    player "Maam, may I remind you that this is only speculation. But the events at hand align badly. If you look at this photo, you see Mr. Wolf signing an agreement with an official, the falcon."
    Bmom "Mr. Felipe."
    player "Yep, so they may have ties with this person. The media states that the agreement is confidential, so they didn't show what's inside it. But that despises the point of transparency… whatever's inside of it, it seems too severe not to show the public"
    Bmom "what are you implying?"
    player "I'm implying that we are meddling with something more profound than the generational crisis for air and clean waters. We seem to have found a loophole for something more profound, if I'm correct. "
    player "That is why Mr. Celtic the wolf wanted to end this court case fast, so he hired Sheep De Lune, the fastest court ender out there. They didn't want anything to spill. "
    player "And surprisingly, this was their first case after the agreement with Mr. Felipe, the falcon. This company is tied with an organization so strong that an official like Mr. Felipe wants in. There are tons of clues… but we need evidence to prove those."
    player "… if we want to win the case your children wanted to file, we have to stress that Dunrar Mifflin barely replants their trees, and we have to surprise them with an argument regarding Mr. Felipe."
    
    show mommabeaver sad
    Bmom "Seems like it, but we seem to need to prepare for the worst."
    player "Indeed. I’m scared of De Lune too. She’s fast at cases, and she will not hesitate to object. "
    Bmom "I hope Iro comes back too… the court case will resume 3 days from now."
    player "I hope so, too… he has two days to report. But knowing him, he has a strict view of justice. He’ll come back with sufficient news. I’ll be filing the case now, Ms. Beaver. Leave the rest to me."
    
    show mommabeaver neutral
    Bmom "Alright!"

    hide mommabeaver with moveoutright
    player "I hope you pull this off, Iro"

    stop music fadeout 2.0
    
label IroWake:
    scene bg basement with Fade(1.5,2.0,1.3)
    show iro neutral at center with dissolve
    show iro mad
    Iro "{sc=2}Huh?!{/sc} Where's I at?!"

    play music "audio/bgm_courtroom.mp3" fadein 3.0 volume 0.3 loop #MUSIC BUTTON BUTTON WONT PLAY
    Hog "Helpu me :<"
    show hog neutral at right with dissolve
    show iro sad 
    Iro "Oh my dog, this looks serious…I’ll find a way to get us out!"
    "Lookie lookie."

    show iro mad
    Iro "{sc=2}Who's there?!{/sc}"
    Celtic "You're in a place where help isn't visibile."

    show wolf neutral at left with moveinleft
    Iro "Celtic, I can't believe you've done this!"
    Celtic "Ain’t it obvious? It’s all money, Iro. You’re a service dog for the law, I am a the wolf of wallstreet."

    show iro neutral 
    Iro "You don’t even look like Leonardo DeCaprio!"
    Celtic "Oh, shut it! You know what I mean. You’re underground. No connection to the outside world. Just us under a crummy old base with nothing but ourselves. Oh, not to mention, some guards are here, and they’ll keep you locked tight. "
    Iro "I'm not in the mood to be tied up right now, but I swear, I’ll get you for this"
    Celtic "I’d like to see you try, service dog. Once I succeed in your friend’s foolish court case, I will take over more land, produce more money, and soon provide more power to dominate this country. "
    
    show iro mad 
    Iro "That’s an act of terrorism, and I will call someone legal enough to get you railed."
    Celtic " Pfft. Guards, watch them with your life. I gotta show this to boss!"
    hide wolf with moveoutleft

    Hog "{bt=2}*Sigh*{/bt}"
    Iro "Darn it!"
    show goose neutral at left with moveinleft
    Guard "I'll be watching you today, lapdog"

    show iro neutral
    Iro "understood hays… "
    Iro "{i}I need to wait for an opening if I wanna succeed… preferably at night when things could go smoother{/i}"
    Iro "Hey, guard, do you offer any food, perhaps?"
    Guard "Shut it, dog!"
    Iro "Rude!"
    stop music fadeout 2.0

label PlayerFirm2:
    scene bg officefirm with Fade(1.5, 2.0, 1.5)
    show zeil normal at left with dissolve
    play music "audio/bgm_lawfirm.mp3" volume 0.3 fadein 3.0 loop

    player "Just one more day till we head into the abyss. I read the documents carefully, and I am still scared of what’s to come. I am not sure if I am ready to take down Sheep De Lune yet… I’ve overprepared, even. This will be a tough one."
    play sound "audio/sfx/sfx_knock.wav"
    "{bt=2}*Knock Knock*{/bt}"
    player "Come in!"

    show cassie neutral at right with moveinright
    Cassie "Hello, [povname]"

    show zeil smile2
    player "Oh hello, Cassie! How may I help you today?"

    show zeil smile
    Cassie "It’s more of like the other way around. You seem to have found a big case?"

    show zeil sad
    player "Yeah, I caught a big fish this time. I would not say I like doing cases like these since lives might be on the line if someone wins or someone fails."

    show zeil normal
    show cassie sad
    Cassie "Hm? Lost of lives? What are you talking about?"
    player "I may have found something terrible that is heavily associated with the case I’m handling."
    Cassie "Aren't you handling a case for those little beavers who want generational justice? I don't see anyone dying there."
    player "Cassie, you see, Mr. Felipe, The Government official, might be protecting Celtic, Dunrar Mifflin’s Ceo, through so-called “legal” rules. Felipe has the power to do so."
    Cassie "You sure are speculating quite a lot here. I know that Celtic is associated with Felipe based on their old public photo holding a sign of waver. That was their only public interaction even."
    Cassie "Are you saying that the waver Felipe signed for Celtic might have been for something else?"

    show zeil normal
    player "Just a speculation. Though I would love to stress that fact in court."
    Cassie "Heyya [povname], be cautious on what you're about to do, okay? If this accusation is incorrect, you might be fooling yourself in front of loads of people (including the media)."
    Cassie "However, if it is correct, you face a literal government official the next time you set foot in court."
    player "I may sound crazy, but those odds are the ones I’m willing to take. I must pursue this with whomever I can for justice and to stop whatever is happening."
    
    show cassie neutral
    Cassie "Pfft, your loss kiddo. But I can help you whenever you need a hand."

    show zeil smile2
    player "Glad to know that you're on my side <3"

    show zeil shocked
    show cassie tsunblush
    Cassie "!!! SSH- SHUT UP >//< {bt=2}*Blush*{/bt}"
    player "Hmm? Did I say something wrong?"

    show zeil normal
    Cassie "n..no it’s just.."
    Cassie "whatEVER! Just do your paperwork, you rookie"

    show zeil delighted
    player "Yes, maam!"

    show zeil smile
    show cassie blush
    Cassie "oh and {bt=2}*still blushng*{/bt} here are some laws regarding your case. Read them well."

    hide cassie with moveoutright
    "{sc=2}*shuts door*{/sc}"
    show zeil smile2
    player "Like said, glad to know that she cares about me and Ben <3"

    stop music fadeout 3.0

label IroWake2:
    scene bg basement with Fade(1.5,2.0,1.3)
    show iro neutral at center with dissolve
    show hog neutral at right with dissolve

    play music "audio/bgm_courtroom.mp3" fadein 3.0 volume 0.3 loop #MUSIC BUTTON BUTTON WONT PLAY
    Iro "It is evening, my dudes. Okay let’s recap the plan right now!"
    Hog "Ok"
    Iro "So I summersault, break his neck, and you get the keys and we baboosh. Got that?"
    Hog "Uhm... or we can make a diversion and take his keys?"
    Iro "{bt=2}*Snaps Fingers*{/bt} Great idea! Good thing I got this hairclip. Free yourself while the guard ain’t looking."
    Hog "Yeah!"
    Hog "{bt=2}*Gets Hairclip and Struggles to Free Himself*{/bt}"
    Iro "Wait, here comes a guard."

    show goose neutral at left with moveinleft
    Guard "What are you two talking bout? Don’t you know y’all will be dead by the time yall come out?"

    show iro mad
    Iro "No way! It’s more like you’ll be {bt}DEAD{/bt} because there aint no way this illegal stuff ain’t not not not goin' public!"
    show iro surprised 
    Guard " Pfft, you’re stuck here, stinky lapdog!"
    show iro mad
    Iro "Oh yeah, well you stink more than a stinkbomb!"
    Guard "HUH? Your butt smells so bad that even a car wash can’t clean your butt!"

    show iro mad with vpunch
    Iro "OHOHOH IT’S ON NOW! Youre so dumb that when I told you to look for your brain, you’d actually go search for it!"

    show iro surprised with hpunch
    Guard "You bark so small that i think youre a chihuahua!"

    show iro mad with vpunch
    Iro "Oh yeah! WELL you so ugly that when you throw a boomerang, it refused to come back!"

    show iro mad with hpunch
    Guard "Pfft! You’re so poor that you can’t even afford to pay attention!"
    Iro "Hey, I got 25 dollars on me right now! "
    Iro "You’re so fat that when you go to space, {sc=2}NASA THOUGHT THEY FOUND A NEW PLANET!{/sc}"
    show iro mad with vpunch

    show iro mad with hpunch
    show iro mad with vpunch
    show iro mad with hpunch
    Guard "..."

    show iro neutral 
    Iro "......"
    Guard "........ :("
    Guard " {bt=2}*starts tearing up*{/bt} a-a..are you a mi-mirror? B-because I hate y-ou!"
    Iro "Sheesh a self burn!"
    Iro "..."

    show iro sad
    Iro "Hey are you okay?"
    Guard "SHUT UP!"
    Guard "{bt=2}*Cries Louder*{/bt}"
    Iro "Oh Jeez... I think I broke her..."
    Guard "Huh well..."

    show iro surprised with hpunch
    Guard "You’re so dead that you’re gonna be roasted dog tonight! {bt=2}*points the gun at Iro*{/bt}"
    hide hog with dissolve
    Iro "HEYHEHEYHEYHEY!!!"
    Guard "GOOD BYE, DOG-"

    show hog shocked at left with easeintop
    show hog shocked at left with vpunch
    Guard "{bt=2}*Head Gets Hit*{/bt}"
    hide goose with dissolve

    Iro "OH MYY GUY, I DIDN’T NOTICE YOU GOT OUT!"
    Hog "Hedgehos are masters of stealth."

    show iro happy 
    Iro "I told you summer saulting was a good idea! {bt=2}*chain opens*{/bt} Let’s baboosh!"
    hide iro with moveoutleft
    hide hog with moveoutleft
    hide iro with fade

    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    Iro "Where to now?"
    menu:
        "Go left":
            Iro "Let's go here!"
        "Go right":
            Iro "Right is always right!"

    hide iro with moveoutleft
    hide hog with moveoutleft
    hide iro with fade

    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    Iro "Wait, isn't that Celtic?"
    Iro "Oh bad Jubbies, he's talking with somebody!"
    hide iro with dissolve
    hide hog with dissolve

    show wolf neutral at left with dissolve
    show felipe shadow at right with dissolve
    unk "So how’s the cush goin?"
    Celtic "The delivery of cush is doing well, sir."
    unk "And the tree business?"
    Celtic "It’s going lousy, sir, but we have constructed a plan to gain tons of money in a flash immediately."
    unk "I’m listening."
    Celtic "Cutting down that ancient tree will provide us with around 400 million in revenue. The only thing stopping us from cutting is the waves of indigenous bumpkins."
    unk "{bt=2}*Pops a cigar*{/bt} heh. You’re cutting an ancient tree after all!"
    unk "But... whatever the prolem is, get it done even if you have to use brute force."
    Celtic "Roger. We’ll get rich with this."
    unk "Oh, and don’t lose the case, Celtic."
    unk "Losing the court case with that rookie will taint my name."
    unk "{bt=2}*crisps cigar on table*{/bt}"
    unk "You know the consequences, right?"
    Celtic "Y-yes sir."
    hide wolf with dissolve
    hide felipe with dissolve

    show iro neutral at center with dissolve
    show hog neutral at right with dissolve
    Iro "Oh Christ, I got that on record..."
    Hog "Let's go."
    hide iro with moveoutleft
    hide hog with moveoutleft

    stop music fadeout 3.0
    jump IroOut

label IroCaught3:
    hide goose2
    hide goose
    hide iro
    hide hog
    show goose neutral with dissolve
    Guard "There you are!"
    hide goose with dissolve

    show iro neutral with dissolve
    show hog neutral with dissolve
    Iro "Oh crab apples they found us!"
    hide iro with dissolve
    hide hog with dissolve

    show goose neutral with dissolve
    Guard "Hands in the air."
    Guard "You're coming with us whether you like it not"
    Guard "Or else."
    $ renpy.full_restart()



label IroOut:
    scene bg nforest with fade
    show iro neutral at center with moveinright
    show hog neutral at right with moveinright

    play music "audio/bgm_irorunaway2.wav" volume 0.3 fadein 3.0 loop
    Iro "Now or never, lad!"    
    Hog "Indeed, friend."
    Iro "There seems to be a confusing route of ways here. Do you know any shortcuts we could use to get out of here fast?"
    Hog "I think so. Follow my lead."
    Iro "Alright-"

    Guard "Where are those snouts?!"
    Crew "I don't know, they msut be hiding in one of these trees."
    Guard "Wherever they are, they're as good as dead meat!"

    Iro "Well one thing's for sure, we gotta hide."
    Hog "I can help you knock them out as the master of stealth."
    Iro "Violence is indeed the answer"
    hide iro with moveoutleft
    hide hog with moveoutleft

    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    show bush at right with dissolve
    Iro "Agh I could barely see anything."
    Hog "Using a flashlight won't help."
    Iro "Yeah, we gotta make our movemtn as silent as possible."
    Guard "Search there, crew!"
    Iro "Ah dawg, they're comin' here."
    
    show goose neutral at left with moveinleft
    Crew "Searchin' the area, boss"
    Iro "{bt=1}I could see him... or her?{/bt}"
    Hog "{bt=1}Your call. Should I jump her or should we run past her?{/bt}"
    Iro "How could you be sure they're a her- you know what nevermind."

    "It is recommendable that you quicksave here."
    "The Game Newly Introduces an Assult Or Evade Mechanism."
    "The More Sneak Points you have, the better the chances of you succeeding an assult."
    "Sneak Points Start at 10 and it gets bigger as you progress. Max points is 50 each."
    $ SneakPoints = 10
    $ AssultPoints = 10

    menu:
        "Assult the Goose!":
            $ AssultPoints += 10
            Hog "Okay, got it."
            hide hog with dissolve
            Crew "Hmm, I smell a dog near me."
            show hog neutral at left with moveinleft
            show hog neutral with hpunch
            "{sc=5}Punch!{/sc}"
            Crew "{sc=1}G-gagh...{/sc}"
            hide goose with dissolve
            
        "Sneak past The Goose!":
            $ SneakPoints += 10
            Iro "Let's sneak past him. I'll follow your lead."
            Hog "Okay, got it."
            hide iro with moveoutright 
            hide hog with moveoutright


label IroOut2:
    scene bg nforest2 with dissolve
    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    if SneakPoints == 20:
        Iro "Alrighties! Passed that guy like it was nothing!"
        Hog "Let's not get toooo cocky, sir."
    else:
        Iro "Nice headlock!"
        Hog "He'll be back in an hour. Good thing I hid his body in a pile of bushes."

    show goose2 neutral at left with dissolve
    Guard "Quack, I wonder where they at."
    Iro "More incoming. I don't think he noticed we're right behind him."
    Hog "Your call, Iro."

    menu:
        "Hit the Goose in the Head":
            Hog "Roger"
            if AssultPoints == 20:
                hide hog with dissolve
                hide goose2
                show goose neutral at left
                Guard "Hey, you're the wanted ma-"
                show hog neutral at left with moveinleft
                show goose with hpunch
                "{sc=5}*Head Smack!*{/sc}"
                Iro "Nice One!"
                $ AssultPoints += 10
                hide goose with dissolve
            else:
                Hog "{bt=2}*Snaps Twig*{/bt}"
                hide goose2
                show goose neutral at left
                Guard "Hey! You're the wanted man!"
                Iro "Oh oopsies, diversion time!"
                transform alpha_dissolve:
                    alpha 0.0
                    linear 0.5 alpha 1.0
                    on hide:
                        linear 0.5 alpha 0
                    # This is to fade the bar in and out, and is only required once in your script

                init: ### just setting variables in advance so there are no undefined variable problems
                    $ timer_range = 0
                    $ timer_jump = 0
                    $ time = 0

                screen countdown:
                    timer 0.0001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
                        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

                    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
                        # ^This is the timer bar.
                        
                label questiontime4:
                    
                    label menu4:
                        $ time = 3                                     ### set variable time to 3
                        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
                        $ timer_jump = 'menu4_slow'                    ### set where you want to jump once the timer runs out
                        show screen countdown                          ### call and start the timer

                        menu:
                            "Hit His Face!":
                                hide screen countdown

                                Iro "Do it, Hog!"               ### stop the timer
                                hide hog with dissolve
                                Guard "What do you think you're talking about?"
                                Iro "Oh nothing, just a slick surprise!"
                                show hog shocked at left with moveinleft
                                show hog with vpunch
                                "{sc=5}*Gets Head Butted*{/sc}"
                                Guard "Agh!"
                                Guard "{sc=5}*Punches Hog*{/sc}"
                                show goose with vpunch
                                Iro "Oh no you don't!"
                                show iro at left with moveinright
                                show iro with hpunch
                                "{sc=5}*Gets Kicked in the Head*{/sc}"
                                Guard "{sc=2}Ugh...{/sc}"
                                hide goose with dissolve

                                Iro "Nice one!"
                                hide iro with moveoutleft
                                hide hog with moveoutleft
                                $ AssultPoints += 10
                                jump IroOut3
                            "Run Away":
                                hide screen countdown                  ### stop the timer
                                Guard "Freeze, I have a gun!"
                                jump IroCaught3

                    label menu4_slow:
                        jump IroCaught3
                            


        "Sneak out Like Nothing Happened":
            Iro "Let's skiddaddle."
            Hog "Roger."
            hide iro with moveoutright
            hide hog with moveoutright
            Guard "Hm? Did something move?"
            Guard "Hmm I bet it's just a litol owl."
            hide goose neutral
            $SneakPoints += 10
            
label IroOut3:
    scene bg nforest4 with dissolve
    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    Iro "We got out of that one!"
    Hog "Let's keep going."
    hide iro with moveoutleft
    hide hog with moveoutleft


    show goose neutral at left with dissolve
    show goose2 neutral at right with dissolve
    Guard "Quack, so what did you have for dinner?"
    Crew "Quack, I had sunflower seeds"
    Guard "Lucky!"
    
    Iro "Oh look, a gang of geese are inspecting the area."
    Iro "You reckin we can 2 v 2 'em?"
    if AssultPoints == 30:
        Hog "I think we can."
    else:
        Hog "Too risky, Iro."
    
    menu:
        "2 v 2!":
            if AssultPoints == 30:
                Iro "Let's hittem up!"
                Guard "Quack"
                Crew "Indeed-"
                show hog neutral at left with moveintop
                show hog with vpunch
                Guard "Quack?!"
                show iro neutral at right with moveintop
                show iro with hpunch
                $ AssultPoints += 10
            else:
                Iro "But we could try!"
                Hog "Okay, if you insist."
                show hog neutral at left with moveintop
                Guard "Quack?!"
                Guard "Hands in the air! {bt=2}*Points Gun at Hog*{/bt}"
                Iro "Oh crabs"
                jump IroCaught3
        "Sneak Past Them.":
            if SneakPoints >= 20:
                Iro "Let's just sneak past them"
                Hog "Got that covered."
                Crew "Quack, Indeed."
                Guard "Indeed, my brother"
                Iro "What are they talking about?"
                Hog "How should I know?"
                Crew "So the seeds last thursday were a hit huh?"
                Guard "I love sunflower seeds and all, but nothing beats sunflower beats."
                Crew "Quack! You're crazy!"
                $ SneakPoints += 10
            else:
                Crew "Hey did you hear something move in the bushes?"
                Guard "Yeah!"
                Crew "Freeze! {bt=2}*points gun at bush*{/bt}"
                jump IroCaught3
    
    hide goose with dissolve
    hide goose2 with dissolve

    show iro neutral with moveinright
    show hog neutral with moveinright
    Iro "Those geese were weird."
    Hog "Indeed."
    hide iro with moveoutleft
    hide hog with moveoutleft

label IroOut4:
    scene bg nforest5 with dissolve
    show iro neutral with moveinright
    show hog neutral at right with moveinright

    Iro "Looks like we're halfway out of the forest."
    Hog "I've never been into this part of the forest."
    Iro "Well you're in for a treat because people here are nuts!"
    hide iro with moveoutleft
    hide hog with moveoutleft

    show goose2 neutral at left with dissolve
    show goose neutral at center with dissolve
    show goosewalky right at right with dissolve

    Guard "I know they're here!"
    Crew "Quack."
    Guard "Welp, I'm calling for reinforcements."
    Crew "Is that necessary? It's 3 against 2"
    Guard "plus we have guns!"
    Crew "Right?!"
    Guard "Ok fine."
    Iro "Ulala, 3 geese."
    Hog "now that's a flock."
    Iro "Okay, I think it's possible to beat em up. We can tag team."

    if AssultPoints >= 30:
        Hog "Good call."
        Hog "I'll beat the goose at the left."
        Iro "I'll kick the one at the right, then we sandwich the center!"
        Iro "Haha! Goose sandwich."
    else:
        Hog "No, it's better if we sneak."
    menu:
        "Tag Team Brawl!":
            Hog "Alright, if you insist!"
            show hog neutral at left with moveinleft
            show hog with hpunch
            hide goose2 with dissolve
            if AssultPoints >= 40:
                Guard "{sc=3}Quack!!!{/sc}"
                Hog "{sc=3}Now, Iro!{/sc}"
                Crew "{sc=3}Oh no you don't! Freeze, I have a gun!{/sc}"
                transform alpha_dissolve:
                    alpha 0.0
                    linear 0.5 alpha 1.0
                    on hide:
                        linear 0.5 alpha 0
                    # This is to fade the bar in and out, and is only required once in your script

                init: ### just setting variables in advance so there are no undefined variable problems
                    $ timer_range = 0
                    $ timer_jump = 0
                    $ time = 0

                screen countdown:
                    timer 0.00001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
                        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

                    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
                        # ^This is the timer bar.
                        
                label questiontime5:
                    
                    label menu5:
                        $ time = 3                                     ### set variable time to 3
                        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
                        $ timer_jump = 'menu4_slow'                    ### set where you want to jump once the timer runs out
                        show screen countdown                          ### call and start the timer

                        menu:
                            "Kick his Snout!":
                                hide screen countdown 
                                show hog at center with moveinleft
                                Hog "{sc=2}*Attempts to kick snout*{/sc}"
                                Guard "{bt=4}*Kick Sweeps Hog's Feet*{/bt}"
                                Hog "{bt=2}*Falls Down*{/bt}"
                                Hog "Awwww man."
                                Guard "Freeze! I have a gun!"
                                Iro "CRAP I didn't save him in time."

                                jump IroCaught3
                            "Grab a Grip Of His Gun!":
                                hide screen countdown                  ### stop the timer
                                Guard "I'm not afraid to shoot y-"
                                show hog neutral at center with moveinleft
                                show hog with vpunch
                                Hog "{bt=2}*Moves the Gun and Grips The Gun*{/bt}"
                                Guard "{bt=2}*Struggles*{/bt}"
                                Crew "I got 'ya, Boss!"
                                Crew "{bt=2}*Points gun at Hog*{/bt}"
                                Crew "{sc=2}Screw off, little man!{/sc}"
                                Iro "Now's my chance!"
                                transform alpha_dissolve:
                                    alpha 0.0
                                    linear 0.5 alpha 1.0
                                    on hide:
                                        linear 0.5 alpha 0
                                    # This is to fade the bar in and out, and is only required once in your script

                                init: ### just setting variables in advance so there are no undefined variable problems
                                    $ timer_range = 0
                                    $ timer_jump = 0
                                    $ time = 0

                                screen countdown:
                                    timer 0.0001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
                                        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

                                    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
                                        # ^This is the timer bar.
                                        
                                label questiontime6:
                                    
                                    label menu6:
                                        $ time = 3                                     ### set variable time to 3
                                        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
                                        $ timer_jump = 'menu4_slow'                    ### set where you want to jump once the timer runs out
                                        show screen countdown                          ### call and start the timer

                                        menu:
                                            "Throw A Rock While Hidden":
                                                hide screen countdown
                                                Iro "{sc=3}Skiddaddllee Skiddloddle, your face is now a noodle! {/sc}{bt=2}*Picks Up Rock*{/bt}"
                                                Crew "Huh who said that?!"
                                                Iro "{bt=2}*Throws Rock at Crew*{/bt}"
                                                show rock at right with moveinright
                                                show rock with hpunch
                                                Crew "AUGH!"
                                                Iro "Happy Birthday to the Ground!"
                                                hide rock with dissolve
                                                show iro neutral at right with moveinright
                                                show iro with hpunch
                                                Iro "{bt=2}*Summmersault*{/bt}"
                                                hide goosewalky with dissolve

                                                Guard "{sc}Awwww crap.{/sc}"
                                                menu:
                                                    "Goose Sandwich!":
                                                        show iro at center with moveinright
                                                        show iro with hpunch
                                                        Guard "{sc}AAAAAAAAAAAAAAAAAAAAAA{/sc}"
                                                        hide goose with dissolve
                                                        Iro "haha goose sandwich"

                                                        $ AssultPoints += 10
                                                        jump IroOut5
                                                    "Take Down! (The Cool Way)":
                                                        show iro at center with moveinright
                                                        show iro with hpunch
                                                        Guard "{sc}AAAAAAAAAAAAAAAAAAAAAA{/sc}"
                                                        hide goose with dissolve

                                                        Hog "That was pretty cool."
                                                        Iro "I am something of a judo expert myself."
                                                        $ AssultPoints += 10
                                                        jump IroOut5

                                            "Summersault!":
                                                hide screen countdown                  ### stop the timer
                                                Iro "Summersault!!!!!"
                                                show iro neutral at right with moveinright
                                                Crew "{sc=2}WHO SAID THAT?{/sc} {bt=2}*points the gun at Iro*{/bt}"
                                                Hog "You just gotta say it?!"
                                                jump IroCaught3

                                                

                                    label menu6_slow:
                                        Crew "Boomboom! {sc=5}FLOOR, NOW!{/sc}"
                                        jump IroCaught3

                                

                            "Throw A Rock in his Face!":
                                hide screen countdown
                                Hog "{bt=2}*Grabs a Rock*{/bt}"
                                Guard "Oh no you don't!"
                                show hog with hpunch
                                Guard "{bt=2}*Shoot Hog's arm*{/bt}"
                                Hog "{sc=6}GAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/sc}"
                                Guard "Freeze! I'm not afraid to shoot!"
                                Iro "Oh crap, I can't move or else he'll get shot more."
                                jump IroCaught3
                                


                    label menu5_slow:
                        Crew "Can't think can you! {sc=5}Now Go DOWN THE FLOOR!{/sc}"
                        jump IroCaught3

            else:
                Iro "Time to butt i-"
                Crew "Oh no you don't"
                Crew "Freeze! I have a gun and I'm not afraid to use it!"
                Iro "Oh dalmatians."
                jump IroCaught3
        "Sneak":
            if SneakPoints >= 20:
                Iro "I changed my mind! Let's sneak past them."
                Hog "I catch your drift."
                $ SneakPoints += 10 
            else:
                Iro "Let's just sneak past them."
                Hog "Good call, but I want you to be careful since this place has too many twigs-"
                Iro "{bt=3}*Snaps Twig*{/bt}"
                Hog "Oh no."
                Guard "OVER THERE! I KNEW IT!"
                Crew "Put yoru hands in the air!"
                jump IroCaught3

label IroOut5:
    scene bg nforest6 with dissolve
    show hog neutral at right with dissolve
    show iro neutral at center with dissolve
    Hog "That was a bit hard..."
    Iro "That was literally Crazy. We just skiaddled 3 geese"
    if AssultPoints == 50:
        Iro "All we did was attack right now. I think we can handle the world."
    if SneakPoints == 50:
        Iro "All we did was sneak right now. I think I may have mastered the art of the SNEAK."
    
    Iro "In-game wise, we would've had around [SneakPoints] SneakPoints now!"
    Hog "And we would acquire about [AssultPoints] AssultPoints now!"

    if SneakPoints == 50:
        Iro "Hmm we have maxxed our SneakPoints Tree now I guess."
    elif AssultPoints == 50:
        Hog "Hmm we have maxxed our AssultPoints now then"
    else:
        Iro "Our points are pretty random."
    
    Iro "Hmm we have good stats to begin with. Let's keep going now, Ho-"
    Guard "{sc=2}THERE THEY ARE!! REINFORCEMENTS!!!!!{/sc}"
    Iro "Welp hehe, I think we should be running now."
    "..."
    Hog "{sc=3}RUNNNNN!!!!{/sc}"
    hide iro with moveoutleft
    hide hog with moveoutleft

    show goose2 neutral at center with moveinright
    show goosewalky left at right with moveinright
    Guard "Gah! I see them over there!"
    Crew "... HAH... {sc}HAHHHHH REINFORCEMENTSSSSSSSS!!!!{/sc}"
    hide goose2 with moveoutleft
    hide goosewalky with moveoutleft

label IroOut6:
    scene bg nforest3 with dissolve
    show iro neutral at center with moveinright
    show hog neutral at right with moveinright
    Iro "{bt=2}*pants*{/bt} We've been running all night, Hog..."
    Hog "Indeed, my friend... {bt=2}*pants*{/bt}"
    Hog "Wait, this is the road to my village!"
    Iro "Omg! I recommend we split up, I have some unfinished business to do in law."
    Iro "You'd be more safer there than here."
    Hog "Iro... you freed me from the depths of despair."
    Hog "And we fought side by side in the midst of trouble."
    Hog "Forever, you have my deepest gratitude."
    Hog "Thank you for everything."
    Iro "Hahaha! I feel flattered but it's all in the day's work~! You be careful now, okie?"
    Hog "{bt=2}*Salutes* I proclaim you as master of stealth now.{/bt}"
    hide hog with dissolve

    Iro "What a nice guy."
    Guard "Hey! There he is!"
    Iro "Gotta blast!"
    hide iro with moveoutleft

    show iro neutral with moveinright
    Iro "Okay, this is bad... Looks like I gotta go all out it running all night!"
    Crew "STOP HIM!"
    Iro "heh... I'm gonna love this."
    Iro "Good thing the sun is rising."
    Iro "I might be able to say my last words whilst staring at this glorius sunrise."
    Crew "{sc=4}FIRE IN THE HOLE!!{/sc}"
    Crew "{bt=2}*GUNSHOTS*{/bt}"

    show iro with hpunch
    show iro with vpunch
    show iro with hpunch
    show iro with vpunch
    show iro with hpunch
    show iro with vpunch
    show blood1 with dissolve
    Iro "{sc=5}*Arms get hit*{/sc}"
    Iro "{sc=5}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRFFF{/sc}"
    Crew "I heard him squeel in pain! let's get him!"
    Iro "I...'m not going down wihtout a fight!"
    Iro "[povname] You gotta... stall the time... before I get.. there.."
    hide iro with moveoutleft
    stop music fadeout 3.0

label Case2_Start2:
    show black with Dissolve(2.0)
    play music "audio/bgm_courtroom2.wav" volume 0.3 fadein 3.0 loop
    "-Iro Couldn't Come In Time-"
    "-Now it is...-"
    "-Court Day.-"
    scene bg courtroom with Fade(2.0,1.5,2.0)
    show zeil normal with dissolve
    player "{i}Iro isn't here yet... this is bad.{/i}"
    Bmom "He isn't here yet?"
    show mommabeaver neutral at left with moveinleft
    show zeil sad
    player "Not yet…. Looks like we have to rely on our instincts to pull this court session off."

    show zeil normal 
    Bmom "Have you filed the police yet?"
    player "Yes and they didn’t give a reply too. I asked 5 police stations now… and I have been up all night trying to identify his location…"
    Bmom "This is bad..."

    hide zeil with dissolve
    hide mommabeaver with dissolve
    show baliff neutral with dissolve

    Lady "For the trial, all rise. Trial 101083 in now in session. Honorable (Carl Cabales) please proceed."

    show carl neutral at center with dissolve
    show baliff at right with moveinleft
    Carl "Alright, we’ve been in court for two days now. This issue is so big that it might take more than two days to solve this session. Why so? Because we are asking for the freedom of trees in a particular area while making a lot of laws regarding the session at hand."
    Carl "Welp, you know how sessions work. Opposition, please start your stance."

    hide baliff with dissolve
    hide carl with dissolve

    show zeil normal at right with dissolve
    show triplet neutral at center with dissolve

    menu:
        "Explain Stance":
            player "Thank you, your honor. Today I’m representing these 3 triplets with their right of expression. The subject matter of the complaint is of common and general interest not just to several, but to all citizens of the Philippines. "

    hide triplet with dissolve
    show zeil at center with easeinright
    player "Consequently, since the parties are so numerous, it becomes impracticable, if not totally impossible, to bring all of them before the court. We likewise declare that the plaintiffs therein are numerous and representative enough to ensure the full protection of all concerned interests. "
    player "To put in perspective, the triplets are representing a generation to come. Needless to say, every generation has a responsibility to the next to preserve that rhythm and harmony for the full enjoyment of a balanced and healthful ecology."
    player "Put a little differently, the minors' assertion of their right to a sound environment constitutes, at the same time, the performance of their obligation to ensure the protection of that right for the generations to come."
    player "The complaint focuses on one specific fundamental legal right -- the right to a balanced and healthful ecology which, for the first time in our nation's constitutional history, is solemnly incorporated in the fundamental law."
    player "Section 16, Article II of the 1987 Constitution explicitly provides:
            SEC. 16. The State shall protect and advance the right of the people to a balanced and healthful ecology in accord with the rhythm and harmony of nature."
    player "This right unites with the right to health which is provided for in the preceding section of the same article:
            SEC. 15. The State shall protect and promote the right to health of the people and instill health consciousness among them."
    
    hide zeil with dissolve
    show sheep neutral with dissolve
    Sheep " {i}What a feisty introduction, player. I am starting  to like how you let things roll.{/i}"
    hide sheep with dissolve

    show carl neutral with dissolve
    Carl "I’m guessing that they sitll want certain laws to be implemented?"
    hide carl

    show zeil normal
    player "Yes"
    hide zeil

    show carl neutral
    Carl "Alright. Miss Sheep, what is your statement?"
    hide carl

    show sheep neutral
    Sheep " Despite the stance that these beaver kids potray, the court of appeles state that, with the right of permit, the ruling of chopping trees is uphold well. "
    Sheep "As stated, the rigt for an ecological future is indeed maintained."
    Sheep "The Right for a human right’s environment is maintained becasue we, as practitioners of what is ecologically right, conduct monthly replants of trees. In addition to that, the permits provided last court session were proof of belief that we operate under law.  "
    Sheep "Public records reveal that the defendant's, predecessors have granted timber license agreements ('TLA's') to various corporations to cut the aggregate area of 3.89 million hectares for commercial logging purposes."
    Sheep "With that plot of land at hand, indigenous tribes living daily lives will definately get the respect they need for their ancient land."
    Sheep "With that, I conclude my statement."
    hide sheep with dissolve

    show carl neutral with dissolve
    Carl "Alright, this is Indeed a tough one again hays."
    hide carl 

    show zeil annoyed
    player "Court was never easy >:("
    player "Where is Iro anyways?"
    hide zeil
    stop music fadeout 3.0
label IroOut7:
    scene bg factory2 with Fade(1.5, 0.6, 1.5)
    Iro "Oh Dalmatians, I barely got out of that one."
    show iro neutral with moveinright
    Iro "Looks like I made it to the factory in one piece haha! Or... two pieces if you count the blood."
    Crew "He is near! I could see his footsteps!"
    Iro "Oh come on! Give me a break!"
    hide iro with moveoutleft
    
    show goose2 neutral with moveinright
    Crew "Hah! How the tables have turned!"
    Guard "Close the exits! He's getting nearer!"
    Crew "Roger!"
    hide goose2 with moveoutleft
    
    scene bg factory3 with dissolve
    show iro neutral with moveinright
    Iro "I could see the exit!! My car is waiting for me!!!"
    Crew "Not so Fast!"
     
    show goose2 neutral at right with moveinright
    show iro at left with moveinright
    Crew "It's you against me, dog!"
    Iro "Heh... just like last time?"
    Crew "Indeed... but this time, I ain't gonna lose!"
    Iro "Alright, I'd like to see you try! Master of Judo against master of hammers!"
    Crew "{sc=2}I like the odds!{/sc}"

    play music "audio/bgm_irofight.wav" volume 0.3 fadein 3.0 loop

    #New stuff will be added here.
    #If AssultPoints >= 50 : Player will Get One Punch Option
    #If SneakPoints >= 50 : Player will get Run Away Option
    #If random, player will get one punch, one fight, or one dodge option.
    #If A Battle Scene regarding the player's attributes will hold. A battle scene that will require the player to mix their Assult and Sneak attributes.

    if AssultPoints >= 50:
        jump OnePunch
    elif SneakPoints >= 50:
        jump HideOut
    else:
        jump MixFight

label MixFight:
    menu:
        "Punch His Face!":
            jump MixFight2
        "Snout Kick!":
            jump MixFight2
        "Poke His Eyes!":
            jump MixFight2

label MixFight2:
    Iro "{sc=1}AAAAAAAA!!!{/sc}"
    Crew "{sc=1}AAAAAAAA!!!{/sc}"

    show goose2 at center with moveinright
    show iro at center with moveinleft
    show iro with vpunch
    show iro with hpunch

    Iro "{sc=2}Ouch!{/sc}"
    Crew "{sc=2}AGH! Did you really have to do that?!{/sc}"
    show goose2 at right with easeinleft
    Iro "Yes, I di-"

    Crew "{sc=4}*Starts Swinging Hammer!*{/sc}"
    Iro "King in the castle! That is a dangerous mama!"
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
label questiontime7:
    
    label menu7:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer

        $ IroSwim = False

        menu:
            "Run and Ram!":
                hide iro with dissolve
                hide screen countdown
                jump MixFight3
            "Dodge Roll!":
                hide iro with dissolve
                hide screen countdown                  
                jump MixFight3

    label menu7_slow:
        show goose2 at center
        show goose2 with hpunch
        Iro "Ouch!"
        jump MixFight3

label MixFight3:
    show iro neutral at left with moveinright
    Iro "That was uncalled for!"
    Iro "{sc=2}*Push and Kicks Goose!*{/sc}"
    show goose2 with hpunch

    Crew "{sc=4}*sighs*{/sc}"
    Iro "{bt=4}*pants*{/bt}"
    Crew "{sc=3}This has got to end now!{/sc}"

    Iro "Indeed."
    menu:
        "{sc=4}One Punch!{/sc}":
            jump OnePunch
        "The Great Escape!":
            jump HideOut




label HideOut:
    menu:
        "The Great Escape!":
            Iro "I have sneak into every area in the forest for quite some time now."
            Crew "So? You're a scared dog! You won't even fight us!"
            Iro "Heh, that's what you think!"
            Crew "Huh?!"
            Iro "{sc=2}*Throws Rock at Crew Member*{/sc}*"
            Crew "{sc=3}*Dodge*{/sc}"
            Crew "You missed!"
            Iro "I wasn't aiming at you!"
            Crew "Huh?!"
            Iro "Lights out, goose!"
            show black with dissolve
            Crew "{sc=3}HUH?! HEY!{/sc}"
            Iro "{sc=1}*Escapes*{/sc}"
            Iro "Adios Y' Gracias!"
            hide iro with dissolve
            hide black with dissolve
            Crew "{sc=3}Huh?! Where is he?!{/sc}"
            Crew "CRAP THE DOORS ARE CLOSED. IM LOCKED IN!"
            Iro "HAHA! Adios!"
            Crew "{sc=4}IROOOOO!!!{/sc}"
            jump Chapter2_FinalExam

label OnePunch:
    menu:
        "{sc=4}One Punch!{/sc}":
            Crew "I know you're gonna pull of something sick so {sc=4}HERE IS THE GANG!{/sc}"
            Crew "{sc=4}GANG, GET HIM!{/sc}"
            Guard "{sc=5}EAT FIST, DOG!{/sc}"
            show goose neutral at left with moveinright
            show goosewalky left at left with moveintop
            show goosewalky right at left with moveinleft
            show goose2 at left with moveinright
            Crew "Dodge this, DOG!"
            Iro "Wrong mistake, my friend. Wrong mistake."
            Crew "Hu-"
            Iro "This is.."
            Iro "{b}{sc=2}Goodbye.{/sc}{/b}"
            show black with dissolve
            Crew "{sc=2}H...huh?!{/sc}"
            Iro "I have bent space and time."
            Iro "It is time, mr. Crew member."
            Crew "Wh...{sc=4}WHAT ARE YOU TALKING ABOUT?!{/sc}"
            Iro "I'm sorry for I have to do this."
            Crew "HUH?!"
            Iro "{bt}*Sigh*{/bt}"
            Iro "{sc=2}One....{/sc}"
            Iro "{sc=10}PUUUUUUUUUUUUUNCCCCCCCCCCHHHHHHHHHHHHHHHHHHHHHH{/sc}"
            Crew "{sc=6}AYOOOO?!!!!{/sc}"
            Iro "{sc=20}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/sc}"
            Guard "{sc=10}WAIT NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO{/sc}"
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            Iro "{bt=1}*sigh*{/bt}"
            Iro "{sc=5} 20 PERCENT OF MY POWER! {/sc}"
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            Iro "{bt=5}*sigh*{/bt}"
            Iro "{sc=5} 40 PERCENT OF MY POWER! {/sc}"
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            Iro "{bt=5}*sigh*{/bt}"
            Iro "{sc=5} You... LEAVE ME NO CHOICE!!{/sc}"
            Iro "{sc=10}100 PERCENT!{/sc}"
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            show black with vpunch
            show black with hpunch
            hide black with dissolve
            Iro "Heh."
            hide goose neutral with dissolve
            hide goosewalky left with dissolve
            hide goosewalky right with dissolve
            hide goose2 with dissolve
            Crew "{sc=5}It.....{/sc}"
            Crew "{sc=3}Doesn't{/sc}"
            Crew "{sc=1}Hurt at all...{/sc}"
            Iro "That is because I stunned you for an hour."
            Iro "Don't even try catching up with me now! I have justice to serve!"
            hide iro with moveoutleft
            jump Chapter2_FinalExam

label Chapter2_FinalExam:
    stop music fadeout 3.0
    scene bg courtroom with Fade(1.5,2.0,1.3)
    show carl neutral with dissolve

    play music "audio/bgm_courtroom2.wav" volume 0.3 fadein 3.0 loop
    Carl "Your turn, Opposition. Give us another stance."
    hide carl with dissolve

    show zeil normal with dissolve
    player "“Twenty-five (25) years ago, the Philippines had sixteen (16) million hectares of rainforests, accounting for roughly 53 percent of the country's land mass"
    player "However, satellite images taken in 1987 reveal that only 1.2 million hectares of rainforests remained, accounting for only 4 percent (4.0 percent) of the country's land area."
    player "According to more recent estimates, there are just 850,000 hectares of virgin old-growth rainforests left, or around 2.8 percent of the Philippine archipelago's total land mass, and roughly 3.0 million hectares of immature and uneconomical secondary growth forests.”"
    player "“Another point is that At the current pace of deforestation, which is almost 200,000 hectares per year or 25 hectares per hour — including nightfall, Saturdays, Sundays, and holidays — the Philippines would be devoid of forest resources by the end of this decade, if not sooner."
    player "The negative implications, devastating consequences, substantial injury, and irreversible damage that this sustained trend of deforestation will have on the plaintiff minor's generation and future generations are obvious and undisputed."
    player "In reality, the environmental losses listed in paragraph 6 are already being felt, experienced, and suffered by the plaintiff adults' generation."
    hide zeil with dissolve

    show sheep neutral with dissolve
    Sheep "{i}... I honestly didn’t expect you to be this assertive, [povname]. Compared to last time, you were a bit of a nitwit in law. But now, you’re starting to be a formidable opponent. I appluad you. Though I’m not going down easily.{/i}"
    hide sheep

    show carl neutral
    Carl "These are indeed nice points. Any objections. Mrs. De Lune?”"
    hide carl neutral

    show sheep neutral
    Sheep "It’s Ms- you know waht? Nevemind. I do have objections. It’s that we have timber license agreements with everyone…"
    hide sheep
    stop music fadeout 3.0

label Chapter_Almost:
    scene bg reccomp with dissolve
    show cassie sad at left with dissolve 
    play music "audio/bgm_lawfirm.mp3" volume 0.3 fadein 3.0 loop
    Cassie "I hope [povname] is doing okay..."
    Cassie "Hmm is that a dog?"
    Iro "IN COMINGGG!!!!!!"

    show cassie shocked 
    Cassie "Huh?"
    Cassie "Wait is that I-"
    Iro "{sc=2}INCOMINGG DOG!{/sc}"
    show iro neutral at right with moveinright
    show iro with vpunch

    Iro "{bt}Ugh....{/bt}"
    Cassie "W-wait Iro?! What are you doing here?!"

    show cassie sad
    show iro mad
    Iro "Heh, long story, miss Meow Meow."
    Iro "But I gotta know where [povname] is!"
    show iro neutral
    show cassie neutral

    Cassie "He's at the lawfirm right now! Hurry!"
    Iro "Oh dang my dalmatians, gotta blasties, miss Meowy!"
    hide iro with moveoutright

    Cassie "... what an odd dog."
    stop music fadeout 3.0

label Chapter2_FinalExam2:
    scene bg courtroom with Fade(1.5,2.0,1.3)
    show zeil normal with dissolve
    play music "audio/bgm_courtroom2.wav" volume 0.3 fadein 3.0 loop
    player "The court session is going well for me and Sheep. We are providing 100 percent Good points once more. Though this time, she’s more factual than before. This is bad, since I too try to be factual here."
    hide zeil

    show carl neutraltable
    Carl "Carl “Hays… why do y’all have to mkae things hard?"
    hide carl 

    show zeil sad 
    player "{i}Another Stalemate, huh...{/i}"
    hide zeil

    show carl neutraltable
    Carl "With the proper introductions of law and nature given by [povname], things have been reasonable on their end. The next generation’s healthy ecological standards are indeed helpful for the better good of everything. "
    Carl "However, Ms. Sheep De Lune also provided points needed for a fairer environment. LumberLaws are a thing, and they have shown lots of evidence of actual replanting. They even hired agents to prove that… which is kinda overkill if you ask me."
    hide carl 

    show sheep neutral
    Sheep "{i}Not again. With this pace, he is asking for a stalemate{/i}"
    hide sheep

    show carl neutraltable
    Carl "I’m sad to say that, over my 10 years of beinga  a local judge, this has been one of my most intense cases ever. With that I proclaim this session as a stale-"
    show carl with hpunch
    Iro "OBJECTION!"
    hide carl

    show iro mad with dissolve
    Iro "'Tis I! Iro the Insepctor, Lawyer, Dalmatian COllector, and cute DOG!"
    hide iro

    show mommabeaver cry
    Bmom "IROOO!!"
    hide mommabeaver

    show triplet neutral
    Paddles "It's Iro!!"
    Stumpy "The inspector made it in time!"
    Nugget "Doggo!!"
    hide triplet

    show sheep neutral
    Sheep "Iro?! The Formiddable City Inspector?!"
    hide sheep

    show iro mad
    Iro "I.. I have clear evidence of.. Questionability …"
    hide iro 

    show wolf neutral
    Celtic "... heh. It's surely not about me!"
    hide wolf neutral

    show iro mad
    Iro "Dunrar Mifflin has been operating questionable acts under our noses! They have been transactioning multiple drugs in their forestry with evidence of this photo! {i}*Shows Photo to Everyone*{/i}"
    hide iro 

    show carl neutral
    Carl "This.. THIS IS OUTRAGEOUS?!"
    hide carl 

    show sheep neutral
    Sheep "No way, this is actual evidence from an insepctor. Iro the legendary inspector, who GOES ABOVE BOUNDS to prove something. This piece of evidence is nothing but true."
    hide sheep

    "Everyone in the courtroom gasped."

    show sheep neutral
    Sheep "This is… destructive and way out of bounds. How could this fly over my head?! Over my past 5 years of being a lawyer…"
    hide sheep

    show zeil smug
    player "And with that, how does the defendant want to defend themselves?"
    hide zeil

    show wolf neutral
    Celtic ".... Uhm!!! My humble lawyer, Mrs. Sheep De Lune, can explain all of this for me-"
    hide wolf neutral

    show sheep neutral
    Sheep "Regarding the case for a healthier ecology, All administrative remedies with the defendant's office have been exhausted by the plaintiff."
    Sheep "Plaintiffs presented defendant with a final demand to terminate all logging permits in the nation on March 2, 1990. As Annex , a copy of the plaintiffs' letter dated March 1, 1990 is attached."
    hide sheep

    show zeil shocked
    player "{i}Oh my, Miss De Lune is helping us?{/i}"
    hide zeil

    show wolf neutral
    Celtic "Wait werent you supposed to help me?"
    hide wolf

    show sheep neutral
    Sheep "However, I do say that this form of ecological acquisition is deemed APPROVED. With the impending amount of illegal transactions happening in the forests, Dunbar Mifflin used the tribe’s human rights as a place for quiet transactions."
    Sheep "However, may I please know if the one I’m saying is true? Regarding the license, sir Iro"
    hide sheep 

    show iro mad
    Iro "I have captured photos of fake license transactions by a shadowy figure and Mr. Celtic to add to this case. This has been a tough case since I, too, had to be wary of my acts in getting this information. I hold one of the plagiarized documents of many fake licenses bestowed upon sir Celtic’s name!"
    hide iro 

    show sheep neutral
    Sheep "I HAVE BEEN DEFENDING A THIEF, A CORRUPT OFFICIAL, AND A LIAR THE WHOLE TIME!? You hyppocrite! The guts of you to hire a prestine lawyer as I?!"
    hide sheep

    show iro neutral
    Iro "Before I forget, Celtic and his crew were planning to cut an ancient tree speical for the indigenous people. They even hurt and harassed those people who tried defending their tree!"
    hide iro 

    show carl neutral
    Carl "This is... over the top. Mr. Celtic, PLEASE defend yourself."
    hide carl

    show sheep neutral
    Sheep "No, your honour. I accuse, my defendant, with the support of multiple evidences proclaimed by Iro Lockheart,{b} as GUILTY of faking NUMEROUS permits {/b} and for LYING TO ME!"
    Sheep "Mr. Bear, despite the layers of encryption your permit database has, why is this so?!"
    hide sheep

    show bear with dissolve
    Beary "It seems like I too have been damned. An official higher than Celtic must've paved their way into our database and approved it as theirs without our confirmation."
    hide bear
    show zeil shocked
    player "{i}On official?! This might be Mr. Felipe.{/i}"
    hide zeil
    show bear
    Beary "I hearby conclude Permit 6882094328 and 4405189312 as fake and illegal permits!"
    hide bear

    show sheep neutral
    Sheep "Is this enough to prove Celtic the LIAR guilty of everything he does?!"
    Sheep "IF NOT then..."
    Sheep "The specific provisions applicable to particular licenses or permits in this title, the City Council may revoke any license or permit issued under this title after it has been issued, when any one or more of the following grounds are found to exist:"
    Sheep "Illegal issuance of the permit or license;  Issuance of the permit or license without authority or power; Issuance under an unauthorized ordinance or under an ordinance illegally adopted; Issuance in violation of an ordinance."
    Sheep "GOSH, and the lsit GOES ON AND ON!"
    hide sheep with dissolve

    show iro mad with dissolve
    Iro "The Indigenous promotes sustainable forest management as expressed in their respect to customary laws pertaining to land rights, adoption of upland cultivation practices following soil and water conservation principles, stand management to promote ample supply of wood and fuel wood, and biodiversity protection"
    Iro "Furthermore, they symbolize our undying Filipino culture.  Hence, the government, NGOs and other concerned stakeholders need to continuously support programmes in order to protect the aesthetic and traditional value of the Indigenous landscapes."
    Iro "Celtic, with no due respect, violated these standards. {i}*Shows Photos*{/i}"
    hide iro with dissolve

    show zeil normal
    player "Under Section 14, Article XIV, id. we must conserve and promote the nation's cultural heritage and resources (sic)"
    player "Under Section 16, Article II, id. we must protect and advance the right of the people to a balanced and healthful ecology in accord with the rhythm and harmony of nature."
    player "Finally, defendant's act is contrary to the highest law of humankind — the natural law — and violative of plaintiffs' right to self-preservation and perpetuation."
    player "There is no other plain, speedy and adequate remedy in law other than the instant action to arrest the unabated hemorrhage of the country's vital life support systems and continued rape of Mother Earth."
    hide zeil

    show carl neutral with dissolve
    Carl "..."
    Carl "This is the frist time... I saw 3 lawyers make a trio to expose... a corrupt official..."
    Carl "I am... amazed."
    show carl neutraltable
    Carl "Ehem. But with that note. I conclude, the defendant with tied strings to an unknown official, as {b}guilty{/b} of charge for his... multiple cases."
    Carl "Dunrar Mifflin's Operations will be halted for further inspection. Your licenses shall be inspected. Plus, you have to pay for the charges you have been given."
    Carl "This is next level."
    Carl "I know people messed up exist, but I have never met someone as messed up as you, Celtic."
    Carl "Really? Even hitting an indigenous person?"
    show carl neutraltable hammer with vpunch
    stop music fadeout 3.0

label Chapter2_CourtDone:
    scene bg courtroom with Fade(3.0,1.0,3.0)
    show mommabeaver cry at right with dissolve
    show triplet neutral at center with dissolve
    play music "audio/bgm_victory.wav" fadein 3.0 volume 0.3 loop

    Bmom "Did.."
    Paddles "{sc=1}Mom... we...{/sc}"
    Stumpy "{sc=5}MOM, WE WON THE CASE!{/sc}"
    Nugget "I want chicken nugger"
    Bmom "{sc=5}KIDS!!! I CAN'T EXPLAIN ME RIGHT NOW!!!{/sc}"
    show mommabeaver at center with moveinright
    Bmom "{sc=2}*CRIES MORE AND HUGS KIDS*{/sc}"
    Stumpy "{bt}WAAAAAAAAAAAAAHHHHH{/bt}"
    Paddles "{sc=3}WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/sc}"
    Nugget "i want fries, mom"
    Stumpy "{sc=2}FOR THE GENERATIONS TO COME!{/sc}"
    Paddles "{sc=2}INDEED!{/sc}"
    Nugget "Yes!"
    Bmom "{sc=5}MY KIDSSSSSSSSSSS!!!! T-T{/sc}"

    scene bg courtroom with fade
    show zeil normal at left with dissolve
    show iro neutral at center with dissolve

    player "I-Iro...."
    Iro "Arf."
    player "..."
    Iro "..."

    show iro happy
    Iro "I mean WHAT'S UP [povname] !!! DID YA MISS ME?!"

    show zeil sad 
    player "{sc=2}OF COURSE I DID{/sc}"
    player "{sc=2}I WAS SO WORRIED!!! *Hugs iro*{/sc}"
    Iro "Hehe, I smell like dog poo hehehehe"
    player "Yeah..."
    Iro "Yknow stuff was crazy back there... with all those fighting and sneaking! and runnin! endlesss runninggg!!!!!!! I felt like a pup."
    player "Still, Iro!!! >:( I am so glad that you're okay!!! :("
    player "We were all so worried!!!"
    player "You were gone for 2 days?! No police wanted to help us for some werid reason..."
    show zeil normal

    show iro mad
    Iro "It must be Celtic and his strings."
    player "Yeah. I have to tell you soemthing later. It's about Felipe and Celtic."

    show iro surprised
    Iro "Felipe... the government official?"

    show zeil smile2
    show iro neutral
    player "Oh wait, that's Sheep De Lune!"
    player "Sheep!"

    show sheep neutral at right with moveinright
    Sheep "You called, [povname] ?"
    player "Yeah... I was gonna ask, why did you help us?"
    Sheep "[povname] it isn't that complicated, okay?"
    Sheep "I am consistently serious, I have integrity, always honest, has etiquette, and I was raised by classists."

    show zeil annoyed
    player "{i}You're narcissistic too.{/i}"
    show zeil normal
    Sheep "I am... the type of person who would instantly DROP the case if I sense something fishy."
    Sheep "I don't like working with criminals. It taints my name, and my theory of law."
    Sheep "By far, this was the most stressful one. I can't believe I believed what must be unbelievable."
    Sheep "And on that note... *bows* I am sorry, [povname] for I have sided with someone I did not know was evil."

    player "{i}Jeez talk about a formal apology...{/i}"

    show zeil smile
    player "It's okay, Sheep. I know you're the type of lady who woul-"
    show zeil shocked
    Sheep "So let me treat you in a fancy buffet worth 1000 dollars per head! My treat~"
    show zeil annoyed
    player "{i}Like said, she interrupts me mid-sentence.{/i}"
    show zeil smile
    player "No, it's okay Miss De Lune. I am fine with the apology. I'm not that materialistic."
    Sheep "Still, please take this coupon. It gives you 1000 dollars off on your orders in said Buffet. It's fancy, and I hope you could use it to date with someone!"
    
    show zeil annoyed
    player "HEY! I am not into dating righ-"
    Sheep "Oh really?"
    Sheep "With those looks, you must be falling for some colleague in your firm."

    show zeil shocked
    player "Hey!"

    show iro happy
    Iro "Heh, I knew you got it in you, [povname] . I knew you liked the Meow meow!"

    show zeil annoyed 
    player "No, I do not >:( She is my colleague!"
    Sheep "Heh. We'll see."

    show iro neutral
    Sheep "Anyways, I have to go now. I have a fancy buffet reserved for Ms. De Lune."
    Sheep "Ciao!!!"
    hide sheep with moveoutright

    show zeil smile2
    player "What a sweet and fancy Sheep!"
    Iro "I will get going now, my friend. I have other things to insp.. {sc=1}insepc.......{/sc}"
    stop music fadeout 3.0

    show zeil normal
    Iro "{sc=5}*COLLAPSES*{/sc}"
    show iro with vpunch
    hide iro with dissolve
    show zeil shocked

    player "{sc=1}Iro?{/sc}{sc=4}IRO!!!!!!!!!!!{/sc}"
    stop music fadeout (4.0)
    show black with Dissolve(5.0)
    

label ExtraScene2:
    "Iro Was Rushed Into The Hospital."
    "Doctor Medications Stated That He Fell Unto a Coma."
    "-End of Chapter 2-"
    scene bg basement with Fade(0.5,0.0,0.5)
    unk "Hmm..."
    Celtic "Boss... I could explain..."
    unk "Welp! Haha! {sc=3}Crazy{/sc} me am I? For {sc=3}trusting{/sc} a wolf who can't even contain their excitement for {sc=5}CASH?!{/sc}"
    Celtic "Boss, it ain't like that..."

    show blood8 with hpunch 
    unk "{sc=2}*Slaps Celtic with a Gun*{/sc}"
    unk "Hehe."
    unk "{sc=5}I get... {/sc}{sc=1}a little crazy....{/sc} {sc=3} CELTIC, OF DUNRAR MIFFLIN.{/sc}"
    Celtic "{sc=1}*Coughs Blood* B-boss... We have new leads...{/sc}"
    unk "{sc=5}NEW LEADS FOR NEW BUSINESS?! {/sc} {sc=3}OR NEW LEADS FOR EXTORTION?!{/sc}"
    Celtic "{sc=1}B-both...{/sc}"
    unk "Heh."
    unk "{sc=2}You know, Celtic...{/sc}"
    unk "A rookie of a lawyer, together with this Sheep De Lune... and really? A childish dog as an inspector... and a pack of beavers wanting to save the day?"
    unk "They roused suspicion on me, Celtic. Over my past 13 years of governance, they finally bat an eye on me."
    unk "{sc=3}BAHHAHAHAHAHHAHAA{/sc}"
    unk "{sc=4}IT TOOK THEM 13 YEARS, CELTIC. 13 GODDAMN YEARS!{/sc}"
    unk "I think that calls for a celebration."
    unk "13 years of whatever the hell we're doing, and 1 week of damn inspecting."
    unk "You've indeed tainted my name, {sc=1}Celtic.{/sc}"
    Celtic "{sc=2}B-boss, Please... we can talk this out!{/sc}"
    unk "I've given you too many chances, old pumpkin."
    unk "{cps=8}Toooooooooooo many chances, old partner.{/cps}"
    unk "{cps=8}The Tree Business Was A Fluke.{/cps}"
    Celtic "{sc=5}BOSS, PLEA-{/sc}"
    unk "What a dumb piece of crap. Imagine those as your last words? {sc=1}I'll make sure to engrave that on your gravestone.{/sc}"
    unk "{cps=7}6 Feet Under The Ground.{/cps}"
    unk "{cps=7}{sc}Worms eating your skin.{/sc}{/cps}"
    unk "Heh! Why am I prolonging this? {sc=5}EAT LED!{/sc}"

    show blood7 with hpunch

    unk "Hmp. Cleaning blood up is my expertise I guess."

    show felipe neutral with dissolve
    Felipe "I guess the delivery is going well, I pressume?"
    Felipe "Tristan, my finest handler and smartest customer."
    Felipe "You've indeed tackled the situation well."
    
    show felipe at right with moveinleft
    show tristan neutral at left with moveinleft

    Tristan "Indeed, Mr. Felipe."
    Tristan "The delivery of the drugs are on the way to our station, ready for distribution"
    
    Felipe "Oh hush, Tristan. You've earned the right to call me Fill, my very own nickname."
    Tristan "Heh, I hope so, Boss. But my respect for you is still high."
    Felipe "You flatter me, my boy. You're like a son to me sometimes."
    Felipe "{bt=2}*Gets straw and powder*{/bt}"
    Felipe "To victory, my lad!"
    Tristan "Heh. We haven't won yet boss, remember?"
    Felipe "{cps=9}What makes you say that?{/cps}"
    Tristan "I think we're being speculated."
    Felipe "Hmm..."
    Tristan "We are in a brink of being "

label Chapter3_BeforeStart:
    scene bg osfirm with Fade(2.0,1.5,1.0)
    show zeil normal with dissolve
    play music "audio/bgm_lawfirm.mp3" fadein 3.0 volume 0.3 loop #MUSIC BUTTON

    player "{i}It's been quite a while now since Ben stopped coming into work.{/i}"
    player "{i}He hasn’t contacted me since that time I messaged him if he was alright. He said he was just going to just take some time off work, but hasn’t it been too long?{/i}"

    show zeil shocked
    player "{i}Maybe he’s finally going to retire… this line of work IS stressful, and Ben deserves to retire. He’s done so much to help the public! I think he deserves the rest.{/i}"
    
    show zeil smile 
    player "{i}I should go visit him at his place one of these days! I’ll even bring Cassie along, maybe we can stop by that cafe and buy him that delicious pandesal.){/i}"

    scene bg officefirm with fade
    show zeil smile2 at left with dissolve 
    player "{i}Yeah, that’s seems like a great idea. I’ll tell Cassie about it when I see her-{/i}"

    show zeil shocked
    player "{sc=1}!!!{/sc}"

    show zeil bored
    show cassie sad at right with moveinright
    player "Cassie??? You scared me! Don’t just jump out like that! Jeez…"
    
    show zeil shocked
    player "{i}Oh she's crying?!{/i}"

    show zeil sad
    player "C-cassie?, why- what- what is it, Whats wrong?"
    Cassie "{sc=1}I-It's Ben!!! He-{/sc}"

    stop music fadeout 2.0

label Chapter3_Start:
    scene bg courtroom with Fade(2.0,1.5,2.0)

    play music "audio/bgm_courtroom3.wav" fadein 3.0 volume 0.3 loop    
    show carl neutraltable with dissolve
    show baliff neutral at right with dissolve
    Lady "For the trial, all rise. RTC branch 24 is now in session. Honorable Carl Cabales, please proceed."
    Carl "Thank you, you may all be seated"

    play sound "audio/sfx/sfx_gavel1tap.wav" #Gavel Tap

    Carl "Let's call the case"
    Lady "the court is now in session, we call on case #133438 .People of the Philippines, plaintiff-appealee vs  Felipe (Falcon) Dimapilis, accused - appealant."

    hide baliff with dissolve

    Carl "Is the prosecution ready?"

    hide carl
    show zeil normal with dissolve
    player "Yes, your honor."
    hide zeil

    show carl neutral
    Carl "Is the Defense ready?"
    hide carl with dissolve

    show tristan neutral with dissolve
    Tristan "Yes your honor."
    hide tristan

    show carl neutral
    Carl "We will now hear the opening statement of the prosecution."
    hide carl with dissolve

    show zeil concerned with dissolve
    player "{i}i need to win this case,or else ill never know what ben wanted to achieve. What was he doing? why didnt he ask for help?{/i}"
    
    show zeil normal
    player "Your honor, members of the jury, my name is [povname] and I represent the People of the Phillipines in this case."
    player "We intend to prove that, Accused, {b}Felipe Dimapilis{/b} had stabbed a senior lawyer, Benjamin (binturong) Bustamante during a business meeting in the afternoon."
    
    show zeil angry 
    player "By being the lead cause to benjamin’s passing, he unlawfully and willfully took away a person’s life. When you have heard all the facts, please decided a verdict of guilty."
    hide zeil 

    show carl neutral
    Carl " would the defense like to give a opening statement or would you like to give the stand to the prosecution side until they rests their case?"
    hide carl 

    show tristan neutral 
    Tristan "We would like to stay your honor in the case of the People of the {b}Philipines vs Felipe Dimapilis {/b}."
    Tristan "My name is Tristan (Tiger) Benavides and i represent Felipe Dimapilis in this case. My client, Felipe was accused of murder, rather than a homocide that only transpired due to Benjamin’s verbal threats towards Felipe Dimapilis."
    Tristan "Once we have stated the facts, the verdict we ask for your honor is {b}Not Guilty.{/b}"
    hide tristan 
    
    show carl neutral 
    Carl "Thank you. For the persecution, you may now call on your first witness."
    hide carl 

    show zeil smile
    player "yes, your honor. The persecution would like to call on Ms. Terisita (Tariktik) Kaparo to the stand."
    hide zeil

    show baliff neutral with dissolve
    Lady "Do you swear to tell the whole truth and nothing but the truth so help me God?"
    hide baliff with dissolve

    show bird neutral at left with dissolve
    Terisita "Y-yes, I swear!"
    
    show zeil question at right with dissolve
    player "May I proceed your honor?"
    hide zeil 
    hide bird

    show carl neutral with dissolve
    Carl "yes, you may now proceed."
    hide carl with dissolve

    show bird neutral at left with dissolve
    show zeil smile at right with dissolve
    player "Please Introduce yourself miss"

    show zeil question at right with dissolve
    Terisita "My name is Terisita Kaparo and I'm one of be Mr. Bustamante’s many business partners."

    show zeil smug
    player "On October 21, around 9’oclock, where were you Ms. Kaparo?"
    Terisita "I believe i was on my way to a meeting with Mr. Bustamante in his home."
    show zeil question 

    menu: 
        "Were you the only one in the house during the meeting?":
            player "Were you the only one in the house during the meeting?"
            Terisita "No, I wasn’t the only one there in Mr. Bustamate’s home"
            Terisita "On the way to the house, I was alone but I ran into {b}Mrs. Hernandez, another fellow business partner{/b}, and we ended up going there together when we found out we were both called by Benjamin."
            player "Who else was in Mr. Bustamante’s home?"
            Terisita "{b}Mr. Miedes{/b} was already in the house when we arrived, and {b}Mr. Dimapilis{/b} showed up as well."
        "Was somebody else with you in the house during this meeting?":
            player "Was somebody else with you in the house during this meeting?"
            Terisita "Yes, there were four of us - excluding Mr. Bustamante - in the house."
            player "And who were these three guests with you in Mr. Bustamante’s home?"
            Terisita "{b}Mrs. Hernandez, another fellow business partner of ours {/b}who I ran into when I was heading towards Benjamin’s house,  {b}Mr. Miedes{/b}, and {b}Mr. Dimapilis.{/b}"


    $ PlayerChance = 3
    $ Choice1 = False
    $ Choice2 = False
    $ Choice3 = False

label Chap3_Inter1Checker:
    if Choice2 and Choice3:
        jump Chap3_Inter1Done
    else:
        menu:
            "So, what time would you say Mrs. Hernandez joined?":
                $ Choice1 = True
                jump Inter1Choice1

            "What was Mr. Miedes doing in Mr. Bustamante’s home?":
                $ Choice2 = True
                jump Inter1Choice2

            "Was Mr. Dimapilis also part of the meeting with you?":
                $ Choice3 = True
                jump Inter1Choice3
        
label Inter1Choice1:
    player "So, what time would you say Mrs. Hernandez joined?"

    show zeil shocked
    Terisita "Weren’t you listening to my statement?"
    show zeil bored
    player "Uh..."
    Terisita " I clearly said I ran into Mrs. Hernandez on the way to Benjamin’s house, so, of course, we arrived together at the same time!"

    show zeil smug 
    Carl "Are you alright [povname]? Everyone in the room heard Mrs. Kaparo’s statement but you. Please pay attention."

    show zeil annoyed
    player "{i}What was I thinking?! I can't mess up again.{/i}"

    show zeil question 
    $ PlayerChance -= 1
    jump Chap3_Inter1Checker

label Inter1Choice2:
    player "What was Mr. Miedes doing in Mr. Bustamante’s home?"

    show zeil concerned
    Terisita "Um… I’m not really sure… He seemed to be just waiting for something in Benjamin’s home."

    show zeil annoyed
    player "{i}That lead nowhere. I should ask another question{/i}"
    show zeil question
    jump Chap3_Inter1Checker

label Inter1Choice3:
    player "Was Mr. Dimapilis also part of the meeting with you?"
    Terisita "Im unsure, When Mr. Bustamante invited me h-he did not mention other individuals who will be present in the m-meeting we agreed upon."
    jump Chap3_Inter1Checker

label Chap3_Inter1Done:
    show zeil question 
    player "I see,  Well Ms. Kaparo, going back on your statement, you said that Mr. Dimapilis had exhanged a few words with Mr. Bustamente? Can you please elaborate?"

    show zeil shocked
    Terisita "To my knowledge, I believe mr. Bustamante and Mr. dimapilis share a history together. "

    show zeil normal
    Terisita "So when Mr. dimapilis started conversing, I assumed it was somewhat private so I chose to stay away from eavesdropping."
    Terisita "In any case, I was too far to hear anything clear, however I did hear Mr Bustamante say in “stop, before someone gets hurt” in a stern tone then Mr. Dimapilis left. "
    player "Did anything unusual happen after their exchange?"

    show zeil smug
    Terisita "Obviously!"

    show zeil bored
    player "Would you care to elaborate on that Ms. Terisita?"
    Terisita "Mr. Dimapilis left for a while, but then he came back… and then h-he, {sc=2}he…{/sc}"

    show zeil concerned
    player "{i}I hope I was right...{/i}"

    show zeil shocked
    Terisita "{sc=2}He stabbed Benjamin!{/sc}"

    show zeil smug
    player "Who stabbed Mr. Bustamante?"

    show zeil shocked
    Terisita "Why, {sc=1}it was Mr. Felipe Dimapilis!{/sc}"
    player "When Mr. Bustamante was stabbed, where were you in the house?"

    show zeil annoyed
    Terisita "I was directly in front of them as it was happening."

    show zeil smug 
    player "Exactly how far were you away from them?"
    Terisita "I would say a meter or 2"

    show zeil question
    player "and what part of the body was Mr. Bustamante stabbed?"
    
    show zeil sad
    Terisita "He was stabbed in the back."
    player "And if i remember correctly miss, that the accused, Mr. Dimapilis stabbed Mr. Bustamante’s back, did you happen to see the weapon that was used to harm him?"
   
    Terisita "It was a Knife."

    show zeil normal
    player "That is all, your honor."

    hide bird with moveoutleft
    show zeil at center with moveinright
    player "{i}I wonder how will the defense counter what we just witnessed?{/i}"
    hide zeil

    show carl neutral
    Carl "Thank you, [povname]. Would the defense like to cross examine?"
    hide carl 

    "{b}Factoid:{/b} Cross examination: used to combat an unreliable testimony from a witness. It attacks the accuracy and truth behind the nature of a testimony."

    show tristan neutral with dissolve
    Tristan "Yes, your honor."
    hide tristan

    show carl neutral
    Carl "You may proceed."
    hide carl 

    show bird neutral at left with moveinleft
    show tristan neutral at right with moveinright
    Tristan "Ms. Terisita, could you please restate what you had heard Mr. Bustamante had said to Mr. Dimapilis."
    Terisita "he had said 'Stop, before someone gets hurt'"
    Tristan "Your honor, I believe that the accused was threatened by Mr. Bustamante. The statement alone showed a possible infliction of hurt towards an individual, i. E my client."
    Tristan "Anyone in a situation like this would be thrown to a fit of panic which can cause a multitude of outcome however since what was used as a threat was physical, they retailiated physically through the act of stabbing."
    Tristan "That is all, your honor."
    hide tristan with moveoutright
    hide bird with moveoutleft

    show zeil annoyed
    player "{i}ah.. So you're focused on lowering the blow on your client huh?{/i}"
    "The appelant is attempting to argue for {b}appreciation of mitigating circumstances of passion and obfuscation.{/b} It essentially means that the crime was commited due to a burst of emotion evoked by stimuli enough to throw away all sense of reason. "
    "Basically getting very mad enough to be able to hurt someone physically"
    hide zeil

    show carl neutral 
    Carl "Would the prosecution like to redirect?"
    hide carl 

    "{b}Factoid:{/b} redirect:examination of your own witness after a cross examination."

    show zeil smug
    player "No, your honor."
    hide zeil 

    show carl neutral
    Carl "You may go back to your seat, Mrs. Kaparo."
    Carl "does the prosecution have anymore witnesses to present?"
    hide carl

    show zeil normal 
    player "Yes your honor. The prosecution would like to call  {b}Mrs. Theodora Hernandez{/b} to  the witness stand"
    hide zeil

    show smol
    Theodora "Hello everyone! My name Theodora Hernandez, I am also a long time business partner of Mr. Bustamante."
    show smol at left with moveinleft
    show zeil question at right with moveinright
    player "So tell me Mrs. Hernandez, how close were you to Mr. Bustamante and the accused when they having their 'private conversation'"

    Theodora "why I was alot more closer than Ms. Kaparo was! For some reason she opped to move away when Mr. Bustamante and Mr. Dimapilis started conversing."
    player "Did anything in their conversation sound unusual to you? "

    show zeil smug 
    Theodora "I really can’t say I have. The whole conversation they were having was pretty hush hush y'know?"

    show zeil shocked 
    Theodora "Oh! But I did hear Mr. Bustamante saying something all stern like."
    Theodora "It was something along the lines of: ‘You need to stop before someone gets hurt. Im sorry Im not in a good mood for this discussion’ and ‘can you please leave’ a bit after."
    
    show zeil smug
    player "Well isn't that  kinda sinister?"
    player "Despite being close to the victim by proximity, why was it you were not able to hear the rest of their conversation?"

    hide zeil
    hide smol 

    show tristan neutral
    Tristan "{sc=2}{b}Objection!{/b}{/sc}"
    Tristan "That is an opinonated statement"
    hide tristan 


    "{b}Factoid:{/b} Opinionated statement: witness testified based on their opinion- no facts but only subjectivity"

    show carl neutral with dissolve
    Carl "Objection sustained. Good ears, Tristan. It's kinda terrifying."
    hide carl 

    show zeil annoyed 
    player "{i}shoot, I said that aloud, i gotta be more careful.{/i}"
    hide zeil

    show smol at left with moveinleft
    show zeil question at right with moveinleft
    Theodora "Well y’see a tricycle with a loud engine zoomed by. It was soo loud it muffled some parts of the conversation."
    player "Can you describe what had happened between the accused and Mr. Bustamante."
    Theodora " It all happened fast y’see? We didnt even see Mr. Dimapilis return, cause im guessing it was because  Myself and Ms. kaparo were both preoccupied with the documents that was given to us by Mr. Bustamante."
    
    show zeil shocked 
    Theodora "All of the sudden he came from behind and stabbed Mr. Bustamante in front of our eyes! "
    player "Did you notice anything off about the accused when he approached the victim?"

    show zeil normal 
    Theodora "well for starters he didnt really alert anyone that he arrived and he also approached Mr. Bustamante from behind. He was also carrying something?"

    hide zeil 
    hide smol

    show tristan neutral 
    Tristan "If so, how come you didnt alarm Mr. Bustamante?"
    hide tristan 

    show smol at left
    show zeil question at right
    Theodora "Y’see I didnt see the weapon on Mr. Bustamante, not until he was stabbed."
    player "That is all your honor."
    hide zeil with dissolve
    hide smol with dissolve
    
    show carl neutral with dissolve
    Carl "Would the defense like to cross examine"
    hide carl 

    show tristan neutral
    Tristan "Yes, your honor."
    hide tristan 

    show carl neutral 
    Carl "Proceed."
    hide carl

    show smol at left with moveinleft
    show tristan neutral at right with moveinright 
    Tristan "Mrs. Hernandez, you said that you weren't able to hear the conversation between he victim and the accused because of a loud tricycle driving by."
    Tristan "Can you please tell the court what time the tricycle had gone by."
    Theodora "I'm afraid I cannot specify the time my dear."
    Theodora "I was too engulfed in the conversation that the time didnt really seem to be relevant. "
    Tristan "How can we be certain that a tricycle did pass by during the conversation?"
    Tristan "Mrs. Hernandez, are you certain that you did not mis hear what Mr. Bustamante had said?"
    Theodora "I- Uh i guess its possible that i had misheard some parts. My age does really hinder my everyday living these days."
    Tristan " And if i recall correctly, you said you hadnt seen the weapon the accused was holding until the crime had already been executed?"
    Theodora "well yea!"
    Tristan " As I recall Mrs. Hernandez the weapon that had been used was a 5-inch knife with a 9-inch blade, dont you think that would be easy to spot right away?"
    Theodora "Yeah..."
    Tristan "You would need to hide it before its actual use."
    Theodora " As I recall, weren't you the one who pulled the knife out of Mr. Bustamante’s back?"
    Theodora "Yes I did."
    Theodora "{i}Somehow, my nonchallant style has disperssed. Who even is this?{/i}"
    Tristan "How come you pulled the knife out knowing that it could cause more damage to the victim?"
    show smol with hpunch

    player "Objection!"

    hide smol 
    hide tristan 

    show zeil annoyed 
    player "Compound Question!"
    hide zeil 

    "{b}Factoid:{/b} The compound question objection is when there are two or more questions combined into one question. They are banned in court because they have the ability to confuse the witness and the judge."
    
    show carl neutral 
    Carl "Objection sustained."
    hide carl 

    show smol at left
    show tristan neutral at right
    Tristan "Pfft."
    Tristan "Why did you pull the knife out of the victim’s body?"
    Theodora "I pulled it cause it damaged his body. I mean you would pull something off if it harms you."
    Tristan "Do recall a jacket nearby the knife that was used?"
    Theodora "I had noticed the jacket hanging onto the knife when i opped to pull in out."
    Tristan "The jacket was left hanging onto the knife lodged into the victim's back can prolude to the fact that the jacket may have been used to hide a big weapon such as a 5-inch knife with a 9-inch blade."
    Tristan "Furthur evidence to back that up would be the bloodstains on the jacket."
    Tristan "However, that begs the question of why would you use such a noticeable weapon to take a person’s life."
    Tristan "Its not very discreet because of its size and you cant quite dispose of it quickly either."
    Tristan "If this was truly a murder, wouldnt the accused had planned more carefully? Bring a more compact or at least natural looking weapon to do the deed."
    Tristan "The way the crime was executed was careless."
    Tristan "That is all, your honor."
    hide smol with dissolve
    hide tristan with dissolve

    show carl neutral with dissolve
    Carl "...."
    Carl "Would the prosecution like to redirect?"
    hide carl with dissolve

    show zeil smile 
    player "Yes, your honor."

    show zeil normal at right with moveinright
    show smol at left with moveinleft
    player "Mrs. Hernandez, you were in close proximity with Mr. Bustamante when he was talking to the accused correct?"
    Theodora "Yes"
    player " Your honor, I believe Mrs. Hernandez’s hearing did not fail her. "
    player " If she truly had an issue with hearing she wouldnt have been able to give us a sentence that is similarly worded with what Ms. Kaparo had heard."
    player "as for the loud tricycle engine, if Mrs. hernandez had hearing problems she wouldnt had heard their conversation in the fist place with how they were whispering. "
    player "If anything she would have just heard the tricycle zooming by."
    player "That is all your honor."
    hide smol with dissolve
    hide zeil with dissolve

    show carl neutral with dissolve
    Carl "Would the Defense like to Re-Cross Examine?"
    hide carl 

    "{b}Re-Cross Examine:{/b} a chance to question the witness again. Used to combat an unreliable testimony from a witness. It attacks the accuracy and truth behind the nature of a testimony."

    show tristan neutral 
    Tristan "No, your honor."
    hide tristan

    show carl neutraltable
    Carl "Does the prosecution want to cal lanother witness to the stand."
    hide carl

    show zeil normal
    player "Yes your honor. Prosecution would like to call {b}Mr. Bunoy Miedes{/b} to the witness stand"
    hide zeil


label desheveled_court:
    show zeil normal with dissolve
    player "Please introduce yourself witness"
    hide zeil normal

    "A silence falls in the court as eveyone waits for the witness to formally introduce himself."
    "..."
    "..."
    "..."
    

    show bunoy happy at right with vpunch
    show zeil normal at left with moveinleft
    Bunoy "HM! HM! HELLO TO EVERYONE IN COURT!"
    hide bunoy happy 

    show bunoy neutral at right
    show zeil normal at left
    player "*startled*"
    player "OH GEEZES!"
    Bunoy "My name is Bunoy Miedes! Im the victim’s far away neighbor!"
    hide zeil normal
    hide bunoy neutral

    show zeil concerned with dissolve
    player "{i}Faraway neighbor?{/i}"
    hide zeil concerned

    show zeil normal at left with dissolve
    show bunoy neutral at right with dissolve 
    player "Mr. Miedes can you tell us what you were doing in the victim’s home?"
    Bunoy "Oh, I was actually there cause i was waiting to be picked up by my tricycle for WORK!"
    player "I see. Mr. Miendes can you please describe the events that had transpired with the victim?"
    Bunoy "Well, while Mrs. Hernandez and Ms Kaparo was discussing something with Mr. Bustamante. The accused had stabbed him from behind and ran toward the direction of the Municipal Hall."
    Bunoy "Basically what happened is that Ms. Hernandez quickly went to Mr. Bustamante in a rush and took out the knife with the jacket lodged into Mr. Bustamante’s back."
    Bunoy "During that time myself and  Ms. terisita went to look for help. Once we did get a few people to help us with the search, I lead them towards the direction i saw him run towards. HMM HMM! We later found out he was going to the police station. Apparently he surrendered HMM HM!"
    player "Thank Mr. Miedes. That will be all your honor."

    hide zeil normal
    hide bunoy neutral

    show carl neutraltable with dissolve
    Carl "does the prosecution want to call another witness to the stand?"
    hide carl

    show zeil normal
    player "Yes your honor. Prosecution would like to call {b}Mr. Bryan Bustamante{/b} to the witness stand"

    "A familiar but not so familiar frame emerges from the crowd."
    "A young binturong walks to the stand calmly despite having eyes that looked like they had been crying for weeks."
    "You remember that face, in fact you remember that face on a child you met once before."
    "After the oath of honesty, it was time for you to question the witness."

    player "please introduce yourself witness."

    show zeil normal at left 
    show bryan neutral at right with dissolve 

    Bryan "H-Hello everyone. My name is Bryan B-Bustamante. I’m the victim’s son that was informed of my father’s incident by Mrs. Hernandez."
    player "Mr witness what transpired as you heard the news of your father?"
    Bryan "Well when Mrs. Hernandez informed me of my father’s incident we had rushed back home only to see my father being taken by the ambulance of the nearby hospital."
    Bryan "I followed suit along with Mr. Miedes with the supplies needed and the documents my dad had kept for business."
    player "that will be all your honor."

    hide zeil normal
    hide bryan neutral 

    show carl neutraltable with dissolve
    Carl "Would the defense like to cross examine?"
    hide carl

    show tristan neutral with dissolve
    Tristan "no your honor."
    hide tristan neutral

    show carl neutraltable with dissolve
    Carl "does the prosecution want to call another witness to the stand?"
    hide carl

    show zeil normal
    player "Yes your honor. Prosecution would like to call  {b}Mr Totoy Bibo Ouano{/b} to  the witness stand"
    hide zeil normal

    "A Philippine mouse deer emerges from the crowd."
    "It was a police man, in a peculiar size at that however size hardly equates for the amount of skill an individual can offer on the table."
    "Oath of honesty was executed by the baliff and the witness and again the stand was open for questioning"
    

    show zeil normal at left 
    show toty neutral at right with dissolve 
    player "please introduce yourself witness."
    Totoy "AHeM! My name is Totoy Bibo Ouano sir/mam! I am an inspector that was present in Tandian police station where the accused surrendered"
    player "how did the accused surrender?"
    Totoy "Well quite frankly he came in all blodied. I of course thought of the worst possible reason for why he was bloodied."
    Totoy "But before I could approach to check him he just blurted out that he had stabbed someone! So I took him in custody immediately for questioning. That is all sir/mam."
    player "what other occurrences had happened afterwards?"
    Totoy "well while I was dealing with the accused, I had my collegue, Analyn inspect the crime scene."
    Totoy "She came back and recovered the evidences that you hold now in your evidence folder as far as I know sir/mam."
    player "that will be all your honor."
    hide zeil normal
    hide toty neutral


    show carl neutraltable with dissolve
    Carl "Would the defense like to cross examine?"
    hide carl

    show tristan neutral with dissolve
    Tristan "yes your honor."
    hide tristan neutral

    show carl neutraltable with dissolve
    Carl "proceed"
    hide carl

    show tristan neutral at left with moveinleft
    show toty neutral at right with dissolve
    Tristan "Didn’t you say the accused confessed that he had stabbed someone?"
    Totoy "Yes he did"
    Tristan "by chance did he also provide you where the incident had happened?"
    Totoy "yes in fact he did"
    Tristan "that will be all my questions your honor."
    hide tristan neutral
    hide toty neutral

    show carl neutraltable with dissolve
    Carl "does the prosecution want to call another witness to the stand?"
    hide carl

    show zeil normal
    player "Yes your honor. Prosecution would like to call {b}Ms. Analyn Garcia{/b} to the witness stand"
    hide zeil normal

    "A small squeak can barely be heard from the court as a Isarog striped shrew-rat came out from under a huge crowd."
    "Yet again it was another policeman (why are all the police soo small?) proudly flashing the police badge on their uniform as the walk to the stand."
    "The oath of honesty was executed and the questioning progress is a go."
    

    show zeil normal at left 
    show analyn neutral at right with dissolve

    player "please introduce yourself witness."
    Analyn "My name is Analyn Garcia and I am a Police officer of Tandian Police station."
    player "Now tell us Ms. Garcia. What did the crime scene look like?"

    Analyn "when I arrived at the crime scene there was blood on and near a chair. There was a pool of blood near the base of the chair, and near it t was a jacket."
    Analyn "At least I thought it was JUST a jacket but as i inspected closely, I had noticed that there was a knife."
    Analyn "To be exact it was a 15-inch knife with a 9-inch blade with a width of 1 inch at its widest and 1 cm."
    Analyn "This knife was lodged into the jacket making a hole in the jacket."
    player "That will be all your honor."
    hide zeil normal
    hide analyn normal

    show carl neutraltable with dissolve
    Carl "Would the defense like to cross examine?"
    hide carl
    
    show tristan neutral with dissolve
    Tristan "yes your honor."
    hide tristan neutral

    show carl neutraltable with dissolve
    Carl "proceed"
    hide carl

    show tristan neutral at left with moveinleft
    show analyn neutral at right with dissolve
    Tristan "As you said, the jacket with the knife lodged into it was left in the crime scene?"
    Analyn "correct"
    Tristan "It was found in plain sight?"
    Analyn "Affirmative"
    Tristan "That is all my questions your honor."
    hide tristan neutral
    hide analyn neutral

    show carl neutraltable with dissolve
    Carl "would the prosecution like to redirect?"
    hide carl

    show zeil normal
    player "no your honor."
    hide zeil normal

    show carl neutraltable with dissolve
    Carl "does the prosecution want to call another witness to the stand?"
    hide carl

    show zeil normal
    player "Yes your honor. Prosecution would like to call {b}Mr John Ramos{/b} to the witness stand"
    hide zeil normal

    "A Palawan- peacock arose from the croud elegantly with his feathers drawing the crowd’s attention."
    "There was no denying this peacock’s beauty carrying the attire of a physician as he walks towards the stand."
    "The witness preforms the oath of honesty and once again you were called to the front of the court."
    

    show zeil normal at left 
    show antonio neutral at right with dissolve

    player "please introduce yourself witness."
    John "Good morning everyone, my name is John Ramos and I am a physician that attended to Mr. Bustamante."
    player "Mr. Ramos can you please brief us on the condition of the Mr. Bustamante when he had arrived in the hospital."
    John "Well when Mr. Bustamante had arrived he was already in a pretty bad condition. He had about 2.5 cm stab wound on her left scapula which also managed to penetrate the left lung."
    John "You can imagine the amount of damage control we had to conduct that day."
    John "We were actually planning on moving him to another hospital for more of a specialized treatment but sadly he didn’t make it by the time of the transfer."
    player "That is all your honor"
    hide zeil normal
    hide antonio neutral

    show carl neutraltable with dissolve
    Carl "would the defense like to cross examine?"
    hide carl

    show tristan neutral with dissolve
    Tristan "yes your honor."
    hide tristan neutral

    show carl neutraltable with dissolve
    Carl "proceed"
    hide carl

    show tristan neutral at left with moveinleft
    show antonio neutral at right with dissolve
    Tristan "Mr. Ramos in a medical stand point, do you think that the victim would’ve survived if the knife had not been pulled out?"
    John "well that damage is pretty serious when we got him, but I would say that there would be LESS more damage if the knife was indeed not pulled out from the wound."
    Tristan "no further questions your honor"
    hide tristan neutral
    hide antonio neutral 

    show carl neutraltable with dissolve
    Carl "would the prosecution like to redirect?"
    hide carl

    show zeil normal
    player "no your honor."
    hide zeil normal

    show zeil normal
    player "Yes your honor. Prosecution would like to call {b}Ms. Maria Perez{/b} to the witness stand"
    hide zeil normal

    "Emerged from the dark side of the court a Fruit bat appears and flied to the stand."
    "The little creature dawned the same physician attire the peacock had gracefully walked to the stand."
    "With the same process, the oath was done and now the time for questioning has come once again."

    show zeil normal at left 
    show maria neutral at right with dissolve
    player "please introduce yourself witness"
    Maria "Heya! My name is Maria Perez and I am a physician that closely attended by Mr. Bustamante at his stay in the hospital."
    player "Ms. Maria can you please talk about the condition the patient?"
    Maria "Lets see! Oh! He arrived in a pretty bad condition. Yep! Pretty bad!"
    Maria "When we ran him under the X-ray there was a huge bleeding action in the thorax cavity."
    Maria "Oh! In simpler terms"
    Maria "it’s a hugeee space in the body that house organs and tissues that are vital to several systems like the respiratory system and etc! uhuh! in simpler terms!"
    player "Can you tell us how the victim had died?"
    Maria "From my understanding! Yes my understanding! He had died due to hypovolemic shock that is secondary to massive hemorrage. Again in simpler terms! He lost a lot of blood so he died."
    player "that is all your honor."
    hide zeil normal
    hide maria neutral


    show carl neutraltable with dissolve
    Carl "would the defense like to cross examine?"
    hide carl

    show tristan neutral with dissolve
    Tristan "yes your honor."
    hide tristan neutral

    show tristan neutral at left with moveinleft
    show maria neutral at right with dissolve

    Tristan "Ms. Maria you said that Mr. Bustamante had died due to the bleeding"
    Maria "yes that’s true"
    Tristan "so he had not died due to the damage on his lungs?"
    Maria "uh- yes technically he did not die because of the damage dealt to his left lung"
    Tristan "I have no other questions your honor,"
    hide tristan neutral
    hide maria neutral

    show carl neutraltable with dissolve
    Carl "would the prosecution like to redirect?"
    hide carl

    show zeil normal
    player "no your honor."
    hide zeil normal

    show carl neutraltable with dissolve
    Carl "does the prosecution want to call another witness to the stand?"
    hide carl

    show zeil normal
    player "no your honor, that will be all."
    hide zeil normal

    show carl neutraltable with dissolve
    Carl "Thank you, The defense may now call their first witness to the stand."
    hide carl

    show tristan neutral at left
    show carl neutraltable at right 
    Tristan "Thank you your honor. May I proceed?"
    Carl "you may."
    hide tristan neutral
    hide carl neutral 

    show tristan neutral 
    Tristan "The defense would like to call Mrs. Angel Ramirez to the witness stand."
    hide tristan

    "A sweet old pig walks up to the stand carrying her bright blue purse with her"
    "She gave the aura of a queen despite quite obviously not being one."
    "The bailiff assisted and instructed her on the oath of honesty and the defense was now ready."

    show tristan neutral
    Tristan "May I proceed your honor?"
    hide tristan

    show carl neutraltable
    Carl "You may proceed"
    hide carl

    "Witness walks in front of the court to begin the direct examination."
    
    show tristan neutral at left with moveinleft
    show angel neutral at right with dissolve
    Tristan "The defense would like to call Mrs. Angel Ramirez to the witness stand."
    Angel "Why hello everyone, My name is Mrs. Angel Ramirez and I was a civilian that was in the area when the incident happened."
    Tristan "witness can you tell me what you had witnessed on October 21."
    Angel "*snort” I walking by the Bustamante residences and I remember hearing a scream of a woman *snort*."
    Angel "Shortly after the scream a gust of wind zoomed by me, I didn’t really see who it was but I do recall feathers *snort* *snort*."
    Tristan "What did you do witness?"
    Angel "why I just told them I saw someone zoom past me in the direction of the Police station."
    Tristan "Thank you, That will be all your honor."
    hide tristan
    hide angel

    show carl neutraltable with dissolve
    Carl "would the prosecution like to cross examine?"
    hide carl

    show zeil normal
    player "no your honor."
    hide zeil normal

    show carl neutraltable
    Carl "Mrs. Ramirez you may return to your seat."
    Carl "Does the Defense want to call anymore witnesses to the stand?"
    hide carl 

    show tristan neutral at left with dissolve
    show carl neutraltable at right
    Tristan "Defense: yes your honor. May we proceed?"
    Carl "You may proceed"
    hide carl
    hide tristan

    Tristan "The defense would like to call Mr. Cesar Diaz to the witness stand."
    hide tristan

    "A loud thumping can be heard approaching from behind the court."
    "It seems that the witness is quite rough or at least everyone else thinks so?"
    "A Philippine crocodile emerges and walks confidently to the stand, completely oblivious to the noise they were creating in the court."
    "Once again the oath of honesty was recited and it was tme for the defense to start questioning."

    show tristan neutral at left
    show carl neutraltable at right 
    Tristan "May I proceed your honor?"
    Carl "You may proceed"
    hide tristan
    hide carl

    show tristan neutral
    Tristan "Witness please introduce yourself"
    hide tristan 

    show tristan neutral at left with moveinleft
    show ceasar happy at right with moveinright
    Cesar "HELLOOOOOO EVERYONEEEEE!"
    Cesar "MY NAME IS CESAR DIAZ! AND I AM THE INSPECTOR IN CHARGE OF THIS CASE!"
    hide ceasar 

    show carl neutraltable hammer at right with vpunch
    Carl "bashes the hammer* CEASAR- I mean, Mr. Diaz can you PLEASE lower your voice."
    hide tristan

    show ceasar neutral at left
    Cesar "sorry carl"
    Carl "*sigh*"
    Carl "defense, you may proceed."
    hide carl neutraltable hammer 

    show ceasar neutral at right with moveinleft 
    show tristan neutral at left
    Tristan "uhh okay.. aheM Mr. Diaz can you please brief us on the crime scene"
    Cesar "In the crime scene a knife was stabbed into a jacket on the ground."
    Cesar "Both the knife and jacket were covered in blood of the victim."
    Cesar "The blood suggest on the ground suggest that the accused had ran in the direction of the police station."
    Cesar "There was no sign of attempted cover ups in the crime scene."
    Tristan "Mr. Diaz can you give the court a description of what you think had happened based on the evidence."
    Cesar "well judging by the position of the weapon and the the blood marks, topped with the attopsy report."
    Cesar "I’d say it was a crime from behind that came as a surprised, based of the lack of struggling the victim had."
    hide ceasar neutral 
    show ceasar happy at right with dissolve
    Cesar "It’s pretty straightforward, it was a stab and run, but stead of actually running away the perpetrator went straight to the police! HAHA!"
    hide ceasar
    Tristan ".... that was not funny"
    Tristan "ahem!, uhm thank you Mr. Diaz, that will be all your honor"
    hide tristan

    show carl neutraltable
    Carl "You may go back your seat Mr. Diaz. Would the defense like to call another witness per chance?"
    hide carl

    show tristan neutral at left
    Tristan "yes your honor May we proceed?"
    show carl neutraltable at right with moveinright
    Carl "You may"
    hide carl
    show tristan neutral
    Tristan "the defense would like to call on Mr. Felipe Dimapilis to the stand."
    hide tristan

    "The policemen escort a tall falcon to the stand. Despite being the accused the falcon seemed composed."
    "The falcon quietly walked towards the stand both policemen behind him. Unlike most of the witnesses called to the stand, he was the most normal out of all of them."
    "As he took up the oath of honesty with the bailiff he takes a glance towards you then immediately shifts his attention to the defense as they start their first question."

    show tristan neutral 
    Tristan "may I proceed your honor?"
    hide tristan 
    
    show carl neutraltable
    Carl "Proceed"
    hide carl 

    show tristan neutral at left with moveinleft
    show felipe neutral at right with moveinright
    
    Tristan "Mister witness Where were you on October 21?"
    Felipe "I was visiting Mr. Bustamante on account of a business plan i had in mind. But rather than a business based discussion it had transpiredd into a teasing battle and later a debate battle."
    Felipe "Ben was always passionate about what he stood for so he got aggravated with me at some point."
    Felipe "But..."
    Felipe "He said something that rubbed me the wrong way. So i left because of the amount of hurt i felt- betrayal even. I was humuliated by my own friend."
    Felipe "I acted on impulse and took anything i could grab from the marketplace nearby and before i knew it Ben had a knife on his back.. And i was holding it."
    Felipe "I ran away, but I decided to surrender once i saw the chief of the police."
    Tristan "Can you detail to me what you thought was occuring in Mr. Bustamante’s home?"
    Felipe "I really couldn’t tell."
    Felipe "I'd assume it was a business meeting considering that two of her business partner’s was there."
    Felipe "However there was another person there who I wasnt really familiar with so.. Im not quite sure."
    Tristan "That will be all your honor"
    hide felipe
    hide tristan

    show carl neutral with dissolve
    Carl "Would the prosecutor like to cross-examine?"
    hide carl

    show zeil normal 
    player "No, your honor."
    hide zeil

    show carl neutral
    Carl "Alright, Witnesses. You may all go back to your seat."
    Carl "Does the defense have anymore witnesses theyd like to bring to the stand?"
    hide carl

    show tristan neutral 
    Tristan "No, your honor."
    hide tristan

    show carl neutraltable 
    Carl "We call the witness testimonies and arguments heard in court. It shall be submitted and reviewed for resolution."
    hide carl  

    "Factoid: Typically, the judge asks the defense the preferred date  and time for the court final judgement. The schedule is has to be approved by both the defense and the prosecution through a signature. "
    "Final judgement usually happens a few days after the trial depending on the case. In this way, the court can review and have organized schedules per case they encounter every day."
    
    show carl neutraltable
    Carl "Hearing adjourned, so order. "
    Carl "*Slams hammer*"
    play sound "audio/sfx/sfx_gavel1tap.wav"
    hide carl with Fade(3.0,1.5,3.0)

    scene bg osfirm
    show zeil normal with dissolve
    player "Whew that was stressful... "
    player "{i}The whole sesison seems kinda off...{/i}"
    player "{i}Why was Ben’s killer so polite? More than just polite- more like actually guilty for what he did.{/i}"
    show zeil at left with easeinleft
    show cassie happy at right with easeinleft
    Cassie "Good job. Rookie, especially on such a heavy case. Our firm shouldn’t even supposed to be handling this case in hindsight."
    player "Well I think I owe it to Ben. To defend him all I can."
    player "His training would be put to waste if I didn’t"
    Cassie "Me too.. He was one of the best and one of the good ones too."
    Cassie "Why would anyone want to harm him."
    player "It is kinda weird that a few words from ben triggered something terrible. "
    player "Ben is usually careful for his words"
    Cassie "That's true."

    show zeil sad
    player "I still can't believe Ben is..."

    show cassie sad
    Cassie "Me too... He was one of the best and one of the good ones too.  Why would anyone want to harm him."
    player "It is kinda weird that a few words from ben triggered something terrible. Ben is usually careful for his words."
    Cassie "That’s true. Ben was a natural at calming and explaining properly, without bias or too much uneeded emotion."
    Cassie "I mean have you seen that guy talk about his family? Its probably the most wholesome and calming thing ive ever seen on this earth."
    player "Yeah... I miss him"
    Cassie "Me too..."
    Cassie "well don’t relax about this case though Rook."
    player "what do you mean..?"
    Cassie "{i}*Sigh*{/i}we still have a final judgement session in a couple of days"
    Cassie "So we aren’t out of the waters yet. Lets see if you really did do a good job Rookie."
    "To be continued..."











    



    
   












    


    










    


    






    













































