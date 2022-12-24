class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        return Point(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other):
        return Point(self.__x - other.x, self.__y - other.y)

    def __eq__(self, other):
        return (isinstance(other, Point)) and (
            self.__x == other.x and self.__y == other.y
        )

    def __hash__(self):
        return hash((self.__x, self.__y))
