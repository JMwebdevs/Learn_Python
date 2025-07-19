# for loops = execute a block of code a fixed number of times
# 	you can iterate over a range, string, sequence, etc.

# for x in range(1, 11):
#   print(x)
  
# for x in reversed( range(1, 11)):
#   print(x)

# for x in ( range(1, 11, 3)):
#   print(x)

# contactNumber = "0970-113-3410"
# for x in contactNumber:
#   print(x)

for x in range(1, 50):
  if x == 26:
    print("Half of 50")
    break
  else:
    print(x)