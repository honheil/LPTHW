from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Junction(Scene):

    def __init__(self):
        super(Junction, self).__init__()
        self.Junction = Junction

    def enter(self):
        print "OK now we still have enough time to go."
        print "There are two ways, first is left and second is right."
        print "Which way should be the correct direction? 1 / 2"
        correct_one = randint(1,2)
        joption = raw_input("> ")

        if int(joption) != correct_one:
            print "Ok we will take way %s." % joption
            print "Should be fine."
            print "Wait... There are no more way to go, we have chosen a wrong way."
            print "We have no time to get back..."
            return 'bad_ending'

        else:
            print "Ok we will take way %s." % joption
            print "Thanks god. We are on the right track."
            print "And we have arrived the memories landfill!!"
            print "Just put all the bad memories into the truck and transfer them back to the"
            print "storage room. Oh yeah!! Let's go back!!"
            return 'success'
