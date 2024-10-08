# suite_12_3.py

import unittest

from runner_test import RunnerTest
from tests_12_2 import TournamentTest


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromNames(['suite_12_3'])
    runner.run(suite)
