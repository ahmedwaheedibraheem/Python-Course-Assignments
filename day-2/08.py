month = int(input("Enter the month: "))

if month in [3, 4, 5]:
  print("It is Spring!")
elif month in [6, 7, 8]:
  print("It is Summer!")
elif month in [9, 10, 11]:
  print("It is Autumn!")
elif month in [12, 1, 2]:
  print("It is Winter!")
else:
  print("Invalid Month!")