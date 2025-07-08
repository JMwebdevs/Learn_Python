food = input("Enter your favorite food (Enter q to Quit)")
while not food == "q": #kapag iba nilagay mo not means false so kung hindi q
# clinick mo nag enter ka ng favorite food mo ipriprint niya etong nasa baba
  print(f"You like {food}")
  # naglagay tau ng input uli dito para hindi mag infinite
  food = input("Enter your favorite food (Enter q to Quit)")
print("Bye")
