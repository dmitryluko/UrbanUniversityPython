import unittest

from Chapter_6.module_6_1 import Plant


class TestPlant(unittest.TestCase):

    def test_plant_creation_is_correct(self):
        plant = Plant("Rose", False)
        self.assertEqual(plant.name, "Rose")
        self.assertEqual(plant.edible, False)

    def test_plant_creation_with_only_name(self):
        plant = Plant("Rose")
        self.assertEqual(plant.name, "Rose")
        self.assertEqual(plant.edible, False)

    def test_edible_plant_creation(self):
        plant = Plant("Apple", True)
        self.assertEqual(plant.name, "Apple")
        self.assertEqual(plant.edible, True)


if __name__ == "__main__":
    unittest.main()
