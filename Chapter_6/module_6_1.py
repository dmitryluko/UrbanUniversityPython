"""
Задача "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?

Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

Пункты задачи:
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.

"""
from abc import ABC, abstractmethod


class Plant:
    """
    Initializes a new instance of the Plant class.

    :param name: The name of the plant.
    """
    edible: bool = False

    def __init__(self, name: str):
        self.name = name


class EatMixin:
    """

    This module contains the `EatMixin` class.

    `EatMixin` is a mixin class that provides properties and methods related to eating behavior. It has the following attributes:

    - `fed`: A boolean value indicating if the object is currently fed.
    - `alive`: A boolean value indicating if the object is alive.
    - `name`: A string representing the name of the object.

    """
    fed: bool
    alive: bool
    name: str

    def eat(self, food: Plant) -> None:
        """
        This method `eat` is defined within a class and is responsible for eating food.

        :param self: The instance of the class that this method belongs to.
        :param food: The food object that the instance is attempting to eat.

        :return: None

        Raises:
            AttributeError: If the instance does not have `fed` and `alive` attributes.

        This method checks if the instance has the required `fed` and `alive` attributes. If not, it raises an `AttributeError`.
        """
        if not hasattr(self, 'fed') or not hasattr(self, 'alive'):
            raise AttributeError('EatMixin requires fed and alive attributes')

        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Animal(ABC):
    """
    Initializes an instance of the Animal class.

    :param name: The name of the animal.
    :type name: str
    """
    fed: bool = False
    alive: bool = True

    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def eat(self, food: Plant) -> None:
        pass


class Mammal(EatMixin, Animal):
    """
    This code defines a class called Mammal, which is a subclass of the EatMixin and Animal classes.
    """

    def eat(self, food: Plant) -> None:
        super().eat(food)


class Predator(EatMixin, Animal):
    """
    Parameters:
    - `food` (Plant): The plant object that the predator wants to eat.

    Returns:
    - None: This method does not return any value.
    """

    def eat(self, food: Plant) -> None:
        super().eat(food)


class Flower(Plant):
    def __init__(self, name: str):
        super().__init__(name)


class Fruit(Plant):
    """
    The code defines a class called `Fruit` that inherits from the `Plant` class.
    The `Fruit` class has an `__init__` method which initializes an instance of the class with a `name` parameter of type `str`. The `__init__` method also calls the `__init__` method of the parent `Plant` class by passing the `name` parameter and an `edible` parameter set to `True`.

    """

    def __init__(self, name: str):
        super().__init__(name)
        self.edible: bool = True


def main():
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)


if __name__ == '__main__':
    main()
