from RegisteredUserPayment import RegisteredUserPayment
from GuestUserPayment import GuestUserPayment

class PaymentHelper:
    def __init__(self):
        self.previous_payments = []
        self.new_payments = []

    def add_previous_payment(self, previous_payment):
        self.previous_payments.append(previous_payment)

    def add_new_payment(self, new_payment_request):
        self.new_payments.append(new_payment_request)

    def show_previous_payments(self):
        for payment in self.previous_payments:
            payment.previous_payment_info()
            print("------")

    def process_new_payments(self):
        for payment in self.new_payments:
            payment.new_payment()
            print("***********")
