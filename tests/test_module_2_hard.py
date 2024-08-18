import unittest

from Chapter_2.module_2_hard import is_valid_pair


class TestPairValidity(unittest.TestCase):
    def test_is_valid_pair_balanced(self):
        self.assertFalse(is_valid_pair(10, 1, 1))

    def test_is_valid_pair_valid(self):
        self.assertTrue(is_valid_pair(6, 2, 1))

    def test_is_valid_pair_large_values(self):
        self.assertFalse(is_valid_pair(1000000, 500000, 500000))

    def test_is_valid_pair_large_values_valid(self):
        self.assertTrue(is_valid_pair(1000000, 250000, 750000))


if __name__ == "__main__":
    unittest.main()
