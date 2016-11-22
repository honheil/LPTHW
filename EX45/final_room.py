class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class FinalRoom(Scene):

    def __init__(self):
        super(FinalRoom, self).__init__()
        self.FinalRoom = FinalRoom

    def enter(self):
        print "Umm... Why it didn't show that Jenny are going to be happy after losing her bad memories."
        print "It even turns worser. How comes!?!?"
        print "Isn't erase the bad memories can protect her?"
        print "What have I done!!"
        print "what can I do?"

        decision = raw_input("> ")

        if "save" in decision:
            print "Ok I still have half hour left, until Jenny woke up."
            print "I can save her!!"
            print "Gogogo, get all the bad memories back!!"
            return 'save_memories'

        else:
            print "Jenny has woke up."
            print "Everything is ended."
            print "She will never feel what is the real meaning of happiness."
            return 'bad_ending'
