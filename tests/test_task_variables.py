import unittest
from Chapter_1.task_variables import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        expected_output = ("Курс: Python, всего задач: 12, затрачено часов:"
                           " 1.5, среднее время выполнения 0.125 часа.")
        self.assertEqual(solution(), expected_output)

    def test_solution_type(self):
        self.assertTrue(type(solution()) is str)


if __name__ == '__main__':
    unittest.main()
