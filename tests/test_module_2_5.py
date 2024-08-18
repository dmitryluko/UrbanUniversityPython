import unittest

from Chapter_2 import module_2_5


class TestModule25(unittest.TestCase):
    def test_get_matrix(self):
        matrix = module_2_5.get_matrix(3, 3, 0)
        self.assertEqual(matrix, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        matrix = module_2_5.get_matrix(2, 2, 1)
        self.assertEqual(matrix, [[1, 1], [1, 1]])

        matrix = module_2_5.get_matrix(1, 5, 10)
        self.assertEqual(matrix, [[10, 10, 10, 10, 10]])

        matrix = module_2_5.get_matrix(0, 0, 0)
        self.assertEqual(matrix, [])

        matrix = module_2_5.get_matrix(5, 0, 0)
        self.assertEqual(matrix, [[], [], [], [], []])

        matrix = module_2_5.get_matrix(0, 5, 0)
        self.assertEqual(matrix, [])


if __name__ == '__main__':
    unittest.main()
