import unittest
from Chapter_1.task_string import get_first_symbol


class TestGetFirstSymbol(unittest.TestCase):

    def test_get_first_symbol_empty_string(self):
        self.assertRaises(IndexError, get_first_symbol, '')

    def test_get_first_symbol_single_character(self):
        self.assertEqual(get_first_symbol('a'), 'a')

    def test_get_first_symbol_multiple_characters(self):
        self.assertEqual(get_first_symbol('Python'), 'P')

    def test_get_first_symbol_with_whitespace(self):
        self.assertEqual(get_first_symbol(' Hello'), ' ')


if __name__ == "__main__":
    unittest.main()
