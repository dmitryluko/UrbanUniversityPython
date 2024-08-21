"""
Tests output:

Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!

"""
from enum import Enum

# Constants
DOMAIN_WHITELIST = ['.com', '.ru', '.net']
DEFAULT_SENDER = 'university.help@gmail.com'


class EmailStatus(Enum):
    SUCCESS = 'The letter was successfully sent from {sender} to {recipient}.'
    NON_STANDARD_SENDER = 'NON-STANDARD SENDER! Message sent from {sender} to {recipient}.'
    SELF_SEND_ERROR = 'Illegal to send yourself a message!'
    INVALID_EMAIL_ERROR = 'Unable to send email from {sender} to {recipient}.'


class EmailError(Exception):
    pass


class InvalidEmailError(EmailError):
    pass


class SelfSendError(EmailError):
    pass


def is_valid_email(email: str) -> bool:
    return '@' in email and email.split('@')[-1].endswith(tuple(DOMAIN_WHITELIST))


def are_valid_emails(sender: str, recipient: str) -> bool:
    return is_valid_email(sender) and is_valid_email(recipient)


def is_not_self_sending(sender: str, recipient: str) -> bool:
    return sender != recipient


def construct_report(sender: str, recipient: str, status: EmailStatus) -> str:
    if status == EmailStatus.SUCCESS:
        return status.value.format(sender=DEFAULT_SENDER, recipient=recipient)
    elif status == EmailStatus.NON_STANDARD_SENDER:
        return status.value.format(sender=sender, recipient=recipient)
    return status.value


def validate_email_status(sender: str, recipient: str) -> EmailStatus:
    if not are_valid_emails(sender, recipient):
        return EmailStatus.INVALID_EMAIL_ERROR
    if not is_not_self_sending(sender, recipient):
        return EmailStatus.SELF_SEND_ERROR
    if sender == DEFAULT_SENDER:
        return EmailStatus.SUCCESS
    return EmailStatus.NON_STANDARD_SENDER


def emulate_email_sending(message: str, sender: str, recipient: str) -> None:
    print(f"Emulating sending email from {sender} to {recipient} with message: {message}")


def send_email(message: str, recipient: str, sender: str = DEFAULT_SENDER) -> str:
    try:
        status = validate_email_status(sender, recipient)
        if status in [EmailStatus.INVALID_EMAIL_ERROR, EmailStatus.SELF_SEND_ERROR]:
            raise EmailError(status.value)
        emulate_email_sending(message, sender, recipient)
        return construct_report(sender, recipient, status)
    except EmailError as e:
        return str(e)


def main():
    print(send_email('This message is for connection testing', recipient='vasyok1337@gmail.com'))
    print(send_email('You see this message as the best course student!', sender='urban.info@gmail.com',
                     recipient='urban.fan@mail.ru'))
    print(
        send_email('Please correct the assignment', sender='urban.teacher@mail.uk', recipient='urban.student@mail.ru'))
    print(send_email('Reminding myself about the webinar', sender='urban.teacher@mail.ru',
                     recipient='urban.teacher@mail.ru'))


if __name__ == '__main__':
    main()
