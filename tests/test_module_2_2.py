import unittest

from Chapter_2 import module_2_2


class TestModule_2_2(unittest.TestCase):
    def test_get_equals_counter_all_equal(self):
        self.assertEqual(module_2_2.get_equals_counter(1, 1, 1), 3)

    def test_get_equals_counter_two_equal(self):
        self.assertEqual(module_2_2.get_equals_counter(1, 1, 2), 2)
        self.assertEqual(module_2_2.get_equals_counter(2, 1, 2), 2)
        self.assertEqual(module_2_2.get_equals_counter(3, 2, 2), 2)

    def test_get_equals_counter_none_equal(self):
        self.assertEqual(module_2_2.get_equals_counter(1, 2, 3), 0)


if __name__ == '__main__':
    unittest.main()
