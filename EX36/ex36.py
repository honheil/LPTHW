from sys import exit

def woke_up():
    print "What shall I do now? Go out / ask the woman standing in front of me?"

    choice = raw_input("> ")
    if "go" in choice:
        print "'You can't go out. You are still recovering.' The women said."
        woke_up()
    elif "ask" in choice:
        print "'You have slept for a week in the hospital.''"
        print "'And here's your letter. It was with you when you were transferring to here.' The woman said."
        print "The woman left."
        letter()
    else:
        print "I don't know what do you mean."
        woke_up()


def happy_ending():
    print "'HENRY!!' a girl voice came."
    print "Oh my god! That's Rosie."
    print "'I can't imagine you are here, cause I have called you for so many times but nobody answered.'"
    print "Sorry for being late. Something's happened."
    print "'Glad that you are here.'"
    print "Rosie..."
    print "'Yes?'"
    print "What should I say now?"

    choice = raw_input("> ")
    if "kiss" in choice:
        print "Can I kiss you?"
        print "I hope the time can be stopped from now on, and being like that forever."
        print "Now I know where am I, I am in..."
        exit(0)
    else:
        print "'OH NO. The train is about to apart, see you Henry. Take Care!'"
        print "Good luck to your new journey my dearest friend."
        print "'Thanks. And you too, Henry.'"
        print "I will miss you so much."
        print "'Me too. So, see you one day.'"
        print "Ya, see you."
        print "The door closed and we are never getting back together."
        print "I know from now on, the distance between us is getting further and further."
        exit(0)


def train_station():
    print "Where's Rosie?"
    print "Have I missed to see her again?"
    print "Shall I wait here or she has left already? wait here / leave"

    choice = raw_input("> ")
    if "wait" in choice:
        happy_ending()
    elif "leave" in choice:
        end("I think I has missed to see her at last.")
    else:
        "What shall I do now? Wait or not wait!"
        train_station()


def elderly():
    print "The oranges are in front of you. Are you going to help her to pick them up? yes / no"

    choice = raw_input("> ")
    if choice == "yes":
        print "'Thanks so much, young man. May God bless you all the times.' The old lady said."
        print "And she gave you a orange as a gift."
        print "You arrived the station and just saw the train's doors closed, with Rosie inside."
        end("Unless you got a orange.")
    elif choice == "no":
        print "'SORRY!!' and keep running."
        train_station()
    else:
        print "Make decision now!!"
        elderly()


def jam():
    print "Shall I wait on the car or get out now and run?"

    choice = raw_input("> ")
    if "wait" in choice:
        end("After stucking on the road for an hour. Rosie is not in the station anymore.")
    elif "get out" or "go" or "run" in choice:
        print "Ok man, I can make it. Run!!"
        print "'MY ORANGES!' A old lady yelled."
        elderly()
    else:
        print "Go or not go!?"
        jam()


def transport():
    print "How should I go to the train station? subway / taxi / bus?"

    choice = raw_input("> ")
    if choice == "subway":
        print "Great. It takes only 10 minutes."
        train_station()
    elif choice == "taxi":
        print "Oh no. What's wrong today. We are stucked in the middle."
        jam()
    elif choice == "bus":
        print "Oh no. What's wrong today. We are stucked in the middle."
        jam()
    else:
        print "There are no alternative except these three options."
        transport()


def direction():
    print "Which way shall I go, left or right?"

    choice = raw_input("> ")
    if choice == "left":
        print "Ok. That's the exit of the hospital."
        transport()
    elif choice == "right":
        print "'Hey, as I said you can't go anywhere before you are fully recovered.' said the nurse."
        print "You are back to the room."
        action()
    else:
        print "LEFT or RIGHT, again!!"
        direction()


def action():
    print "Shall I go out or stay here?"

    choice = raw_input("> ")
    if "go" in choice:
        direction()
    elif "stay here" in choice:
        end("I can do nothing on it.")
    else:
        print("Henry, you are too lazy to make a decision. Come on!")
        action()


def find_stuff():
    print "Are there any other stuff that I can find any clues?"
    print "Pick up a photo album, mobile phone or diary?"

    choice = raw_input("> ")
    if "photo album" in choice:
        print "Umm... look at the cute baby, that should be my photos in childhood."
        print "Just only childhood photos."
        find_stuff()
    elif "mobile phone" in choice:
        print "Damn, I forgot my pin."
        find_stuff()
    elif "diary" in choice:
        print "Wait, that's the last sentence."
        print "'Rosie gave me a letter today. She will be leaving with the train one week later.'"
        print "'We know we love each other, but the destiny doesn't accept us.'"
        print "'What can I do.'"
        action()
    else:
        print "There are nothing seems like clue except these three stuff."
        find_stuff()


def letter():
    print "Shall I open the envelope? yes / no"

    choice = raw_input("> ")
    if choice == "yes":
        print "Dear Henry,"
        print " "
        print "........."
        print "Wish you all the best and sorry for leaving you."
        print " "
        print "Love, Rosie"
        print "Who is Rosie?"
        find_stuff()
    elif choice == "no":
        print "But why I was holding this letter at that time? I should have a look"
        letter()
    else:
        "Stay concentrate! Just only have two options, Henry."
        letter()


def end(why):
    print why, "Let the story end."
    exit(0)


def start():
    print "Don't go!!!"
    print "Where am I?"
    print "What happened?"
    print "Why am I sitting on a hospital bed?"
    woke_up()

start()
