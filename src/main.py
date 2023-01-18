"""Main file for running the game"""

import pygame

from board import draw_board
from board_layout import boards
from player import draw_player
from utils.config_loader import load_config
from utils.helper import create_color_rgb


def pacman():

    pygame.init()

    # TODO: Find a nicer version of dealing with parameter files
    board_config = load_config("board")
    board_width = board_config.get("board_width")
    board_height = board_config.get("board_height")
    board_background_color = create_color_rgb(board_config.get("background_color"))

    # TODO: Find a nicer version of dealing with parameter files
    player_params = load_config("player")

    screen = pygame.display.set_mode(size=([board_width, board_height]))

    timer = pygame.time.Clock()
    fps = 60

    level = boards

    run = True
    while run:
        timer.tick(fps)
        screen.fill(board_background_color)
        draw_board(screen, level, board_config)
        draw_player(screen, player_params)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    pacman()
