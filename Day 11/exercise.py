

username = input("Enter your Username: ")

if len(username) > 12:
  print("Your username is too long")
elif not username.find(" ") == -1:
  print("Your username must not contain spaces")
elif not username.isalpha():
  print("Your username must not contain digits")
else:
  print(f"Welcome {username}!")