from abc import ABC, abstractmethod

# This is the common interface
class Builder(ABC):
    @abstractmethod
    def add_brand_name(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def insert_wheels(self):
        pass

    '''
    The following method is used to
    retrieve the object that is constructed.
    '''
    @abstractmethod
    def get_vehicle(self):
        pass