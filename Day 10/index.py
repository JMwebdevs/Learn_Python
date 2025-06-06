
#* Conditional Expression
print("\n\t\tConditional Expression\n")


# Positive ot negative
print("Positive and Negative: ")
num = -5
print("1. Positive\n" if num > 0 else "1. Negative\n")

# Even or Odd
print("Even and Odd:")
num2 = 7
result = "2. Even\n" if num2 % 2 == 0 else "2. Odd\n"
print(result)

# Maximum Number
print("Maximum number:")
a = 8
b = 9
maxNum = "3. A\n" if a >= b else "3. B\n"
print(maxNum)

# Minimum Number
print("Minimum number: ")
minNum = "4. A\n" if a <= b else "4. B\n"
print(minNum)

# Age status
print("Status:")
age = 18
print("5. Legal\n" if age >= 18 else "5. Minor\n")

# Temperature
print("Temperature:")
temp = 30
result2 = "6. Hot\n" if temp >= 20 else "6. Cold\n" 
print(result2)

# Access level
print("Access level: ")
user_role = "guest"
accessLevel = "7. Full access\n" if user_role == "guest" else "7. Limited access\n"
print(accessLevel)