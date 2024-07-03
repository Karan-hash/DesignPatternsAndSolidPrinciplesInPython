from abc import ABC, abstractmethod

class FaxDevice(ABC):

    @abstractmethod
    def sendFax(self):
        pass