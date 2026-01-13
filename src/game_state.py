import random
from constants import *
from tile import *
from player import *


from path import gen_simple_path
from path_assignment import colour_path

class GameState:
    def __init__(self, screen):
        self.tiles = self.generate_grid()

        colour_path(gen_simple_path(self.tiles))

        self.player = Player(3*TILE_WIDTH, SCREEN_HEIGHT//2, self.tiles)
        self.screen = screen
        self.cooldown = 0

    def generate_grid(self):
        tiles = []
        for row in range(NO_ROWS):
            cur_row = []
            for column in range(NO_COLS):
                random_col = random.choice(list(Colour))
                x = 3*TILE_WIDTH + TILE_WIDTH*column
                y = SCREEN_HEIGHT//2 - (NO_ROWS//2 - row) * TILE_WIDTH
                cur_row.append(Tile(x, y, TILE_WIDTH, random_col))
            tiles.append(cur_row)

        for row in range(NO_ROWS):
            for column in range(NO_COLS):
                tile = tiles[row][column]
                up = tiles[row-1][column] if row > 0 else None
                down = tiles[row+1][column] if row < NO_ROWS - 1 else None
                left = tiles[row][column-1] if column > 0 else None
                right = tiles[row][column+1] if column < NO_COLS - 1 else None
                tile.set_neighbours(up, down, left, right)

        return tiles[NO_ROWS//2][0]  # Return starting tile

    def draw_initial_grid(self):
        visited = set()
        self.draw_initial_grid_recursive(self.tiles, visited)

    def draw_initial_grid_recursive(self, tile, visited):
        if tile is None or tile in visited:
            return
        tile.draw(self.screen)
        visited.add(tile)
        self.draw_initial_grid_recursive(tile.up, visited)
        self.draw_initial_grid_recursive(tile.down, visited)
        self.draw_initial_grid_recursive(tile.left, visited)
        self.draw_initial_grid_recursive(tile.right, visited)

    def draw(self):
        self.player.previous_tile.draw(self.screen)
        self.player.draw(self.screen)

    def update(self, dt):
        self.player.update(dt)

