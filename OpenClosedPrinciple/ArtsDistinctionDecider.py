from DistinctionDecider import DistinctionDecider

class ArtsDistinctionDecider(DistinctionDecider):
    def evaluate_distinction(self, student):
        if student.score > 70:
            print(f"{student.reg_number} has received a distinction in arts.")
