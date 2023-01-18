"""Characters in the game"""

import pygame


def draw_player(screen, params):

    player_height = params.get("player_height")
    player_width = params.get("player_width")
    unscaled_player_image = pygame.image.load(f"../images/images.jpg")
    player_image = pygame.transform.scale(
        unscaled_player_image, size=(player_height, player_width)
    )  # TODO: Get a better image for the job

    position_x = 450  # TODO: Make this variable
    position_y = 663  # TODO: Make this variable

    direction = 0
    counter = 0

    # Right
    if direction == 0:
        screen.blit(player_image, (position_x, position_y))
    elif direction == 1:
        player_image = pygame.transform.flip(player_image, flip_x=True, flip_y=False)
        screen.blit(player_image, (position_x, position_y))
    elif direction == 2:
        player_image = pygame.transform.rotate(player_image[counter // 2], angle=90)
        screen.blit(player_image, (position_x, position_y))
    elif direction == 3:
        player_image = pygame.transform.rotate(player_image[counter // 2], angle=-90)
        screen.blit(player_image, (position_x, position_y))
