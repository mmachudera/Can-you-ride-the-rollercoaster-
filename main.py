print("Can you ride the rollercoaster? Let's check.")
height = int(input("Wat is you hight in cm? "))
if height < 120:
  print("No,sorry you are too short.")
else:
  print("Yes! Your welcome!")
print("How much will you pay for a ticket?")
age = int(input("How old are you? "))
if age < 12:
  print("The price is 5 euro.")
elif age <= 18:
  print("The price is 7 euro.")
else:
  print("You will pay 12 euro.")
