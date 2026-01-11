import random
from constants import *
from tile import *
from player import *

class GameState:
    def __init__(self, screen):
        self.tiles = self.generate_grid()
        self.current_tile = [NO_ROWS//2, 0]
        self.player = Player(3*TILE_WIDTH, SCREEN_HEIGHT//2)
        self.screen = screen

    def generate_grid(self):
        tiles = []
        for row in range(NO_ROWS):
            tiles.append([])
            for column in range(NO_COLS):
                random_col = random.choice(list(Colour))
                pos_x = 3*TILE_WIDTH + TILE_WIDTH*column
                pos_y = SCREEN_HEIGHT//2 + (NO_ROWS//2 - row) * TILE_WIDTH
                tiles[row].append(Tile(pos_x, pos_y, TILE_WIDTH, random_col))
        return tiles

    def draw(self):
        self.player.draw(self.screen)

    def draw_initial_grid(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)

    def update(self, dt):
        self.player.update(dt)
