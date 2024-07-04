from NanoCar import NanoCar
from FordCar import FordCar

class CarMaker:
    def __init__(self):
        self.nano = NanoCar("Nano XM624 cc")
        self.ford = FordCar("Ford Aspire")

    def get_nano(self):
        # Returns a cloned instance of Nano
        return self.nano.clone()

    def get_ford(self):
        # Returns a cloned instance of ford
        return self.ford.clone()
