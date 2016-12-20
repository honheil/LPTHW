class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
brain_world = Scene("The Brain World", "brain_world",
"""
You are now in Jenny's brain, a place that stored her memory, both good and bad.
Your role is to help Jenny to erase her bad memory, in order to protect her.
But you can only finish it when she is sleeping, if she woke up,
there are no way back and you will be disappeared, so grab your time!!
Ok, we believe you can do it!!

You are going into the bad memory zone now.
It seems so quiet, and dull in the surrounding.
Wait, the gate is locked. You can't go inside.
What can you do now?
""")

keypad = Scene("Keypad", "keypad",
"""
Oh yeah there should be a lock here... Let me find and...
Yes, found something...
Huh, it is a keypad for password.

Ok, 0-9 is shown on the keypad.
You have 5 chances to try.
And the password should be 4 digits.
""")

storage_room = Scene("Storage Room", "storage_room",
"""
Great. We make it!!
Now open the gate and keep moving.

You arrived at the storage room of memories.
There are 4 tubes in total that are storing both bad and good memories.
But they are covered so you can't really see which one represents the bad memories.
What you can do is choosing only one tube to release.
Which one are you going to choose?
""")

final_room = Scene("Final Room", "final_room",
"""
Oh! Let's see.
The bad memories are flowing and you made it!!
Jenny won't memorize these anymore.
It should be great to her.

Umm... Why it didn't show that Jenny are going to be happy after losing her bad memories.
It even turns worser. How comes!?!?
Isn't erase the bad memories can protect her?
What have I done!!
what can I do?
""")

save_memories = Scene("Save Memories", "save_memories",
"""
Ok I still have half hour left, until Jenny woke up.
I can save her!!
Gogogo, get all the bad memories back!!

If we get to the dumping area of memories, I think we can get the bad
memories back. But every 30 minutes the area will digest once and if we are late,
the memories will be lost forever. So grab our time!!
You have two options to choose.
The first one is taking the truck the landfill.
The second one is taking the small plane to the landfill.
Which one are you going to choose? 1 / 2
""")

junction = Scene("Junction", "junction",
"""
Woohoo... the truck is so fast...
We have enough fuel to get to there, no worries.

OK now we still have enough time to go.
There are two ways, first is left and second is right.
Which way should be the correct direction? 1 / 2
""")

success = Scene("You Made It!", "success",
"""
Thanks god. We are on the right track.
And we have arrived the memories landfill!!
Just put all the bad memories into the truck and transfer them back to the
storage room. Oh yeah!! Let's go back!!

Ok all the things are on the right track now
Everything is going to be alright.
At first I thought that if there are no bad memories, Jenny would be happier.
But I just realized that it is wrong."
If there are no bad memories, you never know what is real happiness.
Cherish all the memories you had, and make yourself stronger.
Jenny is going to be woke up... We made it!!
""")

generic_death = Scene("Death...", "death", "Mission failed. I know you had tried your best, but...life is hard.")

# Define the action commands available in each scene
junction.add_paths({
    '2': generic_death,
    '1': success
})

save_memories.add_paths({
    '2': generic_death,
    '1': junction
})

final_room.add_paths({
    '*': generic_death,
    'save': save_memories
})

storage_room.add_paths({
    '*': generic_death,
    '3': final_room
})

keypad.add_paths({
    '0521': storage_room,
    '*': generic_death
})

brain_world.add_paths({
    'leave':generic_death,
    'another gate':generic_death,
    'key': keypad
})

# Make some useful variables to be used in the web application
SCENES = {
    brain_world.urlname : brain_world,
    keypad.urlname : keypad,
    storage_room.urlname : storage_room,
    final_room.urlname : final_room,
    save_memories.urlname : save_memories,
    junction.urlname : junction,
    success.urlname : success,
    generic_death.urlname : generic_death
}
START = brain_world
