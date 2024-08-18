"""
Задача "Нули ничто, отрицание недопустимо!":
Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Нужно выписывать из этого списка только положительные числа до тех пор,
пока не встретите отрицательное или не закончится список (выход за границу).

"""


def get_positive_numbers(my_list: list) -> list:
    output_list = []

    for item in my_list:
        if item > 0:
            output_list.append(item)
            continue

        elif item < 0:
            break

    return output_list


def main():
    demo_array = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

    print(*get_positive_numbers(demo_array), sep='\n')


if __name__ == '__main__':
    main()
