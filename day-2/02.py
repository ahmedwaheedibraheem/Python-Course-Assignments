devices = int(input("Enter the number of devices: "))

if devices == 1:
  print("Basic Plan. The monthly subscription is 120 EGP")
elif devices == 2:
  print("Standard Plan. The monthly subscription is 165 EGP")
elif devices == 3 or devices == 4:
  print("Premium Plan. The monthly subscription is 200 EGP")
else:
  print("Invalid Plan. Disallowed number of devices!")