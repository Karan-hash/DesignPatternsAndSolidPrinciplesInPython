'''
Factory Method Pattern 
GoF Definition 
It defines an interface for creating an object, but lets subclasses decide which class to instantiate. The Factory Method pattern lets a class defer instantiation to subclasses. 
Concept 
Here you start with an abstract creator class (often called a creator) that defines the basic structure of an application, and the subclasses (that derive from this abstract class) take the responsibility of doing the actual instantiation process. The concept will make sense to you when you analyze the following examples. 

Computer World Example 
In database programming, you may need to support different database users. For example, one user may use SQL Server and the other may opt for Oracle. So, when you need to insert data into your database, first you need to create a connection object, such as SqlServerConnection or OracleConnection, and only then can you proceed. If you put the code into an if-else block (or switch statements), you may need to repeat lots of similar code, which isn’t easily maintainable. Also, whenever you start supporting a new type of connection, you need to reopen your code and make modifications. This type of problem can be resolved using the Factory Method pattern. 
Implementation - 
An abstract creator class called AnimalFactory defines the basic structure of the program. As per the definition, the instantiation process is carried out through the subclasses that derive from this abstract class
'''

from DogFactory import DogFactory
from TigerFactory import TigerFactory

if __name__ == "__main__":
    print("*** Factory Method Pattern Demo ***")

    # Create a tiger and display its behavior using TigerFactory
    factory = TigerFactory()
    # animal = factory.create_animal()
    # animal.display_behavior()
    factory.create_and_display_animal("yellow")

    # Create a dog and display its behavior using DogFactory
    factory = DogFactory()
    factory.create_and_display_animal("black")
    # animal = factory.create_animal()
    # animal.display_behavior()