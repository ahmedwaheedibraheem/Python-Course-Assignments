day = int(input("Enter the day: "))
month = int(input("Enter the month: "))

if day < 1 or day > 31 or month < 1 or month > 12:
  print("Invalid Date!")
elif (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day <= 19):
  print("It is Spring!")
elif (
    (month == 6 and day >= 20)
    or (month in [7, 8])
    or (month == 9 and day <= 21)
):
  print("It is Summer!")
elif (
    (month == 9 and day >= 22)
    or (month in [10, 11])
    or (month == 12 and day <= 20)
):
  print("It is Autumn!")
elif (
    (month == 12 and day >= 21)
    or (month in [1, 2])
    or (month == 3 and day <= 19)
):
  print("It is Winter!")
else:
  print("Invalid Date!")