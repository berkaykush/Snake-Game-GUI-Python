import copy
import pygame

from colors import COLORS
from game import Game


class Button:
    def __init__(self, font_type, name, position, elevation):
        font_size = min(
            int(Game.get_cell_width() * 1.5), int(Game.get_cell_height() * 1.5)
        )
        text_font = pygame.font.Font(font_type, font_size)

        width = Game.get_cell_width() * 10
        height = Game.get_cell_height() * 3

        self.__name = name
        self.__pos = position
        self.__elevation = elevation

        self.__bottom_rect = pygame.Rect(
            position.x * Game.get_cell_width(),
            position.y * Game.get_cell_height(),
            width,
            self.__elevation,
        )
        self.__bottom_rect_color = COLORS["DARK BLUE"]

        self.__top_rect = pygame.Rect(
            position.x * Game.get_cell_width(),
            self.__pos.y * Game.get_cell_height(),
            width,
            height,
        )
        self.__top_rect_color = COLORS["BLUE"]

        self.__text_surface = text_font.render(name, True, COLORS["WHITE"])
        self.__text_rect = self.__text_surface.get_rect(center=self.__top_rect.center)

    @property
    def top_rect(self):
        return copy.copy(self.__top_rect)

    @property
    def name(self):
        return self.__name

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, new_value):
        self.__elevation = new_value

    def change_color(self, top_rect_color, bottom_rect_color):
        self.__top_rect_color = top_rect_color
        self.__bottom_rect_color = bottom_rect_color

    def draw(self, screen):
        self.__top_rect.y = (self.__pos.y * Game.get_cell_height()) - self.__elevation
        self.__text_rect.center = self.__top_rect.center

        self.__bottom_rect.midtop = self.__top_rect.midtop
        self.__bottom_rect.height = self.__top_rect.height + self.__elevation

        pygame.draw.rect(
            screen, self.__bottom_rect_color, self.__bottom_rect, border_radius=100
        )
        pygame.draw.rect(
            screen, self.__top_rect_color, self.__top_rect, border_radius=100
        )

        screen.blit(self.__text_surface, self.__text_rect)

    def __eq__(self, other):
        return (isinstance(other, Button)) and (self.__name == other.name)
