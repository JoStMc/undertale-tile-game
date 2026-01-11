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

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour.value, self.position)

    def stepped_on(self, player):
        match self.colour:
            case Colour.YELLOW:
                player.die("Electrocuted")
            case Colour.ORANGE:
                player.update_scent("orange")
            case Colour.BLUE:
                if player.scent == "orange":
                    player.die("Eaten by piranhas")
            case Colour.PURPLE:
                player.update_scent("lemon")
                player.move()
            case Colour.PINK:
                pass
            case Colour.GREEN:
                # To be added
                pass
            case Colour.RED:
                pass
