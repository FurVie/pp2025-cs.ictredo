# 1.student.mark.py

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DoB): ")
        students.append((student_id, student_name, student_dob))
    return students

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks_for_course(students):
    course_id = input("Enter course ID to input marks for: ")
    marks = {}
    for student in students:
        student_id = student[0]
        mark = float(input(f"Enter mark for student {student_id}: "))
        marks[student_id] = mark
    return course_id, marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(course_id, marks):
    print(f"Marks for course ID {course_id}:")
    for student_id, mark in marks.items():
        print(f"Student ID: {student_id}, Mark: {mark}")

def main():
    students = []
    courses = []
    marks = {}

    num_students = input_number_of_students()
    students = input_student_information(num_students)

    num_courses = input_number_of_courses()
    courses = input_course_information(num_courses)

    while True:
        print("Options:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_courses(courses)
        elif choice == 2:
            list_students(students)
        elif choice == 3:
            course_id, course_marks = input_marks_for_course(students)
            marks[course_id] = course_marks
        elif choice == 4:
            course_id = input("Enter course ID to show marks for: ")
            if course_id in marks:
                show_student_marks(course_id, marks[course_id])
            else:
                print("No marks available for this course.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
