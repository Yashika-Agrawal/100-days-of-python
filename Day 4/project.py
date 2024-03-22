rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user = input()
if user == '0':
    print(rock)
elif user == '1':
    print(paper)
else:
    print(scissors)

print("Computer choose:\n")
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if (user == '0' and computer == 0) or (user == '1' and computer == 1) or (user == '2' and computer == 2):
    print("Draw")
elif (user == '0' and computer == 1) or (user == '1' and computer == 2) or (user == '2' and computer == 0):
    print("Computer wins")
else:
    print("User wins")
