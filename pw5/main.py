import curses
import os
import zipfile
from domains.gradebook import Gradebook
import input
import output

def compress_files():
    with zipfile.ZipFile('students.dat', 'w') as zipf:
        for file in ['students.txt', 'courses.txt', 'marks.txt']:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def decompress_files():
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()

def load_data(gradebook):
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as f:
            for line in f:
                student_id, name, dob = line.strip().split(',')
                gradebook.add_student(student_id, name, dob)
    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r') as f:
            for line in f:
                course_id, name, credits = line.strip().split(',')
                gradebook.add_course(course_id, name, int(credits))
    if os.path.exists('marks.txt'):
        with open('marks.txt', 'r') as f:
            for line in f:
                course_id, student_id, mark = line.strip().split(',')
                gradebook.add_mark(course_id, student_id, float(mark))

def main(stdscr):
    decompress_files()
    gradebook = Gradebook()
    load_data(gradebook)

    num_students = input.input_number_of_students(stdscr)
    input.input_student_information(num_students, stdscr, gradebook)

    num_courses = input.input_number_of_courses(stdscr)
    input.input_course_information(num_courses, stdscr, gradebook)

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
            output.list_courses(stdscr, gradebook)
        elif choice == 2:
            output.list_students(stdscr, gradebook)
        elif choice == 3:
            input.input_marks_for_course(stdscr, gradebook)
        elif choice == 4:
            output.show_student_marks(stdscr, gradebook)
        elif choice == 5:
            gradebook.calculate_gpas()
            stdscr.addstr("GPAs calculated.\n")
            stdscr.refresh()
        elif choice == 6:
            gradebook.sort_students_by_gpa()
            stdscr.addstr("Students sorted by GPA.\n")
            stdscr.refresh()
        elif choice == 7:
            compress_files()
            break
        else:
            stdscr.addstr("Invalid choice. Please try again.\n")
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
