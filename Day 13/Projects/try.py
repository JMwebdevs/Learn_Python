while True:
  email = input("Enter your email: ")
  index = email.index("@")
  userName = email[:index]
  domain = email[index + 1:]

  if len(userName) >= 10:
    print("Your Username is too long")
  else:
    print(f"Your Username is {userName} and your Domain is {domain}")
    break
  changeUsername = input("Do you want to change your Username? (yes/no)").lower()
  if changeUsername == "no":
    break
