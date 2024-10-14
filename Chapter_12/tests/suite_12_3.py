# suite_12_3.py

import unittest

from tests_12_4 import RunnerTest
from tests_12_3 import TournamentTest


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromNames(['suite_12_3'])
    runner.run(suite)
