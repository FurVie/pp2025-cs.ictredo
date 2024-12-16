import math
from py.pw4.domains.course import Course
from py.pw4.domains.student import Student


def input_number_of_students(stdscr):
    stdscr.addstr("Enter the number of students in the class: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_student_information(num_students, stdscr, gradebook):
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
        gradebook.students.append(student)

def input_number_of_courses(stdscr):
    stdscr.addstr("Enter the number of courses: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_course_information(num_courses, stdscr, gradebook):
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
        gradebook.courses.append(course)

def input_marks_for_course(stdscr, gradebook):
    stdscr.addstr("Enter course ID to input marks for: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    marks = {}
    for student in gradebook.students:
        stdscr.addstr(f"Enter mark for student {student.student_id}: ")
        stdscr.refresh()
        mark = float(stdscr.getstr().decode())
        mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
        marks[student.student_id] = mark
        student.marks[course_id] = mark
    gradebook.marks[course_id] = marks
