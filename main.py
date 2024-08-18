"""
Just runs all Tests
"""
import unittest


def load_tests():
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    load_tests()
