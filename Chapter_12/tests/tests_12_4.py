import json
import logging.config
import pathlib
import unittest

from functools import wraps
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
        self.is_frozen = False
        logger.info('-' * 50)

    @staticmethod
    def _skip_if_frozen(func):
        # Assuming the skipping logic based on 'is_frozen'
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if getattr(self, 'is_frozen', False):
                self.skipTest("Skipping because the instance is frozen")
                logger.warning('Test is frozen!')
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @_skip_if_frozen
    def test_runner_to_raise_value_err(self):
        with self.assertRaises(ValueError) as cm:
            _ = Runner(name="John Doe", speed=-5)

        logger.info(f'Test to wrong args VALUE for Runner() produces : {cm.exception}')

        self.assertTrue(isinstance(cm.exception, ValueError))
        self.assertEqual(cm.exception.args[0], 'Скорость не может быть отрицательной, сейчас -5')

        logger.info(f'{self.test_runner_to_raise_value_err.__name__}() : PASSED')

    @_skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

        logger.info(f'{self.test_run.__name__}(): PASSED')

    @_skip_if_frozen
    def test_runner_to_rise_type_err(self):

        with self.assertRaises(TypeError) as cm:
            _ = Runner(name=12345, speed=10)

        logger.info(f'Test to wrong args TYPE for Runner() produces : {cm.exception}')

        self.assertTrue(isinstance(cm.exception, TypeError))
        self.assertEqual(cm.exception.args[0], 'Имя может быть только строкой, передано int')

        logger.info(f'{self.test_runner_to_rise_type_err.__name__}() : PASSED')

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

        logger.info(f'{self.test_challenge.__name__}() : PASSED')


if __name__ == '__main__':
    unittest.main()
