import math

a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))

c = math.sqrt((pow(a, 2) + pow(b, 2)))
print(f"The hypothenuse of a rigth triangle is {round(c, 2)} cm")
