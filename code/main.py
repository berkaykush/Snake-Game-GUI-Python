import os
import sys

import pygame

from end_menu import EndMenu
from gameplay import Gameplay
from start_menu import StartMenu


def init_game():
    is_error = pygame.init()

    if is_error[1]:
        print(f'Error {is_error[1]}')
        sys.exit()

    print('Pygame initialized successfully.')


def init_logo():
    logo = pygame.image.load(os.path.join(
        '..', 'resources', 'images', 'game_logo.png'))
    pygame.display.set_icon(logo)


if __name__ == '__main__':
    init_game()
    init_logo()

    start_menu = StartMenu()
    start_menu.run()

    gameplay = Gameplay()
    gameplay.run()

    end_menu = EndMenu()
    while True:
        end_menu.run()
        gameplay.run()
