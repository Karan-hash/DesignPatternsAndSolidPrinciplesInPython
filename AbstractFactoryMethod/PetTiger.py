# PetTiger.py
from Tiger import Tiger
from Dog import Dog

class PetTiger(Tiger):
    def __init__(self, color):
        print(f"A pet tiger with {color} color is created.")

    def about_me(self):
        print("The pet tiger says: Halum. I play in an animal circus.")

    def invite_dog(self, dog):
        print(f"The pet tiger says: I saw a {dog} in my town.")

    def __str__(self):
        return "pet tiger"
