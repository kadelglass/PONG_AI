import pygame

BLACK = (0, 0, 0)


# Paddle class:
class Paddle(pygame.sprite.Sprite):

    # constructor
    def __init__(self, primary, secondary, width, height, screen_bounds):
        # call base init function
        super().__init__()

        # init:
        self.primary = primary
        self.secondary = secondary
        self.width = width
        self.height = height
        self.screen_bounds = screen_bounds

        # init image
        self.image = pygame.Surface([width, height])
        self.image.fill(secondary)
        self.image.set_colorkey(secondary)

        # draw:
        pygame.draw.rect(self.image, primary, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < self.screen_bounds[0]:
            self.rect.y = self.screen_bounds[0]

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > self.screen_bounds[1] - self.height:
            self.rect.y = self.screen_bounds[1] - self.height
