# Liskov substitution principle

# BAD solution
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"Send {message} to {email}")


class SMS(Notification):
    def notify(self, message, phone):
        print(f"Send {message} to {phone}")


if __name__ == "__main__":
    notification = Email()
    notification.notify(message="Ahoj", email="john@smith.com")  # nelze změnit notifikaci na SMS
"""

# GOOD solution with Liskov substitution principle
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} to {self.phone}")


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


if __name__ == "__main__":
    contact = Contact(name="John", email="john@wick.com", phone="123456789")

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    sms_notification.notify("Posílám SMS")
    email_notification.notify("Posílám Email")

    my_notification = SMS(contact.phone)
    my_notification.notify("New message")
    my_notification.notify("New message 2")
    my_notification.notify("New message 3")
    my_notification.notify("New message 4")
    my_notification.notify("New message 5")
