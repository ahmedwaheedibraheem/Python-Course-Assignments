n = int(input("Enter the number of students: "))

total = 0
for i in range(1, n + 1):
  grade = float(input(f"Enter the grade of student ({i}): "))
  total += grade

average = total / n
print(f"The average grade is {average:.1f}")