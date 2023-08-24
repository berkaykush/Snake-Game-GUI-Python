import pygame

from colors import COLORS
from game import Game
from points import Point

from menu_items.buttons import Button


class Menu(Game):
    def __init__(self):
        self._buttons = []
        self._title = ""

    def _init_title(self):
        pass

    def _init_button(self, button_name, button_position):
        return Button(self._font_type, button_name, button_position, elevation=10)

    def run(self):
        pygame.display.set_caption(self._title)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit_game()

                elif event.type == pygame.MOUSEMOTION:
                    for button in self._buttons:
                        if button.top_rect.collidepoint(pygame.mouse.get_pos()):
                            button.change_color(
                                top_rect_color=COLORS["RED"],
                                bottom_rect_color=COLORS["DARK RED"],
                            )
                            continue

                        button.change_color(
                            top_rect_color=COLORS["BLUE"],
                            bottom_rect_color=COLORS["DARK BLUE"],
                        )

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.top_rect.collidepoint(pygame.mouse.get_pos()):
                            button.elevation = 0

                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self._buttons:
                        if button.elevation == 0:
                            button.elevation = 10

                            if button.top_rect.collidepoint(pygame.mouse.get_pos()):
                                if button == self._buttons[0]:
                                    button.change_color(
                                        top_rect_color=COLORS["BLUE"],
                                        bottom_rect_color=COLORS["DARK BLUE"],
                                    )

                                    self._reset_score()
                                    running = False

                                elif (
                                    len(self._buttons) > 1
                                    and button == self._buttons[1]
                                ):
                                    self._quit_game()

            super().run()

    def _draw_game_elements(self):
        super()._draw_game_elements()

        text = self._title
        font_size = min(int(self._cell_width * 2), int(self._cell_height * 2))
        text_pos = Point(10, 5)

        background_pos = Point(3, 3)
        background_size = (self._cell_width * 14, self._cell_height * 4)
        background_color = COLORS["BLUE"]
        border_radius = 100

        self._draw_text(
            text,
            font_size,
            text_pos,
            background_pos,
            background_size,
            background_color,
            border_radius,
        )

        for button in self._buttons:
            button.draw(self._screen)
