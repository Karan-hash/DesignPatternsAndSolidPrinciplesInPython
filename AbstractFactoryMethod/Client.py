'''
The abstract factory is basically a factory of factories. It creates a family of related objects, 
but it does not depend on the concrete classes. In this pattern, you encapsulate a group of individual 
factories that have a common theme. In this process, you do not instantiate a class directly; 
instead, you get a concrete factory and thereafter create products using the factory.

Explanation:
Abstract Factory and Products:

AnimalFactory, Tiger, and Dog are abstract classes with abstract methods.
Concrete Factories:

WildAnimalFactory and PetAnimalFactory implement the create_tiger and create_dog methods.
Concrete Products:

WildTiger and WildDog implement Tiger and Dog, respectively.
PetTiger and PetDog implement Tiger and Dog, respectively.
Client Code:

The client code demonstrates the use of WildAnimalFactory and PetAnimalFactory to create and interact with the animal objects.
'''
from WildAnimalFactory import WildAnimalFactory
from PetAnimalFactory import PetAnimalFactory

if __name__ == "__main__":
    print("*** Abstract Factory Pattern Demo ***\n")

    # Making a wild dog and wild tiger through WildAnimalFactory
    animal_factory = WildAnimalFactory()
    dog = animal_factory.create_dog("white")
    tiger = animal_factory.create_tiger("golden and cinnamon")
    dog.display_me()
    tiger.about_me()
    tiger.invite_dog(dog)
    print("\n************\n")

    # Making a pet dog and pet tiger through PetAnimalFactory now
    animal_factory = PetAnimalFactory()

    dog = animal_factory.create_dog("Dog")
    tiger = animal_factory.create_tiger("yellow")
    dog.display_me()
    tiger.about_me()
    tiger.invite_dog(dog)
    print("\n************\n")
