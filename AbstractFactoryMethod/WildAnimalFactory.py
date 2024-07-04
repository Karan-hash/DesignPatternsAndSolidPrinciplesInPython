# WildAnimalFactory.py
from AnimalFactory import AnimalFactory
from WildDog import WildDog
from WildTiger import WildTiger

class WildAnimalFactory(AnimalFactory):
    def __init__(self):
        print("You opted for a wild animal factory.\n")

    def create_tiger(self, color):
        return WildTiger(color)

    def create_dog(self, color):
        return WildDog(color)
