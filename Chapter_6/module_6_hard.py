"""
Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

"""


class Horse:
    SOUND_HORSE = 'Frrr'

    def __init__(self):
        self.x_distance: float = 0
        self.sound: str = self.SOUND_HORSE

    def run(self, dx: float) -> None:
        self.x_distance += dx


class Eagle:
    SOUND_EAGLE = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance: float = 0
        self.sound: str = self.SOUND_EAGLE

    def fly(self, dy: float) -> None:
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx: float, dy: float) -> None:
        self.run(dx)
        self.fly(dy)

    def voice(self) -> None:
        print(self.sound)

    def get_pos(self) -> tuple[float, float]:
        return self.x_distance, self.y_distance


def main():
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()


if __name__ == '__main__':
    main()

"""
 -> Но! Я бы написал по другому. Здесь явная нехватка абстракции Animal
  
from abc import ABC, abstractmethod

SOUND_HORSE = 'Frrr'
SOUND_EAGLE = 'I train, eat, sleep, and repeat'


class Animal(ABC):
    def __init__(self, sound: str):
        self.position = [0, 0]
        self.sound = sound

    def speak(self) -> None:
        print(self.sound)

    @abstractmethod
    def move(self, distance: float) -> None:
        pass


class Horse(Animal):
    def __init__(self):
        super().__init__(SOUND_HORSE)

    def move(self, dx: float) -> None:
        self.position[0] += dx


class Eagle(Animal):
    def __init__(self):
        super().__init__(SOUND_EAGLE)

    def move(self, dy: float) -> None:
        self.position[1] += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx: float, dy: float) -> None:
        self.run(dx)
        self.fly(dy)

    def run(self, dx: float) -> None:
        Horse.move(self, dx)

    def fly(self, dy: float) -> None:
        Eagle.move(self, dy)

    def get_position(self) -> tuple[float, float]:
        return tuple(self.position)
"""
