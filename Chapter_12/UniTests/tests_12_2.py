import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            for participant in self.participants:
                participant.run()
            completed = self.get_completed_participants()
            place = self.process_completed_participants(completed, finishers, place)

        return finishers

    def get_completed_participants(self):
        return [p for p in self.participants if p.distance >= self.distance]

    def process_completed_participants(self, completed, finishers, place):
        for participant in sorted(completed, key=self.sort_by_distance, reverse=True):
            finishers[place] = participant
            place += 1
            self.participants.remove(participant)

        return place

    @staticmethod
    def sort_by_distance(participant):
        return participant.distance


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrei = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # Introduce Constant
        LINE_SEPARATOR = '-' * 70

        print(f'\n{LINE_SEPARATOR}\nSummary of All Results:\n{LINE_SEPARATOR}')

        for k, v in cls.all_results.items():
            print(f'{k}:')
            for key, value in v.items():
                print(f'    {key}: {value}')

        print(LINE_SEPARATOR)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_andrei_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_usain_andrei_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')


# To run the tests
if __name__ == '__main__':
    unittest.main()
