'''
Nano and Ford Classes (Concrete Prototypes):

These classes extend BasicCar and provide concrete implementations of the clone() method.
Each class initializes specific properties (base_price, on_road_price) unique to the type of car.
'''
from BasicCar import BasicCar
import random

class NanoCar(BasicCar):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.base_price = 5000
        self.on_road_price = self.base_price + random.randint(0, 1000)
    
    def clone(self):
        return super().clone()
    
    def __str__(self):
        return f"Model: {self.model_name}\nPrice: {self.on_road_price}"