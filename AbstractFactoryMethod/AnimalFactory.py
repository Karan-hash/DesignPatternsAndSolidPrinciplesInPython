from abc import ABC, abstractmethod

class AnimalFactory(ABC):
    @abstractmethod
    def create_tiger(self, color):
        pass

    @abstractmethod
    def create_dog(self, color):
        pass