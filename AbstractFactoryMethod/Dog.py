# Dog.py
from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def display_me(self):
        pass
