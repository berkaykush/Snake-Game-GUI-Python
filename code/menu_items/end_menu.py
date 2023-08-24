from colors import COLORS
from points import Point

from menu_items.menu import Menu

class EndMenu(Menu):
    def __init__(self):
        super().__init__()
        self._init_title()

        self._buttons.append(self._init_button("Retry", Point(5, 11)))
        self._buttons.append(self._init_button("Quit", Point(5, 15)))

    # Override
    def _init_title(self):
        self._title = "End Menu"

    # Override
    def _draw_game_elements(self):
        super()._draw_game_elements()

        text = f"Your score is {self._score}"
        font_size = min(int(self._cell_width), int(self._cell_height))
        text_pos = Point(10, 9)

        background_pos = Point(3, 8)
        background_size = (self._cell_width * 14, self._cell_height * 2)
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
