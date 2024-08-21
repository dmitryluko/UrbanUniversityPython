import unittest

from Chapter_3.module_3_2 import is_valid_email


class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@gmail.com"))

    def test_email_without_at_symbol(self):
        self.assertFalse(is_valid_email("testgmail.com"))


if __name__ == "__main__":
    unittest.main()
