import os
import random

import pygame

from game import RESOURCES_PATH, Game


class Apple:
    def __init__(self, free_cells):
        self.__block_position = random.choice(free_cells)

        self.__apple_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'apple.png')).convert_alpha()
        self.__apple_img = pygame.transform.scale(
            self.__apple_img, Game.get_cell_size())

    @property
    def get_block_position(self):
        return self.__block_position

    def pick_new_position(self, free_cells):
        self.__block_position = random.choice(free_cells)

    def draw(self, screen):
        apple_rect_x = self.__block_position.get_x * Game.get_cell_width()
        apple_rect_y = self.__block_position.get_y * Game.get_cell_height()

        apple_rect = pygame.Rect(
            (apple_rect_x, apple_rect_y), Game.get_cell_size())

        screen.blit(self.__apple_img, apple_rect)
