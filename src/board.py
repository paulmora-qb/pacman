"""Function to draw the board"""

import math
from typing import Any, Dict, List

import pygame
from matplotlib import colors

from utils.config_loader import load_config
from utils.helper import create_color_rgb

board_params = load_config("board")


def draw_board(
    screen,
    level: List[int],
    board_params
):

    board_height = board_params.get("board_height")
    board_width = board_params.get("board_width")
    small_dot_radius = board_params.get("small_dot_radius")
    big_dot_radius = board_params.get("big_dot_radius")
    wall_width = board_params.get("wall_width")

    small_dot_color = create_color_rgb(board_params.get("small_dot_color"))
    big_dot_color = create_color_rgb(board_params.get("big_dot_color"))
    wall_color = create_color_rgb(board_params.get("wall_color"))
    ghost_wall_color = create_color_rgb(board_params.get("ghost_wall_color"))

    block_height = (board_height - 50) // 32
    block_width = (board_width) // 30
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(
                    surface=screen,
                    color=small_dot_color,
                    center=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + (0.5 * block_height),
                    ),
                    radius=small_dot_radius,
                )
            elif level[i][j] == 2:
                pygame.draw.circle(
                    surface=screen,
                    color=big_dot_color,
                    center=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + (0.5 * block_height),
                    ),
                    radius=big_dot_radius,
                )
            elif level[i][j] == 3:
                pygame.draw.line(
                    surface=screen,
                    color=wall_color,
                    start_pos=(j * block_width + (0.5 * block_width), i * block_height),
                    end_pos=(
                        j * block_width + (0.5 * block_width),
                        i * block_height + block_height,
                    ),
                    width=wall_width,
                )
            elif level[i][j] == 4:
                pygame.draw.line(
                    surface=screen,
                    color=wall_color,
                    start_pos=(
                        j * block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    end_pos=(
                        j * block_width + block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    width=wall_width,
                )
            elif level[i][j] == 5:
                pygame.draw.arc(
                    surface=screen,
                    color=wall_color,
                    rect=[
                        j * block_width - 0.5 * block_width,
                        i * block_height + 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=0,
                    stop_angle=math.pi / 2,
                    width=wall_width,
                )
            elif level[i][j] == 6:
                pygame.draw.arc(
                    surface=screen,
                    color=wall_color,
                    rect=[
                        j * block_width + 0.5 * block_width,
                        i * block_height + 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=math.pi / 2,
                    stop_angle=math.pi,
                    width=wall_width,
                )
            elif level[i][j] == 7:
                pygame.draw.arc(
                    surface=screen,
                    color=wall_color,
                    rect=[
                        j * block_width + 0.5 * block_width,
                        i * block_height - 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=math.pi,
                    stop_angle=3 / 2 * math.pi,
                    width=wall_width,
                )
            elif level[i][j] == 8:
                pygame.draw.arc(
                    surface=screen,
                    color=wall_color,
                    rect=[
                        j * block_width - 0.5 * block_width,
                        i * block_height - 0.5 * block_height,
                        block_width,
                        block_height,
                    ],
                    start_angle=3 / 2 * math.pi,
                    stop_angle=2 * math.pi,
                    width=wall_width,
                )
            elif level[i][j] == 9:
                pygame.draw.line(
                    surface=screen,
                    color=ghost_wall_color,
                    start_pos=(
                        j * block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    end_pos=(
                        j * block_width + block_width,
                        i * block_height + (0.5 * block_height),
                    ),
                    width=wall_width,
                )
