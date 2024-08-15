# 4th program

"""
Напишите в начале программы однострочный комментарий: "4th program".
Дана строка '123.456'.
Вывести на экран первую цифру после запятой - 4.
"""


def solution1(given_string: str):
    return int(given_string[given_string.find('.') + 1])


def solution2(given_string: str):
    return int(int((float(given_string)) * 10) % 10)


def main():
    data = '123.456'

    print(solution1(data), solution2(data), sep='\n')


if __name__ == '__main__':
    main()
