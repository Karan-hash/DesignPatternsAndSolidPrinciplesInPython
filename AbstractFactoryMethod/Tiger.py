# Tiger.py
from abc import ABC, abstractmethod

class Tiger(ABC):
    @abstractmethod
    def about_me(self):
        pass

    @abstractmethod
    def invite_dog(self, dog):
        pass
