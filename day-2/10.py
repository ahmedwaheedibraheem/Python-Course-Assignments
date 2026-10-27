print("--- Welcome to the Café Robot ---")
category = input(
    "Would you like to have a sandwich or a main dish? "
).lower()

item_price = 0

if category == "sandwich":
  print("\nSandwich Menu:")
  print("1. Cheese Burger (20 pounds)")
  print("2. Double Cheese Burger (25 pounds)")
  print("3. Fish Fillet (30 pounds)")
  print("4. Chicken Fillet (35 pounds)")

  choice = input(
      "Choose your sandwich (Cheese Burger / Double Cheese Burger / Fish Fillet"
      " / Chicken Fillet): "
  ).lower()

  if "double" in choice:
    item_price = 25
  elif "cheese" in choice:
    item_price = 20
  elif "fish" in choice:
    item_price = 30
  elif "chicken" in choice:
    item_price = 35
  else:
    print("Invalid sandwich choice. Defaulting to 0.")

elif category == "main dish" or category == "main":
  print("\nMain Dish Menu:")
  print("1. Grilled Chicken (70 pounds)")
  print("2. Mixed Grill (120 pounds)")
  print("3. Fish & Shrimps (180 pounds)")

  choice = input(
      "Choose your main dish (Grilled Chicken / Mixed Grill / Fish &"
      " Shrimps): "
  ).lower()

  if "grilled chicken" in choice:
    item_price = 70
  elif "mixed" in choice:
    item_price = 120
  elif "shrimp" in choice or "fish" in choice:
    item_price = 180
  else:
    print("Invalid main dish choice. Defaulting to 0.")
else:
  print("Invalid category choice.")

add_ons = input(
    "Would you like to have Drink & Fries with the order? (yes/no): "
).lower()
addon_price = 20 if add_ons == "yes" else 0

subtotal = item_price + addon_price

dining_type = input("Would you like to eat in the café or take away? ").lower()
if "in" in dining_type or "cafe" in dining_type:
  total = subtotal * 1.12  # Adding 12% service charge
else:
  total = subtotal

print(f"\nTotal amount to pay: {total:.2f} pounds")