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

    def add_printing_paper_pieces(self, pieces):
        self._printing_paper_pieces += pieces
        if self._state == MoneyMachineState.NO_PAPER:
            self._state = MoneyMachineState.NEED_PAYMENT
        self._message = "Please pay for the parking"

    def pay_for_one_hour_with_credit_card(self):
        if self._state == MoneyMachineState.NEED_PAYMENT:
            print("Paying $5 for parking")
            self._state = MoneyMachineState.PAID_READY_TO_PRINT
        self._message = "Please click the button to print the ticket"

    def print_ticket(self):
        if self._state == MoneyMachineState.PAID_READY_TO_PRINT:
            self._printing_paper_pieces -= 1
            print(f"Ticket valid thru {datetime.datetime.now() + datetime.timedelta(hours=1)}")
            if self._printing_paper_pieces == 0:
                self._state = MoneyMachineState.NO_PAPER
            else:
                self._state = MoneyMachineState.NEED_PAYMENT
        self._message = "Ticket printed. Please collect it."

    def go_down(self):
        if self._state == MoneyMachineState.PAID_READY_TO_PRINT:
            print("Trying to revert last transaction")
        self._state = MoneyMachineState.UNAVAILABLE
        self._message = "Money machine unavailable"

    def show_message(self):
        print(self._message)


def main():
    parking_ticket_vending_machine = ParkingTicketVendingMachine()
    parking_ticket_vending_machine.show_message()
    parking_ticket_vending_machine.pay_for_one_hour_with_credit_card()


if __name__ == '__main__':
    main()
