# While loop - execute some code WHILE some condition remains true

name = input("Enter your name: ").lower()

while name == "":
  print("You did not enter your name!")
  name = input("Enter your name: ").lower()
  # infinite loop basta True yung while name kapag hindi true exit kana sa loop
print(f"Hello Kupal! {name}")