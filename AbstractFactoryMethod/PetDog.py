# PetDog.py
from Dog import Dog

class PetDog(Dog):
    def __init__(self, color):
        print(f"A pet dog with {color} color is created.")

    def display_me(self):
        print("The pet dog says: Bow-Wow. I prefer to stay at home.")

    def __str__(self):
        return "pet dog"
