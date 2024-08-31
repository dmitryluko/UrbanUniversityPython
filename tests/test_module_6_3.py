import unittest

from Chapter_6.module_6_1 import EatMixin


class TestEatMixin(unittest.TestCase):

    def setUp(self):
        """Prepare a fresh object for each test"""
        self.test_name = 'Test'
        self.eat_mixin = EatMixin()
        self.eat_mixin.name = self.test_name



    def test_name_default(self):
        """Object should have a name"""
        self.assertEqual(self.eat_mixin.name, self.test_name)

    def test_name_is_string(self):
        """Name attribute should be a string"""
        self.assertIsInstance(self.eat_mixin.name, str)


if __name__ == '__main__':
    unittest.main()
