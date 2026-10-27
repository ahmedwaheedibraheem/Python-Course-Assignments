numbers = []
for num in range(1500, 2301):
  if num % 7 == 0 and num % 5 == 0:
    numbers.append(str(num))

print("The numbers are:")
print(", ".join(numbers) + ", end of series.")