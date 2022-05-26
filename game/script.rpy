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
define Barr = Character('Mrs. Barretto (Gina)', color='#7d8782ff')
define Chi = Character('Mr. Barretto (Chi)', color='#7d8782ff')
define Bmom = Character('Momma Beaver', color='#4e4409ff')

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

    scene bg officefirm with Fade(0.5, 0.0, 0.5)
    show zeil normal
    player "Hey, is that Benjamin sleeping in the firm?"
    show zeil normal at left
    with moveinleft
    pause (3.0) #Pauses screen and shows better transition till the next line.
    show benjamin neutral at right
    with dissolve
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
    Ben "Due to their relationship failing because Mr Rivero doesn't want to get intimate with Mrs. Rosa"
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
    show zeil normal at left with moveinleft
    show ferret lady at right with moveinright
    Lady "For the trial, all rise. RTC Branch 139 is now in session. Honorable Carl please proceed"
    show carl neutral with moveinbottom
    Carl "Thank you, you may all be seated."
    "{i}Witnesses sits down{/i}"
    Lady "The court is now in session, we call on case number 119190 (Mr. Robert Barreto Versus the Court of Appeals and Mrs. Rosa Barreto)"
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
    Carl "We will now hear the opening of the Defense"
    hide carl

    show zeil delighted with dissolve
    player "Your honor, I am [povname] and I represent here Mr. Robert Barretto age 24, husband of Ms Rosa Barretto. "
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

    show iro neutral
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
    show iro neutral
    Iro "Yes your honor, I am Iro Lockheart and I represent here Mrs. Rosa Barretto age 23, wife of Mr. Robert Barretto."
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
                show iro neutral with dissolve

            "Let it be":
                $ Objection_FirstCase = False
                show zeil smile
                "{i}I'll see where this goes.{/i}"
                hide zeil
                show iro neutral with dissolve

    if Objection_FirstCase:
        Iro "Oh uhm... {i}I was not expecting that{/i}"
        Iro "{i}I have a reallllyy high possibility of being toasted tonight! Might as well go on and see where this goes ... hays ...{/i}"
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

                show iro neutral with dissolve
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
    Iro "When you decide your verdict, please find the petition to be accepted."
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
    show carl hammer with vpunch #MAKE SOUND EFFECT
    "*Hammer Noise*"
    hide carl with Fade(1.5, 0.0, 0.5)

label AfterChap1:
    show zeil smile2 at left with dissolve
    show benjamin neutral at right with dissolve

    player "{i}I did it, Benjamin! I won my first case!{/i}}"
    Ben "Nice one, kiddo! I knew you could do it!"
    Ben "My pride has further established dominance!" 
    Ben "Tonight we shall celebr-"

    show zeil normal
    "{i}Benjamin's Phone Vibrates{/i}"

    Ben "Heh... looks like I gotta do something important, kiddo."
    player "What is it, Ben-"
    Ben "Gotta blast!"
    hide benjamin with moveoutleft

    show zeil annoyed
    player "That's weird, I swore that he had time for me..."
    
    pause (3.0)
    show zeil sad
    player "..."

    pause (3.0)
    show zeil smile
    player "Oh well, I'll just surprise him in the firm-"
    
    show zeil shocked with hpunch
    Chi "I swear I love you, Gina!"
    hide zeil

    show chi neutral at left with dissolve
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

    hide zeil with moveoutleft 
    

label Chap1_Ending:
    scene bg isfirm with Fade(1.5, 0.0, 0.5)
    "{i}Inside the firm in a silent evening...{/i}"
    show benjamin neutral at left with dissolve
    Ben "Hmm..."
    Ben "So that's what's happening in cout de Forest..."

    if RouteChecker == 0:
        Ben "Case asside, ashamed to see my student bail his first case."
        Ben "Opportunities are rare."
        Ben "What a bad time to be in."

    "{i}Knock Knock{/i}"

    Ben "Come in!"

    show cassie neutral at right with easeinright
    Cassie "Sir, here is your requested coffee"
    Ben "Thank you, Cassie."
    Ben "{i}I'll have to fix this case fast...{/i}"
    Cassie "..."
    Cassie "Sir, if you don’t mind me asking, what are you working at right now?"
    Cassie "It looks like you’re not getting a decent rest and it feels like you are in a tight position."
    pause (3.0)
    Cassie "By any chance, is there something that I could do to make you feel at ease?"
    Ben "You worry too much, child."
    Ben "Thank you for asking, but this is realllly nothing."
    Ben "How about you head out for tonight, don’t worry about me I’ll take a decent rest after I’m done with this."
    Cassie "Alright sir, good work for today!"
    hide cassie with easeoutright
    Ben "Okay... back to my leads."
    "Benjamin continued working all night with a case no one knows about."

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
            $ renpy.full_restart()

label Chapter2_Start:
    scene bg osfirm with Fade(1.0, 1.5, 0.5)
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

    show cassie neutral at right with dissolve
    Cassie "..."
    Cassie "G..good morning, [povname]"

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

    show zeil smile
    Cassie "Oh, right! I stopped by that cafe that just newly opened."
    player "Oh yeah, the one right by the elementary school? How was it?"
    show zeil smile2
    Cassie "Yeah, that one!"
    Cassie "Their pandesal is a taste of heaven on earth"
    show zeil laugh
    player "Really? Well, one of these days, I'll try them!"
    Cassie "They sell them in packages, and actually… "
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
    Cassie "HEY! I-- I would've given Ben as well if he were here!"
    Cassie ">:( So don't feel special, alright?!"

    show zeil laugh
    player "Whatever, thank you Cassie!!"
    player "I should treat you sometime too <3"

    Cassie "Th..that would be nice :)"

    "..."
    "...."
    show zeil normal
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

    player "{i}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/i}"
    player "Hays.. oh well."
    hide zeil with dissolve

    scene bg reccomp with dissolve
    show zeil normal with dissolve
    player "{i}That was extremely awkward!{/i}"
    player "{i}But despite us always bickering, it’s nice to know she does care about Ben and I.{/i}"
    player "Speaking of Ben, I should message him and see if he's alright."

    show zeil shocked at left with easeinleft
    "{i}KNOCK KNOCK{/i}"
    "Hello? Is someone in?"
    player "Oh yes, would you like to talk?"
    "Yes please..."

    show zeil normal
    player "Come in, come in."

    show mommabeaver neutral at right with easeinright
    player "Please, take a seat and make yourself comfortable. How may I help you today?"
    Bmom "Please, my kids have gotten into a national situation and need help."
    player "I'm all ears. Please tell me what happened."

    show zeil bored
    player "{i}Her situation seems serious.{/i}"

    show zeil sad
    Bmom "They let a petition sign all over the City, and thousands of people agreed to stop the continued cutting of virgin forests all around the country. My children are going into a fight with a big company, and they’re not going down without a fight."
    player "{i}I've heard about this issue. These kids are brave.{/i}"
    Bmom "Will you please help them?"

label Chapter2_Choice:
    show zeil normal
    player "{i}Think, [povname] , this situation is big. It's so big that this might take me quite a while to finish.{/i}"
    player "{i}Should I take it? I barely have any experience...{/i}"

    show zeil sad
    player "I might mess this up..."

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

    show zeil smile2
    player "Your kids are very brave, you must very proud."

    Bmom "T-thank you!! Though are you sure you'll help me 'till the end?"
    Bmom "This case is just... life-draining, and I can't find anyone who can help me!"

menu:
    "Yeah, I'm sure. Let's do it!":
        player "Yeah, I'm sure of it, ma'am!"
        Bmom "WAIT YOU ARE?!"

        show zeil shocked
        player "Y-yeah?"

        show zeil normal
        Bmom "N-No one has ever agreed to help me..."
        Bmom "I'm getting all emotional now T-T"
        Bmom "Every Lawfirm agreed to back me down."
        Bmom "But your lawfirm is special..."

        show mommabeaver neutral at left with easeinright
        Bmom "I have nothing to say but thank you! {i}cries and hugs [povname] {/i}"
        $ RouteChecker += 1

        jump Case2

    "Wait, let me think again.":
        show zeil normal
        player "Wait, let me think again."
        Bmom "Alright.., take your time"
        jump Chapter2_Choice



label Chapter2_Dec:
    player "I'm not willing to help you, ma'am..."
    player "The burden is too big for a rookie like me..."
    Bmom "Aww, I'm sure you can do it ! :("
    Bmom "I need anyone right now :("

menu:
    "Sorry, I cant.":
        show zeil shocked
        Bmom "O..Okay :) I.... I understand {i}sobs{/i}"

        show zeil sad
        Bmom "I'll be leaving now, Good bye !"
        hide mommabeaver neutral with moveoutright

        player "That was hard..."
        $ renpy.full_restart()
    "Wait, let me think again.":
        show zeil normal
        player "Wait, let me think again."
        Bmom "Alright.., take your time"
        jump Chapter2_Choice

label Case2:
    player "Case shall start!"
    


    



