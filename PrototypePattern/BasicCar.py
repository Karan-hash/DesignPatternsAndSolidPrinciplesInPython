'''
BasicCar Class:

This serves as the prototype interface or abstract class. It defines the clone() method that subclasses will override to provide specific cloning behavior.
'''
import copy, random

class BasicCar:

    def __init__(self, model_name):
        self.model_name = model_name
        self.base_price = 0
        self.on_road_price = 0
    
    def get_model_name(self):
        return self.model_name
    
    def set_model_name(self, model_name):
        self.set_model_name = model_name

    def clone(self):
        # Using deepcopy to ensure all attributes are copied recursively
        return copy.deepcopy(self)
        