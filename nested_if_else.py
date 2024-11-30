print("Welcome to the roller coster ride:")
height = int(input("Enter your height in cm:"))

if height >= 170 :
    print("You're good to ride.")
    age = int(input("Enter your age:"))
    if age <= 18:
        print("Please buy $7 ticket.")
    else :
        print("Please buy $12 ticket.")
else : 
    print("You're not tall enough")