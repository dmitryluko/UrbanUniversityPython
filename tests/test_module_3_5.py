import unittest
from unittest.mock import patch, Mock

from Chapter_3.module_3_2 import send_email, EmailStatus, EmailError, DEFAULT_SENDER


class TestSendEmail(unittest.TestCase):

    @patch('Chapter_3.module_3_2.validate_email_status')
    @patch('Chapter_3.module_3_2.emulate_email_sending')
    @patch('Chapter_3.module_3_2.construct_report')
    def test_send_email_success(self, mock_construct_report, mock_emulate_email_sending, mock_validate_email_status):
        mock_construct_report.return_value = "Report"
        mock_validate_email_status.return_value = None

        result = send_email("Hello!", "recipient@example.com")

        mock_validate_email_status.assert_called_with(DEFAULT_SENDER, "recipient@example.com")
        mock_emulate_email_sending.assert_called_with("Hello!", DEFAULT_SENDER, "recipient@example.com")
        mock_construct_report.assert_called_with(DEFAULT_SENDER, "recipient@example.com", None)
        self.assertEqual(result, "Report")



if __name__ == "__main__":
    unittest.main()
