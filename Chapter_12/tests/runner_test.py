from Chapter_12.runner import Runner

import unittest


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
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @_skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @_skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
