import pygame

import Money
import Wall
import main

player_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    def __init__(self, file, speed, lev):
        super().__init__(player_group, main.all_sprites)
        self.change_x = 0
        self.change_y = 0
        self.image = main.tile_images[file]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = main.start_pos_level[file][lev - 1]
        main.all_sprites.add(self)
        self.speed = speed

    def moving(self, pazmer, destinations, boarddd, speed):
        if destinations == "r":
            self.rect.x += speed
            for i in Wall.walls_group:
                if self.walls(i):
                    print("Пакмен столкнулся со стеной")
                    self.rect.x -= speed
                else:
                    if self.rect.x + 10 >= pazmer * 30 + 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (
                            pazmer // 2) * 30 + 10:
                        self.rect.x = 10
        elif destinations == "l":
            self.rect.x -= speed
            for i in Wall.walls_group:
                if self.walls(i):
                    print("Пакмен столкнулся со стеной")
                    self.rect.x += speed
            if self.rect.x - 10 <= 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (pazmer // 2) * 30 + 10:
                self.rect.x = pazmer * 30
        elif destinations == "u":
            self.rect.y -= speed
            for i in Wall.walls_group:
                if self.walls(i):
                    print("Пакмен столкнулся со стеной")
                    self.rect.y += speed
        elif destinations == "d":
            self.rect.y += speed
            for i in Wall.walls_group:
                if self.walls(i):
                    print("Пакмен столкнулся со стеной")
                    self.rect.y -= speed

    def previous_direction(self):
        self.pre_x = self.change_x
        self.pre_y = self.change_y

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def walls(self, walls):
        if pygame.sprite.collide_mask(self, walls):
            return True
        return False


class Pacman(Character):
    def __init__(self, speed, lev):
        super().__init__('pac', speed, lev)
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.collides = 0

    def moving(self, pazmer, destinations, boarddd, speed):
        Character.moving(self, pazmer, destinations, boarddd, speed)

    def update(self):
        collides_with_coins = pygame.sprite.spritecollide(self, Money.money_group, True)
        if len(collides_with_coins) > self.collides:
            self.collides = len(collides_with_coins)
            self.score += 10


class Ghost(Character):
    def __init__(self, speed, lev):
        super().__init__('ghost_r', speed, lev)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        collides_with_pacman = pygame.sprite.spritecollide(self, player_group, True)



