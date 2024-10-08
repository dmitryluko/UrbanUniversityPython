import unittest

from Chapter_12.runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @staticmethod
    def _skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            else:
                return func(self, *args, **kwargs)

        return wrapper

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

    @_skip_if_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    @_skip_if_frozen
    def test_race_andrei_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    @_skip_if_frozen
    def test_race_usain_andrei_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')


# To run the tests
if __name__ == '__main__':
    unittest.main()
