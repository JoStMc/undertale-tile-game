import pygame
from constants import TILE_WIDTH
from tile import Colour
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, starting_tile):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        # direction = [up/down, left/right] = [-1/1, -1/1]
        self.direction = [0, 0]
        self.previous_tile = starting_tile
        self.current_tile = starting_tile
        self.moving = False
        self.radius = TILE_WIDTH // 3
        self.cooldown = 0

        self.scent = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def move(self):
        if not self.tile_invalid(self.get_next_tile()):
            self.position[0] += TILE_WIDTH * self.direction[0]
            self.position[1] += TILE_WIDTH * self.direction[1]
            self.current_tile = self.get_next_tile()

    def stepped_on(self, tile):
        match tile.colour:
            case Colour.YELLOW:
                self.die("Electrocuted")
            case Colour.ORANGE:
                self.set_scent("orange")
            case Colour.BLUE:
                if self.scent == "orange":
                    self.die("Eaten by piranhas")
                if (tile.up is not None and tile.up.colour == Colour.YELLOW or
                    tile.down is not None and tile.down.colour == Colour.YELLOW or
                    tile.left is not None and tile.left.colour == Colour.YELLOW or
                    tile.right is not None and tile.right.colour == Colour.YELLOW):
                    self.die("Electrocuted")
            case Colour.PURPLE:
                 self.set_scent("lemon")
                 self.move()
                 if not self.tile_invalid(self.get_next_tile()):
                    self.stepped_on(self.current_tile)
            case Colour.PINK:
                pass
            case Colour.GREEN:
                # To be added
                pass
            case _:
                raise Exception("Tile colour not found")

    def set_scent(self, scent):
        self.scent = scent

    def die(self, message):
        print(message)
        sys.exit()


    def get_next_tile(self):
        match self.direction:
            case [1, 0]:
                return self.current_tile.right
            case [-1, 0]:
                return self.current_tile.left
            case [0, 1]:
                return self.current_tile.down
            case [0, -1]:
                return self.current_tile.up
            case [0, 0]:
                return
            case _:
                raise ValueError("Invalid direction")


    def tile_invalid(self, next_tile):
        return next_tile is None or next_tile.colour == Colour.RED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.moving = False

        self.cooldown -= dt

        if keys[pygame.K_UP]:
            self.direction = [0, -1]
            self.moving = True
        if keys[pygame.K_DOWN]:
            self.direction = [0, 1]
            self.moving = True
        if keys[pygame.K_LEFT]:
            self.direction = [-1, 0]
            self.moving = True
        if keys[pygame.K_RIGHT]:
            self.direction = [1, 0]
            self.moving = True

        if self.cooldown <= 0:

            if self.moving:
                self.previous_tile = self.current_tile
                self.move()
                self.stepped_on(self.current_tile)
                self.cooldown = 0.2
