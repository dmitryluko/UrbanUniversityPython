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


def calculate_structure_sum(data: object) -> int:
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

    total_sum = 0

    if isinstance(data, int):
        total_sum += sum_int(data)
    elif isinstance(data, str):
        total_sum += sum_str(data)
    elif isinstance(data, (list, tuple, set)):
        total_sum += sum_collection(data)
    elif isinstance(data, dict):
        total_sum += sum_dict(data)

    return total_sum


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
