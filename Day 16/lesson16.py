principle = 0
rate = 0
time = 0

while principle <= 0:
  principle = float(input("Enter the principle: "))
  if principle <= 0:
    print("Principle can not be less than to zero")

while rate <= 0:
  rate = float(input("Enter the rate of the interest: "))
  if rate <= 0:
    print("rate can not be less than to zero")

while time <= 0:
  time = int(input("Enter the time of years: "))
  if time <= 0:
    print("years cannot be less than to zero")

total = principle * pow((1 + rate / 100), time)

print(f"The total balance in {time} year/s are {total:.2f}")