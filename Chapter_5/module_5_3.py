"""
Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

"""


class House:

    def __init__(self, name: str, number_of_floors: int):
        self.name: str = name
        self.number_of_floors: int = number_of_floors

    def go_to(self, floor: int) -> None:
        if 1 <= floor <= self.number_of_floors:
            for i in range(1, floor + 1):
                print(i)
        else:
            print('The Floor does not exist')

    @staticmethod
    def get_floors(value):
        """Helper method to get number of floors from value which can be int or AdvancedHouse."""

        if isinstance(value, int):
            return value
        elif isinstance(value, House):
            return value.number_of_floors

        raise TypeError("Value must be an int or an instance of AdvancedHouse")

    def __add__(self, value):
        """Adds an integer number of floors or combines floors of another House."""

        self.number_of_floors += self.get_floors(value)

        return self

    def __radd__(self, value):
        """Supports addition from the right side."""

        return self.__add__(value)

    def __iadd__(self, value):
        """Supports in-place addition."""

        return self.__add__(value)

    def __eq__(self, other):
        """Checks equality based on the number of floors."""

        return self.number_of_floors == self.get_floors(other)

    def __gt__(self, other):
        """Greater than comparison based on the number of floors."""

        return self.number_of_floors > self.get_floors(other)

    def __ge__(self, other):
        """Greater than or equal comparison based on the number of floors."""

        return self.number_of_floors >= self.get_floors(other)

    def __lt__(self, other):
        """Less than comparison based on the number of floors."""

        return self.number_of_floors < self.get_floors(other)

    def __le__(self, other):
        """Less than or equal comparison based on the number of floors."""

        return self.number_of_floors <= self.get_floors(other)

    def __ne__(self, other):
        """Not equal comparison based on the number of floors."""

        return self.number_of_floors != self.get_floors(other)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name: {self.name}, Number of Floors: {self.number_of_floors}'


def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__


if __name__ == '__main__':
    main()
