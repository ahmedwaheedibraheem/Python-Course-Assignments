minutes = int(input("Enter period in minutes: "))
days = minutes // (24 * 60)
hours = (minutes % (24 * 60)) // 60
remaining_minutes = ((minutes % 24) * 60) % 60
print(f"{minutes} minutes contain {days} days, {hours} hours and {remaining_minutes} minutes remaining.")
