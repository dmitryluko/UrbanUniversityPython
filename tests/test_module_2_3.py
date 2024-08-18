# test_module_2_3.py
import unittest

from Chapter_2.module_2_3 import get_positive_numbers


class TestModule23(unittest.TestCase):
    def setUp(self) -> None:
        self.my_list_1 = [1, 2, 3, -4, 5, 6]
        self.my_list_2 = [-1, -2, -3, 4, 5, 6]
        self.my_list_3 = [1, 2, 3, 4, 5, 6]
        self.my_list_4 = [-1, -2, -3, -4, -5, -6]
        self.my_list_5 = [1, 3, 0, -4, 5, 6]

    def test_get_positive_numbers1(self):
        result = get_positive_numbers(self.my_list_1)
        self.assertEqual(result, [1, 2, 3])

    def test_get_positive_numbers3(self):
        result = get_positive_numbers(self.my_list_3)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_get_positive_numbers_zero(self):
        result = get_positive_numbers(self.my_list_5)
        self.assertEqual(result, [1, 3])


if __name__ == '__main__':
    unittest.main()
