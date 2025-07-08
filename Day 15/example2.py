age = int(input("Enter your age: "))

while age < 0:
  print("Age can't be negative")
  age = int(input("Enter your age: "))
print(f"Your are {age} years old")