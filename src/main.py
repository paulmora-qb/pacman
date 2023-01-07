import pygame
import random
from board import draw_board
from colors import BLACK, BLUE
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT
from characters import Pacman, Ghost

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
board_color = BLACK

pygame.init()

screen = draw_board(board_color=board_color)

running = True


# Create a custom event for adding a new enemy

ghost = Ghost(color=BLUE)
player = Pacman()

ghosts = pygame.sprite.Group()
ghosts.add(ghost)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ghost)

# Main loop

while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    ghost.update()

    screen.fill(board_color)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(source=entity.surf, dest=entity.rect)

    if pygame.sprite.spritecollideany(player, ghosts):
        player.kill()
        running = False

    # Show the display
    pygame.display.flip()

pygame.quit()
