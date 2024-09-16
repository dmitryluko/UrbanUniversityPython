"""
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
"""
import itertools


def all_variants(text):
    """Generate all possible substrings of the given text."""
    length = len(text)
    for i in range(1, length + 1):
        for start_index in range(length - i + 1):
            yield extract_substring(text, start_index, i)


def extract_substring(text, start, length):
    """Extract a substring from the provided text starting at the given index with the given length."""
    end_index = start + length
    return text[start:end_index]


# Usage
def main():
    substrings = all_variants('abc')
    for substring in substrings:
        print(substring)


if __name__ == '__main__':
    main()
