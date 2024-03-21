import enum
import datetime


class MoneyMachineState(enum.Enum):
    NO_PAPER = 1
    NEED_PAYMENT = 2
    PAID_READY_TO_PRINT = 3
    UNAVAILABLE = 4


class ParkingTicketVendingMachine:
    def __init__(self):
        self._state = MoneyMachineState.NEED_PAYMENT
        self._printing_paper_pieces = 100
        self._message = ''

    def set_message(self, message):
        self._message = message
        print(f"MESSAGE: {message}")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def get_printing_paper_pieces(self):
        return self._printing_paper_pieces

    def add_printing_paper_pieces(self, pieces):
        self._printing_paper_pieces += pieces
        self._message = "Please pay for the parking"

    def pay_for_one_hour_with_credit_card(self):
        print("Paying $5 for parking")
        self._message = "Please click the button to print the ticket"

    def print_ticket(self):
        self._printing_paper_pieces -= 1
        print(f"Ticket valid thru {datetime.datetime.now() + datetime.timedelta(hours=1)}")
        self._message = "Ticket printed. Please collect it."

    def go_down(self):
        print("Trying to revert last transaction")
        self._message = "Vending machine unavailable"


class ParkingTicketVendingMachineState:
    def move_credit_card_to_sensor(self):
        pass

    def press_printing_button(self):
        pass

    def open_machine_and_add_printing_paper_pieces(self):
        pass


class NoPrintingPaperState(ParkingTicketVendingMachineState):
    def __init__(self, machine):
        self._machine = machine

    def move_credit_card_to_sensor(self):
        self._machine.set_message("Cannot pay because there is no printing paper")

    def press_printing_button(self):
        self._machine.set_message("Please call service for additional printing paper")

    def open_machine_and_add_printing_paper_pieces(self):
        self._machine.add_printing_paper_pieces(100)
        self._machine.state = MoneyMachineState.NEED_PAYMENT


class PaidState(ParkingTicketVendingMachineState):
    def __init__(self, machine):
        self._machine = machine

    def move_credit_card_to_sensor(self):
        self._machine.set_message("Already paid. Press button for printout")

    def press_printing_button(self):
        self._machine.print_ticket()
        if self._machine.get_printing_paper_pieces == 0:
            self._machine.state = MoneyMachineState.NO_PAPER
        else:
            self._machine.state = MoneyMachineState.NEED_PAYMENT

    def open_machine_and_add_printing_paper_pieces(self):
        self._machine.set_message("Only authorized personal can add paper")


class StillNeedToPayState(ParkingTicketVendingMachineState):
    def __init__(self, machine):
        self._machine = machine

    def move_credit_card_to_sensor(self):
        self._machine.pay_for_one_hour_with_credit_card()
        if self._machine.state == MoneyMachineState.NEED_PAYMENT:
            self._machine.state = MoneyMachineState.PAID_READY_TO_PRINT

    def press_printing_button(self):
        self._machine.set_message("You need to pay first")

    def open_machine_and_add_printing_paper_pieces(self):
        self._machine.set_message("Only authorized personal can add paper")


class UnavailableState(ParkingTicketVendingMachineState):
    def __init__(self, machine):
        self._machine = machine

    def move_credit_card_to_sensor(self):
        self._machine.set_message("Vending machine unavailable")

    def press_printing_button(self):
        self._machine.go_down()
        self._machine.state = MoneyMachineState.UNAVAILABLE

    def open_machine_and_add_printing_paper_pieces(self):
        self._machine.set_message("Vending machine unavailable")


def main():
    machine = ParkingTicketVendingMachine()
    state = StillNeedToPayState(machine)
    state.open_machine_and_add_printing_paper_pieces()
    state.press_printing_button()
    state.move_credit_card_to_sensor()

    state = PaidState(machine)
    state.move_credit_card_to_sensor()
    state.open_machine_and_add_printing_paper_pieces()
    state.press_printing_button()


if __name__ == '__main__':
    main()
