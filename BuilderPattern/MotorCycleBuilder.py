from Builder import Builder
from MotorCycle import MotorCycle
class MotorCycleBuilder(Builder):
    def __init__(self):
        self.motor_cycle = MotorCycle("Honda")

    def add_brand_name(self):
        self.motor_cycle.add("Adding the brand name: " + self.motor_cycle.brand_name)

    def build_body(self):
        self.motor_cycle.add("Making the body of the motorcycle.")

    def insert_wheels(self):
        self.motor_cycle.add("2 wheels are added to the motorcycle.")

    def get_vehicle(self):
        return self.motor_cycle