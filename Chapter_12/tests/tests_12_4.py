import json
import logging.config
import pathlib
import unittest
from distutils.command.config import config

from Chapter_12.rt_with_exceptions import Runner

logger = logging.getLogger('Test_12_4')


def setup_logging():
    config_file = pathlib.Path('logging_config.json')

    with config_file.open() as fd:
        config = json.load(fd)

    logging.config.dictConfig(config=config)


class RunnerTest(unittest.TestCase):

    def setUp(self):
        setup_logging()
        logger.debug('Starting "setUp"')
        self.is_frozen = False

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
        logger.info('Starting "test_walk_to_raise" with Exception : ')
        with self.assertRaises(ValueError):
            _ = Runner(name="John Doe", speed=-5)

    @_skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @_skip_if_frozen
    def test_run_to_rise(self):
        logger.info('Starting "test_run with Exception : "')

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
            logger.info('"test_challenge" выполнен успешно')
        except Exception as e:
            logger.exception("Exception in test_challenge")
            self.fail("Exception was raised: " + str(e))


if __name__ == '__main__':
    unittest.main()
