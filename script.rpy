
define S = Character("Smormu")

image smormu happy:
        "Smormu Happy.png"
        zoom .25

image anthonybadonk:
    "BG AnthonyBadonk.png"
    zoom 2.00

label start:

label bgm:

    scene bg 1

    show smormu norm

    play music "audio/02. Normal Days Indeed.mp3" fadein 1.0


    S "Hi! I'm Smormu!"

    show smormu happy

    play music "audio/01. Welcome to the Classroom of the Elite.mp3" fadein 0.5


    S "YOUR HOMO!!!" with vpunch


    scene bg anthonybadonk

    play music "audio/Explosion.wav"

    pause 5.0

    stop music

    play music "audio/02. Normal Days indeed.mp3" fadein 3.0 fadeout 3.0

    scene bg 1

    show smormu norm

    S "Anyway, let's start our DATE!"

    S "Come on! I'll take us to a cool spot in town!"

    scene bg 2
    show smormu norm
    with fade

    S "Here we are! In good ol' Wakomundo."

    label choices:
        S "So... what do you want to do?"
    menu:
        "I wanna fight something":
            jump choices1_a
        "I wanna relax":
            jump choices1_b

    label choices1_a:
        S "Alright, let's go fight then!"
        jump choices1_fight

    label choices1_b:
        S "Alright, let's have a picnic then!"
        jump choices1_picnic


    label choices1_fight:

    S "LOL"

    return

    label choices1_picnic:

    S "LOL2"




    return
