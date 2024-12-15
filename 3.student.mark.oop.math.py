# 3.student.mark.oop.math.py

import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.1f}"

    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course_id, mark in self.marks.items():
            course = next((course for course in courses if course.course_id == course_id), None)
            if course:
                total_credits += course.credits
                weighted_sum += mark * course.credits
        if total_credits > 0:
            self.gpa = weighted_sum / total_credits
        else:
            self.gpa = 0.0


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"


class Gradebook:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number_of_students(self, stdscr):
        stdscr.addstr("Enter the number of students in the class: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def input_student_information(self, num_students, stdscr):
        for _ in range(num_students):
            stdscr.addstr("Enter student ID: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode()
            stdscr.addstr("Enter student name: ")
            stdscr.refresh()
            student_name = stdscr.getstr().decode()
            stdscr.addstr("Enter student date of birth (DoB): ")
            stdscr.refresh()
            student_dob = stdscr.getstr().decode()
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_number_of_courses(self, stdscr):
        stdscr.addstr("Enter the number of courses: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def input_course_information(self, num_courses, stdscr):
        for _ in range(num_courses):
            stdscr.addstr("Enter course ID: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode()
            stdscr.addstr("Enter course name: ")
            stdscr.refresh()
            course_name = stdscr.getstr().decode()
            stdscr.addstr("Enter course credits: ")
            stdscr.refresh()
            course_credits = int(stdscr.getstr().decode())
            course = Course(course_id, course_name, course_credits)
            self.courses.append(course)

    def input_marks_for_course(self, stdscr):
        stdscr.addstr("Enter course ID to input marks for: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()
        marks = {}
        for student in self.students:
            stdscr.addstr(f"Enter mark for student {student.student_id}: ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode())
            mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
            marks[student.student_id] = mark
            student.marks[course_id] = mark
        self.marks[course_id] = marks

    def list_courses(self, stdscr):
        stdscr.addstr("Courses:\n")
        for course in self.courses:
            stdscr.addstr(str(course) + "\n")
        stdscr.refresh()

    def list_students(self, stdscr):
        stdscr.addstr("Students:\n")
        for student in self.students:
            stdscr.addstr(str(student) + "\n")
        stdscr.refresh()

    def show_student_marks(self, stdscr):
        stdscr.addstr("Enter course ID to show marks for: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()
        if course_id in self.marks:
            stdscr.addstr(f"Marks for course ID {course_id}:\n")
            for student_id, mark in self.marks[course_id].items():
                stdscr.addstr(f"Student ID: {student_id}, Mark: {mark}\n")
        else:
            stdscr.addstr("No marks available for this course.\n")
        stdscr.refresh()

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def run(self, stdscr):
        num_students = self.input_number_of_students(stdscr)
        self.input_student_information(num_students, stdscr)

        num_courses = self.input_number_of_courses(stdscr)
        self.input_course_information(num_courses, stdscr)

        while True:
            stdscr.addstr("Options:\n")
            stdscr.addstr("1. List courses\n")
            stdscr.addstr("2. List students\n")
            stdscr.addstr("3. Input marks for a course\n")
            stdscr.addstr("4. Show student marks for a course\n")
            stdscr.addstr("5. Calculate GPAs\n")
            stdscr.addstr("6. Sort students by GPA\n")
            stdscr.addstr("7. Exit\n")
            stdscr.addstr("Enter your choice: ")
            stdscr.refresh()
            choice = int(stdscr.getstr().decode())

            if choice == 1:
                self.list_courses(stdscr)
            elif choice == 2:
                self.list_students(stdscr)
            elif choice == 3:
                self.input_marks_for_course(stdscr)
            elif choice == 4:
                self.show_student_marks(stdscr)
            elif choice == 5:
                self.calculate_gpas()
                stdscr.addstr("GPAs calculated.\n")
                stdscr.refresh()
            elif choice == 6:
                self.sort_students_by_gpa()
                stdscr.addstr("Students sorted by GPA.\n")
                stdscr.refresh()
            elif choice == 7:
                break
            else:
                stdscr.addstr("Invalid choice. Please try again.\n")
                stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(Gradebook().run)
