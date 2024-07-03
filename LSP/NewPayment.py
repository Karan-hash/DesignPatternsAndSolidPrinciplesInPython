from abc import ABC, abstractmethod

class NewPayment(ABC):
    @abstractmethod
    def new_payment(self):
        pass
