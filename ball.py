# imports:
import pygame
from random import randint


# init:


# ball class:
class Ball(pygame.sprite.Sprite):

    # constructor
    def __init__(self, primary, secondary, width, height, speed, screen_bounds):

        # init:

        # base class init
        super().__init__()

        # class init
        self.primary = primary
        self.secondary = secondary
        self.width = width
        self.height = height
        self.screen_bounds = screen_bounds
        self.speed = speed

        # drawing:

        # drawing init
        self.image = pygame.Surface([width, height])
        self.image.fill(secondary)
        self.image.set_colorkey(secondary)

        # draw
        pygame.draw.circle(self.image, primary, (width / 2, height / 2), width / 2)

        # ball logic:

        # velocity
        self.velocity = [randint(speed, speed * 2), randint(-(speed * 2), speed * 2)]

        self.rect = self.image.get_rect()

    # update function
    def update(self):

        # base class
        super().update()

        # update:
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # collision
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-(self.speed * 2), self.speed * 2)
