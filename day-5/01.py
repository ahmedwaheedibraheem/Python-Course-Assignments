grades = [56, 78, 93, 42, 97, 85, 34, 67, 73, 86]

for g in grades:
    if g < 50:
        grades.remove(g)
print(f"""
    The marks above 50 are:{grades}
""")