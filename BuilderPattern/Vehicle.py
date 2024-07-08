from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show_product(self):
        print("These are the construction sequences:")
        for part in self.parts:
            print(part)
