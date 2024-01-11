import pygame
import sys
import os
import random


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):
    # print('data', name)
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_end_screen(lev, intro_text, WIDTH, HEIGHT, im):
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image(im), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(walls_group, all_sprites)
        self.image = tile_images['wal']
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        walls_group.add(self)
        all_sprites.add(self)


class Board(pygame.sprite.Sprite):
    def __init__(self, width):
        super().__init__(tiles_group, all_sprites)
        self.pazmer = width
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.rects = []

    def render(self, screen, razm):
        # global x_pos
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10 + razm * 30, 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10 + razm * 30],
                         [10 + razm * 30, 10 + razm * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10, ((razm // 2) - 1) * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, (razm // 2) * 30 + 10],
                         [10, 10 + razm * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + razm * 30, (razm // 2) * 30 + 10],
                         [10 + razm * 30, 10 + razm * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + razm * 30, 10],
                         [10 + razm * 30, ((razm // 2) - 1) * 30 + 10], width=3)

        for i in range(0, razm):
            for j in range(0, razm):
                if BOARD[i][j] == "0":

                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (10 + 30 * j, 10 + 30 * i, 30, 30))
                else:
                    Wall(10 + 30 * j, 10 + 30 * i)

    def money(self, screen, pazmer):
        for i in range(0, pazmer):
            for j in range(0, pazmer):
                if sp_mone[i][j] == "1":
                    pygame.draw.circle(screen, pygame.Color(255, 215, 0), (10 + 30 * j + 15, 15 + 10 + 30 * i), 3)

    def eat_money(self, x, y):
        global count_money
        x1 = (x - 10) // 30
        y1 = (y - 10) // 30
        if sp_mone[int(y1)][int(x1)] == "1":
            sp_mone[int(y1)][int(x1)] = "0"
            count_money += 1

    def checker(self, x, y, boardd):
        one = (x - 10) // 30
        sec = (y - 10) // 30
        return boardd[int(sec)][int(one)]

    def all_money(self):
        flag = True
        for i in sp_mone:
            for j in i:
                if j == "1":
                    flag = False
                    break
        return flag


class Character(pygame.sprite.Sprite):
    def __init__(self, file, lev):
        super().__init__(player_group, all_sprites)
        self.change_x = 0
        self.change_y = 0
        self.image = tile_images[file]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_pos_level[file][lev - 1]
        all_sprites.add(self)
        player_group.add(self)

    def moving(self, pazmer, destinations, boarddd, speed):
        speed = 3
        if destinations == "r":
            self.rect.x += speed
            if self.rect.x >= (pazmer * 30) - 15:
                self.rect.x -= speed
            if self.rect.x + 10 >= pazmer * 30 + 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (
                    pazmer // 2) * 30 + 10:
                self.rect.x = 10
            else:
                for i in walls_group:
                    if self.update(i):
                        self.rect.x -= speed
        elif destinations == "l":
            self.rect.x -= speed
            if self.rect.x <= 10:
                self.rect.x += speed
            if self.rect.x - 10 <= 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (pazmer // 2) * 30 + 10:
                self.rect.x = pazmer * 30
            else:
                for i in walls_group:
                    if self.update(i):
                        self.rect.x += speed

        elif destinations == "u":
            self.rect.y -= speed
            if self.rect.y <= 10:
                self.rect.y += speed
            else:
                for i in walls_group:
                    if self.update(i):
                        self.rect.y += speed
        elif destinations == "d":
            self.rect.y += speed
            if self.rect.y >= (pazmer * 30) - 15:
                self.rect.y -= speed
            else:
                for i in walls_group:
                    if self.update(i):
                        self.rect.y -= speed

    def previous_direction(self):
        self.pre_x = self.change_x
        self.pre_y = self.change_y

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self, walls):
        if pygame.sprite.collide_mask(self, walls):
            return True
        return False


class Pacman(Character):
    def __init__(self, lev):
        super().__init__('pac', lev)
        self.mask = pygame.mask.from_surface(self.image)

    def moving(self, pazmer, destinations, boarddd, speed):
        Character.moving(self, pazmer, destinations, boarddd, speed)
        Board.eat_money(self, self.rect.x, self.rect.y)

    def died(self, pac, ghos):
        if pygame.sprite.collide_mask(pac, ghos):
            return True
        return False


class Ghost(Character):
    def __init__(self, lev):
        super().__init__('ghost_r', lev)
        self.mask = pygame.mask.from_surface(self.image)


if __name__ == '__main__':
    sl_map = {
        1: "map1.map",
        2: "map2.map",
        3: "map3.map"}
    tile_images = {
        'pac': load_image('pacman.png'),
        'ghost_r': load_image('red_ghost.png'),
        'ghost_c': load_image('ghost1.png'),
        'ghost_o': load_image('orange_ghost.png'),
        'ghost_p': load_image('pink_ghost.png'),
        'wal': load_image('wall.png')}
    # 'money': load_imaghe('ghost1.png')
    start_pos_level = {
        'pac': [(8 * 30 + 10, 10 * 30 + 10), (10 * 30 + 10, 12 * 30 + 10), (12 * 30 + 10, 12 * 30 + 10)],
        'ghost_r': [(8 * 30 + 10, 7 * 30 + 10), (10 * 30 + 10, 9 * 30 + 10), (11 * 30 + 10, 9 * 30 + 10)]
    }
    sl_level = {1: 100, 2 : 170, 3: 200}
    tile_width = tile_height = 50
    player = None
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    pygame.init()
    razmer1 = len(load_level(sl_map[1]))
    x_pos = 30 * (razmer1 // 2) + 10
    y_pos = 30 * (razmer1 // 2 + 2) + 10
    lev_bool = True
    level = 1
    while level <= 3:
        smert = False
        BOARD = load_level(sl_map[level])
        sp_mone = []
        for i in BOARD:
            s = []
            for j in i[0:-1]:
                if j == "0":
                    s.append("1")
                else:
                    s.append("0")
            sp_mone.append(s)
        count_money = 0
        razmer_screen = len(BOARD)
        intro_text = ["Pacman", "",
                      "Уровень " + str(level),
                      "Ваша цель: собрать " + str(sl_level[level]) + " монеты,",
                      "при этом не столкнувшись с приведениями"]
        start_end_screen(level, intro_text, 900, 600, 'fon1.jpg')
        pygame.display.set_caption('Pacman')
        size = width, height = razmer_screen * 30 + 20, razmer_screen * 30 + 20
        screen = pygame.display.set_mode(size)
        board = Board(razmer_screen)
        Board.render(Board, screen, razmer_screen)
        running = True
        press = "r"
        pacmen = Pacman(level)
        ghost = Ghost(level)
        a = random.choice(["u", "l", "r", "d"])
        q = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    k = event.pos
                    print(k)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        press = "l"
                    if event.key == pygame.K_RIGHT:
                        press = "r"
                    if event.key == pygame.K_UP:
                        press = "u"
                    if event.key == pygame.K_DOWN:
                        press = "d"
                pacmen.previous_direction()
            screen.fill((0, 0, 0))
            Board.render(Board, screen, razmer_screen)
            board.money(screen, razmer_screen)
            player_group.draw(screen)
            walls_group.draw(screen)
            pacmen.moving(razmer_screen, press, BOARD, 3)
            if q % 10 == 0:
                a = random.choice(["u", "l", "r", "d"])
            ghost.moving(razmer_screen, a, BOARD, 3)
            pc, gh = player_group
            if pacmen.died(pc, gh):
                running = False
                intro_text = ["Pacman",
                              "Вы проиграли!"]
                start_end_screen(level, intro_text, 800, 500, 'end.jpg')
                continue
            pygame.display.flip()
            q += 1
            if count_money >= sl_level[level]:  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                level += 1
                running = False
                intro_text = ["Pacman",
                              "Вы выиграли!"]
                start_end_screen(level, intro_text, 800, 500, 'end.jpg')
                continue
        all_sprites.remove(pacmen)
        player_group.remove(pacmen)
        all_sprites.remove(ghost)
        player_group.remove(ghost)
        all_sprites.remove(ghost)
        for i in walls_group:
            walls_group.remove(i)

    intro_text = ["Вы прошли игру!"]  # !!!!!!!!!111
    start_end_screen(level, intro_text, 800, 500, 'end.jpg')
