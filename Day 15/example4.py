num = int(input("Enter your number 1 - 20"))

while num < 1 or num > 20:
  print(f"Your number {num} is not valid")
  num = int(input("Enter your number 1 - 20"))
print(f"Your number is {num}")