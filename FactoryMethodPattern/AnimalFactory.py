from abc import ABC, abstractmethod
from Animal import Animal

class AnimalFactory(ABC):

    def create_and_display_animal(self, color):
        print("Showing common behaviors of an animal.")
        animal = self.create_animal(color)
        animal.display_behavior()
    '''
    This is the "factory method"
    Notice that I defer the instantiation
    process to the subclasses.
    '''
    @abstractmethod
    def create_animal(self, color) -> Animal :
        pass