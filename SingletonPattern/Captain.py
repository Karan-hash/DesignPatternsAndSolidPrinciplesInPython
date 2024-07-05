'''
Captain Class:

The Captain class ensures only one instance of the class is created (Singleton pattern).
The constructor (__init__) is designed to raise an exception if an attempt is made to create a second instance.
The get_captain static method ensures that the captain instance is lazily initialized and returns the single instance. It also includes print statements to indicate whether a new instance is created or an existing one is returned.

Lazy Initialization is the concept of deferring object creation until the object is actually first used. If used properly, it can result in significant performance gains.
'''
class Captain:
    _captain = None

    # Making the constructor private
    # to prevent the use of "new"
    def __init__(self):
        if Captain._captain is not None:
            raise Exception("This class is a singleton!")
        else:
            Captain._captain = self

    @staticmethod
    def get_captain():
        # Lazy initialization
        if Captain._captain is None:
            Captain()
            print("\tA new captain is elected for your team.")
        else:
            print("\tYou already have a captain for your team.")
            print("\tSend him for the toss.")
        return Captain._captain
