from AnimalFactory import AnimalFactory
from Dog import Dog

class DogFactory(AnimalFactory):

    # Creating and returning a 'Dog' instance
    def create_animal(self, color) -> Dog:
        return Dog(color)
