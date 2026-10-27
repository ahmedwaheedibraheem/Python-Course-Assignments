salary = float(input("Enter employee's salary: "))
years = int(input("Enter the years of service: "))

if years >= 12:
  bonus = salary * 0.20
elif years >= 8:
  bonus = salary * 0.10
elif years >= 4:
  bonus = salary * 0.05
else:
  bonus = 0.0

print(f"Bonus is {bonus} pounds")