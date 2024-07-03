from Database import Database

class MySQLDatabase(Database):
    def save_emp_id_in_database(self, emp_id):
        print(f"The id: {emp_id} is saved in the MySQL database.")
