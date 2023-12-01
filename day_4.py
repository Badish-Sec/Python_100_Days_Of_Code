# A simple game of RPS

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

player_options = [rock, paper, scissors]

print("What do you choose? Rock, Paper or Scissors?")
choice = int(input("Type 0 for rock, Type 1 for Paper and Type 2 for Scissors "))

print("Player Chose:")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print (scissors)
else:
    print("Invalid Option. Game Over.")
    exit()

print("Computer Chose:")
num = len(player_options)
computer = random.randint(0, num - 1)
comp_options = [rock, paper, scissors]

if computer == 0:
    print(comp_options[0])
elif computer == 1:
    print(comp_options[1])
elif computer == 2:
    print(comp_options[2])

if choice == 0 and computer == 1:
    print("You Lose.")
elif choice == 1 and computer == 2:
    print("You Lose.")
elif choice == 2 and computer == 0:
    print("You Lose.")
elif choice == computer:
    print("Draw.")
else:
    print("You Win.")    





