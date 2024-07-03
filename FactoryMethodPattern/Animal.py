from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def display_behavior(self):
        pass