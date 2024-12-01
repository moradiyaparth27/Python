import random


random_number = random.randint(0, 1)
print(f"The Computer chooses: {random_number}")
user_input = int(input("Choose 0 for Heads or 1 for Tails: "))


if user_input >= 0 and user_input <= 1:
    if user_input == random_number:
        print("You Win!")
    else :
        print("You Loose.")