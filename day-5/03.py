all_numbers = []

for i in range(10):
    user_input = int(input("Enter a number: "))
    all_numbers.append(user_input)

print("List before sorting: ", all_numbers)

all_numbers.sort()
print("List after sorting: ", all_numbers)

largest_three_numbers = all_numbers[9:6:-1]
print("Largest three numbers: ", largest_three_numbers)