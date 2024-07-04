# PetAnimalFactory.py
from AnimalFactory import AnimalFactory
from PetDog import PetDog
from PetTiger import PetTiger

class PetAnimalFactory(AnimalFactory):
    def __init__(self):
        print("You opted for a pet animal factory.\n")

    def create_tiger(self, color):
        return PetTiger(color)

    def create_dog(self, color):
        return PetDog(color)
