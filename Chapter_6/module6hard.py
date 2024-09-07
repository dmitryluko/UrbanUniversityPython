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
from math import pi, sqrt


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.__r = r
        self.__g = g
        self.__b = b

        super().__init__()

    @property
    def rgb_color(self):
        return self.__r, self.__g, self.__b

    @rgb_color.setter
    def rgb_color(self, values):
        r, g, b = values
        if self._is_valid_color(r, g, b):
            self.__r = r
            self.__g = g
            self.__b = b
        else:
            raise ValueError("Invalid color values")

    @staticmethod
    def _is_valid_color(r, g, b) -> bool:
        return all(0 <= val <= 255 for val in (r, g, b))


class Figure:
    SIDES_COUNT = 0
    DEFAULT_COLOR = Color(255, 0, 0)

    def __init__(self, sides=None):

        if sides is not None:
            self.__sides = []
        else:
            self.__sides = sides

        self.__color: Color = self.DEFAULT_COLOR
        self.filled = False

        super().__init__()

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
        if self._is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            raise ValueError("Invalid sides")

    def _is_valid_sides(self, new_sides):
        return len(new_sides) == self.SIDES_COUNT

    def __len__(self):
        return sum(self.__sides)

    def _get_square(self):
        return NotImplemented

    @property
    def square(self):
        return self._get_square()


class Circle(Figure):
    def __init__(self, color, length):
        self.SIDES_COUNT = 1
        super().__init__(length)
        self.color = color
        self._radius = length / (2 * pi)
        self._square = self._get_square()

    @property
    def square(self):
        return self._square

    def radius(self):
        return self._radius


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(sides)

    def _get_square(self):
        a, b, c = self.sides

        semi_perimeter = (a + b + c) / 2
        herons_square = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

        return herons_square


class Cube(Figure):
    def __init__(self, color, *sides):
        self.SIDES_COUNT = 12
        super().__init__(sides)

    def _get_square(self):
        return 6 * pow(self.sides[0], 2)

    @property
    def volume(self):
        return pow(self.sides[0], 3)


def main():
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.color = (55, 66, 77)  # Изменится
    print(circle1.color)
    cube1.color = (300, 70, 15)  # Не изменится
    print(cube1.color)

    # Проверка на изменение сторон:
    cube1.sides = (5, 3, 12, 4, 5)  # Не изменится
    print(cube1.sides)
    circle1.sides = (15)  # Изменится
    print(circle1.sides)

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.volume)


if __name__ == '__main__':
    main()
