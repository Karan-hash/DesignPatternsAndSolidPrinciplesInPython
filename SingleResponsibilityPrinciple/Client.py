from Employee import Employee
from EmployeeIdGenerator import EmployeeIdGenerator
from SeniorityChecker import SeniorityChecker
def show_emp_detail(emp):
    # Display employee detail
    emp.display_emp_detail()
    # Generate the ID
    id_generator = EmployeeIdGenerator()
    emp_id = id_generator.generate_emp_id(emp.first_name)
    print(f"The employee id: {emp_id}")
    # Check the seniority level
    seniority_checker = SeniorityChecker()
    print(f"This employee is a {seniority_checker.check_seniority(emp.experience_in_years)} employee.")

if __name__ == "__main__":
    print("*** A demo that follows the SRP.***")
    robin = Employee("Robin", "Smith", 7.5)
    show_emp_detail(robin)
    print("\n*******\n")
    kevin = Employee("Kevin", "Proctor", 3.2)
    show_emp_detail(kevin)