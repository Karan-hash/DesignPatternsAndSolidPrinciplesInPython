from Builder import Builder
from Car import Car
class CarBuilder(Builder):
    def __init__(self):
        self.car = Car("Ford")
    
    def add_brand_name(self):
        self.car.add("Adding the car brand: " + self.car.brand_name)

    def build_body(self):
        self.car.add("Making the car body.")

    def insert_wheels(self):
        self.car.add("4 wheels are added to the car.")

    def get_vehicle(self):
        return self.car
