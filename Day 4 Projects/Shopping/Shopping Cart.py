
items = input("What items you want to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like? "))

total = price * quantity
print(f"You bought an {items} x {quantity}/pcs")
print(f"The total items you bought are ₱{round(total, 2)} pesos")