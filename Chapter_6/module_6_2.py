"""
Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.

Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.

Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
Каждый объект Vehicle должен содержать следующий методы:
Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
Взаимосвязь методов и скрытых атрибутов:
Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами: __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

Пункты задачи:
Создайте классы Vehicle и Sedan.
Напишите соответствующие свойства в обоих классах.
Не забудьте сделать Sedan наследником класса Vehicle.
Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.


"""
from enum import Enum


class ColorPalette(Enum):
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'
    BLACK = 'black'
    WHITE = 'white'
    PURPLE = 'purple'
    ORANGE = 'orange'
    TURQUOISE = 'turquoise'


# class Vehicle:
#     __COLOR_VARIANTS = [color.value for color in ColorPalette]
#
#     def __init__(self, owner: str, model: str, color: str, engine_power: int):
#         self.owner = owner
#         self.__model = model
#         self.__engine_power = engine_power
#         if color.lower() in Vehicle.__COLOR_VARIANTS:
#             self.__color = color.lower()
#         else:
#             raise ValueError(f'Invalid color: {color}')
#
#     def get_model(self) -> str:
#         return f"Модель: {self.__model}"
#
#     def get_horsepower(self) -> str:
#         return f"Мощность двигателя: {self.__engine_power}"
#
#     def get_color(self) -> str:
#         return f"Цвет: {self.__color}"
#
#     def set_color(self, new_color: str) -> None:
#         if new_color.lower() in Vehicle.__COLOR_VARIANTS:
#             self.__color = new_color.lower()
#         else:
#             print(f"Нельзя сменить цвет на {new_color}")
#
#     def print_info(self) -> None:
#         print(self.get_model())
#         print(self.get_horsepower())
#         print(self.get_color())
#         print(f"Владелец: {self.owner}")
"""
Got it, I see what you're trying to do, but I've got a better solution. Check it out below!
"""


class Vehicle:
    @classmethod
    def get_color_variants(cls):
        return [color.value for color in ColorPalette]

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = self._validate_color(color)

    @staticmethod
    def _validate_color(color: str) -> str:
        color_lower = color.lower()
        if color_lower in Vehicle.get_color_variants():
            return color_lower
        raise ValueError(f'Invalid color: {color}')

    @property
    def model(self) -> str:
        return f"Model: {self._model}"

    @property
    def horsepower(self) -> str:
        return f"Engine Power: {self._engine_power}"

    @property
    def color(self) -> str:
        return f"Color: {self._color}"

    @color.setter
    def color(self, new_color: str) -> None:
        try:
            self._color = self._validate_color(new_color)
        except ValueError:
            print(f"Cannot change color to {new_color}")

    def print_info(self) -> None:
        print(self.model)
        print(self.horsepower)
        print(self.color)
        print(f"Owner: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)

    @property
    def passengers_limit(self):
        return Sedan.__PASSENGERS_LIMIT


def main():
    # Creating an instance of Sedan with STANDARD color palette
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
    vehicle1.print_info()
    # Trying to change color to an invalid color "Pink"
    vehicle1.color = 'Pink'
    # Trying to change color to BLACK
    vehicle1.color = 'BLACK'
    vehicle1.owner = 'Vasyok'
    vehicle1.print_info()


if __name__ == "__main__":
    main()
