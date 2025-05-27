
#!  1.  Type Casting
# Process of converting a value of one data type to another.(str, int, float, bool) 
#*  Example 1: String ang input kaya kapag nag input ka nang number cinoconvert niya as a str
#           age = input("How old are you?: ")
#           print(age)
#           print(type(age))
#*  Example 2: Convert string to int using: int(), so ang magiging data type na niya ay int (<class 'int'>)
#           age = int(input("Enter your age: "))
#           print(age)
#           print(type(age))

#!  2.  Explicit
#*  Example: 
name = "jm"            #(str)
age = 18               #(int)
Avg = 88.88            #(float)
isHandsome = True      #(bool)
# print(type(name))
# print(type(age))
# print(type(Avg))
# print(type(isHandsome))

# Convert float -> int
Avg = int(Avg)
print("Result: ", Avg)
print(type(Avg))

# Convert int -> float
age = float(age)
print("Result: ", age)
print(type(age))

# Convert int -> str
age = str(age)
print("Result: ", age)
print(type(age))

# Convert bool -> str
name = bool(name)
print("Result: ", name)
print(type(name))


#! Implicit
# data types can be converted when you perform a operators.
#* Example: 
x = 20
y = 8.0

x = x / y
print(x)

print("Created: 5/16/25 1:08 am")