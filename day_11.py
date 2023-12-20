#Blackjack game project
import random
import os
user = []
computer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\                
                      |__/                

        """


               
def deal_cards():
    for i in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    
def total_value(user_card, comp_card):
    user_value = sum(user_card)
    computer_value = sum(comp_card)
    print(f"Your Hand: {user_card}")
    print(f"Computer's Hand: [{comp_card[0]}, *]")
    
    game_choice_end = False
    while not game_choice_end:
        choice = input("Do you want more cards? Y/N?: ").lower()
        if choice == "y":
            user_card.append(random.choice(cards))
            user_value = sum(user_card)
            print(f"Your Hand: {user_card} = {user_value}")
            if user_value > 21:
                game_choice_end = True
        else:
            while computer_value <= 16:
                comp_card.append(random.choice(cards))
                computer_value = sum(comp_card)
            game_choice_end = True
    return user_value, computer_value

def bj_check(user_check, comp_check):
    print(f"Final User Hand: {user_check}")
    print(f"Final Computer Hand: {comp_check}")
    game_end = False
    while not game_end:
        if 11 in computer and 10 in computer and len(computer) == 2:
            print("Computer Won. Blackjack!")
            game_end = True
        elif 11 in user and 10 in user and len(user) == 2:
            print("User Won. Blackjack!")
            game_end = True
        elif user_check == 21 and comp_check == 21:
            print("Computer Won.")
            game_end = True 
        elif comp_check == 21:
            print("Computer Won.")
            game_end = True
        elif user_check == 21:
            print("User Won.")
            game_end = True
        else:
            if user_check > 21 and 11 in user:
                ace_index = user.index(11)
                user[ace_index] = 1
                updated_user_check = sum(user)
                print(f"The 11 is now a 1. Hence {updated_user_check}")
                print(f"The Computer's Hand is: {comp_check}")
                print("User Won.")
                game_end = True
            elif user_check > 21:
                print("Computer Won.")
                game_end = True
            elif user_check > comp_check:
                print("User Won.")
                game_end = True
            elif comp_check > 21:
                print("User Won.")
                game_end = True
            else:
                print("Computer Won.")
                game_end = True
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
replay = False
while not replay: 
    user.clear()
    computer.clear()
    print(logo)

    deal_cards()
    user_total, comp_total = total_value(user, computer)
    bj_check(user_total, comp_total)
    replay_choice = input("Would you like to play again? Y/N?: ").lower()
    if replay_choice == "y":
        replay = False
        clear_console()
    else:
        replay = True
