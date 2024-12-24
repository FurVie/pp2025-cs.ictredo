import os

def input_number_of_students(stdscr):
    stdscr.addstr("Enter the number of students in the class: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_student_information(num_students, stdscr, gradebook):
    with open("students.txt", "w") as f:
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
            gradebook.add_student(student_id, student_name, student_dob)
            f.write(f"{student_id},{student_name},{student_dob}\n")

def input_number_of_courses(stdscr):
    stdscr.addstr("Enter the number of courses: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def input_course_information(num_courses, stdscr, gradebook):
    with open("courses.txt", "w") as f:
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
            gradebook.add_course(course_id, course_name, course_credits)
            f.write(f"{course_id},{course_name},{course_credits}\n")

def input_marks_for_course(stdscr, gradebook):
    stdscr.addstr("Enter course ID to input marks for: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    with open("marks.txt", "a") as f:
        for student in gradebook.students:
            stdscr.addstr(f"Enter mark for student {student.student_id}: ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode())
            gradebook.add_mark(course_id, student.student_id, mark)
            f.write(f"{course_id},{student.student_id},{mark}\n")
