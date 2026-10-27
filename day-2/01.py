width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"The area is: {area}")
print(f"The perimeter is: {perimeter}")

if width == height:
  print("The shape is: Square")
elif height > width:
  print("The shape is: Vertical")
else:
  print("The shape is: Horizontal")