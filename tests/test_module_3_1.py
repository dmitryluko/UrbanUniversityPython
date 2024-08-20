import unittest

from Chapter_3.module_3_1 import call_counter


class TestModule31(unittest.TestCase):

    def setUp(self):
        @call_counter
        def dummy_func(val):
            return val * 2

        self.dummy_func = dummy_func

    def test_count_init(self):
        self.assertEqual(self.dummy_func.count, 0)

    def test_call_counter_increase(self):
        self.dummy_func(10)
        self.assertEqual(self.dummy_func.count, 1)

    def test_multiple_calls(self):
        for _ in range(5):
            self.dummy_func(5)
        self.assertEqual(self.dummy_func.count, 5)

    def test_result_of_wrapped_function(self):
        res = self.dummy_func(5)
        self.assertEqual(res, 10)

    def test_multiple_instances_count(self):
        @call_counter
        def another_dummy_func(val):
            return val * 3

        for _ in range(3):
            another_dummy_func(3)
        self.assertEqual(another_dummy_func.count, 3)
        for _ in range(5):
            self.dummy_func(4)
        self.assertEqual(self.dummy_func.count, 5)


if __name__ == "__main__":
    unittest.main()
