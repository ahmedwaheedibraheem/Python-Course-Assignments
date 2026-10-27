import math
radius = float(input("Please enter the radius: "))
diameter = 2 * radius
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"""
  The diameter of the circle is {diameter}.
  The perimeter of the circle is {perimeter}.
  The area of the circle is {area}.
""")
