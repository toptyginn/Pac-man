import pygame
import sys
import os
import random

import Money
import Wall
import Character

# Groups
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()


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
        # clock.tick(FPS)


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
                    Wall.Wall(10 + 30 * j, 10 + 30 * i, 30, 30, Wall.BLUE).draw(screen)

    def money(self, screen, pazmer):
        for i in range(0, pazmer):
            for j in range(0, pazmer):
                if sp_mone[i][j] == "1":
                    Money.Money(3, 2, 10 + 30 * j + 12, 12 + 10 + 30 * i)

    def all_money(self):
        flag = True
        for i in sp_mone:
            for j in i:
                if j == "1":
                    flag = False
                    break
        return flag


#Ma
sl_map = {
        1: "map1.map",
        2: "map2.map",
        3: "map3.map"}
tile_images = {
    'pac': load_image('pacman.png'),
    'ghost_r': load_image('red_ghost.png'),
    'ghost_c': load_image('cyan_ghost.png'),
    'ghost_o': load_image('orange_ghost.png'),
    'ghost_p': load_image('pink_ghost.png'),
    'money': load_image('coin.png')}
start_pos_level = {
    'pac': [(8 * 30 + 10, 10 * 30 + 10), (10 * 30 + 10, 12 * 30 + 10), (12 * 30 + 10, 12 * 30 + 10)],
    'ghost_r': [(7 * 30 + 10, 8 * 30 + 10), (200, 200), (7 * 30 + 10, 8 * 30 + 10)]
    }

if __name__ == '__main__':
    tile_width = tile_height = 50
    player = None
    pygame.init()
    razmer1 = len(load_level(sl_map[1]))
    x_pos = 30 * (razmer1 // 2) + 10
    y_pos = 30 * (razmer1 // 2 + 2) + 10


    for level in [1, 2, 3]:
        BOARD = load_level(sl_map[level])

        # print(BOARD)
        sp_mone = []
        for i in BOARD:
            s = []
            for j in i[0:-1]:
                if j == "0":
                    s.append("1")
                else:
                    s.append("0")
            sp_mone.append(s)
        # for i in sp_mone:
        #    print(i)
        razmer_screen = len(BOARD)
        intro_text = ["Pacman", "",
                      "Уровень " + str(level),
                      "Ваша цель: собрать все монеты,",
                      "при этом не столкнувшись с приведениями"]
        start_end_screen(level, intro_text, 900, 600, 'fon1.jpg')
        pygame.display.set_caption('Pacman')
        size = width, height = razmer_screen * 30 + 20, razmer_screen * 30 + 20
        screen = pygame.display.set_mode(size)
        board = Board(razmer_screen)
        board.render(screen, razmer_screen)
        running = True
        press = "r"
        pacmen = Character.Pacman(1, level)
        ghost = Character.Pacman(0.5, level)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print(sp_mone)
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    k = event.pos
                    print(k)
                    # print(board.checker(k[0], k[1]))
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

                if board.all_money():
                    intro_text = ["Pacman",
                                  "Вы выиграли!"]
                    start_end_screen(level, intro_text, 800, 500, 'end.jpg')
                    running = False

            for i in money_group:
                i.update()

            screen.fill((0, 0, 0))
            board.render(screen, razmer_screen)
            board.money(screen, razmer_screen)
            Character.player_group.draw(screen)
            Character.ghost_group.draw(screen)
            walls_group.draw(screen)
            if level == 2:
                pass
            # print(razmer_screen, "razmer_screen")
            pacmen.moving(razmer_screen, press, BOARD, level)
            a = random.choice(["u", "l", "r", "d"])
            # print(a)
            ghost.moving(razmer_screen, random.choice(["r", "l", "u", "l"]), BOARD, level)
            pygame.display.flip()
        all_sprites.remove(pacmen)
        Character.player_group.remove(pacmen)

        all_sprites.remove(ghost)
        Character.ghost_group.remove(ghost)

        for i in walls_group:
            walls_group.remove(i)

    intro_text = ["Вы прошли игру!"]  # !!!!!!!!!111
    start_end_screen(level, intro_text, 800, 500, 'end.jpg')
