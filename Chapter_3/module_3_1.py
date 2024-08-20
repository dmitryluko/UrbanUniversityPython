"""
Задача "Счётчик вызовов":

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

Пример результата выполнения программы:
Пример выполняемого кода:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
Вывод на консоль:
(8, 'CAPYBARA', 'capybara')
(10, 'ARMAGEDDON', 'armageddon')
True
False
4

"""


def call_counter(func):
    call_counter.__count = 0

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        call_counter.__count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@call_counter
def string_info(string: str) -> (int, str, str):
    return len(string), string.upper(), string.lower()


@call_counter
def is_contains(pattern: str, list_to_search: list[str]) -> bool:
    return True if pattern.lower() in map(lambda x: x.lower(), list_to_search) else False


def get_calls_count() -> int | str:
    return getattr(call_counter, '__count', 'No calls')


def main():
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

    print(get_calls_count())
    print(string_info.count)
    print(is_contains.count)


if __name__ == '__main__':
    main()
