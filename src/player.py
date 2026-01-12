import pygame
from constants import TILE_WIDTH
from tile import Colour
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, starting_tile):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        # direction = [up/down, left/right] = [-1/1, -1/1]
        self.direction = [1, 0]
        self.current_tile = starting_tile
        self.moving = False
        self.radius = TILE_WIDTH // 3
        self.cooldown = 0

        self.scent = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def move(self):
        self.position[0] += TILE_WIDTH * self.direction[0]
        self.position[1] += TILE_WIDTH * self.direction[1]

    def stepped_on(self, tile):
        match tile.colour:
            case Colour.YELLOW:
                self.die("Electrocuted")
            case Colour.ORANGE:
                self.update_scent("orange")
            case Colour.BLUE:
                if self.scent == "orange":
                    self.die("Eaten by piranhas")
            case Colour.PURPLE:
                self.update_scent("lemon")
                self.move()
            case Colour.PINK:
                pass
            case Colour.GREEN:
                # To be added
                pass
            case _:
                raise Exception("Tile colour not found")

    def update_scent(self, scent):
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
            case _:
                raise ValueError("Invalid direction")

    def get_prev_tile(self):
        match self.direction:
            case [1, 0]:
                return self.current_tile.left
            case [-1, 0]:
                return self.current_tile.right
            case [0, 1]:
                return self.current_tile.up
            case [0, -1]:
                return self.current_tile.down
            case _:
                raise ValueError("Invalid direction")

    def detect_collision(self, next_tile):
        return self.__is_out_of_bounds(next_tile) or self.__is_red_tile(next_tile)

    def __is_red_tile(self, next_tile):
        return next_tile.colour == Colour.RED

    def __is_out_of_bounds(self, next_tile):
        return next_tile is None

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
                next_tile = self.get_next_tile()

                if not self.detect_collision(next_tile):
                    self.current_tile = next_tile
                    print(f"Current: {self.current_tile}")
                    print(f"Prev: {self.get_prev_tile()}")
                    print("-------------")

                    self.move()
                    self.stepped_on(self.current_tile)
                    self.cooldown = 0.2
