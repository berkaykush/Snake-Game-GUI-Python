import os
import sys

import pygame

from colors import COLORS
from points import CELL_HEIGHT, CELL_NUMBER, CELL_WIDTH


class Game:
    _screen = pygame.display.set_mode(
        (CELL_WIDTH * CELL_NUMBER, CELL_HEIGHT * (CELL_NUMBER + 1)))

    _fps = 60
    _clock = pygame.time.Clock()

    _font_type = os.path.join('..', 'resources', 'font', 'Bubblegum.ttf')
    _score = 0

    def _increase_score_by(self, increment):
        Game._score += increment

    def _reset_score(self):
        Game._score = 0

    def run(self):
        self._draw_game_elements()
        pygame.display.update()

        Game._clock.tick(Game._fps)

    @staticmethod
    def _quit_game():
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def _draw_game_elements(self):
        self.__draw_screen()

    def __draw_screen(self):
        Game._screen.fill(COLORS['LIGHT GREEN'])

        for y in range(CELL_NUMBER + 1):
            for x in range(CELL_NUMBER):
                if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
                    grass_rect_x = CELL_WIDTH * x
                    grass_rect_y = CELL_HEIGHT * y

                    grass_rect = pygame.Rect(
                        grass_rect_x, grass_rect_y, CELL_WIDTH, CELL_HEIGHT)
                    pygame.draw.rect(
                        Game._screen, COLORS['DARK GREEN'], grass_rect)

    def _draw_text(self, text, font_size, text_pos, background_pos, background_size,
                   background_color, border_radius):
        text_font = pygame.font.Font(Game._font_type, font_size)
        text_surface = text_font.render(text, True, COLORS['WHITE'])

        text_rect = text_surface.get_rect(
            center=(CELL_WIDTH * text_pos.get_x, CELL_HEIGHT * text_pos.get_y))
        background = pygame.Rect(
            (background_pos.get_x * CELL_WIDTH, background_pos.get_y * CELL_HEIGHT), background_size)

        pygame.draw.rect(
            Game._screen, background_color, background, border_radius=border_radius)
        Game._screen.blit(text_surface, text_rect)
