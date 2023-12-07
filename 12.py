import pygame
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = ["0" * 8 + "1" + "0" * 8, "01101110101110110", "0" * 17, "01101011111010110",
                      "00001000100010000", "11101110101110111", "11101000000010111",
                      "0" * 17, "11101000000010111", "11101000000010111", "00001011111010000", "01100000100000110",
                      "00101110101110100", "10100000000000101", "00001001110010000", "01111100100111110", "0" * 17]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.rects = []

    def render(self, screen):
        global x_pos
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
                if self.board[i][j] == "0":
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






        """for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 255:

                    pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (self.cell_size * j + self.left, self.cell_size * i + self.top, self.cell_size,
                                                                      self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                     (self.cell_size * j + self.left, self.cell_size * i + self.top, self.cell_size,
                                      self.cell_size), 1)"""

    def checker(self, x, y):
        one = (x - self.top) // self.cell_size
        sec = (y - self.left) // self.cell_size
        return self.board[int(sec)][int(one)]
"""        if one < self.width and sec < self.height and x > self.left and y > self.top:
            for i in range(self.height):
                for j in range(self.width):
                    xx = self.cell_size * j + self.left
                    yy = self.cell_size * i + self.top
                    if j == one and i == sec:
                        self.board[i][j] = 255 - self.board[i][j]"""
class Character:
    def __init__(self, file, speed):
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
        #if x_pos > 20 and x_pos < 17 * 30 and y_pos > 20 and y_pos < 17 * 30:
        #    flag = True
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 10)
        #else:
        #    flag = False



class Ghost(Character):
    def __init__(self, file, speed):
        super().__init__(file, speed)


class Pacman(Character):
    def __init__(self, file, speed):
        super().__init__(file, speed)

    def moving(self, destinations):
        global x_pos
        global y_pos
        if destinations == "r" and x_pos < 17 * 30 and board.checker(x_pos + 0.25, y_pos) == "0":
            x_pos += 0.25
        elif destinations == "l" and x_pos > 20 and board.checker(x_pos - 0.25, y_pos) == "0":
            x_pos -= 0.25
        elif destinations == "u" and y_pos > 20 and board.checker(x_pos, y_pos - 0.25) == "0":
            y_pos -= 0.25
        elif destinations == "d" and y_pos < 17 * 30 and board.checker(x_pos, y_pos + 0.25) == "0":
            y_pos += 0.25

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 530, 530
    screen = pygame.display.set_mode(size)
    board = Board(17, 17)
    running = True
    x_pos = 300
    y_pos = 300
    pacmen = Pacman("хз", 2)
    press = "r"
    flag = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = event.pos
                print(k)
                board.checker(k[0], k[1])
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    press = "l"
                if event.key == pygame.K_RIGHT:
                    press = "r"
                if event.key == pygame.K_UP:
                    press = "u"
                if event.key == pygame.K_DOWN:
                    press = "d"
        pacmen.moving(press)


        screen.fill((0, 0, 0))
        board.render(screen)
        pacmen.draw(screen, x_pos, y_pos)
        pygame.display.flip()