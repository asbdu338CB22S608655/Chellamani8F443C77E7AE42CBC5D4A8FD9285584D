class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number  # Fixed the assignment here
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("anitha", "A123", 7.8),
    Student("sri mathi", "A124", 9.1),
    Student("Tamil", "A126", 9.9)
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
