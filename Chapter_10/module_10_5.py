"""
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Подготовка:
Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.

"""
from typing import List, Callable
from multiprocessing import Pool
import time


def read_file(name: str) -> List[str]:
    file_lines: List[str] = []
    with open(name, 'r') as file:
        while (line := file.readline()):
            file_lines.append(line)
    return file_lines


def linear_read(filenames: List[str]) -> None:
    for name in filenames:
        read_file(name)


def multiprocessing_read(filenames: List[str]) -> None:
    with Pool() as pool:
        pool.map(read_file, filenames)


def measure_time(function: Callable, *args) -> float:
    start_time = time.time()
    function(*args)
    end_time = time.time()
    return end_time - start_time


def main():
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Measure time for linear read
    linear_time = measure_time(linear_read, filenames)
    print(f"Linear read time: {linear_time}")

    # Measure time for multiprocessing read
    multiprocessing_time = measure_time(multiprocessing_read, filenames)
    print(f"Multiprocessing read time: {multiprocessing_time}")


if __name__ == '__main__':
    main()
