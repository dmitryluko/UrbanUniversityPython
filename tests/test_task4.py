import unittest
from Chapter_1.task4 import solution1


class TestSolution1(unittest.TestCase):

    def test_solution1_case_1(self):
        self.assertEqual(solution1("14.6"), 6, "Expected output is 6")

    def test_solution1_case_2(self):
        self.assertEqual(solution1("10.1"), 1, "Expected output is 1")

    def test_solution1_case_3(self):
        self.assertEqual(solution1("1.9"), 9, "Expected output is 9")

    def test_solution1_case_4(self):
        self.assertEqual(solution1("2928.0"), 0, "Expected output is 0")


if __name__ == '__main__':
    unittest.main()
