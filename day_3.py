# A simple console based, text based, RPG. 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/' . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("You are a holy knight on a mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
begin = input("Type 'Start' to begin the game. ").lower()

if begin == "start":
  print("You are in a vast and lucious forest in hunt for the mystical treasure.")
  choice1 = input("You've encountered a cross roads. Do you go 'Left' or 'Right'? ").lower()
  if choice1 == "left":
    print("You move onward into the forest and eventually arrive at a beach.")
    choice2 = input("Do you swim into the sea or wait for something to happen? ").lower()
    if choice2 == "wait":
      print("Your patience has been rewarded! Three Portals have appeared in front of you.")
      choice3 = input("Three portals of color Red, Blue and Green have appeared in front of you. Which one do you take? ").lower()
      if choice3 == "red":
        print("You have entered a world consumed by hellfire where you will burn for the rest of eternity. Game Over.")
      elif choice3 == "blue":
        print("You have entered an Oceanic Planet. You swim for the treasure but get eaten by a Megalodon. Game Over.")
      elif choice3 == "green":
        print("You have entered a pleasant landscape of greenery and nature. You see a chest in front of you. It's the treasure! Congratulations!. Game Over.")
      else:
        print("A black hole appears and sucks you in. Game Over.")
    else:
      print("You swam into the sea and got poisoned by a group of Jellyfish. Game Over.")
  else:
    print("You got ambushed by Goblins and died. Game Over.")
else:
  print("Invalid Option. Game Over.")
        








