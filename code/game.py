import os
import sys

import pygame

from colors import COLORS

CELL_NUMBER = 20
RESOURCES_PATH = (
    "resources"
    if os.path.basename(os.getcwd()) == "Snake-Game-GUI-Python"
    else os.pardir + os.path.sep + "resources"
)


def init_game():
    is_error = pygame.init()

    if is_error[1]:
        print(f"Error {is_error[1]}")
        sys.exit()

    print("Pygame initialized successfully.")


def init_logo():
    logo = pygame.image.load(os.path.join(RESOURCES_PATH, "images", "game_logo.png"))
    pygame.display.set_icon(logo)


class Game:
    # Protected variables
    _cell_width, _cell_height = 30, 30
    _screen = pygame.display.set_mode(
        (_cell_width * CELL_NUMBER, _cell_height * (CELL_NUMBER + 1))
    )

    _fps = 60
    _clock = pygame.time.Clock()

    _font_type = os.path.join(RESOURCES_PATH, "font", "Bubblegum.ttf")
    _score = 0

    @classmethod
    def get_cell_width(cls):
        return Game._cell_width

    @classmethod
    def get_cell_height(cls):
        return Game._cell_height

    @classmethod
    def get_cell_size(cls):
        return (Game._cell_width, Game._cell_height)

    # Protected method
    def _increase_score_by(self, increment):
        Game._score += increment

    # Protected method
    def _reset_score(self):
        Game._score = 0

    def run(self):
        self._draw_game_elements()
        pygame.display.update()

        Game._clock.tick(Game._fps)

    def _quit_game(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    # Protected method
    def _draw_game_elements(self):
        self.__draw_screen()

    def __draw_screen(self):
        Game._screen.fill(COLORS["LIGHT GREEN"])

        for y in range(CELL_NUMBER + 1):
            for x in range(CELL_NUMBER):
                if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
                    grass_rect_x = Game._cell_width * x
                    grass_rect_y = Game._cell_height * y

                    grass_rect = pygame.Rect(
                        grass_rect_x, grass_rect_y, Game._cell_width, Game._cell_height
                    )
                    pygame.draw.rect(Game._screen, COLORS["DARK GREEN"], grass_rect)

    def _draw_text(
        self,
        text,
        font_size,
        text_pos,
        background_pos,
        background_size,
        background_color,
        border_radius,
    ):
        text_font = pygame.font.Font(Game._font_type, font_size)
        text_surface = text_font.render(text, True, COLORS["WHITE"])
        text_rect = text_surface.get_rect(
            center=(
                Game._cell_width * text_pos.x,
                Game._cell_height * text_pos.y,
            )
        )

        background = pygame.Rect(
            (
                background_pos.x * Game._cell_width,
                background_pos.y * Game._cell_height,
            ),
            background_size,
        )

        pygame.draw.rect(
            Game._screen, background_color, background, border_radius=border_radius
        )
        Game._screen.blit(text_surface, text_rect)
