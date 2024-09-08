"""
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Код для проверки:


Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""

import math

# Error Messages
INVALID_COLOR_MSG = "Color values must be integers between 0 and 255."
INVALID_SIDES_MSG = "Invalid sides for the figure."
INVALID_TRIANGLE_SIDES_MSG = "A triangle must have exactly 3 sides"


class Color:
    def __init__(self, r: int, g: int, b: int):
        if self._is_valid_color(r, g, b):
            self.__r = r
            self.__g = g
            self.__b = b
        else:
            raise ValueError(INVALID_COLOR_MSG)

    @property
    def rgb_color(self):
        return self.__r, self.__g, self.__b

    @rgb_color.setter
    def rgb_color(self, values):
        if isinstance(values, tuple) and len(values) == 3 and all(isinstance(val, int) for val in values):
            if self._is_valid_color(*values):
                self.__r, self.__g, self.__b = values

    @staticmethod
    def _is_valid_color(r, g, b) -> bool:
        return all(0 <= val <= 255 for val in (r, g, b))


class Figure:
    SIDES_COUNT = 0
    DEFAULT_COLOR = Color(255, 0, 0)

    def __init__(self, sides=None, color=None):
        self.__sides = sides if sides is not None and self._is_valid_sides(sides) else [1] * self.SIDES_COUNT
        self.__color = Color(*color) if color is not None else self.DEFAULT_COLOR
        self.filled = False

    @property
    def color(self):
        return self.__color.rgb_color

    @color.setter
    def color(self, values):
        self.__color.rgb_color = values

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, new_sides):
        self.__sides = new_sides if self._is_valid_sides(new_sides) else [1] * self.SIDES_COUNT

    def _is_valid_sides(self, new_sides):
        return isinstance(new_sides, list) and len(new_sides) == self.SIDES_COUNT and all(
            isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def __len__(self):
        return sum(self.__sides)

    def _get_square(self):
        return NotImplemented

    @property
    def square(self):
        return self._get_square()


class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, color, radius):
        super().__init__(color=color, sides=[radius * 2 * math.pi])
        self._radius = radius
        self._square = self._get_square()

    @property
    def square(self):
        return self._square

    @property
    def radius(self):
        return self._radius

    def _get_square(self):
        return math.pi * self._radius ** 2


class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, side1, side2, side3):
        sides = [side1, side2, side3]
        if not self._is_triangle_sides(sides):
            raise ValueError(INVALID_TRIANGLE_SIDES_MSG)
        super().__init__(color=color, sides=sides)

    def _is_triangle_sides(self, sides):
        if isinstance(sides, (list, tuple)) and len(sides) == self.SIDES_COUNT:
            a, b, c = sides
            return a + b > c and a + c > b and b + c > a
        return False

    def _get_square(self):
        a, b, c = self.sides
        s = (a + b + c) / 2

        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    SIDES_COUNT = 1

    def __init__(self, color, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError(INVALID_SIDES_MSG)
        super().__init__(color=color, sides=[side_length])

    def _get_square(self):
        side_length = self.sides[0]
        return 6 * pow(side_length, 2)

    @property
    def volume(self):
        side_length = self.sides[0]
        return pow(side_length, 3)


def main():
    # Create instances of the shapes
    circle1 = Circle((200, 200, 100), 10)  # (Color, radius)
    triangle1 = Triangle((255, 0, 0), 3, 4, 5)  # (Color, side1, side2, side3)
    cube1 = Cube((222, 35, 130), 6)  # (Color, side_length)

    # Print the initial colors
    print("Initial Colors:")
    print(f"Circle: {circle1.color}")
    print(f"Triangle: {triangle1.color}")
    print(f"Cube: {cube1.color}")

    # Change colors
    circle1.color = (55, 66, 77)
    cube1.color = (300, 70, 15)  # Invalid, should not change

    # Print the colors after attempting to change
    print("\nColors After Change Attempt:")
    print(f"Circle: {circle1.color}")
    print(f"Cube: {cube1.color}")

    # Print the sides
    print("\nSides:")
    print(f"Circle (perimeter): {circle1.sides}")
    print(f"Triangle sides: {triangle1.sides}")
    print(f"Cube (side length): {cube1.sides}")

    # Change sides
    cube1.sides = [5, 3, 12, 4, 5]  # Invalid, should not change
    circle1.sides = [15]  # Perimeter will change according to new radius 7.5

    # Print the sides after attempting to change
    print("\nSides After Change Attempt:")
    print(f"Circle (perimeter): {circle1.sides}")
    print(f"Cube: {cube1.sides}")

    # Print perimeter (len) and areas (square, volume)
    print("\nPerimeter, Area and Volume:")
    print(f"Circle perimeter (len): {len(circle1)}")
    print(f"Circle area (square): {circle1.square}")
    print(f"Triangle area (square): {triangle1.square}")
    print(f"Cube area (square): {cube1.square}")
    print(f"Cube volume: {cube1.volume}")


if __name__ == '__main__':
    main()
