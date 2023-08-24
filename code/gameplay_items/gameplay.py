import pygame

from colors import COLORS
from game import CELL_NUMBER, Game
from points import Point

from gameplay_items.apple import Apple
from gameplay_items.snake import Snake


class Gameplay(Game):
    def __init__(self):
        # Increase/decrease the game speed.
        pygame.time.set_timer(pygame.USEREVENT, 60)

        self.__snake = Snake()
        self.__apple = Apple(self.__find_free_cells())

    def run(self):
        pygame.display.set_caption("Gameplay")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit_game()

                elif (
                    event.type == pygame.USEREVENT
                    and self.__snake.curr_direction != Point(0, 0)
                ):
                    self.__snake.move()

                    if self.__is_apple_eaten():
                        self._increase_score_by(1)
                        self.__snake.play_crunch_sound()

                        self.__snake.grow()
                        self.__apple.pick_new_position(self.__find_free_cells())

                    if self.__check_game_over():
                        running = False

                elif event.type == pygame.KEYDOWN:
                    arrow_keys = {
                        pygame.K_UP: "UP",
                        pygame.K_LEFT: "LEFT",
                        pygame.K_RIGHT: "RIGHT",
                        pygame.K_DOWN: "DOWN",
                    }

                    if event.key in arrow_keys:
                        direction = arrow_keys[event.key]

                        if not self.__snake.is_opposite_directions(
                            direction
                        ) and not self.__snake.is_quick_switch(direction):
                            self.__snake.change_direction(arrow_keys[event.key])

            super().run()

        self.__snake.reset()

    def __find_free_cells(self):
        free_cells = []

        for y in range(CELL_NUMBER):
            for x in range(CELL_NUMBER):
                snake_cpy = self.__snake.body_pos
                snake_cpy.append(self.__snake.head_pos)

                if not Point(x, y) in snake_cpy:
                    free_cells.append(Point(x, y))

        return free_cells

    def __is_apple_eaten(self):
        return self.__snake.head_pos == self.__apple.pos

    def _draw_game_elements(self):
        super()._draw_game_elements()

        self.__snake.draw_head(self._screen)
        self.__snake.draw_body(self._screen)

        self.__apple.draw(self._screen)

        text = f"Score: {self._score}"
        font_size = min(int(self._cell_width / 1.5), int(self._cell_height / 1.5))
        text_pos = Point(10, 20.5)

        background_pos = Point(0, CELL_NUMBER)
        background_size = (self._cell_width * CELL_NUMBER, self._cell_height)
        background_color = COLORS["DARKER GREEN"]
        border_radius = 0

        self._draw_text(
            text,
            font_size,
            text_pos,
            background_pos,
            background_size,
            background_color,
            border_radius,
        )

    def __check_game_over(self):
        return self.__snake.head_pos in self.__snake.body_pos
