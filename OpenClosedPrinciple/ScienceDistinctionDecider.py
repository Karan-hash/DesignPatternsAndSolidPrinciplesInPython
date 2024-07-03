from DistinctionDecider import DistinctionDecider

class ScienceDistinctionDecider(DistinctionDecider):
    def evaluate_distinction(self, student):
        if student.score > 80:
            print(f"{student.reg_number} has received a distinction in science.")
