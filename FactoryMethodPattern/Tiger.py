from Animal import Animal

class Tiger(Animal):
    def __init__(self, color):
        print(f"\nA tiger is created with color as {color}")

    def display_behavior(self):
        print("Tiger says: Halum.")
        print("It loves to roam in a jungle.")