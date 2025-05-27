
#!  1.  Variable 
# Reusable container sya ng value (parang sya yung box tapos may laman na pagkain)

#? Diffirent Data Types:
#   - string(str) - series of text(madaming characters)
#   - integer(int) - Whole Number
#   - float - May decimal / floating point
#   - boolean(bool) - True or False

#!  2.  String
# String are series of Character and they can include number but we treat theme as character.
#* Example: 
firstName = "John Mark" #? String
food = "Sisig"
email = "johnmarklapenid7@gmail.com"
#print("Ako is ", firstName)
#print("Masarap ang ", food)

#!  3.  f-string
# you can write a  python expression between {and} characters that can refer to variables or literal values.
#? F - means Format (f"{}")
#* Example: 
#print(f"Ang pogi ni {firstName}")
#print(f"Favorite Food ni {firstName} ay {food}")
#print(f"My email is: {email}")

#!  4.  Integers
# integers is a whole number (Dapat walang Quotation mark "" para hindi maging String ang int)
#* Example: 
age = 18
quantity = 5
numOfStudents = 40
#print(f"I'm {age} years old.")
#print(f"I'm buying {quantity} items")
#print(f"I'm ICT students and my class has {numOfStudents} students")

#!  5.  Float
# Float is a number but contains a decimal portion.
#* Example:
peraKo = 99.99
averageKo = 86.456
distance = 3.3
#print(f"Ang pera ko ay ₱{peraKo} pesos.")
#print(f"Ang avg ng card ko ay: {averageKo}")
#print(f"Ang layo ng aking nilalakad papuntang school ay {distance} kilometer.")

#!  6.  Boolean
# Is either True or False (Binary 1 & 0)
#? The First Letter is Capital
#* Example:
pogiAko = True
for_sale = False
isOnline = True
#print(f"Pogi ba si John mark?: {pogiAko}")

#!  7.  if statements

#* Example 1:
if pogiAko:
    print("Ang pogi ni John mark")
else:
    print("Hindi pogi")

#* Example 2:
if for_sale:
    print("Oo Binebente namin")
else:
    print("Hindi namin binebenta")

#* Example 3:
if isOnline:
    print("Si john mark ay online")
else:
    print("Offline si john mark")