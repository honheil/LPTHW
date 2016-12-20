from nose.tools import *
from map import *

def test_room():
    gold = Scene("GoldScene", "goldroom", """
    This room has gold in it you can grab. There's a door
    to the north.
    """)
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Scene("Center", "center", "Test room in the center.")
    north = Scene("North", "north", "Test room in the north.")
    south = Scene("South", "south", "Test room in the south.")

    center.add_paths({'north':north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.")
    west = Scene("Trees", "trees", "There are trees here, you can go east.")
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_brain_world():
    assert_equal(START.go('leave'), generic_death)
    assert_equal(START.go('another gate'), generic_death)
    room = START.go('key')
    assert_equal(room, keypad)

def test_keypad():
    assert_equal(keypad.go('*'), generic_death)
    room = keypad.go('0521')
    assert_equal(room, storage_room)

def test_final_room():
    assert_equal(final_room.go('*'), generic_death)
    room = final_room.go('save')
    assert_equal(room, save_memories)

def test_save_memories():
    assert_equal(save_memories.go('2'), generic_death)
    room = save_memories.go('1')
    assert_equal(room, junction)
