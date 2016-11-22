from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class StorageRoom(Scene):

    def __init__(self):
        super(StorageRoom, self).__init__()
        self.StorageRoom = StorageRoom

    def enter(self):
        print "You arrived at the storage room of memories."
        print "There are 4 tubes in total that are storing both bad and good memories."
        print "But they are covered so you can't really see which one represents the bad memories."
        print "What you can do is choosing only one tube to release."
        print "Which one are you going to choose?"
        correct_one = randint(1,4)
        tinput = raw_input("> ")

        if int(tinput) != correct_one:
            print "You choose the wrong one."
            print "They are all good memories."
            print "You are watching them flowing to nowhere and be disappear forever."
            return 'bad_ending'

        else:
            print "Oh! Let's see."
            print "The bad memories are flowing and you made it!!"
            print "Jenny won't memorize these anymore."
            print "It should be great to her."
            return 'final_room'
