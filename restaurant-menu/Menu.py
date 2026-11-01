menu = {
    "Pizza": 100,
    "Pasta": 80,
    "Salad": 40,
    "Noodles":40,
        "Hot Dog":90
}

order_total = 0

print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")
print ("Welcome to our Restaurant")
item_1 = input("What would you like to order?? ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} your order is add.")
else:
    print(f"{item_1} is not available.")

another_order = input(" you want another item? (Yes/No) ")

if another_order.lower() == "yes":
    item_2 = input("What is the second item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2}  your order is add .")
    else:
        print(f"{item_2}  is not available.")

print(f"Total bill: ₹{order_total}")