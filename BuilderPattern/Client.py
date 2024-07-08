'''
Detailed Explanation:
Initialization of Builders:

When you create a CarBuilder instance, it initializes a Car object with the brand name "Ford".
When you create a MotorCycleBuilder instance, it initializes a MotorCycle object with the brand name "Honda".
Director's Instructions:

CarDirector instructs the CarBuilder to build the car in the sequence: build body, insert wheels, add brand name.
MotorCycleDirector instructs the MotorCycleBuilder to build the motorcycle in the sequence: add brand name, build body, insert wheels.
Adding Parts:

Each builder method (add_brand_name, build_body, insert_wheels) adds specific parts to the vehicle using the add method of the Vehicle class.
These parts are stored in the parts list of the Vehicle.
Displaying the Product:

After the vehicle is built, the show_product method of the Vehicle class is called.
This method prints a message and then iterates through the parts list, printing each part that was added during the building process.
Output Explanation:
When the CarBuilder builds a car:

It adds "Making the car body."
It adds "4 wheels are added to the car."
It adds "Adding the car brand: Ford."
When the MotorCycleBuilder builds a motorcycle:

It adds "Adding the brand name: Honda."
It adds "Making the body of the motorcycle."
It adds "2 wheels are added to the motorcycle."
The show_product method then displays these sequences of construction for both the car and the motorcycle, showing the exact steps that were taken to build them.


'''
from CarBuilder import CarBuilder
from CarDirector import CarDirector
from MotorCycleBuilder import MotorCycleBuilder
from MotorCycleDirector import MotorCycleDirector

if __name__ == '__main__':
    print("***Builder Pattern Demo with Directors***\n")

    # Creating CarBuilder and CarDirector
    car_builder = CarBuilder()
    car_director = CarDirector()
    car = car_director.instruct(car_builder)
    car.show_product()

    print("\n-------\n")

    # Creating MotorCycleBuilder and MotorCycleDirector
    motorcycle_builder = MotorCycleBuilder()
    motorcycle_director = MotorCycleDirector()
    motorcycle = motorcycle_director.instruct(motorcycle_builder)
    motorcycle.show_product()