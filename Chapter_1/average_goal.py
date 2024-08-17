"""
Задание "Средний балл":
Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":

На вход даны следующие данные:
Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

"""


def solution(grades: list, students: set) -> dict:
    avg_grades = dict()

    for student, grades in zip(sorted(students), grades):
        avg_grades[student] = sum(grades) / len(grades)

    return avg_grades


def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')


def main():
    test_grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    test_students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

    print_dictionary(solution(test_grades, test_students))


if __name__ == '__main__':
    main()
