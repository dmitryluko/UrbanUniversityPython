"""
 Создайте переменные разных типов данных:
  - Создайте переменную name и присвойте ей значение вашего имени (строка).
  - Выведите значение переменной name на экран.
  - Создайте переменную age и присвойте ей значение вашего возраста (целое число).
  - Выведите значение переменной age на экран.
  - Перезапишите в age текущее значение переменной age + новое.
Как неверно (просто перезапись на новое число):
a = 15
a = 17
  - Выведите измененное значение переменной age на экран.
  - Создайте переменную is_student и присвойте ей значение True (логическое значение).
  - Выведите значение переменной is_student на экран.

"""


def main():
    name: str = 'Dmitry'
    age: int = 48
    print(f'Name: {name}')
    print(f'Age: {age}')
    age += 1
    print(f'New Age: {age}')
    is_student: bool = True
    print(f'Is Student: {is_student}')


if __name__ == '__main__':
    main()