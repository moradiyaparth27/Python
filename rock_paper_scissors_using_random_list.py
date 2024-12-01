import random

game_images = [ '''
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_|
               ''', 

               '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
               ''',

               '''
        
          _                     
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
               ''']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice == 0:
    print(f"You Choose: {game_images[0]}")
elif user_choice == 1:
    print(f"You Choose: {game_images[1]}")
elif user_choice == 2:
    print(f"You Choose: {game_images[2]}")
else :
    print("Please make choice wisely: ")

random_choice_by_computer = random.randint(0, 2)
if random_choice_by_computer == 0:
    print(f"Computer choose: {game_images[0]}")
if random_choice_by_computer == 1:
    print(f"Computer choose: {game_images[1]}")
if random_choice_by_computer == 2:
    print(f"Computer choose: {game_images[2]}")
    
if user_choice == 0 and random_choice_by_computer == 1:
    print("You Win!")
elif user_choice == 0 and random_choice_by_computer == 2:
    print("Computer Win!")
elif user_choice == 1 and random_choice_by_computer == 2:
    print("You Win!")
elif user_choice == 1 and random_choice_by_computer == 0:
    print("Computer Win!")
elif user_choice == 2 and random_choice_by_computer == 0:
    print("You Win!")
elif user_choice == 2 and random_choice_by_computer == 1:
    print("Computer Win!")
else : 
    print("It's a Draw! Please Play Again.")