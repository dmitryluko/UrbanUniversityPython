import unittest
from Chapter_1.task_string import reverse_string


class TestReverseString(unittest.TestCase):

    def test_reverse_string_regular(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_numbers(self):
        self.assertEqual(reverse_string("1234567890"), "0987654321")

    def test_reverse_string_mixed(self):
        self.assertEqual(reverse_string("H3ll0 W0rld!"), "!dlr0W 0ll3H")


if __name__ == '__main__':
    unittest.main()
