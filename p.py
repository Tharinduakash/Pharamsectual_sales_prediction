# Task 1: Get the number of students
num_students = int(input("Enter the number of students: "))
student_count = 0

# Task 2 & 3: Get marks and display grades
while student_count < num_students:
    mark = int(input("Enter the mark of the student: "))
    if mark >= 75:
        grade = 'A'
    elif mark >= 55:
        grade = 'B'
    elif mark >= 40:
        grade = 'C'
    elif mark >= 25:
        grade = 'W'
    else:
        grade = 'F'
    print(f"The grade for the student is: {grade}")
    student_count += 1
