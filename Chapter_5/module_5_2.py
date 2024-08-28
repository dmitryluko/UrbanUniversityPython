"""
Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


"""

from module_5_1 import House


class SmartHouse(House):

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name: {self.name}, Number of Floors: {self.number_of_floors}'


def main():
    h1 = SmartHouse('ЖК Эльбрус', 10)
    h2 = SmartHouse('ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))


if __name__ == '__main__':
    main()
