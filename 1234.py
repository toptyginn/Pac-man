import pygame
import sys
import os

def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):
    #print('data', name)
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
        # self.image = tile_images[tile_type]
        # self.rect = self.image.get_rect().move(
        #    tile_width * pos_x, tile_height * pos_y)
        self.pazmer = width
        # self.height = height

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.rects = []

    def render(self, screen):
        # global x_pos
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10 + self.pazmer * 30, 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10 + self.pazmer * 30],
                         [10 + self.pazmer * 30, 10 + self.pazmer * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, 10],
                         [10, ((self.pazmer // 2) - 1) * 30 + 10], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10, (self.pazmer // 2) * 30 + 10],
                         [10, 10 + self.pazmer * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + self.pazmer * 30, (self.pazmer // 2) * 30 + 10],
                         [10 + self.pazmer * 30, 10 + self.pazmer * 30], width=3)
        pygame.draw.line(screen, pygame.Color(0, 0, 255), [10 + self.pazmer * 30, 10],
                         [10 + self.pazmer * 30, ((self.pazmer // 2) - 1) * 30 + 10], width=3)
        for i in range(0, self.pazmer):
            for j in range(0, self.pazmer):
                if BOARD[i][j] == "0":
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (10 + 30 * j, 10 + 30 * i, 30, 30))
                else:
                    pygame.draw.rect(screen, pygame.Color(0, 0, 255), (10 + 30 * j, 10 + 30 * i, 30, 30))


    def money(self, screen):
        for i in range(0, self.pazmer):
            for j in range(0, self.pazmer):
                if sp_mone[i][j] == "1":
                    pygame.draw.circle(screen, pygame.Color(255, 215, 0), (10 + 30 * j + 15, 15 + 10 + 30 * i), 3)

    def eat_money(self, x, y):
        x1 = (x - 10) // 30
        y1 = (y - 10) // 30
        if sp_mone[int(y1)][int(x1)] == "1":  # !!!!!!!!!!!!!!!!!!!1
            sp_mone[int(y1)][int(x1)] = "0"

    def checker(self, x, y, boardd):
        one = (x - 10) // 30
        sec = (y - 10) // 30
        #print(len(boardd), one, sec, x, y, "'ccchhchhcc")

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
    def __init__(self, file, speed):
        super().__init__(player_group, all_sprites)

        self.file = file
        #self.speed = speed

    def moving(self, destination):
        pass

    def death(self):
        pass

    def get_pos(self):
        x, y = (0, 0)
        return (x, y)



class Ghost(pygame.sprite.Sprite):
    def __init__(self, file, speed):
        super().__init__(player_group, all_sprites)
        self.image = tile_images[file]
        self.rect = self.image.get_rect()
        all_sprites.add(self)
        player_group.add(self)


class Pacman(pygame.sprite.Sprite):
    def __init__(self, file, speed, x, y):
        super().__init__(player_group, all_sprites)
        self.image = tile_images[file]
        self.rect = self.image.get_rect()
        all_sprites.add(self)
        player_group.add(self)
        self.rect.x = x
        self.rect.y = y

    def moving(self, speed_pac, pazmer, destinations, boarddd):
        if destinations == "r":
            if self.rect.x + 10 >= pazmer * 30 + 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (pazmer // 2) * 30 + 10:
                self.rect.x = 10
            else:
                if self.rect.x < pazmer * 30 and board.checker(self.rect.x + 10, self.rect.y, boarddd) == "0":
                    self.rect.x += speed_pac
                else:
                    pass  #print(self.rect.x, pazmer, board.checker(self.rect.x + 10, self.rect.y, boarddd))
        elif destinations == "l":

            if self.rect.x - 10 <= 10 and (pazmer // 2 - 1) * 30 + 10 < self.rect.y < (pazmer // 2) * 30 + 10:
                self.rect.x = pazmer * 30
            else:
                if self.rect.x > 10 and board.checker(self.rect.x - 10, self.rect.y, boarddd) == "0":
                    self.rect.x -= speed_pac
        elif destinations == "u" and self.rect.y > 10 and board.checker(self.rect.x, self.rect.y - 10, boarddd) == "0":
            self.rect.y -= speed_pac
        elif (destinations == "d" and self.rect.y < pazmer * 30 and
              board.checker(self.rect.x, self.rect.y + 10, boarddd) == "0"):
            self.rect.y += speed_pac
        Board.eat_money(self, self.rect.x, self.rect.y)


if __name__ == '__main__':
    sl_map = {
        1: "map1.map",
        2: "map2.map"}
    tile_images = {
        'pac': load_image('pac.png'),
        'ghost': load_image('ghost1.png')}
    # 'money': load_imaghe('ghost1.png')
    tile_width = tile_height = 50
    player = None
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    pygame.init()
    razmer1 = len(load_level(sl_map[1]))
    #print(razmer1, "razmer1")
    x_pos = 30 * (razmer1 // 2) + 10
    y_pos = 30 * (razmer1 // 2 + 2) + 10
    #print(x_pos, y_pos)
    pacmen = Pacman("pac", 1, x_pos, y_pos)

    for level in [1, 2]:
        BOARD = load_level(sl_map[level])
        #print(BOARD)
        sp_mone = []
        for i in BOARD:
            s = []
            for j in i:
                if j == "0":
                    s.append("1")
                else:
                    s.append("0")
            sp_mone.append(s)
        #print(len(BOARD))
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
        running = True
        press = "r"


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    k = event.pos
                    print(k)
                    #print(board.checker(k[0], k[1]))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        press = "l"
                    if event.key == pygame.K_RIGHT:
                        press = "r"
                    if event.key == pygame.K_UP:
                        press = "u"
                    if event.key == pygame.K_DOWN:
                        press = "d"
                if board.all_money():
                    intro_text = ["Pacman", "",
                                  "Вы выиграли!"]
                    start_end_screen(level, intro_text, 800, 500, 'end.jpg')
                    running = False

            screen.fill((0, 0, 0))
            board.render(screen)
            board.money(screen)
            player_group.draw(screen)
            if level == 2:
                pass
            #print(razmer_screen, "razmer_screen")
            pacmen.moving(1, razmer_screen, press, BOARD)
            pygame.display.flip()
    intro_text = ["Вы прошли игру!"] #!!!!!!!!!111
    start_end_screen(level, intro_text, 800, 500, 'end.jpg')