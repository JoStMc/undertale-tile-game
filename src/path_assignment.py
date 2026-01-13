import random
from tile import Colour, Tile
from path import gen_simple_path

def colour_path(path):
    '''
    Takes an existing path and colours each tile to make a valid route
    '''
    # The idea is to have valid_colours[i:j]
    # i=1 when purple is invalid - 
    #               that's when the tile the player will slide off the path
    # j= not included until orange is found in the path
    #               j=-1 after stepping on purple
    valid_colours = [Colour.PURPLE, Colour.ORANGE, Colour.PINK, Colour.BLUE]
    
    path[0][0].colour = Colour.PINK
    piranha_safe = True
    
    for i in range(1, len(path)):
        slide_check = 0
        shock_safe = True
        # If origin direction of the next path is not the same as the current's
        tile = path[i][0]
        if i < len(path) -1 and path[i][1] != path[i+1][1]:
            slide_check = 1

        if (tile.up is not None and tile.up.colour == Colour.YELLOW or
            tile.down is not None and tile.down.colour == Colour.YELLOW or
            tile.left is not None and tile.left.colour == Colour.YELLOW or
            tile.right is not None and tile.right.colour == Colour.YELLOW):
            shock_safe = False

        if shock_safe and piranha_safe:
            col_choice = random.choice(valid_colours[slide_check:])

        else:
            col_choice = random.choice(valid_colours[slide_check:-1])

        if col_choice == Colour.ORANGE:
            piranha_safe = False
        elif col_choice == Colour.PURPLE:
            piranha_safe = True

        tile.colour = col_choice

