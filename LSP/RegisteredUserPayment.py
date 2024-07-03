from PreviousPayment import PreviousPayment
from NewPayment import NewPayment

class RegisteredUserPayment(NewPayment, PreviousPayment):
    def __init__(self, name):
        self.name = name

    def previous_payment_info(self):
        print(f"Retrieving {self.name}'s last payment details.")
        # Some code, if any

    def new_payment(self):
        print(f"Processing {self.name}'s current payment request.")
        # Some code, if any
