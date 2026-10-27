total = 0
for i in range(1, 11):
  grade = float(input(f"Enter the grade of student ({i}): "))
  total += grade

average = total / 10
print(f"The average grade is {average:.1f}")