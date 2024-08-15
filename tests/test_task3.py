import unittest
from Chapter_1 import task3


class TestSolution(unittest.TestCase):
    def test_solution(self):
        result = task3.solution()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 6)
        self.assertEqual(result[1], 8)
        self.assertFalse(result[2], True)


if __name__ == '__main__':
    unittest.main()
