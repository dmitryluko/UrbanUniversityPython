"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99

"""
from typing import Callable, Any


def calculate_structure_sum(data: object) -> int:
    def safely_handle_data_(handler_: Callable[[Any], int], data_: Any) -> int:
        if not callable(handler):
            raise ValueError('Handler must be a callable function')
        try:
            return handler_(data_)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise

    def sum_int(i_data: int) -> int:
        return i_data

    def sum_str(s_data: str) -> int:
        return len(s_data)

    def sum_collection(col_data) -> int:
        sub_total = 0
        for item in col_data:
            sub_total += calculate_structure_sum(item)
        return sub_total

    def sum_dict(d_data: dict) -> int:
        sub_total = 0
        for key, value in d_data.items():
            sub_total += calculate_structure_sum(key)
            sub_total += calculate_structure_sum(value)
        return sub_total

    DATA_CORRESPONDING_HANDLER = {
        int: sum_int,
        str: sum_str,
        list: sum_collection,
        tuple: sum_collection,
        set: sum_collection,
        dict: sum_dict,
        object: lambda _: 0,
    }

    handler = DATA_CORRESPONDING_HANDLER[type(data)]
    return safely_handle_data_(handler, data)


def main():
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

    result = calculate_structure_sum(data_structure)
    print(result)


if __name__ == '__main__':
    main()
