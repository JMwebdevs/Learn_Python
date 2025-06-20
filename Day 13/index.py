

email = input("Enter your Email: ")
# index = email.index("@")
userName =  email[:email.index("@")]
domain = email[email.index("@")+ 1:]
if len(userName) > 10:
  print("Your Username is too long")
else:
  print(f"Your Username is {userName} and your domain is {domain}")