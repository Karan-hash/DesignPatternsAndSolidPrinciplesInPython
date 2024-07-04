# WildTiger.py
from Tiger import Tiger
from Dog import Dog

class WildTiger(Tiger):
    def __init__(self, color):
        print(f"A wild tiger with {color} color is created.")

    def about_me(self):
        print("The wild tiger says: I prefer hunting in jungles. Halum.")

    def invite_dog(self, dog):
        print(f"The wild tiger says: I saw a {dog} in the jungle.")

    def __str__(self):
        return "wild tiger"
