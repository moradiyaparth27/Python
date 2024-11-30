print(" Welcome to the Treasure Island.\n Your mission is to find he treasure. ")

road = input("You're at a cross road. Where do you want to go? \n     'Type \"left\" or \"right\" ")

if road == "left" :
    lake = input("You've come to lake. here is an island in the middle of the lake. \n     Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    if lake == "wait" :
        door = input("You arrive at the island unharmed. There is a house with three doors. \n     One red, one yellow and one blue. Which color do you choose? ")
        if door == "yellow":
            print("You've found the treasure. ")
        else:  
            print("Game Over!")
    else:
        print("Game Over! ")
else: 
    print("Game Over! ")