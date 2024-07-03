from ArtsStudent import ArtsStudent
from ScienceStudent import ScienceStudent
from ScienceDistinctionDecider import ScienceDistinctionDecider
from ArtsDistinctionDecider import ArtsDistinctionDecider

def show_student_details(students):
    for student in students:
        print(student)

def evaluate_distinctions(students, distinction_decider):
    for student in students:
        distinction_decider.evaluate_distinction(student)

if __name__ == "__main__":
    print("*** A demo that follows the OCP. ***")

    science_students = [
        ScienceStudent("Sam", "R1", 81.5, "Comp.Sc."),
        ScienceStudent("Bob", "R2", 72, "Physics")
    ]
    
    arts_students = [
        ArtsStudent("John", "R3", 71, "History"),
        ArtsStudent("Kate", "R4", 66.5, "English")
    ]

    print("===Results:===")
    show_student_details(science_students)
    show_student_details(arts_students)

    print("===Distinctions:===")
    science_distinction_decider = ScienceDistinctionDecider()
    arts_distinction_decider = ArtsDistinctionDecider()
    
    evaluate_distinctions(science_students, science_distinction_decider)
    evaluate_distinctions(arts_students, arts_distinction_decider)
