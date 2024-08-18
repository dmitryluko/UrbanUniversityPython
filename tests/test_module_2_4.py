import unittest

from Chapter_2.module_2_4 import is_prime


class TestIsPrimeMethod(unittest.TestCase):

    def test_is_prime_valid(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))

    def test_is_prime_invalid(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(15))

    # def test_is_prime_large(self):
    #     self.assertTrue(is_prime(100000000003))
    #     self.assertFalse(is_prime(100000000006))


if __name__ == '__main__':
    unittest.main()
