
#* PYTHON CALCULATOR
Operators = input("Enter an Operators(*,/,+,-): ")
firstNumber = float(input("Enter first Number: "))
secondNumber = float(input("Enter Second Number: "))

if Operators == "+":
    print(f"Result: {round(firstNumber + secondNumber, 2)}")
elif Operators == "*":
    print(f"Result: {round(firstNumber * secondNumber, 2)}")
elif Operators == "/":
    print(f"Result: {round(firstNumber / secondNumber, 2)}")
elif Operators == "-":
    print(f"Result: {round(firstNumber - secondNumber, 2)}")
else:
    print(f"Error 404! {Operators} is not a Operators.")