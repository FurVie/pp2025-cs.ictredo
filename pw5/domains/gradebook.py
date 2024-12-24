import math
from .student import Student
from .course import Course

class Gradebook:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_student(self, student_id, name, dob):
        student = Student(student_id, name, dob)
        self.students.append(student)

    def add_course(self, course_id, name, credits):
        course = Course(course_id, name, credits)
        self.courses.append(course)

    def add_mark(self, course_id, student_id, mark):
        mark = math.floor(mark * 10) / 10  
        for student in self.students:
            if student.student_id == student_id:
                student.marks[course_id] = mark
                break
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = mark

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)
