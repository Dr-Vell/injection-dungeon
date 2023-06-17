# The script of the game goes in this file.

# CHARACTERS
define m = Character("Me")
define n = Character("Nico")
define l = Character("Laila")
define e = Character("???")
define b1 = Character("Injection Basics", kind=nvl)
define b2 = Character("Description", kind=nvl)
define b2_5 = Character("Types", kind=nvl)
define b3 = Character("Examples", kind=nvl)
define b4 = Character("Protection ", kind=nvl)
define b5 = Character(" ", kind=nvl)
define d = Character(" ", kind=nvl)

# MUSIC
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"
define audio.market_noise = "audio/market-noise.mp3"
define audio.dungeon_air = "audio/dungeon-air.mp3"
define audio.grrr = "audio/grrr.mp3"
define audio.door = "audio/door.mp3"
define audio.combat = "audio/combat.mp3"
define audio.correct = "audio/correct.mp3"
define audio.incorrect = "audio/incorrect.mp3"
define audio.orc_ending = "audio/orc-ending.mp3"
define audio.poison_leak = "audio/poison-leak.mp3"
define audio.horde = "audio/horde.mp3"
define audio.good_ending = "audio/good-ending.mp3"

# FLAGS
define ready = True
define fork = "None"
define puzzle = True
define def_1 = True
define def_2 = True
define def_3 = True
define trials_done = 0
define test_mode = True
define GUI_demo_mode = True

label start:

#################################################################     TESTING AREA     ###################################################################
    
    if GUI_demo_mode == True:
        call demo

    
    if test_mode == True:
        scene bg black
        with fade   

        "Click to run all automatic tests."

        python:
            test_file = open("C:/Users/david/Desktop/Asignaturas/TFG/Juegos/Injection Dungeon/testing.txt", 'w')

            test_file.write("Testing Mode Results\n\n\n")
            test_file.write("> Testing Initial Flag Values:\n\n")
            test_file.write("Testing Mode Results:\n")
            test_file.write(" - ready: " + str(ready == True)+ "\n")
            test_file.write(" - fork: " + str(fork == "None")+ "\n")
            test_file.write(" - puzzle: " + str(puzzle == True)+ "\n")
            test_file.write(" - def_1: " + str(def_1 == True)+ "\n")
            test_file.write(" - def_2: " + str(def_2 == True)+ "\n")
            test_file.write(" - def_3: " + str(def_3 == True)+ "\n")
            test_file.write(" - trials_done: " + str(trials_done == 0)+ "\n")

        "Testing completed. Click again to start manual tests."
        "Test 1: Ready Choice."
        call test_1
        
        scene bg black
        with fade   
        "Test 2: Read book."
        call read_book

        scene bg black
        with fade   
        "Test 3: Stairs or Dark Corridor."
        call test_2

        scene bg black
        with fade   
        "Test 4: First Challenge"
        call first_question_0
        
        scene bg black
        with fade   
        "Test 5: Fork Choice"
        call test_3

        scene bg black
        with fade   
        "Test 6: Second Challenge"
        call first_question_1

        scene bg black
        with fade   
        "Test 7: Third Challenge"
        call first_question_2

        scene bg black
        with fade     
        "Testing completed. Click again to start audio tests."

        "First let's test the music."
        play music gamemusic
        "Playing: 'gamemusic'"
        play music market_noise
        "Playing: 'market_noise'"
        play music dungeon_air
        "Playing: 'dungeon_air'"
        play music combat
        "Playing: 'combat'"
        play music good_ending
        "Playing: 'good_ending'"


        stop music
        "Now let's test the sound effects."
        play sound grrr        
        "Playing: 'grr'"
        play sound door
        "Playing: 'door'"
        play sound correct
        "Playing: 'correct'"
        play sound incorrect
        "Playing: 'incorrect'"
        play sound orc_ending
        "Playing: 'orc_ending'"
        play sound poison_leak
        "Playing: 'poison_leak'"
        play sound horde
        "Playing: 'horde'"

        "Testing completed. Click again to start characters test."

        m "This is you, 'Me' should be displayed"
        n "'Nico' should be displayed"
        l "'Laila' should be displayed"
        e "'???' should be displayed"
        b1 "'Injection Basics' should be displayed"
        b2 "'Description' should be displayed"
        b2_5 "'Types' should be displayed"
        b3 "'Examples' should be displayed"
        b4 "'Protection' should be displayed"
        b5 "Nothing should be displayed as Name"
        d "Nothing should be displayed as Name"     
        
        
        "Testing completed. Click again to exit."

        return

##################################################################     GAME INTRO      ###################################################################

##################### Intro

label start_game:

    play music gamemusic

    scene bg kingdom
    with fade

    pause 1.0

    "You find yourself in the heart of Gara, the Desert Kingdom."

    "This place is commonly known for being a mysterious place that holds countless stories and legends about mystical items, forgotten by the rest of the world."

    scene bg tents
    with fade

    "You've been traveling with your friend Nico for months now."

    "Both of you decided to come here, the great Desert Kingdom's capital, to seek these stories and, if possible, go on a thrilling adventure searching for the 
    legendary items."

    scene bg tent
    with dissolve

    "This is your first day in Gara, so Nico thought it'd be a good idea to go around the place asking for some information about these legends."

    "So he went on his own to the city's market, leaving you behind to guard the tent you both just installed in the city's surroundings."

    m "..."
    m "Damnit!"
    m "He's already gone..."
    m "..."
    m "Well...guess I'll have a nap while I wait for him."
 
    scene bg black
    with fade   

    "You lay inside the tent, hoping to catch up on sleep."
    "..."
    "Not even five minutes pass until you start hearing some noises outside the tent."
    "You quickly get up to see what's going on."


##################### First Dialogue


    scene bg tent
    show nico happy
    with fade

    n "Wakey-wakey!"

    show nico smile

    m "That was fast..."
    m "Any news?"

    show nico happy

    n "Indeed!"

    m "So? What're you waiting for? Spit it!"

    show nico smile

    n "Ive been talking to this ol' man in the market."
    n "After some small talk, he told me about this ancient dungeon no one dares to step into."

    m "Okay..."

    n "There's supposed to be some legendary relic sitting deep inside the dungeon, waiting for us to discover it!"

    m "Now we're talking business."

    n "Yeah so, get your things ready and let's go!"

    m "Sure, let's do it."

    show nico shy

    n "OH! I forgot to mention."
    n "There's this girl, the ol' man's niece."
    n "She heard us talking about the dungeon, so she jumped in saying she'd guide us to the entrance."

    m "Awesome!"
    
    show nico smile
    
    n "She should be waiting for us by the market."
    n "Ready to go?"

label test_1:

    menu:

        "Ready to go?"

        "Yeah, let's waste no more time":
            show nico happy
            n "Let's go."
            if test_mode == True:
                return
            jump market_section

        "Wait a second, I can't find my sword...":
            $ ready = False
            show nico angry
            n "Oh come on! Forget it and let's go!"
            m "Okay fine."
            if test_mode == True:
                return
            jump market_section



##################### Market

label market_section:

    play music market_noise fadeout 1.0 fadein 1.0

    scene bg market
    with fade

    "??" "Over here!"

    n "Oh?"
    n "Laila?"
    n "There she is!"

    show nico happy at left

    n "Hi again!"
    n "This is my partn-"

    show laila angry at right

    l "Stop! No need for introductions since..."
    l "...well...you probably won't scape the cursed dungeon anyways."

    show laila neutral at right

    show nico equisde at left

    n "Hahahahah...right."

    m "A pleasure meeting you too."

    show laila smile at right

    l "Let's get going, I need to come back before night."

    m "Sure, we'll follow you."

    show nico smile at left

    l "Good..."

    jump way_to_dungeon


##################### On the way to the Dungeon

label way_to_dungeon:

    play music gamemusic fadeout 1.0 fadein 1.0

    scene bg way-to-dung
    with fade

    "The three of you leave the city."
    "Laila's words made you feel a little uneasy, but obtaining the relic could save you from much trouble in the future."
    "This is a once-in-a lifetime chance, there's no way you're not going in there!"
    "And Nico seems pretty excited about it too."
    "If you stay together, nothing bad could happen..."
    "Or could it?"

    scene bg dung-entrance
    with fade

    l "Finally! We arrived fellas!"
    n "Are these ruins?"

    show laila smile at right
    with dissolve

    l "There's an entrance to the dungeon inside those ruins."
    l "You'll find it as soon as you go in."
    l "You can't miss it."

    show nico smile at left
    with dissolve

    n "Thanks for bringing us here!"

    show laila neutral at right

    l "...Thanks? I think you misunderstood me before in the market."
    
    show laila angry at right
        
    l "Wheres the gold coins?"

    show laila angeri at right
    show nico equisde at left

    n "Huh?"
    
    "Nico glances at you..."
    "He probably forgot about the deal..."

    m "Nico...not again..."
    n "Please tell me you've got something in your pockets."

    if ready:
        m "You are lucky I got ready pretty fast before coming."
        show nico relieved at left
        m "Here, take these coins, and please, forgive my friend; he can be a bit clumsy sometimes."
    else:
        m "It's your fault I got nothing! You couldn't wait for me to get ready back at the tent!"
        n "Damn...now what? All I can offer her are my clothes..."
        show laila neutral at right
        l "Hmmm, those shoes do look kinda expensive..."
        show laila laugh at right
        l "We got a deal!"
        show nico scared at left
        n "What!"
        m "Yep, that's what you get."
        show nico sad at left
        n "Aaaaaaaaah...okay, fine, you can take 'em."

    show laila smile at right
    show nico smile at left
    l "Yush! It's a pleasure doing business with you guys."
    l "Take care down there!"

    hide laila smile
    with dissolve
    show nico happy

    n "Let's go! Adventure awaits my dear friend!"

    m "Right..."

    jump entering_dungeon

##################################################################     DUNGEON 0      ###################################################################

##################### Entering the Dungeon
label entering_dungeon:

    scene bg black
    with fade

    "Both of you enter the ruins, just to find some stairs..."
    "These stairs go deep down, you can't even see the end."
    
    show nico happy
    with dissolve

    n "Let's race to the end of the stairs! The winner can have the relic for himself!"

    "Nico doesn't think twice before jumping straight into the stairs."

    hide nico happy
    with dissolve

    m "WHAT! No way! Wait for me!"

    "You hope he doesn't fall as you start going down the stairs too..."

    stop music fadeout 1.5

    pause 1.0

    "It's time for the real challenge, the moment you've been waiting all this time is close at hand."

    pause 0.5

    "You feel determined."

    pause 2.0


##################### Finding the Book

    play music dungeon_air fadein 1.5

    scene bg stairs-end
    with fade
    show nico happy
    with dissolve

    n "Hahahahaha!"
    n "You took your time huh?"
    
    show nico smile

    m "Yeah yeah...really funny"
    m "You got lucky I didn't go full force there."

    show nico scared

    n "Ahaa...wait...what's that over there?"

    scene bg book-shrine
    with dissolve

    n "Woah this is so cooool!"

    m "Is that a book?"

    show nico smile at right
    with dissolve

    n "Oh? You're right!"

    "You grab the ancient book."

    show book dusty at truecenter:
        zoom 0.5
    
    "It's really dusty."
    "It must've been here for ages now."

    m "\"Injection Basics\""

    n "...what?"

    m "Maybe this can help us go through the dungeon."

    hide nico smile
    with dissolve
    
    "This book might teach you the basic knowledge of Injection, the infamous web vulnerability."
    "If you know little about it, it's probably a good idea to read it."
    "You can also read it later tho..."
    "Do you want to read the book before doing any deeper?"

    jump read_book

label guide_book:

            nvl clear

            b1 "This is a guide for dealing with Injection."
            b2 "Injection is a type of web vulnerability that occurs when an attacker is able to inject malicious code 
            or commands into an application or database,"
            b5 "causing it to execute unintended actions or reveal sensitive information."

            nvl clear

            b2_5 "The most common type of injection is SQL injection, which occurs when an attacker injects malicious SQL code into 
            an application's database query."
            b5 "This can allow the attacker to bypass authentication, access sensitive information, 
            modify or delete data, and even take control of the entire application or server."
            b5 "Other types of injection vulnerabilities include OS command injection, XML injection, and LDAP injection, cross-site scripting (XSS) injection and  XPath injection." 

            nvl clear

            b5 "These vulnerabilities can be exploited in a similar way to SQL injection, by injecting malicious code into the application's 
            input fields or parameters." 

            b3 "It is a commonly observed practice for attackers to target potential security vulnerabilities in web applications, specifically in areas such as login or registration input fields."
            b5 "The attacker can insert malicious code through these inputs, like this SQL script:"
            b5 "{b}'; DROP TABLE importantDocs; --'{/b}" 
            b5 "SQL injection attacks specifically target systems that use SQL databases, but it is important to note that there are other types of injection attacks that can affect different types of 
            systems."

            nvl clear


            b5 "Therefore, while SQL databases are a common target for this type of attack, it is important to be aware of and protect against other types of injection attacks as well."

            b4 "Injection attacks can be prevented by using prepared statements, input validation, and parameterized queries to ensure 
            that user input is properly sanitized and not treated as executable code. "
            
            b5 "It is important for developers to be aware of 
            injection vulnerabilities and take steps to prevent them in their applications."
            
            b5 "Additionally, web application firewalls and IDS/IPS systems
            can also be used to detect and block injection attacks."

            nvl clear

            return

label read_book:
    menu:
        "Read it?"
        "Sure, any help is welcomed!":
            call guide_book from _call_guide_book

            m "Okay, I'm done with this."

            hide book dusty
            with dissolve

            n "Zzz"

            m "You really fell asleep in here..."
            m "NICO!"

            show nico scared

            n "Dude! Don't scare me like that again!"

            m "Let's go, I'm done reading."

            n "Finally, took you long enough..."

            if test_mode == True:
                return

            jump fork_0

        "Nah, I'm fine thanks.":
            m "I'm not in the mood of reading right now..."

            hide book dusty
            with dissolve

            show nico happy
            with dissolve

            n "Me neither so...let's get going!"

            if test_mode == True:
                return

            jump fork_0



label fork_0:
    
    scene bg fork_0
    with fade

    n "Uh oh..."

    show nico neutral
    with dissolve

    n "This corridor splits in two paths..."
    n "Which way now?"

label test_2:
    menu:
        "Which way will you take?"

        "The shining stairs":
            m "These shining stairs inspire confidence, let's go that way."
            show nico smile
            n "Right on!"
            if test_mode == True:
                return
            jump final_door_0

        "The dark corridor":
            m "Let's take the dark path...shining stuff must be some trap...right?"
            show nico equisde 
            n "...okay? I'll trust you on this."
            if test_mode == True:
                return
            jump phase_1


label final_door_0:

    scene bg final_door
    with fade
    show nico neutral at right
    with dissolve

    n "Woah..."
    n "Look at this big ass door."

    m "Theres something written on the side..."
    m "\"Shouldst thou seek the object of virtue, thou must needs overcome the three trials that rest in the shadows of this sanctuary.\" "
    m "\"And once thou hast triumphed over the three trials, thou must gather the three fragments of the key, won from each of them, to unlock the chamber wherein the object of virtue lies.\""

    m "Hmm...this riddle is pretty straightforward."

    show nico equisde at right
    n "Uhmm...of course! It's really easy to solve hahaha...right."
    n "Just to confirm that we are on the same page..."
    n "What do you think it means?"

    m "Well, it probably means there's like three challenges that we need to beat in order to obtain the key to this door and get the relic. Right?"

    n "Of course! I was thinking the very same thing! hehe..."

    m "Okay so, \"the shadows of this sanctuary\"..."
    m "We can try going through the dark corridor from before."
    show nico smile at right
    n "Yeah, sounds about right, let's go!"
    jump phase_1


##################################################################     DUNGEON 1      ###################################################################


label phase_1:

    scene bg black
    "..."
    "You both enter the dark corridor."
    "You walk carefully through the dark with Nico, trying not to bump into anything."


    scene bg phase_1
    
    n "Finally some light!"
    m "Look at this writings."
    m "Theres some buttons below...I wonder what they do."

    play sound grrr
    pause 2.0

    show nico scared at left
    with dissolve

    n "Wait...did you hear that?"
    m "Yeah...we're not alone."

    play sound door
    pause 3.0

    show nico terrified at left

    n "Damnit! The door is closing!"
    m "We can't scape now!"

    m "There must be some way to open the gates..."
    m "Lemme read the writings, these buttons must be the key."

    show nico angeri at left

    n "Okay I'll cover you, there's a scary looking creature rushing to us!"

    show orc angeri at right:
        zoom 0.7

    play sound grrr
    "???" "AAAAAAAAAAAAAAHHHhhhhhh!"

    show nico terrified at left

    n "AAAAAAAAAAAAAAAAAAAAA!"
    m "Give me a minute, I think I can solve it!"
    n "Take your time mate! It's not like we're gonna get killed or anything!"

    hide nico terrified
    hide orc angeri
    with dissolve

    play music combat

    pause 0.5
    "This is definetly a good time to \"save game\"..."
    pause 0.5

    "The writing says the following..."
    "First Trial."
    "Answer correctly if you want to scape alive."
    jump first_question_0

label first_question_0:

    "\"What does {b}Injection{/b} mean, in the context of web vulnerabilities?\""
    "{b}Red button{/b}: Type of vulnerability that allows an attacker to redirect website traffic to a different web address."
    "{b}Green button{/b}: Exploitation of a security vulnerability in a web application that allows an attacker to inject and execute malicious code or commands."
    "{b}Blue button{/b}: Technique used to speed up the loading time of web pages by injecting additional JavaScript code."
    "{b}Yellow button{/b}: Security mechanism used by web applications to prevent unauthorized access to sensitive data."
    menu:
        "Which one will you press?"
        "Red button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Green button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound correct
            m "Nice! Sounds like I was right."
        "Blue button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Yellow button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_1

            m "Okay, now I should be able to answer."
            jump first_question_0

    
    play music combat

    "The writings magically change."
    "There's a new question."
    jump second_question_0

label second_question_0:
    "\"What are the various {b}types of injection{/b} attacks that can occur in the context of web vulnerabilities?\""
    "{b}Red button{/b}: SQL injection, Link injection, metadata injection, LDAP injection, XPath injection, and XML injection."
    "{b}Green button{/b}: Web cookies injection, cross-site scripting (XSS) injection, metadata injection, multimedia injection, XPath injection, and XML injection."
    "{b}Blue button{/b}: Web cookies injection, Link injection, command injection, multimedia injection, XPath injection, and XML injection."
    "{b}Yellow button{/b}: SQL injection, cross-site scripting (XSS) injection, command injection, LDAP injection, XPath injection, and XML injection."
    menu:
        "Which one will you press?"
        "Red button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Green button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Blue button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Yellow button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound correct
            m "Nice! Sounds like I was right."
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_2

            m "Okay, now I should be able to answer."
            jump second_question_0

    
    play music combat

    pause 0.5
    play sound grrr
    n "Hurry up dude! I wont be able to hold much longer!"
    m "I'm almost done! Hang in there Nico!"

    pause 0.5

    "The writings magically change."
    "There's a new question."
    jump third_question_0

label third_question_0:
    "\"What can the attacker {b}accomplish{/b} through the use of injection?\""
    "{b}Red button{/b}: An attacker can use injection to reduce the amount of storage space required for the application."
    "{b}Green button{/b}: Injection can be used to increase the speed of the affected system."
    "{b}Blue button{/b}: Unauthorized access to sensitive data, modify or delete data, execute malicious code on the affected system, and take control of the system or application."
    "{b}Yellow button{/b}: Attackers can obtain access to the company's physical assets such as office furniture and equipment."
    menu:
        "Which one will you press?"
        "Red button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Green button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "Blue button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound correct
            m "Nice! Sounds like I was right."
        "Yellow button":
            m "I hope this is the one..."
            stop music
            "*click*"
            play sound incorrect
            pause 1.0
            jump bad_ending_orcs
        "<Help> Read book":
            m "The book should be able to help me with this..."
            
            call guide_book from _call_guide_book_3

            m "Okay, now I should be able to answer."
            jump third_question_0

    if test_mode == True:
        return

    play sound door
    pause 3.0

    "..."
    "The gates seem to be opening."

    play music dungeon_air

    show orc angeri_2 at right:
        zoom 0.7

    e "You shall pass now, adventurers."

    show nico scared at left

    n "Huh?"
    n "You're friendly now?"

    e "You have prevailed through the first trial."
    e "Now, please, continue going forward."

    show nico equisde at left

    n "...okay? This is kinda weird but..."

    show nico happy at left

    n "Good job with the buttons mate, one minute later and we'd be beaten on the floor."

    m "Yeah, we got lucky there."
    m "Let's keep going."

    e "Wait adventurers, take this before you go."
    "The orc approaches and gives you a cool stone fragment."

    m "This must be one of the key fragments."
    m "Two more and the relic is ours."

    n "Let's go then!"

    jump fork_1

label fork_1:

    scene bg fork_1
    with fade

    n "Uh oh..."

    show nico neutral
    with dissolve

    n "This corridor splits in two paths..."
    n "The left corridor says \"Attack\" and the right corridor says \"Defend\"."
    n "Which way now?"

label test_3:

    menu:
        "Which way will you take?"

        "Left":
            m "Attack...let's go that way."
            show nico smile
            n "Right on!"
            $ fork = "Attack"
            if test_mode == True:
                return
            jump phase_2

        "Right":
            m "Defend...let's go that way."
            show nico smile 
            n "Right on!"
            $ fork = "Defend"
            if test_mode == True:
                return
            jump phase_3


##################################################################     DUNGEON 2      ###################################################################

label phase_2:

    scene bg black
    "..."
    "You both enter the dark corridor on the left."
    "You walk carefully through the dark with Nico, trying not to bump into anything."

    n "...is that-"

    scene bg phase_2
    with fade

    show nico terrified at left
    with dissolve

    n "a HUGE ASS SPIDER?"
    m "I think so."
    "..."
    "You get a little closer, just to be sure."
    "..."
    m "Oh nevermind, it's just a statue."

    show nico scared at left

    n "Ooof, thankgod...I was about to faint right here."
    "..."
    show nico smile at left
    n "Oh, a button, let's see what it does..."
    m "Wait!"
    "*crack*"
    m "Nico!"

    show nico equisde at left

    n "Uh oh..."

    show bg phase_2_ven
    with dissolve

    n "Shit."
    
    m "This looks poisonous as hell..."

    n "Then hurry up and find how to stop it!"

    m "Look who's talking..."

    pause 0.5

    m "Let's see whats in the spider."

    scene bg phase_2_close 
    with dissolve

    n "Look! It activated some kind of screen."

    m "This must be the text of the second trial."
    m "Let's solve it quickly before it's too late."
    
    "The text reads something like this:"
    "\"Indicate whether the following statements are true or false.\""
    "Pull from one of the spider's legs to do so."
    "Pulling {b}left legs{/b} indicates {b}true{/b}."
    "Pulling {b}right legs{/b} indicates {b}false{/b}."

    pause 0.5
    #"Keep in mind that if time runs out, you will die from the poison."
    "This is definetly a good time to \"save game\"..."
    pause 0.5

    play music combat
    "First statement:"
    
label first_question_1:
    menu:
        "The {b}register section{/b} of a web is the {b}only{/b} input with which a malicious user can exploit the system through {b}SQL injection{/b}."
        "True":
            m "I'll pull the left leg..."
            stop music
            "*crack*"
            play sound incorrect
            pause 1.0
            jump bad_ending_poison
        "False":
            m "I'll pull the right leg..."
            stop music
            "*crack*"
            play sound correct
            m "Nice! Sounds like I was right." 
            m "You can try this kind of attack from other inputs, like search forms, or even in the comments."   
            pause 0.5
            play music combat
            "Second statement:" 
            jump second_question_1
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_4

            m "Okay, now I should be able to answer."
            jump first_question_1

label second_question_1:
    menu:       
        "The following sentence represents a example of an register input from a Javascript Injection attack: {b}'admin; DROP TABLE users; --'{/b}"
        "True":
            m "I'll pull the left leg..."
            stop music
            "*crack*"
            play sound incorrect
            pause 1.0
            jump bad_ending_poison
        "False":
            m "I'll pull the right leg..."
            stop music
            "*crack*"
            play sound correct
            m "Nice! Sounds like I was right."
            m "That was SQL injection most likely."
            show nico terrified
            n "Keep going omagaaawd! We wont make it in time!!"
            m "I'm doing my best! Shush!"
            hide nico terrified
      
            pause 0.5
            play music combat
            "Third statement:"
            jump third_question_1 
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_5

            m "Okay, now I should be able to answer."
            jump second_question_1

label third_question_1:
    menu:       
        "SQL injection is an {b}outdated attack{/b} technique and no longer poses a threat to modern applications."
        "True":
            m "I'll pull the left leg..."
            stop music
            "*crack*"
            play sound incorrect
            pause 1.0
            jump bad_ending_poison
        "False":
            m "I'll pull the right leg..."
            stop music
            "*crack*"
            play sound correct
            m "Nice! Sounds like I was right."
            m "SQL injection is still a commonly used attack technique and continues to pose a significant threat to modern web applications."
      
            pause 0.5
            play music combat
            "Fourth statement:" 
            jump fourth_question_1
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_6

            m "Okay, now I should be able to answer."
            jump third_question_1

label fourth_question_1:
    menu:       
        "The following input causes an unprotected system against SQL injection to delete the users table from the database: {b}'admin; DROP TABLE users; --'{/b}."
        "True":
            m "I'll pull the left leg..."
            stop music
            "*crack*"
            play sound correct
            m "Nice! Sounds like I was right."
            m "Tho that's quite the terrifying input, I hope I don't suffer it anytime soon..."
            n "I'm...not feeling too good right now..."
            m "Just one more question Nico!"
            pause 0.5
            play music combat
            "Fifth statement:" 
            jump fifth_question_1
        "False":      
            m "I'll pull the right leg..."
            stop music
            "*crack*"
            play sound incorrect
            pause 1.0
            jump bad_ending_poison
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_7

            m "Okay, now I should be able to answer."
            jump fourth_question_1


label fifth_question_1:
    menu:       
        "Injection attacks are only effective on systems that use relational databases."
        "True":
            m "I'll pull the left leg..."
            stop music
            "*crack*"
            play sound incorrect
            pause 1.0
            jump bad_ending_poison
        "False":
            m "I'll pull the right leg..."
            stop music
            "*crack*"
            play sound correct
            m "Great! We are saved!"
            m "While SQL injection attacks were initially aimed at relational databases, it is also possible to perform similar attacks on non-relational databases and other data storage technologies."
            if test_mode == True:
                return
            jump phase_2_ending
        "<Help> Read book":
            m "The book should be able to help me with this..."

            call guide_book from _call_guide_book_8

            m "Okay, now I should be able to answer."
            jump fifth_question_1

label phase_2_ending:

    play music dungeon_air
    scene bg phase_2
    with fade
    "*Nico pats your head*"
    show nico happy
    with dissolve
    n "Magaaaaad, you really know your stuff."
    m "You're welcomed dumbass."
    n "Riiigt Riiight, let's keep go-"
    show nico scared
    "*The spider core breaks and leaves a key fragment on the surface*"
    m "Oh, almost forgot about the key!"
    n "So, one more and we're done right?"
    m "Yeah, I can't wait to grab the relic and hit the bed, I need to catch up on sleep..."

    show nico smile

    n "Let's go back to the split."

    $ trials_done = trials_done + 1
    jump back_to_split

label back_to_split:

    scene bg black
    with fade
    "You both go back to the dark corridor."
    pause 0.5
    scene bg fork_1
    with fade

    

    if trials_done >= 2:
        m "We got all the key fragments, let's go back to the hall."
        n "Yush!"
        jump key_forgery

    elif fork == "Attack":
        m "So, I guess we need to go the other way now."
        n "Right! Defend time!"
        jump phase_3
    elif fork == "Defend":
        m "So, I guess we need to go the other way now."
        n "Right! Attack time!"
        jump phase_2
    






##################################################################     DUNGEON 3      ###################################################################

label phase_3:

    scene bg black
    with fade
    "..."
    "You both enter the dark corridor on the right."
    "You walk for a while through the dark, until you spot a light."
    pause 0.5

    scene bg phase_3
    with fade    
    m "That's-"
    n "The last key fragment!!"
    n "That was easy..."
    m "Nah, there's something wrong..."
    pause 0.5 
    "You both hear steps..."
    "...a ton of them."
    "It's like if a whole army was after you."
    n "Oh no..."
    m "Look! The wall has something written!"
    
    scene bg phase_3_close
    with dissolve

    n "What now?!"
    m "It's the trial text again."
    m "It gives some instructions to..."
    m "...to stop the horde!!"    
    n "NICE! Do your thing again mate!"

    pause 0.5
    "This is definetly a good time to \"save game\"..."
    pause 0.5

    "The text says the following:"
    "\"Harken, shouldst thou desire to halt the initial onslaught of the Horde, thou must needs discern which of the following three methods provides a stout defense against an Injection attack.\""
    pause 0.5
    "Seems like you'll need to choose the correct defense for the upcoming raid."
    "If you dont choose the right defenses, you won't be able to uphold."
    pause 0.5    
    play music combat

    "These are the options:"

label first_question_2:
    menu:
        "Which of these techniques helps {b}prevent{/b} Injection attacks?"
        "Use of parameterized queries and prepared statements to ensure that user input is treated as data and not as executable code.":
            $ puzzle = False
            $ def_1 = False
            m "It says we need to move this flag on the floor back and forth."
            n "Easy peasy."
        "Input validation and sanitization to ensure that user input is in the expected format and does not contain malicious code.":
            $ puzzle = False
            $ def_1 = False
            m "It says we need to move this flag on the floor back and forth."
            n "Easy peasy."
        "Both":
            m "It says we need to move this torch on the wall back and forth."
            n "Easy peasy."
        "<Help> Read book":
            m "The book should be able to help me with this..."
            call guide_book from _call_guide_book_9
            m "Okay, now I should be able to answer."
            jump first_question_2


label second_question_2:
    menu:
        "Which of these techniques helps {b}identifying{/b} Injection attacks on time?"
        "Increasing the speed of servers so that they can process incoming requests at a fast enough rate that any injection attack will make the system overload.":
            $ puzzle = False
            $ def_2 = False
            m "Then, it says we need to...cry? like little babies."
            n "Roger."
        "Intrusion detection/prevention systems (IDS/IPS) to monitor network traffic for signs of unauthorized access, malicious activities, and attacks.":
            m "Then, it says we need to shout with all our might."
            n "Roger."
        "Both":
            $ puzzle = False
            $ def_2 = False
            m "Then, it says we need to...cry? like little babies."
            n "Roger."
        "<Help> Read book":
            m "The book should be able to help me with this..."
            call guide_book from _call_guide_book_10
            m "Okay, now I should be able to answer."
            jump second_question_2

label third_question_2:
    menu:
        "Which of these techniques helps {b}fixing{/b} systems which suffered from Injection attacks?"
        "Conduct a thorough security audit to identify and patch any vulnerabilities that were exploited in the attack.":
            m "Lastly, it says we need to stand still and keep staring at them."
            n "Okay, here we go!"
        "Turning off the affected systems and turning them back on again, as this might clear up any issues caused by the attack. ":
            $ puzzle = False
            $ def_3 = False
            m "Then, it says we need to drop our weapons."
            n "Okay, here we go!"
        "Both":
            $ puzzle = False
            $ def_3 = False
            m "Then, it says we need to drop our weapons."
            n "Okay, here we go!"
        "<Help> Read book":
            m "The book should be able to help me with this..."
            call guide_book from _call_guide_book_11
            m "Okay, now I should be able to answer."
            jump third_question_2

label resolve_trial:

    stop music
    
    play music dungeon_air

    scene bg horde
    with fade

    pause 0.5
    "As the horde approaches, you both remember the instructions from the wall."

    if def_1:
        "First, you move the torch on the floor back and forth."
        pause 0.5
        "The horde becomes slower and stand still in front of you."
    else:
        "First, you move the flag on the floor back and forth."
        pause 0.5
        "The horde starts to shout even louder..."

    if def_2:
        "Then, you both start yelling like crazy."
        pause 0.5
        "Some of the raiders seem a bit scared of you..."
    else:
        "Then, you both start crying like little babies..."
        pause 0.5
        "The horde starts laughing at you."

    if def_3:
        "Lastly, you stand still and keep staring at them with fierce faces."
        pause 0.5
        "The horde stares back at you with fierce faces too."
    else:
        "Lastly, you drop you weapons and tell Nico to do so too."
        pause 0.5
        "The horde starts approaching you slowly, with fierce looking faces..."

    if not puzzle:
            jump bad_ending_horde

    e "You both look like fine fellas! It's been a while since anyone from the outside came in here!"

    show nico terrified at right

    n "The goblin is talking!"
    e "Indeed mister hooman, you can take the key fragment over there and get the hell out of here."
    m "Doesn't sound too friendly, let's do what he says."

    show nico scared

    n "...sure"
    e "AAAAaaaagh!  I really was hoping they'd fail so we could have a feast..."
    e "It's been ages since our last proper meal."
    n "Mate, they talking about us like food, we better get out of here quickly before they change their mind."
    m "I agree, let's go."
    "You grab the key fragment and return to where you came from."

    $ trials_done = trials_done + 1
    if test_mode == True:
        return
    jump back_to_split

label key_forgery:

    scene bg fork_0
    with fade

    show nico relieved
    with dissolve

    n "Phew...that was close."
    m "Yeah, but hey, look what we got now!"

    show nico happy

    n "Right! They key should be complete now!"

    "You take the three fragments and put them together."
    n "Let's go to back to the gate and claim the relic."
    m "Right on!"
    
    scene bg black
    with fade

    "You both climb the shiny stairs again."
    "Feeling excited."
    "What could the relic be after all this trouble you went through?"

    scene bg final_door
    with fade
    show nico smile at right
    with dissolve

    pause 0.5
    n "Let's do it pal!"
    m "Here we go!"

    "You push the recently completed key into the door's slot with all your might."

    "*clank*"

    "They key seems to fit perfectly in the slot."
    "You start to hear engines go wild."


    show bg final_door_open
    with dissolve

    m "It's open now!"
    show nico happy at right
    n "The first who takes the relic gets to keep it!"
    hide nico happy at right
    with dissolve
    "Nico starts sprinting through the door."
    m "You bastard! Not again!"
    "You follow him."



##################################################################      ENDINGS       ###################################################################



label good_ending:

    scene bg relic_hallway
    with fade

    stop music
    play music good_ending volume 0.5

    "You find yourself running through a golden hall."
    "You've never seen something like this before."
    "But first you need to catch up to Nico, who doesnt seem to be be stopping anytime soon."
    m "Wait dumbass! There could be a trap!"
    show nico happy
    with dissolve
    n "I won't fall for it hahaha, keep chasing!"
    m "This guy..."

    scene bg relic_chamber
    with dissolve

    "You reach Nico at last."
    "He's standing still before the relic."

    show nico angeri at right
    with dissolve

    n "Don't tell me this is the relic..."
    m "Is that a diploma?"
    n "This must surely be a joke."
    m "Lemme read it."
    "This document says the following:"

    init:
        $ import time
        $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()


    nvl clear

    d "Certificate of Completion."

    d "This document certifies that you hava successfully completed a series of web vulnerability tests related to Injection techniques."

    d "During the course of this program, you have demonstrated proficiency in identifying, exploiting and mitigating a common web-based injection known as Injection."

    d "This achievement is a testament to your dedication and hard work in developing expertise in the field of web security."

    d "Presented on this [day] day of [month], [year]."

    d "Sincerely,"

    d "The WEBSEC TEAM."

    "{b}Good ending{/b}."


    return

label bad_ending_orcs:
    
    show nico terrified at left
    with dissolve

    show orc angeri_2 at right
    with dissolve

    play sound orc_ending
    pause 3
    scene bg black
    "{b}Bad Ending 1: Smashed by orcs{/b}."
    return

label bad_ending_poison:
    "*The screen blocks itself*"
    show nico terrified
    n "No...no no, nonononononononono!"
    m "...sorry mate."
    play music poison_leak
    scene bg phase_2_close_poison 
    pause 3
    scene bg black
    "{b}Bad Ending 2: Death by poisoning{/b}."
    return

label bad_ending_horde:
    n "It's not working mate!"
    m "Damnit, we must have fail some step."
    n "Nooooooooooooooo!"
    play sound horde
    pause 3
    scene bg black
    "{b}Bad Ending 2: Eaten by the Horde{/b}."
    return
