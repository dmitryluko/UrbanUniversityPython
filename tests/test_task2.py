import unittest
import math
import sys

from Chapter_1.task2 import solution


class TestTask2Solution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(solution())
        self.assertFalse((9.98 > 9.99) & (math.isclose(1000, 1000.1, abs_tol=1e-9)))


if __name__ == '__main__':
    unittest.main()
