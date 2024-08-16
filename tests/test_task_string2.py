import unittest
from Chapter_1.task_string import get_last_symbol


class TestStringMethods(unittest.TestCase):

    def test_get_last_symbol_normal_string(self):
        self.assertEqual(get_last_symbol("Hello"), "o")

    def test_get_last_symbol_single_character(self):
        self.assertEqual(get_last_symbol("a"), "a")

    def test_get_last_symbol_with_spaces(self):
        self.assertEqual(get_last_symbol("Hello World "), " ")

    def test_get_last_symbol_empty_string(self):
        with self.assertRaises(IndexError):
            get_last_symbol("")


if __name__ == '__main__':
    unittest.main()
