class Component:
    def send_request(self, context=None):
        pass


class ActionAppliedMessage(Component):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def display_info(self):
        print("Action was applied successfully")

    def send_request(self, context=None):
        self._mediator.send_info(self, "ActionAppliedMessage")


class SelectOptions(Component):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def display_options(self):
        print("Options are: Save, Load, Restart")

    def choose_save(self):
        print("Status was saved")

    def choose_load(self):
        print("Loading previous data")

    def choose_restart(self):
        print("Status is restarting")

    def hide_options(self):
        print("Hiding options")

    def send_request(self, context=None):
        self._mediator.send_info(self, context if context else "displayOptions")


class WarningMessage(Component):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def show_warning_message(self):
        print("Are you sure?")

    def hide_warning(self):
        print("")

    def send_request(self, context=None):
        self._mediator.send_info(self, "WarningMessage")


class Mediator:
    def send_info(self, requester, context):
        pass


class UserActionMediator(Mediator):
    def __init__(self, action_applied_message, select_options, warning_message):
        self._action_applied_message = action_applied_message
        self._select_options = select_options
        self._warning_message = warning_message
        self._action_applied_message.set_mediator(self)
        self._select_options.set_mediator(self)
        self._warning_message.set_mediator(self)

    def send_info(self, requester, context):
        if requester == self._action_applied_message:
            self._action_applied_message.display_info()
            self._warning_message.hide_warning()
            self._select_options.hide_options()
        elif requester == self._select_options:
            if context == "load":
                self._select_options.choose_load()
                self._action_applied_message.display_info()
            elif context == "restart":
                self._select_options.choose_restart()
                self._warning_message.show_warning_message()
            elif context == "save":
                self._select_options.choose_save()
                self._action_applied_message.display_info()
            elif context == "displayOptions":
                self._select_options.display_options()
        elif requester == self._warning_message:
            if context == "hide":
                self._warning_message.hide_warning()
            else:
                self._warning_message.show_warning_message()


def main():
    action_applied_message = ActionAppliedMessage()
    select_options = SelectOptions()
    warning_message = WarningMessage()

    mediator = UserActionMediator(action_applied_message, select_options, warning_message)

    print("--------------------------")
    select_options.send_request()
    print("--------------------------")
    select_options.send_request("load")
    print("--------------------------")
    select_options.send_request("save")
    print("--------------------------")
    select_options.send_request("restart")
    print("--------------------------")
    select_options.send_request("hide")


if __name__ == '__main__':
    main()
