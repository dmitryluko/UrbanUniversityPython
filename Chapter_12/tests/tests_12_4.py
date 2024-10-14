import logging
import unittest

from Chapter_12.rt_with_exceptions import Runner


# logger = logging.getLogger(__name__)
#
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='runner_tests.log',
#     filemode='w',
#     encoding='utf-8'
# )


class RunnerTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_frozen = False

        self.logger = logging.getLogger('test_logger')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='runner_tests.log',
            filemode='w',
            encoding='utf-8'
        )

    @staticmethod
    def _skip_if_frozen(func):
        # Assuming the skipping logic based on 'is_frozen'
        def wrapper(self, *args, **kwargs):
            if getattr(self, 'is_frozen', False):
                self.skipTest("Skipping because the instance is frozen")
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @_skip_if_frozen
    def test_walk_to_raise(self):
        self.logger.info('Starting "test_walk_to_raise" with Exception : ')
        with self.assertRaises(ValueError):
            _ = Runner(name="John Doe", speed=-5)

    @_skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @_skip_if_frozen
    def test_walk_to_raise(self):
        self.logger.info('Starting "test_walk with Exception : ')
        with self.assertRaises(ValueError):
            _ = Runner(name="John Doe", speed=-5)

    @_skip_if_frozen
    def test_run_to_rise(self):
        self.logger.info('Starting "test_run with Exception : "')

        with self.assertRaises(ValueError):
            _ = Runner(name="John Doe", speed=-5)

    @_skip_if_frozen
    def test_challenge(self):
        try:
            runner1 = Runner("Runner1")
            runner2 = Runner("Runner2")
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.distance)
            self.logger.info('"test_challenge" выполнен успешно')
        except Exception as e:
            self.logger.exception("Exception in test_challenge")
            self.fail("Exception was raised: " + str(e))


# To run the tests
if __name__ == '__main__':
    unittest.main()
