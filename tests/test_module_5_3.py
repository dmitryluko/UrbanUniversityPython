import unittest

from Chapter_5.module_5_3 import House


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house_1 = House("House 1", 2)
        self.house_2 = House("House 2", 5)
        self.house_3 = House("House 3", 10)


    def test_get_floors(self):
        self.assertEqual(House.get_floors(self.house_2), 5)
        self.assertEqual(House.get_floors(10), 10)
        with self.assertRaises(TypeError):
            House.get_floors("Non-integer value")

    def test_add(self):
        self.house_1 += 2  # Add an integer.
        self.assertEqual(self.house_1.number_of_floors, 4)

        self.house_1 += self.house_2  # Add a House object.
        self.assertEqual(self.house_1.number_of_floors, 9)

    def test_radd(self):
        result = 2 + self.house_1
        self.assertEqual(result.number_of_floors, 4)

    def test_equality(self):
        self.assertEqual(self.house_1, House("House 4", 2))
        self.assertNotEqual(self.house_1, self.house_2)

    def test_comparisons(self):
        self.assertTrue(self.house_3 > 5)
        self.assertTrue(self.house_3 >= 10)
        self.assertTrue(self.house_1 < self.house_2)
        self.assertTrue(self.house_1 <= 2)

    def test_len(self):
        self.assertEqual(len(self.house_3), 10)

    def test_str(self):
        self.assertEqual(str(self.house_1), "Name: House 1, Number of Floors: 2")


if __name__ == '__main__':
    unittest.main()
