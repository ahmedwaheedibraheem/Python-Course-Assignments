students_number = int(input("Enter students number: "))

names = []
grades_7th = []
grades_12th = []
grades_att = []
grades_final = []
grades_total = []

for i in range(students_number):
    name = input("Enter student name: ")
    names.append(name)
    grade_7th = int(input("Enter grade of 7th: "))
    grades_7th.append(grade_7th)
    grade_12th = int(input("Enter grade of 12th: "))
    grades_12th.append(grade_12th)
    grade_att = int(input("Enter grade of attendance: "))
    grades_att.append(grade_att)
    grade_final = int(input("Enter grade of the final: "))
    grades_final.append(grade_final)
    total = sum([grade_7th, grade_12th, grade_att, grade_final])
    grades_total.append(total)

print("""Name\t\t\t\t\t\t7th\t\t\t12th\t\tAtt\t\t\tFinal\t\t\tTotal""")
print("""___________________________________________________________________""")
for i in range(students_number):
    print(f"""{names[i]}\t\t\t\t\t\t{grades_7th[i]}\t\t\t{grades_12th[i]}\t\t\t{grades_att[i]}\t\t\t{grades_final[i]}\t\t\t{grades_total[i]}""")