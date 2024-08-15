# Importing necessary module and classes
import unittest
from Chapter_1.task1 import solution


# Defining a class for the test cases
class TestSolution(unittest.TestCase):
    def test_output_type(self):
        """
        Test if the output of the function is a float.
        """
        self.assertIsInstance(solution(), float)

    def test_output_value(self):
        """
        Test if the function computes the correct output.
        """
        self.assertEqual(solution(), 15)


# Running the tests
if __name__ == "__main__":
    unittest.main()
