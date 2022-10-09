import pygame

from colors import COLORS
from menu import Menu
from points import CELL_HEIGHT, CELL_WIDTH, Point


class EndMenu(Menu):
    def __init__(self):
        super().__init__()
        self._init_title()

        self._buttons.append(self._init_button('Retry', Point(5, 11)))
        self._buttons.append(self._init_button('Quit', Point(5, 15)))

    def _init_title(self):
        self._title = 'End Menu'
        pygame.display.set_caption(self._title)

    def _draw_game_elements(self):
        super()._draw_game_elements()

        text = f'Your score is {self._score}'
        font_size = min(int(CELL_WIDTH), int(CELL_HEIGHT))
        text_pos = Point(10, 9)
        background_pos = Point(3, 8)
        background_size = (CELL_WIDTH * 14, CELL_HEIGHT * 2)
        background_color = COLORS['BLUE']
        border_radius = 100
        self._draw_text(text, font_size, text_pos, background_pos,
                        background_size, background_color, border_radius)