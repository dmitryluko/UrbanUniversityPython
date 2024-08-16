import unittest
from Chapter_1.task_string import get_every_second_symbol


class TestGetEverySecondSymbol(unittest.TestCase):

    def test_all_alphabet(self):
        self.assertEqual(get_every_second_symbol("abcdefghijklmnopqrstuvwxyz"), "bdfhjlnprtvxz")

    def test_empty_string(self):
        self.assertEqual(get_every_second_symbol(""), "")

    def test_single_character(self):
        self.assertEqual(get_every_second_symbol("a"), "")

    def test_numbers(self):
        self.assertEqual(get_every_second_symbol("123456789"), "2468")


if __name__ == '__main__':
    unittest.main()
