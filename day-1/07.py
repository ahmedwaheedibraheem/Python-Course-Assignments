num_of_apples = int(input("Enter the number of apples: "))
num_of_dozens = num_of_apples // 12
num_of_remaining_apples = num_of_apples % 12
print(f"""
{num_of_apples} apples contain:
    * {num_of_dozens} dozen(s) of apples; and
    * {num_of_remaining_apples} remaining apple(s).
""")
