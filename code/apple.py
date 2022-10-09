import os
import random

import pygame

from points import CELL_HEIGHT, CELL_WIDTH


class Apple:
    def __init__(self, free_cells):
        self.__block_position = random.choice(free_cells)

        self.__apple_img = pygame.image.load(os.path.join(
            '..', 'resources', 'images', 'apple.png')).convert_alpha()
        self.__apple_img = pygame.transform.smoothscale(
            self.__apple_img, (CELL_WIDTH, CELL_HEIGHT))

    @property
    def get_block_position(self):
        return self.__block_position

    def pick_new_position(self, free_cells):
        self.__block_position = random.choice(free_cells)

    def draw(self, screen):
        apple_rect_x = self.__block_position.get_x * CELL_WIDTH
        apple_rect_y = self.__block_position.get_y * CELL_HEIGHT

        apple_rect = pygame.Rect(
            apple_rect_x, apple_rect_y, CELL_WIDTH, CELL_HEIGHT)

        screen.blit(self.__apple_img, apple_rect)
