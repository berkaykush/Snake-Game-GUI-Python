from points import Point

from menu_items.menu import Menu


class StartMenu(Menu):
    def __init__(self):
        super().__init__()
        self._init_title()

        self._buttons.append(self._init_button("Play", Point(5, 8)))

    def _init_title(self):
        self._title = "Start Menu"
