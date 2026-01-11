import pygame
from constants import TILE_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        # direction = [up/down, left/right] = [-1/1, -1/1]
        self.direction = pygame.Vector2(0, 1)
        self.moving = False
        self.radius = TILE_WIDTH // 3

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def move(self):
        self.position += TILE_WIDTH * self.direction

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -1)
            self.moving = True
        if keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 1)
            self.moving = True
        if keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1, 0)
            self.moving = True
        if keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1, 0)
            self.moving = True


        if self.moving:
            self.move()
