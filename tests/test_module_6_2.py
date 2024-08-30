import unittest

from Chapter_6.module_6_1 import Animal, Plant


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.lion = Animal("Lion")
        self.grapes = Plant("Grapes")

    def test_eat_edible_food(self):
        self.grapes.edible = True
        self.lion.eat(self.grapes)
        self.assertTrue(self.lion.fed)

    def test_eat_non_edible_food(self):
        self.grapes.edible = False
        self.lion.eat(self.grapes)
        self.assertFalse(self.lion.alive)

    def test_initial_conditions(self):
        self.assertEqual(self.lion.name, "Lion")
        self.assertTrue(self.lion.alive)
        self.assertFalse(self.lion.fed)

    def test_name(self):
        self.assertEqual(self.lion.name, "Lion")

    def test_alive(self):
        self.assertEqual(self.lion.alive, True)

    def test_fed(self):
        self.assertEqual(self.lion.fed, False)


if __name__ == '__main__':
    unittest.main()
