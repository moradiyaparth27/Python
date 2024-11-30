print("Welcome to the roller coster ride:")
height = int(input("Enter your height in cm:"))
age = int(input("Enter your age:"))

if height >= 170 and age <= 18:
    print("You're good to ride. Please buy $7 ticket.")
elif height >= 170 and age > 18:
    print("You're good to ride. Please buy $12 ticket.")
else : 
    print("You're not tall enough")