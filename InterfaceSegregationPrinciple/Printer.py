from abc import ABC, abstractmethod

class Printer(ABC):

    @abstractmethod
    def printDocument(self):
        pass