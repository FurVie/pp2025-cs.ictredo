import curses
import pickle
import gzip
import os

def input_number_of_students(stdscr):
    stdscr.addstr("Enter the number of students in the class: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_student_information(num_students, stdscr):
    students = []
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
        students.append((student_id, student_name, student_dob))
    return students

def input_number_of_courses(stdscr):
    stdscr.addstr("Enter the number of courses: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_course_information(num_courses, stdscr):
    courses = []
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
        courses.append((course_id, course_name, course_credits))
    return courses

def input_marks_for_course(students, stdscr):
    stdscr.addstr("Enter course ID to input marks for: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    marks = {}
    for student in students:
        stdscr.addstr(f"Enter mark for student {student[0]}: ")
        stdscr.refresh()
        mark = float(stdscr.getstr().decode())
        marks[student[0]] = mark
    return course_id, marks

def save_data_to_pickle(students, courses, marks):
    with gzip.open('students.dat', 'wb') as f:
        pickle.dump((students, courses, marks), f)

def load_data_from_pickle():
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as f:
            students, courses, marks = pickle.load(f)
        return students, courses, marks
    return None, None, None
