import random

class EmployeeIdGenerator:
    def generate_emp_id(self, emp_first_name):
        random_number = random.randint(0, 999)
        emp_id = emp_first_name[0] + str(random_number)
        return emp_id