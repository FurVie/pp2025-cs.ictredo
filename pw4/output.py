def list_courses(stdscr, gradebook):
    stdscr.addstr("Courses:\n")
    for course in gradebook.courses:
        stdscr.addstr(str(course) + "\n")
    stdscr.refresh()

def list_students(stdscr, gradebook):
    stdscr.addstr("Students:\n")
    for student in gradebook.students:
        stdscr.addstr(str(student) + "\n")
    stdscr.refresh()

def show_student_marks(stdscr, gradebook):
    stdscr.addstr("Enter course ID to show marks for: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    if course_id in gradebook.marks:
        stdscr.addstr(f"Marks for course ID {course_id}:\n")
        for student_id, mark in gradebook.marks[course_id].items():
            stdscr.addstr(f"Student ID: {student_id}, Mark: {mark}\n")
    else:
        stdscr.addstr("No marks available for this course.\n")
    stdscr.refresh()
