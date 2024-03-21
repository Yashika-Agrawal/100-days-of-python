print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
age =int(input("What's your age?"))
if height > 120 :
  print("You can ride the rollercoaster!")
  if age<12:
    bill=5
    print('Your bill is $5')
  elif age>=12 and age<18:
    bill=7
    print('Your bill is $7')
  elif age>=18:
    bill=12
    print('Your bill is $12')
  elif age>=45 and age<=55:
    bill=0
    print('Your bill is $0')

else:
  print("You can't ride the rollercoaster!")

photos=input("Do you want photos? Y or N")
if photos=='Y':
  bill+=3
  print(f"Your bill is {bill}")
else:
  print(f"Your bill is {bill}")

