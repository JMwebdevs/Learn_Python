item1 = "pancit canton"
quantity1 = 4
price1 = 14.75

item2 = "Coke 1000ml"
quantity2 = 2
price2 = 35.0

item3 = "ice"
quantity3 = 3
price3 = 5.0

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

grand_total = total1 + total2 + total3

print(f"{'Receipt':>28}")
print("-" * 50)
print(f"{"Items":<20}{"Quantity":>5}{"Price":>10}{"Total":>10}" )
print("-" * 50)
print(f"{item1:<10}{quantity1:>11}{price1:>14.5}{total1:>10}")
print(f"{item2:<10}{quantity2:>13}{price2:>14.5}{total2:>10}")
print(f"{item3:<10}{quantity3:>14}{price3:>14.5}{total3:>10}")
print("-" * 50)
print(f"{'TOTAL':>35}{grand_total:>13}")


