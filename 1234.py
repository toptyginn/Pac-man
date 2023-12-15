import pygame
import sys
import os


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):
    print('data', name)
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen():
    intro_text = ["Pacman", "",
                  "Уровень первый",
                  "Ваша цель: собрать все монеты,",
                  "при этом не столкнувшись с приведениями"]
    WIDTH = 900
    HEIGHT = 600
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    # screen.fill((0, 0, 0))

    fon = pygame.transform.scale(load_image('fon1.jpg'), (WIDTH, HEIGHT))
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

    # font = pygame.font.Font(None, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        # clock.tick(FPS)


BOARD = load_level("map2.map")
tile_images = {
    'pac': load_image('pac.png'),
    'ghost': load_image('ghost1.png')}
# 'money': load_imaghe('ghost1.png')

tile_width = tile_height = 50
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

MONE = []
for i in BOARD:
    s = []
    for j in i:
        if j == "0":
            s.append("1")
        else:
            s.append("0")
    MONE.append(s)


class Board(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(tiles_group, all_sprites)
        # self.image = tile_images[tile_type]
        # self.rect = self.image.get_rect().move(
        #    tile_width * pos_x, tile_height * pos_y)
        self.width = width
        self.height = height

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.rects = []

    def render(self, screen):
        #global x_pos
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10 + 17 * 30, 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10 + 17 * 30],
                         [10 + 17 * 30, 10 + 17 * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10, 7 * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 8 * 30 + 10],
                         [10, 10 + 17 * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 17 * 30, 8 * 30 + 10],
                         [10 + 17 * 30, 10 + 17 * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 17 * 30, 10],
                         [10 + 17 * 30, 7 * 30 + 10], width=3)
        for i in range(0, 17):
            for j in range(0, 17):
                if BOARD[i][j] == "0":
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (10 + 30 * j, 10 + 30 * i, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.Color(0, 0, 255), (10 + 30 * j, 10 + 30 * i, 30, 30))

        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 6 * 30, 10 + 7 * 30],
                         [10 + 8 * 30, 7 * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 9 * 30, 10 + 7 * 30],
                         [10 + 11 * 30, 7 * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 6 * 30, 10 + 7 * 30],
                         [10 + 6 * 30, 9 * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 6 * 30, 10 + 9 * 30],
                         [10 + 11 * 30, 9 * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + 11 * 30, 10 + 7 * 30],
                         [10 + 11 * 30, 9 * 30 + 10], width=3)

    def money(self, screen):
        for i in range(0, 17):
            for j in range(0, 17):
                if MONE[i][j] == "1":
                    pygame.draw.circle(screen, pygame.Color(255, 215, 0), (10 + 30 * j + 15, 15 + 10 + 30 * i), 3)

    def eat_money(self, x, y):
        x1 = (x - 10) // 30
        y1 = (y - 10) // 30
        if MONE[int(y1)][int(x1)] == "1":      #!!!!!!!!!!!!!!!!!!!1
            MONE[int(y1)][int(x1)] = "0"

    def checker(self, x, y):
        one = (x - 10) // 30
        sec = (y - 10) // 30
        return BOARD[int(sec)][int(one)]


class Character(pygame.sprite.Sprite):
    def __init__(self, file, speed):
        super().__init__(player_group, all_sprites)

        self.file = file
        self.speed = speed

    def moving(self, destination):
        pass

    def death(self):
        pass

    def get_pos(self):
        x, y = (0, 0)
        return (x, y)

    def draw(self, screen, x_pos, y_pos):
        global flag
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 10)


class Ghost(Character, pygame.sprite.Sprite):
    def __init__(self, file, speed):
        super().__init__(player_group, all_sprites)
        print(tile_images[file], "prov")
        self.image = tile_images[file]
        self.rect = self.image.get_rect()
        all_sprites.add(self)
        player_group.add(self)


class Pacman(Character, pygame.sprite.Sprite):
    def __init__(self, file, speed):
        super().__init__(player_group, all_sprites)
        print(tile_images[file], "prov")
        self.image = tile_images[file]
        self.rect = self.image.get_rect()
        all_sprites.add(self)
        player_group.add(self)
        self.rect.x = 100
        self.rect.y = 100
        self.speed = speed

    def moving(self, screen, destinations):
        if destinations == "r" and self.rect.x < 17 * 30 and board.checker(self.rect.x + 10, self.rect.x) == "0":

            self.rect.x += self.speed
            Board.eat_money(self, self.rect.x, self.rect.y)
        elif destinations == "l" and self.rect.x > 10 and board.checker(self.rect.x - 10, self.rect.x) == "0":
            self.rect.x -= self.speed
            Board.eat_money(self, self.rect.x, self.rect.y)
        elif destinations == "u" and self.rect.y > 10 and board.checker(self.rect.x, self.rect.y - 10) == "0":
            self.rect.y -= self.speed
            Board.eat_money(self, self.rect.x, self.rect.y)
        elif destinations == "d" and self.rect.y < 17 * 30 and board.checker(self.rect.x, self.rect.y + 10) == "0":
            self.rect.y += self.speed
            Board.eat_money(self, self.rect.x, self.rect.y)

    """def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 10)"""


if __name__ == '__main__':
    start_screen()
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 530, 530
    screen = pygame.display.set_mode(size)
    board = Board(17, 17)
    running = True
    x_pos = 300
    y_pos = 300
    pacmen = Pacman("pac", 0.5)
    press = "r"
    flag = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = event.pos
                print(k)
                print(board.checker(k[0], k[1]))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    press = "l"
                if event.key == pygame.K_RIGHT:
                    press = "r"
                if event.key == pygame.K_UP:
                    press = "u"
                if event.key == pygame.K_DOWN:
                    press = "d"

        screen.fill((0, 0, 0))
        board.render(screen)
        board.money(screen)
        player_group.draw(screen)
        #pacmen.draw(screen, x_pos, y_pos)
        pacmen.moving(screen, press)
        pygame.display.flip()
