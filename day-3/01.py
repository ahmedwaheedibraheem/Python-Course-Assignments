m = int(input("Enter the first number: "))
n = int(input("Enter the last number: "))

total_sum = 0
for i in range(m, n + 1):
  if i % 2 == 0:
    total_sum += i

print(f"The sum of even numbers between {m} and {n} is: {total_sum}")