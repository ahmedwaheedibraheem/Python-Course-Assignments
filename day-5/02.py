students_number = int(input("Enter the number of students: "))
all_numbers = []

for i in range(students_number):
    grade = int(input("Enter the grade of student (" + str(i+1) + "): "))
    all_numbers.append(grade)

print(f"""
    The heighest grade is {max(all_numbers)}.
    The lowest grade is {min(all_numbers)}.
""")