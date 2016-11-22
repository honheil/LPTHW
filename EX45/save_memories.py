class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class SaveMemories(Scene):

    def __init__(self):
        super(SaveMemories, self).__init__()
        self.SaveMemories = SaveMemories

    def enter(self):
        print "If we get to the dumping area of memories, I think we can get the bad"
        print "memories back. But every 30 minutes the area will digest once and if we are late,"
        print "the memories will be lost forever. So grab our time!!"
        print "You have two options to choose."
        print "The first one is taking the truck the landfill."
        print "The second one is taking the small plane to the landfill."
        print "Which one are you going to choose? 1 / 2"

        option = raw_input("> ")

        if option == '1':
            print "Woohoo... the truck is so fast..."
            print "We have enough fuel to get to there, no worries."
            return 'junction'

        elif option == '2':
            print "1, 2, 3... Set off!!"
            print "Wait wait wait. Oh no, the fuel is going to be exhausted."
            print "Please... no..."
            return 'bad_ending'

        else:
            print "Nooooo, you only have these two options to choose."
            return 'save_memories'
