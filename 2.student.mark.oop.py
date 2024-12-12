# 2.student.mark.oop.py

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"


class Gradebook:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self, num_students):
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth (DoB): ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self, num_courses):
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks_for_course(self):
        course_id = input("Enter course ID to input marks for: ")
        marks = {}
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.student_id}: "))
            marks[student.student_id] = mark
        self.marks[course_id] = marks

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student)

    def show_student_marks(self):
        course_id = input("Enter course ID to show marks for: ")
        if course_id in self.marks:
            print(f"Marks for course ID {course_id}:")
            for student_id, mark in self.marks[course_id].items():
                print(f"Student ID: {student_id}, Mark: {mark}")
        else:
            print("No marks available for this course.")

    def run(self):
        num_students = self.input_number_of_students()
        self.input_student_information(num_students)

        num_courses = self.input_number_of_courses()
        self.input_course_information(num_courses)

        while True:
            print("Options:")
            print("1. List courses")
            print("2. List students")
            print("3. Input marks for a course")
            print("4. Show student marks for a course")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.list_courses()
            elif choice == 2:
                self.list_students()
            elif choice == 3:
                self.input_marks_for_course()
            elif choice == 4:
                self.show_student_marks()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    gradebook = Gradebook()
    gradebook.run()