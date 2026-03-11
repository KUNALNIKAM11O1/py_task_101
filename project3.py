#  Project 3:Online Food Ordering System
# Description:
# Create a Command Line Interface based food ordering system.(script mode)
# Menu:
# 1. Pizza - ₹150
# 2. Burger - ₹100
# 3. Fries - ₹60
# 4. Cold Drink - ₹40
# • Ask user to select items (single choice or multiple)
# • Ask quantity for each selected item
# • Calculate total bill
# • If total bill > ₹300, apply ₹50 discount
# • Display final bill with item details and discount applied (if any)
# e.g. python food_order.py
# output:
# Welcome to Online Food Ordering!
# Menu:
# 1. Pizza - ₹150
# 2. Burger - ₹100
# Enter your choice: 1
# Enter quantity: 2
# Your total bill is ₹300


print("Welcome to Online Food Ordering!")
print("\nMenu:")
print("1. Pizza - ₹150")
print("2. Burger - ₹100")
print("3. Fries - ₹60")
print("4. Cold Drink - ₹40")

menu = {
    1: ("Pizza", 150),
    2: ("Burger", 100),
    3: ("Fries", 60),
    4: ("Cold Drink", 40)
}

total_bill = 0
order_details = []

while True:
    choice = int(input("\nEnter your choice (1-4): "))

    if choice in menu:
        quantity = int(input("Enter quantity: "))
        item_name, price = menu[choice]
        item_total = price * quantity
        total_bill += item_total
        order_details.append((item_name, quantity, item_total))
    else:
        print("Invalid choice!")

    more = input("Do you want to order more? (yes/no): ").lower()
    if more != "yes":
        break

discount = 0
if total_bill > 300:
    discount = 50
    total_bill -= discount

print("\n Final Bill")
for item in order_details:
    print(f"{item[0]} x {item[1]} = ₹{item[2]}")

if discount > 0:
    print(f"Discount Applied: -₹{discount}")

print(f"Total Payable Amount: ₹{total_bill}")
