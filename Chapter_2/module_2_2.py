"""
Задача "Все ли равны?":
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0

Пример результата выполнения программы:
Ввод в консоль 1:
123
456
789

Вывод на консоль 1:
0

Ввод в консоль 2:
42
69
42

Вывод на консоль 2:
2


"""


def get_equals_counter(first: int, second: int, third: int) -> int:
    eq_counter_ = 0

    if first == second == third:
        eq_counter_ = 3
    elif first == second or first == third or second == third:
        eq_counter_ = 2

    return eq_counter_


def main():
    print(get_equals_counter(*map(int, input().split())))


if __name__ == '__main__':
    main()
