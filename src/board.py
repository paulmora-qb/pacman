import pygame

WALL_SIZE = 20
BOARD_HEIGHT = 2000
BOARD_WIDTH = 1000


def draw_board(board_color: str):

    screen = pygame.display.set_mode([BOARD_WIDTH, BOARD_HEIGHT])
    screen.fill(board_color)

    return screen
