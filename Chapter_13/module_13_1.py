"""
Задача "Асинхронные силачи":
Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. Реализуйте следующую логику в функции:
В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
"""
import asyncio


async def start_strongman(name: str, power: int) -> None:
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament() -> None:
    participants = [
        ("Алексей", 2),
        ("Иван", 3),
        ("Сергей", 1)
    ]

    tasks = [start_strongman(name, power) for name, power in participants]

    await asyncio.gather(*tasks)


def main():
    asyncio.run(start_tournament())


if __name__ == '__main__':
    main()
