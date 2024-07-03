from abc import ABC, abstractmethod

class PreviousPayment(ABC):
    @abstractmethod
    def previous_payment_info(self):
        pass
