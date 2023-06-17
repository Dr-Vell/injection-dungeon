image bg = "demo/bg.jpg"
image aya = "demo/Ayame Errkk.png"
image nan = "demo/Nana Confident.png"
define aya = Character('Ayame', color="#055")
define nan = Character('Nana', color="#505")

label demo:
    show bg
    show aya at left
    aya "Ha... Hi... {w=.5}My name is Ayame... {w=.5}Your host for this demo... {w=.5}Call me Aya."
    show nan at right
    nan "And I'm Nana, {w=.5}Let's jump to the menu examples."
    label demo_first_menu:
        menu:
            "More menues":
                jump demo_more_menus
            "Input":
                jump demo_inputs
            "Long dialogue":
                jump demo_long_dialogue
            "History":
                jump demo_history
            "Exit":
                return
        return

label demo_inputs:
    aya "what's your name?"
    python:
        name = renpy.input("My name is...")
        name = name.strip()
        if not name:
            name = "Smog"
    aya "My name is [name]! Nice to meet you."
    menu:
        "return to the first menu":
            jump demo_first_menu
        "Exit":
            return

label demo_more_menus:
    menu:
        "This menu has some long text"
        "A very long menu to test how the menues look when we have lots of text in choices, in other words: testing multiline frames":
            aya "Wow that was long."
        "A short one to compare":
            aya "what to do now?"
    menu:
        "return to the first menu":
            jump demo_first_menu
        "Exit":
            return


label demo_long_dialogue:
    aya "Let me explain something useful... "
    aya "There's an ideal lenght of text that allows you to read with ease... {w}It has little to do with the font size and its visibility... {w}You can read ten to twenty words before you lose track of where were you reading from, in a long line. "
    aya "It's a good idea to break long text into lines and if it's longer than few lines, breaking it into multiple peaces of dialogues. "
    extend "That's exactly the reason why newspapers are columns of text instead of starting from one side and going all the way to the other side. "
    nan "Well I guess that's more than enough text to see how much you can fit in the say window before something goes awry."
    nan "Keep in mind, it's a game, not a book... "
    nan "You can have one centence per page and it comes out in roughly the same file size."
    label demo_long_dialogue_menu:
        menu:
            "return to the first menu":
                jump demo_first_menu
            "I need and even bigger block of text":
                aya "Let me explain it again... "
                extend "There's an ideal lenght of text that allows you to read with ease... "
                extend "It has little to do with the font size and its visibility... "
                extend "You can read ten to twenty words before you lose track of where were you reading from, in a long line. "
                extend "It's a good idea to break long text into lines and if it's longer than few lines, breaking it into multiple peaces of dialogues. "
                extend "That's exactly the reason why newspapers are columns of text instead of starting from one side and going all the way to the other side. "
                extend "Well I guess that's more than enough text to see how much you can fit in the say window before something goes awry."
                extend "Keep in mind, it's a game, not a book... "
                extend "You can have one centence per page and it comes out in roughly the same file size."
                jump demo_long_dialogue_menu
            "Exit":
                return

label demo_history:
    aya "let's make some history"
    nan "do I have something to say here?"
    aya "yes we need lots of chitcat"
    nan "cool I wanted to add something"
    aya "what?"
    nan "let the narrator say something"
    aya "of curse"
    aya "hey narrator"
    "huh, who? me?"
    aya "yes you, sitting silent on the corner watching girls stip, what's going on on your filty brain?"
    "nothing, I swear"
    nan "yeah he's a pervert"
    aya "obviously"
    "I'm not"
    aya "so desprate"
    nan "so obvious"
    aya "do we have enough history now?"
    nan "I guess so"
    nan "let's check"
    menu:
        "return to the first menu":
            jump demo_first_menu
        "Exit":
            return
