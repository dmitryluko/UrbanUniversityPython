import unittest

from Chapter_4.hw_4_1.true_math import divide


class TestTrueMath(unittest.TestCase):

    def test_divide_with_normal_values(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_with_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_with_zero_denominator(self):
        self.assertEqual(divide(10, 0), float('inf'))

    def test_divide_with_both_zero(self):
        self.assertEqual(divide(0, 0), float('inf'))


if __name__ == "__main__":
    unittest.main()
