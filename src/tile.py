import pygame
from enum import Enum

class Colour(Enum):
    YELLOW = "yellow"
    RED = "red"
    GREEN = "green"
    ORANGE = "orange"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, colour):
        super().__init__()
        self.position = pygame.Rect(x - width//2, y - width//2, width, width)
        self.colour = colour

        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def set_neighbours(self, up, down, left, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour.value, self.position)
