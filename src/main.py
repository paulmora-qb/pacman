import pygame
from colors import BLACK, BLUE, MAGENTA, WHITE, YELLOW
from board import boards
from typing import List
import math

pygame.init()

board_width = 900
board_height = 950
SMALL_DOT_RADIUS = 4
BIG_DOT_RADIUS = 10
WALL_WIDTH = 3
screen = pygame.display.set_mode([board_width, board_height])

timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font("freesansbold.ttf", 20)
level = boards


def draw_board(level: List[int]):
    block_height = (board_height - 50) // 32
    block_width = (board_width) // 30
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(
                    surface=screen,
                    color=YELLOW,
                    center=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + (0.5 * block_height),
                    ),
                    radius=SMALL_DOT_RADIUS,
                )
            elif level[i][j] == 2:
                pygame.draw.circle(
                    surface=screen,
                    color=YELLOW,
                    center=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + (0.5 * block_height),
                    ),
                    radius=BIG_DOT_RADIUS,
                )
            elif level[i][j] == 3:
                pygame.draw.line(
                    surface=screen,
                    color=BLUE,
                    start_pos=(j * block_width + (0.5 * block_width), i * block_height),
                    end_pos=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + block_height,
                    ),
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 4:
                pygame.draw.line(
                    surface=screen,
                    color=BLUE,
                    start_pos=(
                        j * block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    end_pos=(
                        j * block_width + block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 5:
                pygame.draw.arc(
                    surface=screen,
                    color=BLUE,
                    rect=[
                        j * block_width - 0.5 * block_width,
                        i * block_height + 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=0,
                    stop_angle=math.pi / 2,
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 6:
                pygame.draw.arc(
                    surface=screen,
                    color=BLUE,
                    rect=[
                        j * block_width + 0.5 * block_width,
                        i * block_height + 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=math.pi / 2,
                    stop_angle=math.pi,
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 7:
                pygame.draw.arc(
                    surface=screen,
                    color=BLUE,
                    rect=[
                        j * block_width + 0.5 * block_width,
                        i * block_height - 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=math.pi,
                    stop_angle=3 * math.pi / 2,
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 8:
                pygame.draw.arc(
                    surface=screen,
                    color=BLUE,
                    rect=[
                        j * block_width - 0.5 * block_width,
                        i * block_height - 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=1.5 * math.pi,
                    stop_angle=2 * math.pi,
                    width=WALL_WIDTH,
                )
            elif level[i][j] == 9:
                pygame.draw.line(
                    surface=screen,
                    color=WHITE,
                    start_pos=(
                        j * block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    end_pos=(
                        j * block_width + block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    width=WALL_WIDTH,
                )


run = True
while run:
    timer.tick(fps)
    screen.fill(BLACK)

    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
