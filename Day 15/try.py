name = input("Enter your name: ")
while name == "":
  print("You did not enter your name!\n")
  rename = input("Do you want to Re-enter your name? (y/n)").lower()
  if rename != "n":
    name = input("Enter your name: ")
  elif rename != "y":
    print("okay")
    break
  else:
    print("Error 404")
else:
  print(f"Hello {name}")