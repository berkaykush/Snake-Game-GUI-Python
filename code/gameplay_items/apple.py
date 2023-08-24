import copy
import os
import random

import pygame

from game import RESOURCES_PATH, Game


class Apple:
    def __init__(self, free_cells):
        self.__pos = random.choice(free_cells)

        self.__img = pygame.image.load(
            os.path.join(RESOURCES_PATH, "images", "apple.png")
        ).convert_alpha()

        self.__img = pygame.transform.scale(self.__img, Game.get_cell_size())

    @property
    def pos(self):
        return copy.copy(self.__pos)

    def pick_new_position(self, free_cells):
        self.__pos = random.choice(free_cells)

    def draw(self, screen):
        apple_rect_x = self.__pos.x * Game.get_cell_width()
        apple_rect_y = self.__pos.y * Game.get_cell_height()

        apple_rect = pygame.Rect((apple_rect_x, apple_rect_y), Game.get_cell_size())

        screen.blit(self.__img, apple_rect)
