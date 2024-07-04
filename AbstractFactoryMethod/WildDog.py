# WildDog.py
from Dog import Dog

class WildDog(Dog):
    def __init__(self, color):
        print(f"A wild dog with {color} color is created.")

    def display_me(self):
        print("The wild dog says: I prefer to roam freely in jungles. Bow-Wow.")

    def __str__(self):
        return "wild dog"
