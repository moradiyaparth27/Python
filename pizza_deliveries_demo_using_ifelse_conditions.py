print("Welcome to pizza delivery.")
size = input("What size pizza do you want? S,M or L? ")
pepperoi = input("Do you want pepperoi on your pizaa? Y or N: ")
cheese = input("Do you want cheese on your pizza? Y or N: ")

price = 0

if size == "S" :
    price += 15
    if pepperoi == "Y" :
        price += 2
        if cheese == "Y" :
            price += 1
elif size == "M" :
    price += 20
    if pepperoi == "Y" :
        price += 3
        if cheese == "Y" :
            price += 1
elif size == "L" :
    price += 25
    if pepperoi == "Y" :
        price += 3
        if cheese == "Y" :
            price += 1


print(f"Your total would be: ${price}.")