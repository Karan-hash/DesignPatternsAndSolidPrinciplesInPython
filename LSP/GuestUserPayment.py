from NewPayment import NewPayment

class GuestUserPayment(NewPayment):
    def __init__(self):
        self.name = "guest"

    def new_payment(self):
        print(f"Processing {self.name}'s current payment request.")
        # Some code, if any
