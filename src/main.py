import pygame
from board import draw_board
from board_layout import boards
from utils.config_loader import load_config


def pacman():

    pygame.init()

    board_config = load_config("board")

    board_width = board_config.get("board_width")
    board_height = board_config.get("board_height")

    screen = pygame.display.set_mode(size=([board_width, board_height]))

    timer = pygame.time.Clock()
    fps = 60

    font = pygame.font.Font("freesansbold.ttf", 20)
    level = boards

    run = True
    while run:
        timer.tick(fps)
        screen.fill((0, 0, 0))
        draw_board(screen, level, board_config)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    pacman()
