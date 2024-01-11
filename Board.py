import pygame

import Money
import Wall
import main


class Board(pygame.sprite.Sprite):
    def __init__(self, width):
        super().__init__(main.tiles_group, main.all_sprites)
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
                if main.BOARD[i][j] == "0":

                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (10 + 30 * j, 10 + 30 * i, 30, 30))
                else:
                    Wall.Wall(10 + 30 * j, 10 + 30 * i, 30, 30, Wall.BLUE).draw(screen)

    def money(self, screen, pazmer):
        for i in range(0, pazmer):
            for j in range(0, pazmer):
                if main.sp_mone[i][j] == "1":
                    coin = Money.Money(3, 2, 10 + 30 * j + 12, 12 + 10 + 30 * i)
                    screen.blit(coin.image)

    def all_money(self):
        flag = True
        for i in main.sp_mone:
            for j in i:
                if j == "1":
                    flag = False
                    break
        return flag
