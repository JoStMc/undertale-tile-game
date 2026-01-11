import pygame
import sys
from constants import *
from player import Player
from tile import *
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #clock = pygame.time.Clock()
    #dt = 0

    player = Player(2*TILE_WIDTH, SCREEN_HEIGHT//2)

    no_rows = 9
    no_cols = 20
    tiles = []
    for row in range(no_rows):
        #tiles.append([])
        for column in range(no_cols):
            random_col = random.choice(list(Colour))
            pos_x = 3*TILE_WIDTH + TILE_WIDTH*column
            pos_y = SCREEN_HEIGHT//2 + (no_rows//2 - row) * TILE_WIDTH
            tiles.append(Tile(pos_x, pos_y, TILE_WIDTH, random_col))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #dt = clock.tick(60)/1000

        player.draw(screen)

        for tile in tiles:
            tile.draw(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()
