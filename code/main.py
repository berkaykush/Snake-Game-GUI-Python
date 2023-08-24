import time

from game import init_game, init_logo

from gameplay_items.gameplay import Gameplay

from menu_items.start_menu import StartMenu
from menu_items.end_menu import EndMenu

if __name__ == "__main__":
    init_game()
    init_logo()

    start_menu = StartMenu()
    start_menu.run()

    gameplay = Gameplay()
    gameplay.run()

    end_menu = EndMenu()

    while True:
        time.sleep(0.4)
        end_menu.run()
        gameplay.run()
