from AnimalFactory import AnimalFactory
from Tiger import Tiger

class TigerFactory(AnimalFactory):

    # Creating and returning a 'Tiger' instance
    def create_animal(self, color) -> Tiger:
        return Tiger(color)