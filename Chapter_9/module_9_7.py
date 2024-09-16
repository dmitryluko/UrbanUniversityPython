"""
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""

import math

# Constants for messages
COMPOSITE_MSG = "Составное"  # Composite number
PRIME_MSG = "Простое"  # Prime number


def is_prime_number(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime_number(result):
            print(PRIME_MSG)
        else:
            print(COMPOSITE_MSG)
        return result

    return wrapper


@is_prime
def sum_three_numbers(a, b, c):
    return a + b + c


def main():
    result = sum_three_numbers(2, 3, 6)
    print(result)


if __name__ == '__main__':
    main()
