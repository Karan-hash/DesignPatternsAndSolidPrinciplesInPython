from PaymentHelper import PaymentHelper
from RegisteredUserPayment import RegisteredUserPayment
from GuestUserPayment import GuestUserPayment

if __name__ == "__main__":
    print("***A demo that follows the LSP.***\n")

    helper = PaymentHelper()

    # Instantiating two registered users.
    robin = RegisteredUserPayment("Robin")
    jack = RegisteredUserPayment("Jack")

    # Instantiating a guest user's payment.
    guest_user1 = GuestUserPayment()

    # Consolidating the previous payment's info to the helper.
    helper.add_previous_payment(robin)
    helper.add_previous_payment(jack)

    # Consolidating new payment requests to the helper.
    helper.add_new_payment(robin)
    helper.add_new_payment(jack)
    helper.add_new_payment(guest_user1)

    # Retrieve all the previous payments of registered users.
    helper.show_previous_payments()

    # Process all new payment requests from all users.
    helper.process_new_payments()
