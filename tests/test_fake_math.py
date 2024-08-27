import unittest

from Chapter_4.hw_4_1 import fake_math


class FakeMathTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.num1 = 10
        self.num2 = 5
        self.zero = 0

    def tearDown(self) -> None:
        self.num1 = None
        self.num2 = None
        self.zero = None

    def test_divide_success(self):
        result = fake_math.divide(self.num1, self.num2)
        self.assertEqual(result, 2.0)

    def test_divide_zero_division_error(self):
        result = fake_math.divide(self.num1, self.zero)
        self.assertEqual(result, 'Error')


if __name__ == '__main__':
    unittest.main()
