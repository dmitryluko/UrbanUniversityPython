"""
Задача "Рекурсивное умножение цифр":
Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

Пункты задачи:
Напишите функцию get_multiplied_digits и параметр number в ней.
Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
Стек вызовов будет выглядеть следующим образом:
get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

Пример результата выполнения программы:
Исходный код:
result = get_multiplied_digits(40203)
print(result)
Вывод на консоль:
24

"""
from functools import reduce


def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number


def get_multiplied_digits_func(number: int) -> int:
    return reduce(
        lambda x, y: x * y,
        filter(lambda x: x != 0, map(int, str(number)))
    )


def main():
    print(get_multiplied_digits(40203))
    print(get_multiplied_digits_func(40203))


if __name__ == '__main__':
    main()
