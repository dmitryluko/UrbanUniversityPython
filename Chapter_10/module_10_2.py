"""
Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
Пункты задачи:
Создайте класс Knight с соответствующими описанию свойствами.
Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.
"""

import threading
import time


class Knight(threading.Thread):
    SLEEP_DURATION = 1  # Sleep duration in seconds

    def __init__(self, name: str, power: int):
        super().__init__()
        self.TOTAL_ENEMIES = 100  # Class variable shared among all instances
        self.name = name
        self.power = power

    def run(self) -> None:
        days = 0
        self.announce_attack()

        while self.TOTAL_ENEMIES > 0:
            self.fight_one_day()
            days += 1
            if self.TOTAL_ENEMIES > 0:
                self.report_progress(days)
            else:
                self.announce_victory(days)
                break

    def announce_attack(self) -> None:
        print(f'{self.name}, на нас напали!')

    def fight_one_day(self) -> None:
        time.sleep(Knight.SLEEP_DURATION)

        if self.TOTAL_ENEMIES <= self.power:
            self.TOTAL_ENEMIES = 0
        else:
            self.TOTAL_ENEMIES -= self.power

    def report_progress(self, days: int) -> None:
        print(f'{self.name} сражается {days} день(дня/дней)..., осталось {self.TOTAL_ENEMIES} воинов.')

    def announce_victory(self, days: int) -> None:

        print(f'{self.name} одержал победу спустя {days} день(дня/дней)!')


def main() -> None:
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Сражение окончено!")


if __name__ == '__main__':
    main()
