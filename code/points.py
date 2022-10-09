CELL_WIDTH, CELL_HEIGHT = 30, 30
CELL_NUMBER = 20  # Please do not change the value.


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    def __add__(self, other):
        return Point(self.__x + other.get_x, self.__y + other.get_y)

    def __sub__(self, other):
        return Point(self.__x - other.get_x, self.__y - other.get_y)

    def __eq__(self, other):
        return (isinstance(other, Point)) \
            and (self.__x == other.get_x and self.__y == other.get_y)

    def __hash__(self):
        return hash((self.__x, self.__y))
