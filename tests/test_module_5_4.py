import unittest

from Chapter_5 import module_5_4


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house_a = module_5_4.House("HouseA", 3)
        self.house_b = module_5_4.House("HouseB", 2)

    def test_initialization(self):
        self.assertEqual(self.house_a.name, "HouseA")
        self.assertEqual(self.house_a.number_of_floors, 3)

    def test_history(self):
        self.assertIn("HouseA", module_5_4.House.houses_history)
        self.assertIn("HouseB", module_5_4.House.houses_history)

    def test_go_to(self):
        self.assertIsNone(self.house_a.go_to(1))

    def test_get_floors(self):
        self.assertEqual(module_5_4.House.get_floors(5), 5)
        self.assertEqual(module_5_4.House.get_floors(self.house_a), 3)

    def test_addition_operations(self):
        result_house = self.house_a + self.house_b
        self.assertEqual(result_house.number_of_floors, 5)
        self.assertEqual(result_house.name, "HouseA")

        self.house_a += self.house_b
        self.assertEqual(self.house_a.number_of_floors, 5)

    def test_comparisons(self):
        self.assert_house_equality(self.house_a, self.house_b)
        self.assert_house_inequality(self.house_a, self.house_b)
        self.assert_house_greater(self.house_a, self.house_b)
        self.assert_house_greater_equal(self.house_a, self.house_b)
        self.assert_house_less(self.house_a, self.house_b)
        self.assert_house_less_equal(self.house_a, self.house_b)

    def assert_house_equality(self, house_a, house_b):
        self.assertFalse(house_a == house_b)

    def assert_house_inequality(self, house_a, house_b):
        self.assertTrue(house_a != house_b)

    def assert_house_greater(self, house_a, house_b):
        self.assertTrue(house_a > house_b)

    def assert_house_greater_equal(self, house_a, house_b):
        self.assertTrue(house_a >= house_b)

    def assert_house_less(self, house_a, house_b):
        self.assertFalse(house_a < house_b)

    def assert_house_less_equal(self, house_a, house_b):
        self.assertFalse(house_a <= house_b)
        self.assertTrue(self.house_a != self.house_b)
        self.assertTrue(self.house_a > self.house_b)
        self.assertTrue(self.house_a >= self.house_b)
        self.assertFalse(self.house_a < self.house_b)
        self.assertFalse(self.house_a <= self.house_b)

    def test_len(self):
        self.assertEqual(len(self.house_a), 3)

    def test_str(self):
        self.assertEqual(str(self.house_a), 'Name: HouseA, Number of Floors: 3')


if __name__ == "__main__":
    unittest.main()
