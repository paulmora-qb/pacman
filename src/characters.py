import pygame
import pygame.gfxdraw
from colors import BLUE, YELLOW
import random
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from board import BOARD_HEIGHT, BOARD_WIDTH

CHARACTER_SIZE = 20


class Ghost(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Ghost, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=(BOARD_HEIGHT / 2, BOARD_WIDTH / 2))

    def update(self):

        direction_number = random.randint(1, 4)

        # Going up
        if direction_number == 1:
            self.rect.move_ip(0, -5)
        # Going Down
        elif direction_number == 2:
            self.rect.move_ip(0, 5)
        # Left
        elif direction_number == 3:
            self.rect.move_ip(-5, 0)
        # Right
        elif direction_number == 4:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > BOARD_WIDTH:
            self.rect.right = BOARD_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= BOARD_HEIGHT:
            self.rect.bottom = BOARD_HEIGHT


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super(Pacman, self).__init__()
        self.surf = pygame.Surface((CHARACTER_SIZE, CHARACTER_SIZE), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.surf, 15, 15, 14, (0, 255, 0))
        pygame.gfxdraw.filled_circle(self.surf, 15, 15, 14, (0, 255, 0))

        self.surf.fill(YELLOW)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > BOARD_WIDTH:
            self.rect.right = BOARD_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= BOARD_HEIGHT:
            self.rect.bottom = BOARD_HEIGHT
