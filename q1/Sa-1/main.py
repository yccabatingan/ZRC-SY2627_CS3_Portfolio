
class AssignmentSubmission:
    def __init__(self,student_name,student_id,assignment_title):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = "2026-10-01"
        self.__is_submitted = True
        self.__grade = 0
        self.__submitted_files = []

    def __validate_grade(self,score):
        if self.__grade < 0:
            return True

    def __check_submission_status(self):
        if self.__is_submitted == True:
            return "Assignment is submitted"
        else:
            return "No files submitted"

    def __assign_grade(self,score):
        self.__grade = score
        return self.__grade

    def add_file(self,filename):
        self.__submitted_files.append(filename)

    def remove_file(self,filename):
        self.__submitted_files.remove(filename)

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        if self.__is_submitted == True:
            status = "Submitted"
        else:
            status = "Missing"
        length = len(self.__submitted_files)
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: {status} ({length} files) | Grade: {self.__grade}"

student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103")

print(student1.add_file("main.py"))
print(student1.add_file("report.pdf"))
print(student1.get_status_report())
