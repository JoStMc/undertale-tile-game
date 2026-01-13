from constants import NO_COLS
import random

def gen_simple_path(starting_tile):
    '''
    Generates a simple path which never goes left; it only goes
    up or down and to the right

    Return: (tile, origin direction)
    '''
    # The idea is that each step is a random choice of [i:j]
    # If i=0, up is a valid direction, otherwise 1
    # If j=3, down is a valid direction, otherwise 2
    valid_direction = ["up", "right", "down"]
    path = [(starting_tile, '')]
    previous_tile = starting_tile
    i = 0
    j = 3
        
    steps_remaining = NO_COLS - 1
    while steps_remaining > 0:
        if previous_tile.up is None:
            i = 1
        if previous_tile.down is None:
            j = 2
        
        direction = random.choice(valid_direction[i:j])

        i = 0
        j = 3

        # Sets i and j correspondingly so the path doesn't go up and then down
        # or vice versa
        if direction == "up":
            path.append((previous_tile.up, "up"))
            previous_tile = previous_tile.up
            j = 2
        elif direction == "down":
            path.append((previous_tile.down, "down"))
            previous_tile = previous_tile.down
            i = 1
        else:
            path.append((previous_tile.right, "right"))
            previous_tile = previous_tile.right
            steps_remaining -= 1

    for tile in path:
        print(tile[1], end=", ")
    return path
