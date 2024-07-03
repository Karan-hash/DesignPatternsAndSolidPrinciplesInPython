class Employee:
    def __init__(self, first_name, last_name, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.experience_in_years = experience

    def display_emp_detail(self):
        print(f"The employee name: {self.last_name}, {self.first_name}")
        print(f"This employee has {self.experience_in_years} years of experience.")
