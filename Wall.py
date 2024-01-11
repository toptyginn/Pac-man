import pygame

import main

walls_group = pygame.sprite.Group()
BLUE = (0, 0, 255)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__(walls_group, main.all_sprites)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
