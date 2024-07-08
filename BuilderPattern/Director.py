from abc import ABC, abstractmethod

class Director(ABC):
    # Director knows how to use/instruct the builder to create a vehicle.
    @abstractmethod
    def instruct(self, builder):
        pass