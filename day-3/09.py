loan = float(input("Enter the loan amount: "))
interest = float(input("Enter the interest rate: "))

print(f"\n{'Month':<10} | {'Amount'}")
print("-" * 18)

for month in range(13):
  amount = loan * ((1 + interest) ** month)
  print(f"{month:<10} | {int(round(amount))}")