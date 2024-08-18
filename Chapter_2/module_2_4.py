"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).

"""


def is_legal(number: int) -> bool:
    return 2 <= number


def is_prime(number: int) -> bool:
    if not is_legal(number):
        return False

    is_prime_ = True
    for divider in range(2, number):
        if number % divider == 0:
            is_prime_ = False
            break

    return is_prime_


def is_composite(number: int) -> bool:
    if not is_legal(number):
        return False

    return not is_prime(number)


def get_primes_and_not_primes(numbers: list) -> tuple:
    primes_ = list(filter(is_prime, numbers))
    composite_ = list(filter(is_composite, numbers))

    return primes_, composite_


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    print('Primes: ', *get_primes_and_not_primes(numbers)[0])
    print('Not Primes: ', *get_primes_and_not_primes(numbers)[1])


if __name__ == '__main__':
    main()
