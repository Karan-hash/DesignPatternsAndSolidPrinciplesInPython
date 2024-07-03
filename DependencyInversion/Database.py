from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save_emp_id_in_database(self, emp_id):
        pass
