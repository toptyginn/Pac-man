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
        print(one, sec)
        print(self.board[sec][one])
"""        if one < self.width and sec < self.height and x > self.left and y > self.top:
            for i in range(self.height):
                for j in range(self.width):
                    xx = self.cell_size * j + self.left
                    yy = self.cell_size * i + self.top
                    if j == one and i == sec:
                        self.board[i][j] = 255 - self.board[i][j]"""


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 530, 530
    screen = pygame.display.set_mode(size)
    board = Board(17, 17)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = event.pos
                print(k)
                board.checker(k[0], k[1])
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()