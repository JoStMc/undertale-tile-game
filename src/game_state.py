import random
from constants import *
from tile import *
from player import *

class GameState:
    def __init__(self, screen):
        self.tiles = self.generate_grid()
        self.player = Player(3*TILE_WIDTH, SCREEN_HEIGHT//2)
        self.current_tile = [0, NO_ROWS//2]
        self.previous_tile =[0, 0]
        self.screen = screen
        self.cooldown = 0

    def generate_grid(self):
        tiles = []
        for row in range(NO_ROWS):
            tiles.append([])
            for column in range(NO_COLS):
                random_col = random.choice(list(Colour))
                pos_x = 3*TILE_WIDTH + TILE_WIDTH*column
                pos_y = SCREEN_HEIGHT//2 - (NO_ROWS//2 - row) * TILE_WIDTH
                tiles[row].append(Tile(pos_x, pos_y, TILE_WIDTH, random_col))
        return tiles

    def draw(self):
        self.player.draw(self.screen)
        self.tiles[self.previous_tile[1]][self.previous_tile[0]].draw(self.screen)

    def draw_initial_grid(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)

    def update(self, dt):
        self.cooldown -= dt

        if self.cooldown <= 0:
            self.player.update()

            if self.player.moving:
                self.cooldown = 0.2

                self.previous_tile = self.current_tile.copy()
                self.current_tile[0] += self.player.direction[0] 
                self.current_tile[1] += self.player.direction[1] 

