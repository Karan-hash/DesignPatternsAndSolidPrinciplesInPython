from Database import Database

class OracleDatabase(Database):
    def save_emp_id_in_database(self, emp_id):
        print(f"The id: {emp_id} is saved in the Oracle database.")
