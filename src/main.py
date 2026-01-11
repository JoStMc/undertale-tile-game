import pygame
import sys
from constants import *
from game_state import GameState
from tile import *
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState(screen)

    game_state.draw_initial_grid()
    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game_state.draw()
        game_state.update(dt)

        pygame.display.update()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
