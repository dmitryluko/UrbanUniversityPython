import unittest
from Chapter_1.task_string import get_second_half


class TestGetSecondHalf(unittest.TestCase):
    def test_get_second_half_odd_length(self):
        self.assertEqual(get_second_half("12345"), "345")

    def test_get_second_half_even_length(self):
        self.assertEqual(get_second_half("Urban"), "ban")

    def test_get_second_half_empty_string(self):
        self.assertEqual(get_second_half(''), '')

    def test_get_second_half_single_character(self):
        self.assertEqual(get_second_half('a'), 'a')

    def test_get_second_half_special_characters(self):
        self.assertEqual(get_second_half('&*()@#'), ')@#')


if __name__ == '__main__':
    unittest.main()
