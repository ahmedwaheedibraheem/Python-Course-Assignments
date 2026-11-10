exam_1_grades = []
exam_2_grades = []
max_grade = []

for i in range(5):
    print(f"""Enter the marks of student ({i + 1}):""")
    exam_1 = int(input("""    Exam (1): """))
    exam_1_grades.append(exam_1)
    exam_2 = int(input("""    Exam (2): """))
    exam_2_grades.append(exam_2)
    max_grade.append(max([exam_1, exam_2]))

print("""Exam 1\t\tExam 2\t\tMax Grade""")
for i in range(5):
 print(f"""{exam_1_grades[i]}\t\t\t{exam_2_grades[i]}\t\t\t{max_grade[i]}""")



