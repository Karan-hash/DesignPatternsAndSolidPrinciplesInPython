'''
In the provided Python implementation, the copy.deepcopy function is used to clone the objects, which performs a deep copy of the objects.

Deep Copy vs. Shallow Copy
Shallow Copy:

A shallow copy of an object is a new object whose instance variables are identical to the original object. However, the nested objects within the original object are not copied; instead, references to these objects are shared.
In Python, you can create a shallow copy using the copy.copy function.
Deep Copy:

A deep copy creates a new object and recursively copies all objects found in the original. This means that the new object and its nested objects are completely independent of the original object.
In Python, you can create a deep copy using the copy.deepcopy function.
Which is More Useful for the Prototype Pattern?
The choice between deep copy and shallow copy depends on the context and requirements of the prototype pattern:

Deep Copy is more useful when:

You want to create completely independent copies of the object, including all nested objects.
Modifications to the cloned object should not affect the original object in any way.
The object contains nested objects that need to be copied as well.
Shallow Copy is more useful when:

The object contains references to immutable objects (e.g., numbers, strings, tuples), and you do not need to copy them.
You are okay with the cloned object sharing references to the nested objects with the original object.
You want to perform a faster copy, as shallow copying is usually more performant than deep copying.


The Client.py script demonstrates how to use the Prototype Pattern to create and work with prototype objects (Nano and Ford cars).

'''
from CarMaker import CarMaker

def print_car_detail(car):
    print("Editing a cloned model:")
    print(f"Model: {car.model_name}")
    # Editing the on-road price of a car (this is an optional step)
    car.on_road_price += 100
    print(f"It's on-road price: ${car.on_road_price}")

if __name__ == "__main__":
    print("***Prototype Pattern Modified Demo***\n")
    
    car_maker = CarMaker()
    
    # Working with a Nano car
    nano = car_maker.get_nano()
    print(nano)
    print("-------")
    
    # Getting a cloned version of Nano
    cloned_car = nano.clone()
    
    # Working with the cloned Nano
    print_car_detail(cloned_car)
    print("-------\n")
    
    # Working with a Ford car copy
    ford = car_maker.get_ford()
    print(ford)
    print("-------")
    
    # Getting a cloned version of Ford
    cloned_car = ford.clone()
    
    # Working with the cloned Ford
    print_car_detail(cloned_car)
    print("-------\n")
