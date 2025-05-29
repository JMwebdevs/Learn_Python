
#! if - do some code only IF some condition is TRUE
#! Else - do something else.

age = int(input("Enter your age: "))

if age >= 60:
    print("Your to old to signup")
# Any code underneath if statements should be indented
elif age >= 18:
    print("Legal")
# elif - ElseIf | we can check more condition before reaching else
# you can add as many elif statement as you want 
elif age < 0:
    print("You haven't been born yet")
elif age >= 60:
    print("Your to old to signup")
# else condition is last resort 
else:
    print("minor")