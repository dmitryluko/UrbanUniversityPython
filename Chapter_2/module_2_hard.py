"""
Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).

Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)


Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)


К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движутся на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.

Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.
6 4+16 5+15 6+14 7+13 8+12 9+11

"""
PAIR_LIMIT = 20


def is_valid_pair(number: int, first: int, second: int) -> bool:
    """
    This function checks if a pair of integers is a valid pair based on a given number.

    :param number: The number against which the validity of the pair is checked.
    :param first: The first integer in the pair.
    :param second: The second integer in the pair.
    :return: True if the pair is valid, False otherwise.
    """
    if first == second or (first + second) == 0:
        return False

    return number % (first + second) == 0


def generate_pairs(number: int) -> list[str]:
    """
    Generates pairs of numbers that are valid for the given number.

    :param number: The input number for which pairs are generated.
    :return: A list of strings representing the generated pairs.
    """
    pairs = []
    for i in range(1, PAIR_LIMIT + 1):
        for j in range(i + 1, PAIR_LIMIT + 1):
            if is_valid_pair(number, i, j):
                pairs.append(f"{i}{j}")
    return pairs


def get_password(number: int) -> int:
    """Generates a password from a given number.

    :param number: The number used to generate the password.
    :return: The generated password.
    """
    pairs = generate_pairs(number)
    return int(''.join(pairs))


def main():
    for n in range(3, PAIR_LIMIT + 1):
        print(f'{n=}: {get_password(n)}')


if __name__ == '__main__':
    main()
