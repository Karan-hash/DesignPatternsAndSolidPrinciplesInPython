'''
Client Code:
Demonstrates the Singleton pattern by attempting to create multiple instances of the Captain class.
The get_captain method ensures only one instance exists and returns the same instance on subsequent calls.
'''
from Captain import Captain
if __name__ == '__main__':
    print("***Singleton Pattern Demo***\n")
    print("Trying to make a captain for your team.")
    captain1 = Captain.get_captain()
    
    print("Trying to make another captain for your team:")
    captain2 = Captain.get_captain()
    
    if captain1 is captain2:
        print("Both captain1 and captain2 are the same.")
