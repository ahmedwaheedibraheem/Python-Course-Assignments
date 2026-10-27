held = int(input("Enter the number of classes held: "))
attended = int(input("Enter the number of classes attended: "))

percentage = (attended / held) * 100
print(f"Attendance is {percentage}%")

if percentage >= 75:
  print("You can enter the final exam.")
else:
  medical = input("Do you have a medical cause (Y/N): ").upper()
  if medical == "Y":
    print("You can enter the final exam.")
  else:
    print("You are not allowed to enter the exam.")