import curses
from domains.gradebook import Gradebook
from input import input_number_of_students, input_student_information, input_number_of_courses, input_course_information, input_marks_for_course
from output import list_courses, list_students, show_student_marks

def main(stdscr):
    gradebook = Gradebook()

    num_students = input_number_of_students(stdscr)
    input_student_information(num_students, stdscr, gradebook)

    num_courses = input_number_of_courses(stdscr)
    input_course_information(num_courses, stdscr, gradebook)

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
            list_courses(stdscr, gradebook)
        elif choice == 2:
            list_students(stdscr, gradebook)
        elif choice == 3:
            input_marks_for_course(stdscr, gradebook)
        elif choice == 4:
            show_student_marks(stdscr, gradebook)
        elif choice == 5:
            gradebook.calculate_gpas()
            stdscr.addstr("GPAs calculated.\n")
            stdscr.refresh()
        elif choice == 6:
            gradebook.sort_students_by_gpa()
            stdscr.addstr("Students sorted by GPA.\n")
            stdscr.refresh()
        elif choice == 7:
            break
        else:
            stdscr.addstr("Invalid choice. Please try again.\n")
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
