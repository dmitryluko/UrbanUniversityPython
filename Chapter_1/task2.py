# 2nd program

"""
Напишите в начале программы однострочный комментарий: "2nd program".
Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
 Предполагаемый результат: True
"""
import math


def solution() -> bool:
    return (9.99 > 9.98) & (not math.isclose(1000, 1000.1, rel_tol=1e-9))


def main():
    print(solution())


if __name__ == '__main__':
    main()
