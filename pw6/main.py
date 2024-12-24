import curses
from input import (
    input_number_of_students,
    input_student_information,
    input_number_of_courses,
    input_course_information,
    input_marks_for_course,
    save_data_to_pickle,
    load_data_from_pickle
)
from output import list_courses, list_students, show_student_marks
from domains.gradebook import Gradebook

def main(stdscr):
    
    students, courses, marks = load_data_from_pickle()
    gradebook = Gradebook()

    if students and courses and marks:
        gradebook.add_students(students)
        gradebook.add_courses(courses)
        for course_id, course_marks in marks.items():
            gradebook.input_marks(course_id, course_marks)

    num_students = input_number_of_students(stdscr)
    students_info = input_student_information(num_students, stdscr)
    gradebook.add_students(students_info)

    num_courses = input_number_of_courses(stdscr)
    courses_info = input_course_information(num_courses, stdscr)
    gradebook.add_courses(courses_info)

    marks = {}
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
            list_courses(gradebook.courses, stdscr)
        elif choice == 2:
            list_students(gradebook.students, stdscr)
        elif choice == 3:
            course_id, course_marks = input_marks_for_course(gradebook.students, stdscr)
            gradebook.input_marks(course_id, course_marks)
            marks[course_id] = course_marks
        elif choice == 4:
            stdscr.addstr("Enter course ID to show marks for: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode()
            if course_id in marks:
                show_student_marks(course_id, marks[course_id], stdscr)
            else:
                stdscr.addstr("No marks available for this course.\n")
                stdscr.refresh()
        elif choice == 5:
            gradebook.calculate_gpas()
            stdscr.addstr("GPAs calculated.\n")
            stdscr.refresh()
        elif choice == 6:
            gradebook.sort_students_by_gpa()
            stdscr.addstr("Students sorted by GPA.\n")
            stdscr.refresh()
        elif choice == 7:
            save_data_to_pickle(gradebook.students, gradebook.courses, marks)
            break
        else:
            stdscr.addstr("Invalid choice. Please try again.\n")
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
