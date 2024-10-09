import unittest
import logging

from Chapter_12.rt_with_exceptions import Runner, Tournament

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @staticmethod
    def _skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @_skip_if_frozen
    def test_walk(self):
        try:
            # Creating object with a negative speed which should throw an exception
            runner = Runner(name="John Doe", speed=-5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.error("Exception in test_walk: Неверная скорость для Runner", exc_info=True)
            self.fail("Exception was raised: " + str(e))

    @_skip_if_frozen
    def test_run(self):
        try:
            # Creating object with an invalid type for name which should throw an exception
            runner = Runner(name=12345, speed=10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.error("Exception in test_run: Неверный тип данных для объекта Runner", exc_info=True)
            self.fail("Exception was raised: " + str(e))

    @_skip_if_frozen
    def test_challenge(self):
        try:
            runner1 = Runner("Runner1")
            runner2 = Runner("Runner2")
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.distance)
            logging.info('"test_challenge" выполнен успешно')
        except Exception as e:
            logging.error("Exception in test_challenge", exc_info=True)
            self.fail("Exception was raised: " + str(e))


class TournamentTest(unittest.TestCase):
    is_frozen = False

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
        logging.info('\n%s\nSummary of All Results:\n%s', LINE_SEPARATOR, LINE_SEPARATOR)
        for k, v in cls.all_results.items():
            logging.info('%s:', k)
            for key, value in v.items():
                logging.info('    %s: %s', key, value)
        logging.info(LINE_SEPARATOR)

    @_skip_if_frozen
    def test_race_usain_nick(self):
        try:
            tournament = Tournament(90, self.usain, self.nick)
            result = tournament.start()
            TournamentTest.all_results[1] = result
            self.assertTrue(result[max(result.keys())] == 'Ник')
            logging.info('"test_race_usain_nick" выполнен успешно')
        except Exception as e:
            logging.error("Exception in test_race_usain_nick", exc_info=True)
            self.fail("Exception was raised: " + str(e))

    @_skip_if_frozen
    def test_race_andrei_nick(self):
        try:
            tournament = Tournament(90, self.andrei, self.nick)
            result = tournament.start()
            TournamentTest.all_results[2] = result
            self.assertTrue(result[max(result.keys())] == 'Ник')
            logging.info('"test_race_andrei_nick" выполнен успешно')
        except Exception as e:
            logging.error("Exception in test_race_andrei_nick", exc_info=True)
            self.fail("Exception was raised: " + str(e))

    @_skip_if_frozen
    def test_race_usain_andrei_nick(self):
        try:
            tournament = Tournament(90, self.usain, self.andrei, self.nick)
            result = tournament.start()
            TournamentTest.all_results[3] = result
            self.assertTrue(result[max(result.keys())] == 'Ник')
            logging.info('"test_race_usain_andrei_nick" выполнен успешно')
        except Exception as e:
            logging.error("Exception in test_race_usain_andrei_nick", exc_info=True)
            self.fail("Exception was raised: " + str(e))


# To run the tests
if __name__ == '__main__':
    unittest.main()
