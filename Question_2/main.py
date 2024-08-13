import os
STUDENTS_FILE = 'students.txt'
COURSES_FILE = 'courses.txt'
ENROLLMENTS_FILE = 'enrollments.txt'
GRADES_FILE = 'grades.txt'

def load_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return file.readlines()

def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.writelines(data)

def add_student(student_id, name, age):
    students = load_file(STUDENTS_FILE)
    students.append(f"{student_id},{name},{age}\n")
    save_to_file(STUDENTS_FILE, students)
    print(f"Student {name} added successfully.")

def view_students():
    students = load_file(STUDENTS_FILE)
    if not students:
        print("No students available.")
        return
    for student in students:
        student_id, name, age = student.strip().split(',')
        print(f"ID: {student_id}, Name: {name}, Age: {age}")

def add_course(course_id, course_name):
    courses = load_file(COURSES_FILE)
    courses.append(f"{course_id},{course_name}\n")
    save_to_file(COURSES_FILE, courses)
    print(f"Course {course_name} added successfully.")

def view_courses():
    courses = load_file(COURSES_FILE)
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        course_id, course_name = course.strip().split(',')
        print(f"ID: {course_id}, Name: {course_name}")

def enroll_student(student_id, course_id):
    enrollments = load_file(ENROLLMENTS_FILE)
    enrollments.append(f"{student_id},{course_id}\n")
    save_to_file(ENROLLMENTS_FILE, enrollments)
    print(f"Student {student_id} enrolled in course {course_id}.")

def view_enrollments():
    enrollments = load_file(ENROLLMENTS_FILE)
    if not enrollments:
        print("No enrollments available.")
        return
    for enrollment in enrollments:
        student_id, course_id = enrollment.strip().split(',')
        print(f"Student ID: {student_id}, Course ID: {course_id}")

def assign_grade(student_id, course_id, grade):
    grades = load_file(GRADES_FILE)
    grades.append(f"{student_id},{course_id},{grade}\n")
    save_to_file(GRADES_FILE, grades)
    print(f"Grade {grade} assigned to student {student_id} for course {course_id}.")

def view_grades():
    grades = load_file(GRADES_FILE)
    if not grades:
        print("No grades available.")
        return
    for grade in grades:
        student_id, course_id, grade_value = grade.strip().split(',')
        print(f"Student ID: {student_id}, Course ID: {course_id}, Grade: {grade_value}")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. View Courses")
        print("5. Enroll Student")
        print("6. View Enrollments")
        print("7. Assign Grade")
        print("8. View Grades")
        print("9. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            add_student(student_id, name, age)
        elif choice == '2':
            view_students()
        elif choice == '3':
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            add_course(course_id, course_name)
        elif choice == '4':
            view_courses()
        elif choice == '5':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            enroll_student(student_id, course_id)
        elif choice == '6':
            view_enrollments()
        elif choice == '7':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter grade: ")
            assign_grade(student_id, course_id, grade)
        elif choice == '8':
            view_grades()
        elif choice == '9':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
