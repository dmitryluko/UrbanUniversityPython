import unittest

from Chapter_3 import module_3_hard


class TestModule3Hard(unittest.TestCase):

    def test_calculate_structure_sum_with_int(self):
        actual = module_3_hard.calculate_structure_sum(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_str(self):
        actual = module_3_hard.calculate_structure_sum("string")
        expected = 6
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_list(self):
        actual = module_3_hard.calculate_structure_sum([1, 2, "words", [1, 2], {"key": 2}])
        expected = 16
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_tuple(self):
        actual = module_3_hard.calculate_structure_sum((1, 2, "words", [1, 2], {"key": 2}))
        expected = 16
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_set(self):
        actual = module_3_hard.calculate_structure_sum({1, 2, "words"})
        expected = 8
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_dict(self):
        actual = module_3_hard.calculate_structure_sum({"key": 2, 2: "words", "nested": {"key": "value"}})
        expected = 26
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_object(self):
        actual = module_3_hard.calculate_structure_sum(object())
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_structure_sum_with_unknown_data_type_raises_exception(self):
        with self.assertRaises(Exception):
            module_3_hard.calculate_structure_sum(None)


if __name__ == '__main__':
    unittest.main()
