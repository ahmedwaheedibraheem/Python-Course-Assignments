units = int(input("Enter the units consumed (in KW): "))

if units >= 1 and units <= 99:
  bill = units * 0.15
elif units >= 100 and units <= 199:
  bill = units * 0.30
elif units >= 200 and units <= 299:
  bill = units * 0.40
elif units >= 300:
  bill = units * 0.50
else:
  bill = 0.0

print(
    f"Your monthly consumption is {units} and your total bill is {bill} Pounds"
)