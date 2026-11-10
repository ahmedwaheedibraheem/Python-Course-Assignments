group_a = []

group_a_len = int(input("Please enter the GRADES of students registered in Group (a): "))
for i in range(group_a_len):
    grade = int(input(f"""  Student ({i + 1}): """))
    group_a.append(grade)

group_b = []

group_b_len = int(input("Please enter the GRADES of students registered in Group (b): "))
for i in range(group_b_len):
    grade = int(input(f"""  Student ({i + 1}): """))
    group_b.append(grade)

all_grades = group_a + group_b
print(f"""
The concatenated grades: {all_grades}.
""")
