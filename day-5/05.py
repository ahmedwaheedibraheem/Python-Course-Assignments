students_number = int(input("Please enter the number of students: "))

all_grades = []
failure_grades = []
above_avg_grades = []

for i in range(students_number):
    student_grade = int(input(f"""  Student ({i + 1}): """))
    all_grades.append(student_grade)

average = sum(all_grades) / len(all_grades)

for i in all_grades:
    if i < 50:
        failure_grades.append(i)
    if i > average:
        above_avg_grades.append(i)

print(f"""
The average grade is {average}
The number of students who failed is {len(failure_grades)}
The number of students above average is {len(above_avg_grades)}
""")

