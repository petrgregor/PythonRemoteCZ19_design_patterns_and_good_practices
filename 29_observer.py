class BaseObserver:
    def __init__(self, chat_channel):
        self._chat_channel = chat_channel
        chat_channel.subscribe(self)

    def handle_message(self, message, user_type):
        pass

    def get_observer_type(self):
        pass

    def send_message(self, message):
        self._chat_channel.send_message(message, self.get_observer_type())


class UserObserver(BaseObserver):
    def __init__(self, chat_channel, user_name):
        super().__init__(chat_channel)
        self._user_name = user_name
        print(f"User {self._user_name} is joining the {chat_channel.get_name()}")

    def handle_message(self, message, user_type):
        if user_type != 'ADMIN':
            print(f"{self._user_name} sees message {message}")

    def get_observer_type(self):
        return "USER"


class AdminObserver(BaseObserver):
    def __init__(self, chat_channel, admin_name):
        super().__init__(chat_channel)
        self._admin_name = admin_name
        print(f"{self._admin_name} joined {chat_channel.get_name()} as admin")

    def handle_message(self, message, user_type):
        print(f"{self._admin_name} sees {message} from user whose type is {user_type}")

    def get_observer_type(self):
        return "ADMIN"


class ChatChannel:
    def __init__(self, name):
        self._name = name
        self._observers = []
        self._messages = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def send_message(self, message, observer_type):
        self._messages.append(message)
        self.notify_about_change(message, observer_type)

    def notify_about_change(self, message, observer_type):
        for observer in self._observers:
            observer.handle_message(message, observer_type)

    def get_name(self):
        return self._name


def main():
    chat_channel = ChatChannel("design-patterns")

    user_a = UserObserver(chat_channel, "Andrew")
    user_b = UserObserver(chat_channel, "Alice")
    admin_a = AdminObserver(chat_channel, "John")
    admin_b = AdminObserver(chat_channel, "Anna")

    user_a.send_message("Hello all")
    user_b.send_message("Hi Andrew")
    admin_a.send_message("Anna, they can't see what we write")
    admin_b.send_message("Yes, I know")


if __name__ == '__main__':
    main()
