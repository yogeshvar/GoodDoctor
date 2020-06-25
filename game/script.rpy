define maggie   = Character("Maggie")
define robin    = Character("Dr.Robin")
define bong_cha = Character("Bong-Cha")
define min_jun  = Character("Min-Jun")
define rosy     = Character("Su-Lee")
define shilpa   = Character("Shilpa")
define si_woo   = Character("Si-Woo")
define kim      = Character("Dr.Kim")
define leon     = Character("Dr.Leon")
define mark     = Character("Dr.Mark")
define lee      = Character("Dr.Lee")
define robert   = Character("Mr.Robert ")
define brown    = Character("Ms.Brown")
define cathy    = Character("Ms.Cathy")
define sage     = Character("Ms.Sage")

image hospital_entrance = "images/hospital_entrance.png"
image road_crossing = im.Scale("images/road_crossing.png",1920,1080)
image crossed_street = im.Scale("images/street1.png",1920,1080)
image board_meeting = "images/board_meeting.png"
image hospital_room_1 = "images/hospital_room_1.png"
image hospital_room_2 = "images/hospital_room_2.png"
image main_smile_1 = "images/main_smile_1.png"
image si_woo_normal = im.Scale("images/si_woo_normal.png",670,1070)
image si_woo_confused = im.Scale("images/si_woo_confused.png",670,1070)
image si_woo_nervous = im.Scale("images/si_woo_nervous.png",670,1070)
image si_woo_shocked = im.Scale("images/si_woo_shocked.png",670,1070)
image si_woo_angry = im.Scale("images/si_woo_angry.png",670,1070)
image si_woo_flustered = im.Scale("images/si_woo_flustered.png",670,1070)

label start:
    scene road_crossing
    with fade
    pause
    $ main = renpy.input("What's your name?")
    if main == "":
        "Please enter your name"
    main "Hi my name is [main]"

    show main_smile_1 at left

    jump start_scene_1

label start_scene_1:
    "[main] is waiting to cross the road, so that she can go for her interview"
    show main_sad_1 at left
    pause
    "As she is afraid of fast cars and bikes."
    hide main_sad_1
    show si_woo_normal at right
    si_woo "Do you mind? If I help you, cross the road."
    show main_annoyed at left
    main "..."
    show main_angry at left
    main "Do I know you?"
    show main_neutral_1 at left
    si_woo "Does it matter? I can see you are bit afraid to cross the road. Let me help you."
    main "I'm not afraid, it's just I'm not used to it."
    "[main] doesn't want to showcase her as weak."
    menu:
        si_woo "Okay, do you want follow my lead?"
        "Thanks for you help.":
            jump follow_lead
        "I can do it.":
            jump walk_alone

label follow_lead:
    scene crossed_street
    with fade
    pause
    main "Thanks for your help. If you don't mind, in a bit of hurry."
    menu:
        si_woo "No mention. Looks you are heading to the Madison Hospital. Is it so ?"

        "Yes. And you?":
            jump together_to_hospital
        "Sorry, I have to go":
            jump walk_to_hospital

    "Crossed roaded successfully."
    return

label together_to_hospital:
    "Walking together."
    "Thanks for playing. We are working on the next versions. See you soon."
    "If you have any suggestions regarding anyways, please visit https://https://github.com/yogeshvar/GoodDoctor"
    return

label walk_alone:
    "Trying to walk alone."
    "Thanks for playing. We are working on the next versions. See you soon."
    "If you have any suggestions regarding anyways, please visit https://https://github.com/yogeshvar/GoodDoctor"
    return
