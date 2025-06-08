print("\n\t\t\tString Methods\n ")


# Len function
username = input("Enter your username: \n")
print(f"1. len: {len(username)}")

# find function
result = username.find("o")
print(f"2. find: {result}")

# rfind
result2 = username.rfind("o")
print(f"3. rfind: {result2}")

# capitalize
result3 = username.capitalize()
print(f"4. Capitalize: {result3}")

# UpperCase
result4 = username.upper()
print(f"5. UpperCase: {result4}")

# LowerCase
result5 = username.lower()
print(f"6. LowerCase: {result5}")

# isDigit
result6 = username.isdigit()
print(f"7. isdigit: {result6}")

# isAlpha
result7 = username.isalpha()
print(f"8. isAlpha: {result7}")

# count
result8 = username.count(" ")
print(f"9. Count: {result8} Spaces")

# replace
result9 = username.replace("j", "H")
print(f"10. Replace letter j to H: {result9}")