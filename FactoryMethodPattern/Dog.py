from Animal import Animal

class Dog(Animal):
    def __init__(self, color):
       print(f"\nA dog is created with color as {color}")

    def display_behavior(self):
        print("It says: Bow-Wow.")
        print("It prefers barking.")
