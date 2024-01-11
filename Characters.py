import pygame


tile_width = tile_height = 0


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.change_x = 0
        self.change_y = 0
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.pre_x = x
        self.pre_y = y

    def previous_direction(self):
        self.pre_x = self.change_x
        self.pre_y = self.change_y

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Find a new position for the player
    def update(self, walls, gate):
        old_x = self.rect.left
        new_x = old_x + self.change_x
        prev_x = old_x + self.pre_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        prev_y = old_y + self.pre_y

        if pygame.sprite.collide_mask(self, walls):
            self.rect.left = old_x
            self.rect.top=prev_y
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                 self.rect.top = old_y
                 print('a')
        else:

            self.rect.top = new_y



        # if gate != False:
        #     gate_hit = pygame.sprite.spritecollide(self, gate, False)
        #     if gate_hit:
        #         self.rect.left = old_x
        #         self.rect.top = old_y


class Ghost(Character):
    def changespeed(self, list, ghost, turn, steps, l):
        try:
            z = list[turn][2]
            if steps < z:
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps += 1
            else:
                if turn < l:
                    turn += 1
                elif ghost == "clyde":
                    turn = 2
                else:
                    turn = 0
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps = 0
            return [turn, steps]
        except IndexError:
            return [0, 0]


def move(hero, destination, Map):
    x, y = hero.pos
    if destination == 'up':
        if y > 0 and Map[y - 1][x] == '.':
            hero.move(x, y - 1)
    if destination == 'down':
        if y < len(Map) and Map[y + 1][x] == '.':
            hero.move(x, y + 1)
    if destination == 'left':
        if x > 0 and Map[y][x - 1] == '.':
            hero.move(x - 1, y)
    if destination == 'right':
        if x < len(Map[0]) and Map[y][x + 1] == '.':
            hero.move(x + 1, y)





