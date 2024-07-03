from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, reg_number, score):
        self.name = name
        self.reg_number = reg_number
        self.score = score
        self.department = None

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Reg Number: {self.reg_number}\n"
                f"Dept: {self.department}\n"
                f"Marks: {self.score}\n*******")
