x = int(input("Enter a number: "))

print(f"\n{'Number':<10} | {'Factorial'}")
print("-" * 22)

factorial = 1
for i in range(1, x + 1):
  factorial *= i
  print(f"{i:<10} | {factorial}")