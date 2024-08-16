"""
В переменную example запишите любую строку.
Выведите на экран(в консоль) первый символ этой строки.
Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
Выведите на экран(в консоль) это слово наоборот.
Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
"""


def get_first_symbol(given_string: str) -> str:
    return given_string[0]


def get_last_symbol(given_string: str) -> str:
    return given_string[-1]


def get_second_half(given_string: str) -> str:
    output_string = given_string[len(given_string) // 2:]
    return output_string


def reverse_string(given_string: str) -> str:
    output_string = given_string[::-1]
    return output_string


def get_every_second_symbol(given_string: str) -> str:
    output_string = given_string[1::2]
    return output_string


def main():
    example = 'This is an example string'

    print(get_first_symbol(example))
    print(get_last_symbol(example))
    print(get_second_half(example))
    print(reverse_string(example))
    print(get_every_second_symbol(example))

    print(get_second_half('Urban'))
    print(get_every_second_symbol('Топинамбур'))

    print(get_every_second_symbol('abcdefghijklmnopqrstuvwxyz'))


if __name__ == '__main__':
    main()
