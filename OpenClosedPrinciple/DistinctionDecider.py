from abc import ABC, abstractmethod

class DistinctionDecider(ABC):
    @abstractmethod
    def evaluate_distinction(self, student):
        pass
