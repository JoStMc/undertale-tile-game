import pygame
from constants import TILE_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        # direction = [up/down, left/right] = [-1/1, -1/1]
        self.direction = [1, 0]
        self.moving = False
        self.radius = TILE_WIDTH // 3

        self.scent = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def move(self):
        self.position[0] += TILE_WIDTH * self.direction[0]
        self.position[1] += TILE_WIDTH * self.direction[1]

    def update(self):
        keys = pygame.key.get_pressed()
        self.moving = False

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
