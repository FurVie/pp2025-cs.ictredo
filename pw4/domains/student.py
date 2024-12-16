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
