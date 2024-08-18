"""
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.

"""


def get_matrix(n: int, m: int, value: int) -> list:
    return [[value for _ in range(m)] for _ in range(n)]


def main():
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    print(result1)
    print(result2)
    print(result3)


if __name__ == '__main__':
    main()
