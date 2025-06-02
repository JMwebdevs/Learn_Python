
#! Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter a unit (K or L): ")

# kapag kilo napili niya i coconvert niya ito into pounds
if unit == "K":
  weight = weight * 2.205
  print(f"Your weight is {round(weight, 2)}lbs.")

# kapag pounds(lbs) napili niya i coconvert niya ito sa kgs
elif unit == "L":
  weight = weight / 2.205
  print(f"Your weight is {round(weight, 2)}kgs.")
else: 
  print(f"the {unit} you input is invalid!")