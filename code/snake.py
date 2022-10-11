import os

import pygame

from game import CELL_NUMBER, RESOURCES_PATH, Game
from points import Point

SNAKE_DIRECTIONS = {
    'UP': Point(0, -1),
    'LEFT': Point(-1, 0),
    'RIGHT': Point(1, 0),
    'DOWN': Point(0, 1)
}


class Snake:
    def __init__(self):
        self.__head_block_position = Point(3, 3)
        self.__body_block_positions = [Point(1, 3), Point(2, 3)]

        self.__init_head_img()
        self.__curr_head_img = self.__head_right_img

        self.__init_tail_img()
        self.__curr_tail_img = self.__tail_left_img

        self.__init_body_block_img()
        self.__curr_body_block_img = self.__body_horizontal_img

        self.__crunch_sound = pygame.mixer.Sound(
            os.path.join(RESOURCES_PATH, 'sound', 'crunch.wav'))

        # Snake does not move until a player presses an arrow key.
        self.__curr_direction = Point(0, 0)
        self.__num_blocks_to_grow = 0

    def __init_head_img(self):
        self.__head_up_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'head_up.png')).convert_alpha()
        self.__head_up_img = pygame.transform.smoothscale(
            self.__head_up_img, Game.get_cell_size())

        self.__head_left_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'head_left.png')).convert_alpha()
        self.__head_left_img = pygame.transform.smoothscale(
            self.__head_left_img, Game.get_cell_size())

        self.__head_right_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'head_right.png')).convert_alpha()
        self.__head_right_img = pygame.transform.smoothscale(
            self.__head_right_img, Game.get_cell_size())

        self.__head_down_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'head_down.png')).convert_alpha()
        self.__head_down_img = pygame.transform.smoothscale(
            self.__head_down_img, Game.get_cell_size())

    def __init_tail_img(self):
        self.__tail_up_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'tail_up.png')).convert_alpha()
        self.__tail_up_img = pygame.transform.smoothscale(
            self.__tail_up_img, Game.get_cell_size())

        self.__tail_left_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'tail_left.png')).convert_alpha()
        self.__tail_left_img = pygame.transform.smoothscale(
            self.__tail_left_img, Game.get_cell_size())

        self.__tail_right_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'tail_right.png')).convert_alpha()
        self.__tail_right_img = pygame.transform.smoothscale(
            self.__tail_right_img, Game.get_cell_size())

        self.__tail_down_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'tail_down.png')).convert_alpha()
        self.__tail_down_img = pygame.transform.smoothscale(
            self.__tail_down_img, Game.get_cell_size())

    def __init_body_block_img(self):
        self.__body_horizontal_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_horizontal.png')).convert_alpha()
        self.__body_horizontal_img = pygame.transform.smoothscale(
            self.__body_horizontal_img, Game.get_cell_size())

        self.__body_vertical_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_vertical.png')).convert_alpha()
        self.__body_vertical_img = pygame.transform.smoothscale(
            self.__body_vertical_img, Game.get_cell_size())

        self.__body_bl_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_bl.png')).convert_alpha()
        self.__body_bl_img = pygame.transform.smoothscale(
            self.__body_bl_img, Game.get_cell_size())

        self.__body_br_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_br.png')).convert_alpha()
        self.__body_br_img = pygame.transform.smoothscale(
            self.__body_br_img, Game.get_cell_size())

        self.__body_tl_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_tl.png')).convert_alpha()
        self.__body_tl_img = pygame.transform.smoothscale(
            self.__body_tl_img, Game.get_cell_size())

        self.__body_tr_img = pygame.image.load(os.path.join(
            RESOURCES_PATH, 'images', 'body_tr.png')).convert_alpha()
        self.__body_tr_img = pygame.transform.smoothscale(
            self.__body_tr_img, Game.get_cell_size())

    @property
    def get_head_block_position(self):
        return self.__head_block_position

    @property
    def get_body_block_positions(self):
        return self.__body_block_positions.copy()

    @property
    def get_curr_direction(self):
        return self.__curr_direction

    @property
    def get_num_blocks_to_grow(self):
        return self.__num_blocks_to_grow

    def set_num_blocks_to_grow(self, num_blocks_to_grow):
        self.__num_blocks_to_grow += num_blocks_to_grow

    def grow_by_one_block(self):
        self.__body_block_positions.insert(
            0, self.__body_block_positions[0] - self.__curr_direction)

        self.__num_blocks_to_grow -= 1

    def reset(self):
        self.__head_block_position = Point(3, 3)
        self.__body_block_positions = [Point(1, 3), Point(2, 3)]

        self.__curr_direction = Point(0, 0)
        self.__num_blocks_to_grow = 0

    def move(self):
        for index, body_block in enumerate(self.__body_block_positions):
            if body_block == self.__body_block_positions[-1]:
                self.__body_block_positions[index] = self.__head_block_position
                continue

            self.__body_block_positions[index] = self.__body_block_positions[index + 1]

        self.__head_block_position += self.__curr_direction

    def move_from_one_end_to_the_other_end(self):
        end_points = {
            Point(CELL_NUMBER, self.__head_block_position.get_y):
                Point(0, self.__head_block_position.get_y),

            Point(-1, self.__head_block_position.get_y):
                Point(CELL_NUMBER - 1, self.__head_block_position.get_y),

            Point(self.__head_block_position.get_x, CELL_NUMBER):
                Point(self.__head_block_position.get_x, 0),

            Point(self.__head_block_position.get_x, -1):
                Point(self.__head_block_position.get_x, CELL_NUMBER - 1)
        }

        if self.__head_block_position in end_points:
            self.__head_block_position = end_points[self.__head_block_position]

    def play_crunch_sound(self):
        self.__crunch_sound.play()

    def is_opposite_directions(self, direction):
        '''
        if direction of the snake and current direction are in the opposite direction of each other,
        then direction of the snake cannot be equal to current direction.
        '''
        return SNAKE_DIRECTIONS[direction] + self.__curr_direction == Point(0, 0)

    def is_quick_switch(self, direction):
        '''
        It should not be possible to crash into yourself by changing
        the direction multiple times before the next step.
        '''
        return self.__head_block_position + SNAKE_DIRECTIONS[direction] \
            == self.__body_block_positions[-1]

    def change_direction(self, direction):
        self.__curr_direction = SNAKE_DIRECTIONS[direction]

    def __check_for_end_point_relations(self, relation):
        return {
            Point(0, CELL_NUMBER - 1): Point(0, -1),
            Point(CELL_NUMBER - 1, 0): Point(-1, 0),
            Point(1 - CELL_NUMBER, 0): Point(1, 0),
            Point(0, 1 - CELL_NUMBER): Point(0, 1)
        }.get(relation, relation)

    def __update_head_graphics(self):
        head_relation = self.__body_block_positions[-1] - \
            self.__head_block_position

        head_relation = self.__check_for_end_point_relations(head_relation)

        self.__curr_head_img = {
            Point(0, 1): self.__head_up_img,
            Point(1, 0): self.__head_left_img,
            Point(-1, 0): self.__head_right_img,
            Point(0, -1): self.__head_down_img
        }.get(head_relation, self.__curr_head_img)

    def __update_tail_graphics(self):
        tail_relation = self.__body_block_positions[1] - \
            self.__body_block_positions[0]

        tail_relation = self.__check_for_end_point_relations(tail_relation)

        self.__curr_tail_img = {
            Point(0, 1): self.__tail_up_img,
            Point(1, 0): self.__tail_left_img,
            Point(-1, 0): self.__tail_right_img,
            Point(0, -1): self.__tail_down_img
        }.get(tail_relation, self.__curr_tail_img)

    def __update_body_graphics(self, body_block_relation_1, body_block_relation_2):
        body_block_relation_1 = self.__check_for_end_point_relations(
            body_block_relation_1)
        body_block_relation_2 = self.__check_for_end_point_relations(
            body_block_relation_2)

        if body_block_relation_1.get_x == body_block_relation_2.get_x:
            self.__curr_body_block_img = self.__body_vertical_img

        elif body_block_relation_1.get_y == body_block_relation_2.get_y:
            self.__curr_body_block_img = self.__body_horizontal_img

        else:
            if body_block_relation_1.get_x == -1 and body_block_relation_2.get_y == -1 \
                    or body_block_relation_1.get_y == -1 and body_block_relation_2.get_x == -1:
                self.__curr_body_block_img = self.__body_tl_img

            elif body_block_relation_1.get_x == -1 and body_block_relation_2.get_y == 1 \
                    or body_block_relation_1.get_y == 1 and body_block_relation_2.get_x == -1:
                self.__curr_body_block_img = self.__body_bl_img

            elif body_block_relation_1.get_x == 1 and body_block_relation_2.get_y == -1 \
                    or body_block_relation_1.get_y == -1 and body_block_relation_2.get_x == 1:
                self.__curr_body_block_img = self.__body_tr_img

            elif body_block_relation_1.get_x == 1 and body_block_relation_2.get_y == 1 \
                    or body_block_relation_1.get_y == 1 and body_block_relation_2.get_x == 1:
                self.__curr_body_block_img = self.__body_br_img

    def draw_head(self, screen):
        snake_head_rect_x = self.__head_block_position.get_x * Game.get_cell_width()
        snake_head_rect_y = self.__head_block_position.get_y * Game.get_cell_height()

        snake_head_rect = pygame.Rect(
            (snake_head_rect_x, snake_head_rect_y), Game.get_cell_size())

        self.__update_head_graphics()
        screen.blit(self.__curr_head_img, snake_head_rect)

    def draw_body(self, screen):
        for index, body_block in enumerate(self.__body_block_positions):
            snake_body_rect_x = body_block.get_x * Game.get_cell_width()
            snake_body_rect_y = body_block.get_y * Game.get_cell_height()

            snake_body_rect = pygame.Rect(
                (snake_body_rect_x, snake_body_rect_y), Game.get_cell_size())

            # check for tail
            if index == 0:
                self.__update_tail_graphics()
                screen.blit(self.__curr_tail_img, snake_body_rect)
                continue

            body_block_relation_1 = self.__body_block_positions[index - 1] - body_block

            if index == len(self.__body_block_positions) - 1:
                body_block_relation_2 = self.__head_block_position - body_block
            else:
                body_block_relation_2 = self.__body_block_positions[index + 1] - body_block

            self.__update_body_graphics(
                body_block_relation_1, body_block_relation_2)
            screen.blit(self.__curr_body_block_img, snake_body_rect)
