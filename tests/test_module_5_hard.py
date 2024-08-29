import hashlib
import unittest
from dataclasses import dataclass, field

from Chapter_5.module_5_hard import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User('admin', 'secure_password', 25)

    def test_create_user(self):
        self.assertEqual(self.user.nickname, 'admin')
        self.assertEqual(self.user.password, 'secure_password')
        self.assertEqual(self.user.age, 25)

    def test_hash_password(self):
        hashed_password = int(hashlib.sha256('secure_password'.encode()).hexdigest(), 16)
        self.assertEqual(self.user.hash_password('secure_password'), hashed_password)

    def test_check_password(self):
        self.assertTrue(self.user.check_password('secure_password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_user_str(self):
        self.assertEqual(self.user.__str__(), 'User admin')


if __name__ == "__main__":
    unittest.main()
