
price1 = -3.14159 
price2 = 2000.4342
print("\n\tDay - 14 | Format Specifier")
print(f"{'-'*40}")
print(f"1. Price 1 is {price1:.2f}")
print(f"2. Price 1 is {price1:10}")
print(f"3. Price 1 is {price1:010}")
print(f"4. Price 1 is {price1:<10}") # space katapos ng value
print(f"5. Price 1 is {price1:>10}") # space bago ang value
print(f"6. Price 1 is {price1:^10}") # yung value ay center sa space
print(f"7. Price 2 is {price2:+}") # sign of value
print(f"8. Price 1 is {price1: }") # 
print(f"9. Price 2 is {price2:+,.2f}") # separator ',' along width 2 decimal places
print(f"10. Price 2 is {price2:,}") # each thousand place with comma
print(f"{'-'*40}\n")






