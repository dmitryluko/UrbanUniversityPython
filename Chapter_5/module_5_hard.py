"""
Задание "Свой YouTube":

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"

"""
import hashlib
import time
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class User:
    nickname: str
    password: str
    age: int
    __hashed_password: int = field(init=False)

    def __post_init__(self):
        self.__hashed_password = self.hash_password(self.password)

    @staticmethod
    def hash_password(password: str) -> int:
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password: str) -> bool:
        return self.__hashed_password == self.hash_password(password)

    def __str__(self):
        return f'User {self.nickname}'


@dataclass
class Video:
    title: str
    duration: int
    adult_mode: bool = False
    time_now: int = 0


class UrTube:
    def __init__(self):
        self.users: List[User] = []
        self.videos: List[Video] = []
        self.current_user: Optional[User] = None

    def log_in(self, nickname: str, password: str) -> None:
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                return
        self.current_user = None
        print("Invalid nickname or password")

    def register(self, nickname: str, password: str, age: int) -> None:
        if any(user.nickname == nickname for user in self.users):
            print(f"User {nickname} already exists")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"User {nickname} registered and logged in")

    def log_out(self) -> None:
        if self.current_user:
            print(f"User {self.current_user.nickname} logged out")
        self.current_user = None

    def add(self, *videos: Video) -> None:
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word: str) -> List[str]:
        search_word_lower: str = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title: str) -> None:
        if self.current_user is None:
            print("Please log in to watch videos")
            return

        video: Optional[Video] = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Video not found")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("You are under 18 years old. Access denied.")
            return

        print(f"Starting '{video.title}'...")
        for second in range(1, video.duration + 1):
            print(f"{second}", end=" ", flush=True)
            time.sleep(1)
        print("\nEnd of video")
        video.time_now = 0


def main():
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


if __name__ == "__main__":
    main()
