from sys import exit
from random import randint
from keypad import *
from storage_room import *
from final_room import *
from save_memories import *
from junction import *

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('success')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class BadEnding(Scene):

    scripts = [
        "I know you had tried your best, but...life is hard.",
        "Mission failed.",
        "You are done."
    ]

    def enter(self):
        print BadEnding.scripts[randint(0, len(self.scripts)-1)]
        exit(1)

class BrainWorld(Scene):

    def enter(self):
        print "You are now in Jenny's brain, a place that stored her memory, both good and bad."
        print "Your role is to help Jenny to erase her bad memory, in order to protect her."
        print "But you can only finish it when she is sleeping, if she woke up,"
        print "there are no way back and you will be disappeared, so grab your time!!"
        print "Ok, we believe you can do it!!"
        print "\n"
        print "You are going into the bad memory zone now."
        print "It seems so quiet, and dull in the surrounding."
        print "Wait, the gate is locked. You can't go inside."
        print "What can you do now?"

        action = raw_input("> ")

        if "key" in action:
            print "Oh yeah there should be a lock here... Let me find and..."
            print "Yes, found something..."
            print "Huh, it is a keypad for password."
            return 'keypad'

        elif "leave" or "another gate" in action:
            print "Maybe there are any other gates to go inside."
            print "OH NOOOOOOOO!! The guards discovered you."
            print "RINNNNNNNNNNNG!! The alarm is ringing."
            print "Jenny has woke up!!"
            return 'bad_ending'

        else:
            print "It's not a good method to solve the problem."
            return 'brain_world'

class Success(Scene):

    def enter(self):
        print "Ok all the things are on the right track now"
        print "Everything is going to be alright."
        print "At first I thought that if there are no bad memories, Jenny would be happier."
        print "But I just realized that it is wrong."
        print "If there are no bad memories, you never know what is real happiness."
        print "Cherish all the memories you had, and make yourself stronger."
        print "Jenny is going to be woke up... We made it!!"

class Map(object):

    scenes = {
        'bad_ending': BadEnding(),
        'brain_world': BrainWorld(),
        'keypad': Keypad(),
        'storage_room': StorageRoom(),
        'final_room': FinalRoom(),
        'save_memories': SaveMemories(),
        'junction': Junction(),
        'success': Success(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('brain_world')
a_game = Engine(a_map)
a_game.play()
