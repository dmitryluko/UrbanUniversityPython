"""
Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

"""
def main():
    # Lists given in the task
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    # Generator comprehension for first_result
    first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

    # Generator comprehension for second_result
    second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

    # Example usage of the generator comprehensions
    print(list(first_result))  # Output: [1, 2]
    print(list(second_result))  # Output: [False, False, True]


if __name__ == '__main__':
    main()
