"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
"""
import asyncio
import aiofiles


async def write_words(word_count: int, file_name: str) -> None:
    async with aiofiles.open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            await file.write(f"Какое-то слово № {i}\n")

    print(f"Завершилась запись в файл {file_name}")


async def main():
    await asyncio.gather(
        write_words(10, "example1.txt"),
        write_words(30, "example2.txt"),
        write_words(200, "example3.txt"),
        write_words(100, "example4.txt")
    )


if __name__ == '__main__':
    asyncio.run(main())
