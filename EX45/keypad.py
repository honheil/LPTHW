class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Keypad(Scene):

    def __init__(self):
        super(Keypad, self).__init__()
        self.Keypad = Keypad

    def enter(self):
        print "Ok, 0-9 is shown on the keypad."
        print "You have 5 chances to try."
        print "And the password should be 4 digits."
        pw = '0521'
        pwinput = raw_input("> ")
        pwcount = 0

        while pwinput != pw and pwcount < 2:
            print "Wrong password"
            pwcount += 1
            pwinput = raw_input("> ")

        while pwinput != pw and pwcount == 2:
            print "Wait... Would the password be the birthday of Jenny?"
            print "As I remember it is in May."
            pwcount += 1
            pwinput = raw_input("> ")

        while pwinput != pw and pwcount == 3:
            print "It is in twenty-something of May I guess."
            pwcount += 1
            pwinput = raw_input("> ")

        if pwinput == pw:
            print "Great. We make it!!"
            print "Now open the gate and keep moving."
            return 'storage_room'
        else:
            print "It is still locked and alarm is ringing now."
            print "You are caught by the guard."
            return 'bad_ending'
