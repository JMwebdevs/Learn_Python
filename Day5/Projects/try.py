import math

#! CIRCUMFERENCE
radius = float(input("Enter a radius of a circle: "))
result = 2 * math.pi * radius
print(f"The Circumstances of a circle is {round(result, 2)}cm")

#! AREA OF A CIRCLE
radius = float(input("Enter a radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of a circle is {round(area, 2)}cm")

#! HYPOTENUSE OF A RIGTH TRIANGLE
a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))
result = math.sqrt((pow(a, 2)+pow(b, 2)))
print(f"The hypotenuse of a rigth triangle is {round(result, 2)}cm")