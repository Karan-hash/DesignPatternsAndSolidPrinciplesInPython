from OracleDatabase import OracleDatabase
from MySQLDatabase import MySQLDatabase
from UserInterface import UserInterface

def main():
    print("***A demo that follows the DIP.***")

    # Using Oracle now
    database = OracleDatabase()
    user_interface = UserInterface(database)
    user_interface.save_employee_id("E001")

    # Using MySQL now
    database = MySQLDatabase()
    user_interface = UserInterface(database)
    user_interface.save_employee_id("E002")

if __name__ == "__main__":
    main()
