"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

"""


class House:
    houses_history = []

    def __init__(self, name: str, number_of_floors: int):
        self.name: str = name
        self.number_of_floors: int = number_of_floors

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.name = args[0]

        cls.houses_history.append(instance.name)

        return instance

    def __del__(self):
        print(f'{self.name} is destroyed, but saved for history')

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

        floors_to_add = self.get_floors(value)

        return House(self.name, self.number_of_floors + floors_to_add)

    def __radd__(self, value):
        """Supports addition from the right side."""

        return self.__add__(value)

    def __iadd__(self, value):
        """Supports in-place addition."""

        new_house = self.__add__(value)

        self.name = new_house.name
        self.number_of_floors = new_house.number_of_floors
        return self

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
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)


if __name__ == '__main__':
    main()
