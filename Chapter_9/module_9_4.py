"""
Задача "Функциональное разнообразие":
Lambda-функция:
Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.

Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.

Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything.

Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.

"""
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


def main():
    # Test Lambda-function
    first = 'Мама мыла раму'
    second = 'Рамена мало было'
    result = list(map(lambda f, s: f == s, first, second))
    print(
        result)  # Output: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

    # Test Closure
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    # Test __call__ Method
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())  # Output could be Да, Нет, or Наверное
    print(first_ball())  # Output could be Да, Нет, or Наверное
    print(first_ball())  # Output could be Да, Нет, or Наверное


if __name__ == '__main__':
    main()