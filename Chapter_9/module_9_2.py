"""
Задача:
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.
"""

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


def main():
    # Создание списка с длинами строк не менее 5 символов
    first_result = [len(s) for s in first_strings if len(s) >= 5]

    # Создание списка пар слов одинаковой длины
    second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

    # Создание словаря строк с чётной длиной
    third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

    print(first_result)
    print(second_result)
    print(third_result)


if __name__ == '__main__':
    main()
