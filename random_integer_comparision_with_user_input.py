import random

random_integer = random.randint(1, 10)
print(random_integer)
user_input = int(input("Enter your choice of number from 1 to 10. "))
if user_input >= 1 and user_input<= 10:
    if user_input == random_integer:
        print("You & Computer both selected same numbers. ")
    else:
        print("You & Computer both selected different numbers. ")
