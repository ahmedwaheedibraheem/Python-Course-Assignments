total = 0
count = 0

grade = float(input("Enter the first grade: "))
while 0 <= grade <= 100:
  total += grade
  count += 1
  grade = float(input("Enter the next grade: "))

if count > 0:
  average = total / count
  print(f"The average grade is {average:.1f}")
else:
  print("No valid grades entered.")