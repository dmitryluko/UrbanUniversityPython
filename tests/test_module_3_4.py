import unittest

from Chapter_3.module_3_2 import are_valid_emails


class TestValidEmails(unittest.TestCase):

    def test_both_are_valid(self):
        self.assertTrue(are_valid_emails("test@test.com", "test2@test.com"))

    def test_both_are_invalid(self):
        self.assertFalse(are_valid_emails("test", "test2"))

    def test_only_sender_is_valid(self):
        self.assertFalse(are_valid_emails("test@test.com", "test2"))

    def test_only_recipient_is_valid(self):
        self.assertFalse(are_valid_emails("test", "test2@test.com"))

    def test_empty_strings(self):
        self.assertFalse(are_valid_emails("", ""))

    def test_valid_email_with_unusual_symbols(self):
        self.assertTrue(are_valid_emails("test@te$t.com", "test2@te$st.com"))


if __name__ == "__main__":
    unittest.main()
