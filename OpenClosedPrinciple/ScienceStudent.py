from Student import Student

class ScienceStudent(Student):
    def __init__(self, name, reg_number, score, dept):
        super().__init__(name, reg_number, score)
        self.department = dept
