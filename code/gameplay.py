import pygame

from apple import Apple
from colors import COLORS
from game import Game
from points import CELL_HEIGHT, CELL_NUMBER, CELL_WIDTH, Point
from snake import Snake


class Gameplay(Game):
    def __init__(self):
        pygame.display.set_caption('Gameplay')

        # Increase/decrease the game speed.
        pygame.time.set_timer(pygame.USEREVENT, 50)

        self.__snake = Snake()
        self.__blocks_to_grow = 3

        self.__apple = Apple(self.__find_free_cells())

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit_game()

                elif event.type == pygame.USEREVENT \
                        and self.__snake.get_curr_direction != Point(0, 0):
                    if self.__snake.get_num_blocks_to_grow:
                        self.__snake.grow_by_one_block()

                    self.__snake.move()
                    self.__snake.move_from_one_end_to_the_other_end()

                    if self.__is_apple_eaten():
                        self._increase_score_by(1)
                        self.__apple.pick_new_position(
                            self.__find_free_cells())

                        self.__snake.play_crunch_sound()
                        self.__snake.set_num_blocks_to_grow(
                            self.__blocks_to_grow)

                    if self.__check_game_over():
                        running = False

                elif event.type == pygame.KEYDOWN:
                    arrow_keys = {
                        pygame.K_UP: 'UP',
                        pygame.K_LEFT: 'LEFT',
                        pygame.K_RIGHT: 'RIGHT',
                        pygame.K_DOWN: 'DOWN'
                    }

                    if event.key in arrow_keys:
                        direction = arrow_keys[event.key]

                        if not self.__snake.is_opposite_directions(direction) \
                                and not self.__snake.is_quick_switch(direction):
                            self.__snake.change_direction(
                                arrow_keys[event.key])

            super().run()

        self.__snake.reset()

    def __find_free_cells(self):
        free_cells = []

        for y in range(CELL_NUMBER):
            for x in range(CELL_NUMBER):
                snake_cpy = self.__snake.get_body_block_positions
                snake_cpy.append(self.__snake.get_head_block_position)

                if not Point(x, y) in snake_cpy:
                    free_cells.append(Point(x, y))

        return free_cells

    def __is_apple_eaten(self):
        return self.__snake.get_head_block_position == self.__apple.get_block_position

    def _draw_game_elements(self):
        super()._draw_game_elements()

        self.__snake.draw_head(self._screen)
        self.__snake.draw_body(self._screen)

        self.__apple.draw(self._screen)

        text = f'Score: {self._score}'
        font_size = min(int(CELL_WIDTH / 1.5), int(CELL_HEIGHT / 1.5))
        text_pos = Point(10, 20.5)
        background_pos = Point(0, CELL_NUMBER)
        background_size = (CELL_WIDTH * CELL_NUMBER, CELL_HEIGHT)
        background_color = COLORS['DARKER GREEN']
        border_radius = 0
        self._draw_text(text, font_size, text_pos, background_pos,
                        background_size, background_color, border_radius)

    def __check_game_over(self):
        return self.__snake.get_head_block_position in self.__snake.get_body_block_positions