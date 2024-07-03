from Database import Database

class UserInterface:
    def __init__(self, database: Database):
        self.database = database

    def save_employee_id(self, emp_id):
        self.database.save_emp_id_in_database(emp_id)
