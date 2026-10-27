distance_in_meters = float(input("Enter distance in meters: "))
distance_in_kms = distance_in_meters // 1000
remaining_meters = distance_in_meters % 1000
print(f"""
{distance_in_meters} is equivalent to:
    * {distance_in_kms} Kilometers; and
    * {remaining_meters} meters.
""")