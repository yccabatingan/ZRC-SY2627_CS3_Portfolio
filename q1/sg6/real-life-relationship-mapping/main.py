# Write a short Python code snippet showing a Course adding a Student object to a list. 
#mapping.py
class Student:

    def __init__(self, name: str, studentId: str):
        self.name = name
        self.studentId = studentId


class Course:

    def __init__(self, courseName: str):
        self.courseName = courseName
        self.students = []

    def addStudent(self, student: Student):
        self.students.append(student)


student1 = Student("Yoanna", "PSHS-ZRC-026")
student2 = Student("Cooler Yoanna", "PSHS-ZRC-062")

crs = Course("Computer Science")

crs.addStudent(student1)
crs.addStudent(student2)

print(f"Course: {crs.courseName}")
print(f"Student 1: {student1.name} ({student1.studentId})")
print(f"Student 2: {student2.name} ({student2.studentId})")