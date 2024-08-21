import unittest
from enum import Enum

from Chapter_3.module_3_2 import EmailStatus


class TestEmailStatus(unittest.TestCase):
    def test_class_attributes(self):
        self.assertTrue(hasattr(EmailStatus, 'SUCCESS'))
        self.assertTrue(hasattr(EmailStatus, 'NON_STANDARD_SENDER'))
        self.assertTrue(hasattr(EmailStatus, 'SELF_SEND_ERROR'))
        self.assertTrue(hasattr(EmailStatus, 'INVALID_EMAIL_ERROR'))

    def test_class_name(self):
        self.assertEqual(EmailStatus.__class__.__name__, 'EnumType')

    def test_class_value(self):
        self.assertEqual(EmailStatus.SUCCESS.value,
                         'The letter was successfully sent from {sender} to {recipient}.')
        self.assertEqual(EmailStatus.NON_STANDARD_SENDER.value,
                         'NON-STANDARD SENDER! Message sent from {sender} to {recipient}.')
        self.assertEqual(EmailStatus.SELF_SEND_ERROR.value, 'Illegal to send yourself a message!')
        self.assertEqual(EmailStatus.INVALID_EMAIL_ERROR.value,
                         'Unable to send email from {sender} to {recipient}.')


if __name__ == "__main__":
    unittest.main()
